from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from btc_benchmark import load_benchmark_data, run_benchmark
from btc_benchmark.decisions import baseline_rules as br
from btc_benchmark.features import technical_indicators as ti


RUN_DIR = Path(__file__).resolve().parent
REPO_ROOT = Path("/Users/sungs/ai-lab/sources/checkouts/btc_benchmark")
TEAM = "ai_lab_autoresearch_cycle1_151519"


def _clean_pos(pos: np.ndarray, mode: str = "long_cash") -> np.ndarray:
    pos = np.where(np.isfinite(pos), pos, 0.0)
    if mode == "long_cash":
        return np.where(pos > 0, 1.0, 0.0)
    if mode == "short_cash":
        return np.where(pos < 0, -1.0, 0.0)
    return np.clip(pos, -1.0, 1.0)


@dataclass
class StaticRule:
    name: str
    kind: str
    params: dict
    horizon: int = 1

    def fit(self, data, train_start, train_end) -> None:
        return None

    def positions(self, data, start, end) -> np.ndarray:
        candles = data.candles.iloc[:end]
        if self.kind == "always_long":
            pos = np.ones(len(candles), dtype="float64")
        elif self.kind == "ema":
            pos = br.ema_crossover(candles, **self.params)
        elif self.kind == "donchian":
            pos = br.donchian_breakout(candles, **self.params)
        elif self.kind == "rsi":
            pos = br.rsi_mean_reversion(candles, **self.params)
        else:
            raise ValueError(self.kind)
        return np.asarray(pos[start:end], dtype="float64")


@dataclass
class EmaVolFilter:
    name: str
    fast: int
    slow: int
    vol_window: int
    quantile: float
    prefer: str
    mode: str = "long_cash"
    horizon: int = 1
    threshold: float | None = None

    def fit(self, data, train_start, train_end) -> None:
        candles = data.candles.iloc[:train_end]
        vol = ti.rolling_volatility(candles["close"], self.vol_window).iloc[train_start:train_end]
        self.threshold = float(vol.dropna().quantile(self.quantile)) if vol.notna().any() else None

    def positions(self, data, start, end) -> np.ndarray:
        candles = data.candles.iloc[:end]
        base = br.ema_crossover(candles, fast=self.fast, slow=self.slow, mode=self.mode)
        vol = ti.rolling_volatility(candles["close"], self.vol_window).to_numpy("float64")
        if self.threshold is None or not np.isfinite(self.threshold):
            filt = np.ones(len(candles), dtype=bool)
        elif self.prefer == "low":
            filt = vol <= self.threshold
        else:
            filt = vol >= self.threshold
        pos = np.where(filt, base, 0.0)
        return _clean_pos(pos, self.mode)[start:end]


@dataclass
class FundingCarryFilter:
    name: str
    fast: int
    slow: int
    funding_threshold: float
    mode: str = "long_cash"
    horizon: int = 1

    def fit(self, data, train_start, train_end) -> None:
        return None

    def positions(self, data, start, end) -> np.ndarray:
        candles = data.candles.iloc[:end].copy()
        base = br.ema_crossover(candles, fast=self.fast, slow=self.slow, mode=self.mode)
        funding = data.aux.get("funding")
        if funding is None or funding.empty:
            return _clean_pos(base, self.mode)[start:end]
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
        rate = pd.to_numeric(aligned["funding_rate"], errors="coerce").to_numpy("float64")
        pos = np.where(rate <= self.funding_threshold, base, 0.0)
        return _clean_pos(pos, self.mode)[start:end]


def report_key(report: dict) -> tuple[bool, float, float]:
    return (
        not bool(report.get("disqualified", True)),
        float(report.get("net", float("-inf"))),
        float(report.get("net_cost2x", float("-inf"))),
    )


def main() -> None:
    data = load_benchmark_data(REPO_ROOT, include_sub_bars=False)
    candidates = [
        StaticRule("candidate_always_long", "always_long", {}),
        StaticRule("candidate_ema_24_96_long_cash", "ema", {"fast": 24, "slow": 96, "mode": "long_cash"}),
        StaticRule("candidate_ema_48_192_long_cash", "ema", {"fast": 48, "slow": 192, "mode": "long_cash"}),
        StaticRule("candidate_ema_12_48_long_cash", "ema", {"fast": 12, "slow": 48, "mode": "long_cash"}),
        StaticRule("candidate_ema_24_96_long_short", "ema", {"fast": 24, "slow": 96, "mode": "long_short"}),
        StaticRule("candidate_donchian_24_long_cash", "donchian", {"window": 24, "mode": "long_cash"}),
        StaticRule("candidate_donchian_72_long_cash", "donchian", {"window": 72, "mode": "long_cash"}),
        StaticRule("candidate_rsi_14_35_65_long_cash", "rsi", {"window": 14, "low": 35.0, "high": 65.0, "mode": "long_cash"}),
        EmaVolFilter("candidate_ema_48_192_lowvol_q60", 48, 192, 72, 0.60, "low"),
        EmaVolFilter("candidate_ema_48_192_lowvol_q40", 48, 192, 72, 0.40, "low"),
        EmaVolFilter("candidate_ema_48_192_highvol_q60", 48, 192, 72, 0.60, "high"),
        FundingCarryFilter("candidate_ema_48_192_funding_le_0", 48, 192, 0.0),
        FundingCarryFilter("candidate_ema_48_192_funding_le_5bp", 48, 192, 0.0005),
    ]

    reports_dir = RUN_DIR / "candidate_reports"
    reports_dir.mkdir(exist_ok=True)
    leaderboard = RUN_DIR / "candidate_leaderboard.jsonl"
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
        reports.append(report)
        (reports_dir / f"{strategy.name}.json").write_text(json.dumps(report, indent=2, default=str) + "\n")

    best = max(reports, key=report_key)
    confirm = run_benchmark(
        StaticRule("candidate_always_long_default_gates", "always_long", {})
        if best["strategy"] == "candidate_always_long"
        else next(c for c in candidates if c.name == best["strategy"]),
        data,
        gates=True,
        leaderboard_path=RUN_DIR / "confirm_leaderboard.jsonl",
        team=TEAM,
    )
    (RUN_DIR / "confirm_best_report.json").write_text(json.dumps(confirm, indent=2, default=str) + "\n")

    summary_rows = sorted(reports, key=report_key, reverse=True)
    compact = [
        {
            "strategy": r["strategy"],
            "dq": r["disqualified"],
            "net": r["net"],
            "sharpe": r["sharpe"],
            "max_drawdown": r["max_drawdown"],
            "turnover": r["turnover"],
            "cost2x": r["net_cost2x"],
            "cost5x": r["net_cost5x"],
            "next_open": r["net_next_open"],
            "funding_aware": r["net_funding_aware"],
            "random_pctile": r["random_pctile"],
        }
        for r in summary_rows
    ]
    (RUN_DIR / "candidate_summary.json").write_text(json.dumps(compact, indent=2) + "\n")


if __name__ == "__main__":
    main()
