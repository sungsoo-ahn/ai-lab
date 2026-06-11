from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from btc_benchmark import load_benchmark_data, run_benchmark
from btc_benchmark.decisions import baseline_rules as br
from btc_benchmark.features import technical_indicators as ti


RUN_DIR = Path(__file__).resolve().parent
REPO_ROOT = Path("/Users/sungs/ai-lab/sources/checkouts/btc_benchmark")
TEAM = "ai_lab_autoresearch_cycle3_223228"
ALWAYS_LONG_FLOOR = 1.5005
PREFLIGHT_EMA_NET = -0.8668
ALWAYS_LONG_DRAWDOWN = -0.6670


def _funding_rate_by_bar(data: Any, candles: pd.DataFrame) -> np.ndarray:
    funding = data.aux.get("funding")
    if funding is None or funding.empty:
        return np.full(len(candles), np.nan, dtype="float64")
    left = pd.DataFrame(
        {
            "timestamp_close": pd.to_datetime(candles["timestamp_close"], utc=True),
            "_row": np.arange(len(candles), dtype=int),
        }
    ).sort_values("timestamp_close")
    right = funding.copy()
    right["event_time"] = pd.to_datetime(right["event_time"], utc=True)
    right = right.sort_values("event_time")
    aligned = pd.merge_asof(
        left,
        right[["event_time", "funding_rate"]],
        left_on="timestamp_close",
        right_on="event_time",
        direction="backward",
    ).sort_values("_row")
    return pd.to_numeric(aligned["funding_rate"], errors="coerce").to_numpy("float64")


def _apply_persistence(
    raw: np.ndarray,
    *,
    enter_confirm: int,
    exit_confirm: int,
    min_hold: int,
    cooldown: int,
) -> np.ndarray:
    out = np.zeros(len(raw), dtype="float64")
    state = 0.0
    true_run = 0
    false_run = 0
    hold = 0
    wait = 0
    for i, value in enumerate(raw):
        if bool(value):
            true_run += 1
            false_run = 0
        else:
            false_run += 1
            true_run = 0

        if state == 0.0:
            if wait > 0:
                wait -= 1
            if wait == 0 and true_run >= enter_confirm:
                state = 1.0
                hold = 0
        else:
            hold += 1
            if hold >= min_hold and false_run >= exit_confirm:
                state = 0.0
                hold = 0
                wait = cooldown
        out[i] = state
    return out


@dataclass
class StaticRule:
    name: str
    kind: str
    params: dict[str, Any]
    horizon: int = 1

    def fit(self, data: Any, train_start: int, train_end: int) -> None:
        return None

    def positions(self, data: Any, start: int, end: int) -> np.ndarray:
        candles = data.candles.iloc[:end]
        if self.kind == "always_long":
            pos = np.ones(len(candles), dtype="float64")
        elif self.kind == "ema":
            pos = br.ema_crossover(candles, **self.params)
        else:
            raise ValueError(self.kind)
        return np.asarray(pos[start:end], dtype="float64")


@dataclass
class RegimeOverlay:
    name: str
    trend_slow: int | None = None
    trend_fast: int | None = None
    funding_max: float | None = None
    vol_window: int | None = None
    vol_quantile: float | None = None
    drawdown_window: int | None = None
    drawdown_min: float | None = None
    enter_confirm: int = 1
    exit_confirm: int = 1
    min_hold: int = 1
    cooldown: int = 0
    horizon: int = 1

    vol_threshold: float | None = None

    def fit(self, data: Any, train_start: int, train_end: int) -> None:
        if self.vol_window is None or self.vol_quantile is None:
            self.vol_threshold = None
            return
        candles = data.candles.iloc[:train_end]
        vol = ti.rolling_volatility(candles["close"], self.vol_window).iloc[train_start:train_end]
        self.vol_threshold = float(vol.dropna().quantile(self.vol_quantile)) if vol.notna().any() else None

    def positions(self, data: Any, start: int, end: int) -> np.ndarray:
        candles = data.candles.iloc[:end]
        close = pd.to_numeric(candles["close"], errors="coerce")
        closev = close.to_numpy("float64")
        keep = np.ones(len(candles), dtype=bool)

        if self.trend_slow is not None and self.trend_fast is None:
            slow = ti.ema(close, self.trend_slow).to_numpy("float64")
            keep &= closev > slow
            keep &= np.isfinite(slow)

        if self.trend_slow is not None and self.trend_fast is not None:
            fast = ti.ema(close, self.trend_fast).to_numpy("float64")
            slow = ti.ema(close, self.trend_slow).to_numpy("float64")
            keep &= fast > slow
            keep &= np.isfinite(fast) & np.isfinite(slow)

        if self.funding_max is not None:
            rate = _funding_rate_by_bar(data, candles)
            keep &= np.isnan(rate) | (rate <= self.funding_max)

        if self.vol_window is not None and self.vol_threshold is not None and np.isfinite(self.vol_threshold):
            vol = ti.rolling_volatility(close, self.vol_window).to_numpy("float64")
            keep &= np.isfinite(vol) & (vol <= self.vol_threshold)

        if self.drawdown_window is not None and self.drawdown_min is not None:
            peak = close.rolling(self.drawdown_window, min_periods=self.drawdown_window).max()
            dd = close / peak - 1.0
            ddv = dd.to_numpy("float64")
            keep &= np.isfinite(ddv) & (ddv >= self.drawdown_min)

        pos = _apply_persistence(
            keep,
            enter_confirm=max(1, int(self.enter_confirm)),
            exit_confirm=max(1, int(self.exit_confirm)),
            min_hold=max(1, int(self.min_hold)),
            cooldown=max(0, int(self.cooldown)),
        )
        return pos[start:end].astype("float64")


def decision_key(report: dict[str, Any]) -> tuple[Any, ...]:
    dq = bool(report.get("disqualified", True))
    delta_bh = float(report.get("delta_vs_always_long", -999.0))
    drawdown_improvement = float(report.get("drawdown_improvement_vs_always_long", -999.0))
    funding = float(report.get("net_funding_aware") or -999.0)
    cost2 = float(report.get("net_cost2x", -999.0))
    cost3 = float(report.get("net_cost3x", -999.0))
    cost5 = float(report.get("net_cost5x", -999.0))
    next_open = float(report.get("net_next_open", -999.0))
    concentration = report.get("per_year_abs_net_concentration")
    concentration_score = 999.0 if concentration is None else -float(concentration)
    random_pctile = report.get("random_pctile")
    random_value = -1.0 if random_pctile is None else float(random_pctile)
    return (
        not dq,
        delta_bh > 0,
        cost3 > 0,
        cost5 > 0,
        delta_bh,
        drawdown_improvement,
        funding,
        cost2,
        cost3,
        cost5,
        next_open,
        concentration_score,
        random_value,
    )


def annotate(report: dict[str, Any]) -> dict[str, Any]:
    per_year = report.get("per_year") or {}
    year_nets = [float(v.get("net", 0.0)) for v in per_year.values()]
    abs_sum = sum(abs(x) for x in year_nets)
    concentration = max((abs(x) for x in year_nets), default=0.0) / abs_sum if abs_sum else None
    out = dict(report)
    out["delta_vs_always_long"] = round(float(out["net"]) - ALWAYS_LONG_FLOOR, 4)
    out["delta_vs_preflight_ema"] = round(float(out["net"]) - PREFLIGHT_EMA_NET, 4)
    out["drawdown_improvement_vs_always_long"] = round(float(out["max_drawdown"]) - ALWAYS_LONG_DRAWDOWN, 4)
    out["per_year_abs_net_concentration"] = None if concentration is None else round(float(concentration), 4)
    return out


def compact_record(rank: int, report: dict[str, Any]) -> dict[str, Any]:
    return {
        "rank": rank,
        "strategy": report["strategy"],
        "dq": report["disqualified"],
        "net": report["net"],
        "delta_vs_always_long": report["delta_vs_always_long"],
        "drawdown": report["max_drawdown"],
        "drawdown_improvement": report["drawdown_improvement_vs_always_long"],
        "turnover": report["turnover"],
        "cost2x": report["net_cost2x"],
        "cost3x": report["net_cost3x"],
        "cost5x": report["net_cost5x"],
        "next_open": report["net_next_open"],
        "funding_aware": report["net_funding_aware"],
        "random_pctile": report["random_pctile"],
        "per_year_abs_net_concentration": report["per_year_abs_net_concentration"],
    }


def main() -> None:
    data = load_benchmark_data(REPO_ROOT, include_sub_bars=False)
    candidates: list[Any] = [
        StaticRule("cycle3_always_long_floor", "always_long", {}),
        StaticRule("cycle3_control_ema_72_288_long_cash", "ema", {"fast": 72, "slow": 288, "mode": "long_cash"}),
        RegimeOverlay("cycle3_control_funding_le_5bp", funding_max=0.0005),
        RegimeOverlay("cycle3_control_drawdown252_ge_minus20", drawdown_window=252, drawdown_min=-0.20),
        RegimeOverlay("cycle3_ema384_lowvol168_q80_retest", trend_slow=384, vol_window=168, vol_quantile=0.80),
        RegimeOverlay(
            "cycle3_ema384_lowvol168_q80_exit6_min24",
            trend_slow=384,
            vol_window=168,
            vol_quantile=0.80,
            exit_confirm=6,
            min_hold=24,
        ),
        RegimeOverlay(
            "cycle3_ema384_lowvol168_q80_enter3_exit12_min48",
            trend_slow=384,
            vol_window=168,
            vol_quantile=0.80,
            enter_confirm=3,
            exit_confirm=12,
            min_hold=48,
        ),
        RegimeOverlay(
            "cycle3_ema384_lowvol336_q85_exit6_min24",
            trend_slow=384,
            vol_window=336,
            vol_quantile=0.85,
            exit_confirm=6,
            min_hold=24,
        ),
        RegimeOverlay(
            "cycle3_ema384_lowvol336_q90_exit12_min48",
            trend_slow=384,
            vol_window=336,
            vol_quantile=0.90,
            exit_confirm=12,
            min_hold=48,
        ),
        RegimeOverlay(
            "cycle3_ema384_lowvol720_q85_exit12_min72",
            trend_slow=384,
            vol_window=720,
            vol_quantile=0.85,
            exit_confirm=12,
            min_hold=72,
        ),
        RegimeOverlay(
            "cycle3_ema384_lowvol168_q80_funding5bp_exit6",
            trend_slow=384,
            vol_window=168,
            vol_quantile=0.80,
            funding_max=0.0005,
            exit_confirm=6,
            min_hold=24,
        ),
        RegimeOverlay(
            "cycle3_ema384_drawdown252_minus20_exit6",
            trend_slow=384,
            drawdown_window=252,
            drawdown_min=-0.20,
            exit_confirm=6,
            min_hold=24,
        ),
    ]

    reports_dir = RUN_DIR / "cycle3_candidate_reports"
    reports_dir.mkdir(exist_ok=True)
    leaderboard = RUN_DIR / "cycle3_candidate_leaderboard.jsonl"
    confirm_leaderboard = RUN_DIR / "cycle3_confirm_leaderboard.jsonl"
    for path in (leaderboard, confirm_leaderboard):
        if path.exists():
            path.unlink()

    reports = []
    for strategy in candidates:
        report = run_benchmark(
            strategy,
            data,
            gates=True,
            gate_max_cutoffs=64,
            leaderboard_path=leaderboard,
            team=TEAM,
        )
        enriched = annotate(report)
        reports.append(enriched)
        (reports_dir / f"{strategy.name}.json").write_text(json.dumps(enriched, indent=2, default=str) + "\n")

    ranked = sorted(reports, key=decision_key, reverse=True)
    best = ranked[0]
    best_strategy = next(c for c in candidates if c.name == best["strategy"])
    confirmed = annotate(
        run_benchmark(
            best_strategy,
            data,
            gates=True,
            leaderboard_path=confirm_leaderboard,
            team=TEAM,
        )
    )
    (RUN_DIR / "cycle3_confirm_best_report.json").write_text(json.dumps(confirmed, indent=2, default=str) + "\n")

    compact = [compact_record(i + 1, r) for i, r in enumerate(ranked)]
    (RUN_DIR / "cycle3_candidate_summary.json").write_text(json.dumps(compact, indent=2) + "\n")


if __name__ == "__main__":
    main()
