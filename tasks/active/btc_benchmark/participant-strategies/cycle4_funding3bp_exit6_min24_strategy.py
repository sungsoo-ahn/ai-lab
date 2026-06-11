from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd

from btc_benchmark.features import technical_indicators as ti


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


def _apply_exit_persistence(raw: np.ndarray, *, exit_confirm: int, min_hold: int) -> np.ndarray:
    out = np.zeros(len(raw), dtype="float64")
    state = 0.0
    true_run = 0
    false_run = 0
    hold = 0
    for i, value in enumerate(raw):
        if bool(value):
            true_run += 1
            false_run = 0
        else:
            false_run += 1
            true_run = 0

        if state == 0.0:
            if true_run >= 1:
                state = 1.0
                hold = 0
        else:
            hold += 1
            if hold >= min_hold and false_run >= exit_confirm:
                state = 0.0
                hold = 0
        out[i] = state
    return out


@dataclass
class Cycle4Funding3bpExit6Min24:
    name: str = "cycle4_funding3bp_exit6_min24"
    horizon: int = 1
    trend_slow: int = 384
    funding_max: float = 0.0003
    vol_window: int = 168
    vol_quantile: float = 0.80
    exit_confirm: int = 6
    min_hold: int = 24
    vol_threshold: float | None = None

    def fit(self, data: Any, train_start: int, train_end: int) -> None:
        candles = data.candles.iloc[:train_end]
        vol = ti.rolling_volatility(candles["close"], self.vol_window).iloc[train_start:train_end]
        self.vol_threshold = float(vol.dropna().quantile(self.vol_quantile)) if vol.notna().any() else None

    def positions(self, data: Any, start: int, end: int) -> np.ndarray:
        candles = data.candles.iloc[:end]
        close = pd.to_numeric(candles["close"], errors="coerce")
        closev = close.to_numpy("float64")
        slow = ti.ema(close, self.trend_slow).to_numpy("float64")
        rate = _funding_rate_by_bar(data, candles)
        keep = (closev > slow) & np.isfinite(slow)
        keep &= np.isnan(rate) | (rate <= self.funding_max)
        if self.vol_threshold is not None and np.isfinite(self.vol_threshold):
            vol = ti.rolling_volatility(close, self.vol_window).to_numpy("float64")
            keep &= np.isfinite(vol) & (vol <= self.vol_threshold)
        pos = _apply_exit_persistence(keep, exit_confirm=self.exit_confirm, min_hold=self.min_hold)
        return pos[start:end].astype("float64")
