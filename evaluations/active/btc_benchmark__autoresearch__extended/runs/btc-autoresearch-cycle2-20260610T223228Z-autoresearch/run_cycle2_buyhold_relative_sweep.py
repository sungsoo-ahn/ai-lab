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
TEAM = "ai_lab_autoresearch_cycle2_223228"
ALWAYS_LONG_FLOOR = 1.5005
PREFLIGHT_EMA_NET = -0.8668


def _clean_long_cash(pos: np.ndarray) -> np.ndarray:
    pos = np.where(np.isfinite(pos), pos, 0.0)
    return np.where(pos > 0, 1.0, 0.0).astype("float64")


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
class BuyHoldOverlay:
    name: str
    trend_slow: int | None = None
    trend_fast: int | None = None
    funding_max: float | None = None
    vol_window: int | None = None
    vol_quantile: float | None = None
    drawdown_window: int | None = None
    drawdown_min: float | None = None
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
        keep = np.ones(len(candles), dtype=bool)

        if self.trend_slow is not None and self.trend_fast is None:
            slow = ti.ema(close, self.trend_slow).to_numpy("float64")
            keep &= close.to_numpy("float64") > slow
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

        return np.where(keep[start:end], 1.0, 0.0).astype("float64")


def decision_key(report: dict[str, Any]) -> tuple[Any, ...]:
    dq = bool(report.get("disqualified", True))
    delta_bh = float(report.get("delta_vs_always_long", -999.0))
    drawdown_improvement = float(report.get("drawdown_improvement_vs_always_long", -999.0))
    funding = float(report.get("net_funding_aware") or -999.0)
    cost5 = float(report.get("net_cost5x", -999.0))
    next_open = float(report.get("net_next_open", -999.0))
    random_pctile = report.get("random_pctile")
    random_value = -1.0 if random_pctile is None else float(random_pctile)
    return (not dq, delta_bh, drawdown_improvement, funding, cost5, next_open, random_value)


def annotate(report: dict[str, Any]) -> dict[str, Any]:
    per_year = report.get("per_year") or {}
    year_nets = [float(v.get("net", 0.0)) for v in per_year.values()]
    abs_sum = sum(abs(x) for x in year_nets)
    concentration = max((abs(x) for x in year_nets), default=0.0) / abs_sum if abs_sum else None
    out = dict(report)
    out["delta_vs_always_long"] = round(float(out["net"]) - ALWAYS_LONG_FLOOR, 4)
    out["delta_vs_preflight_ema"] = round(float(out["net"]) - PREFLIGHT_EMA_NET, 4)
    out["drawdown_improvement_vs_always_long"] = round(float(out["max_drawdown"]) - (-0.6670), 4)
    out["per_year_abs_net_concentration"] = None if concentration is None else round(float(concentration), 4)
    return out


def main() -> None:
    data = load_benchmark_data(REPO_ROOT, include_sub_bars=False)
    candidates: list[Any] = [
        StaticRule("cycle2_always_long_floor", "always_long", {}),
        StaticRule("cycle2_ema_48_192_long_cash_ref", "ema", {"fast": 48, "slow": 192, "mode": "long_cash"}),
        StaticRule("cycle2_ema_72_288_long_cash", "ema", {"fast": 72, "slow": 288, "mode": "long_cash"}),
        StaticRule("cycle2_ema_96_384_long_cash", "ema", {"fast": 96, "slow": 384, "mode": "long_cash"}),
        BuyHoldOverlay("cycle2_bh_close_gt_ema192", trend_slow=192),
        BuyHoldOverlay("cycle2_bh_close_gt_ema384", trend_slow=384),
        BuyHoldOverlay("cycle2_bh_ema48_gt_ema192", trend_fast=48, trend_slow=192),
        BuyHoldOverlay("cycle2_bh_ema96_gt_ema384", trend_fast=96, trend_slow=384),
        BuyHoldOverlay("cycle2_bh_funding_le_0", funding_max=0.0),
        BuyHoldOverlay("cycle2_bh_funding_le_1bp", funding_max=0.0001),
        BuyHoldOverlay("cycle2_bh_funding_le_5bp", funding_max=0.0005),
        BuyHoldOverlay("cycle2_bh_lowvol72_q80", vol_window=72, vol_quantile=0.80),
        BuyHoldOverlay("cycle2_bh_lowvol168_q80", vol_window=168, vol_quantile=0.80),
        BuyHoldOverlay("cycle2_bh_drawdown252_ge_minus20", drawdown_window=252, drawdown_min=-0.20),
        BuyHoldOverlay("cycle2_bh_drawdown720_ge_minus30", drawdown_window=720, drawdown_min=-0.30),
        BuyHoldOverlay(
            "cycle2_bh_ema192_funding_le_5bp",
            trend_slow=192,
            funding_max=0.0005,
        ),
        BuyHoldOverlay(
            "cycle2_bh_ema384_lowvol168_q80",
            trend_slow=384,
            vol_window=168,
            vol_quantile=0.80,
        ),
        BuyHoldOverlay(
            "cycle2_bh_drawdown720_funding_le_5bp",
            drawdown_window=720,
            drawdown_min=-0.30,
            funding_max=0.0005,
        ),
    ]

    reports_dir = RUN_DIR / "cycle2_candidate_reports"
    reports_dir.mkdir(exist_ok=True)
    leaderboard = RUN_DIR / "cycle2_candidate_leaderboard.jsonl"
    if leaderboard.exists():
        leaderboard.unlink()

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
            leaderboard_path=RUN_DIR / "cycle2_confirm_leaderboard.jsonl",
            team=TEAM,
        )
    )
    (RUN_DIR / "cycle2_confirm_best_report.json").write_text(json.dumps(confirmed, indent=2, default=str) + "\n")

    compact = [
        {
            "rank": i + 1,
            "strategy": r["strategy"],
            "dq": r["disqualified"],
            "net": r["net"],
            "delta_vs_always_long": r["delta_vs_always_long"],
            "drawdown": r["max_drawdown"],
            "drawdown_improvement": r["drawdown_improvement_vs_always_long"],
            "turnover": r["turnover"],
            "cost2x": r["net_cost2x"],
            "cost3x": r["net_cost3x"],
            "cost5x": r["net_cost5x"],
            "next_open": r["net_next_open"],
            "funding_aware": r["net_funding_aware"],
            "random_pctile": r["random_pctile"],
            "per_year_abs_net_concentration": r["per_year_abs_net_concentration"],
        }
        for i, r in enumerate(ranked)
    ]
    (RUN_DIR / "cycle2_candidate_summary.json").write_text(json.dumps(compact, indent=2) + "\n")


if __name__ == "__main__":
    main()
