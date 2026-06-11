from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd


EMA_GRID = (
    (96, 384),
    (120, 480),
    (144, 576),
    (168, 504),
    (168, 672),
    (168, 840),
    (192, 768),
    (216, 864),
    (240, 960),
)
ALL_IN_BPS = 10.0
FLOOR = 0.25
TAIL_BARS = 24 * 91
EDGE_THRESHOLD = 0.025


def _ema_long_cash(candles: pd.DataFrame, fast: int, slow: int) -> np.ndarray:
    close = pd.to_numeric(candles["close"], errors="coerce")
    fast_ema = close.ewm(span=fast, adjust=False, min_periods=fast).mean()
    slow_ema = close.ewm(span=slow, adjust=False, min_periods=slow).mean()
    pos = np.where(fast_ema.to_numpy() > slow_ema.to_numpy(), 1.0, 0.0)
    warmup = (fast_ema.isna() | slow_ema.isna()).to_numpy()
    return np.where(warmup, 0.0, pos).astype("float64")


def _net_return(close: np.ndarray, positions: np.ndarray, all_in_bps: float = ALL_IN_BPS) -> float:
    if len(close) < 2:
        return float("nan")
    ret = close[1:] / close[:-1] - 1.0
    pos = positions[:-1]
    prev = np.concatenate([[0.0], positions[:-2]])
    turnover = np.abs(pos - prev)
    net = pos * ret - turnover * (all_in_bps / 10000.0)
    return float(np.prod(1.0 + net) - 1.0)


def _floor_positions(base: np.ndarray, floor: float = FLOOR) -> np.ndarray:
    return floor + (1.0 - floor) * base


@dataclass
class PromotableConditionalFloorStrategy:
    name: str = "ema_selected_cond_floor25_tail3m_passive_edge_025pct_promoted"
    horizon: int = 1
    grid: tuple[tuple[int, int], ...] = EMA_GRID
    floor: float = FLOOR
    tail_bars: int = TAIL_BARS
    edge_threshold: float = EDGE_THRESHOLD
    selected: tuple[int, int] | None = None
    use_floor: bool = False
    audit_log: list[dict] = field(default_factory=list)

    def fit(self, data, train_start: int, train_end: int) -> None:
        train = data.candles.iloc[train_start:train_end]
        train_close = pd.to_numeric(train["close"], errors="coerce").to_numpy("float64")
        scored = []
        for fast, slow in self.grid:
            pos = _ema_long_cash(data.candles, fast, slow)[train_start:train_end]
            scored.append((_net_return(train_close, pos), fast, slow))
        scored.sort(key=lambda row: (row[0], -row[2], -row[1]), reverse=True)
        best_net, fast, slow = scored[0]
        self.selected = (fast, slow)

        tail_start = max(train_start, train_end - self.tail_bars)
        tail_close = pd.to_numeric(
            data.candles["close"].iloc[tail_start:train_end],
            errors="coerce",
        ).to_numpy("float64")
        base = _ema_long_cash(data.candles, fast, slow)[tail_start:train_end]
        passive = np.ones(train_end - tail_start, dtype="float64")
        floored = _floor_positions(base, self.floor)
        base_net = _net_return(tail_close, base)
        passive_net = _net_return(tail_close, passive)
        floor_net = _net_return(tail_close, floored)
        passive_edge = passive_net - base_net
        floor_edge = floor_net - base_net
        self.use_floor = bool(passive_edge > self.edge_threshold and floor_edge > 0.0)
        self.audit_log.append(
            {
                "train_start": int(train_start),
                "train_end": int(train_end),
                "tail_start": int(tail_start),
                "tail_bars": int(train_end - tail_start),
                "fast": int(fast),
                "slow": int(slow),
                "train_net": round(float(best_net), 6),
                "base_tail_net": round(float(base_net), 6),
                "passive_tail_net": round(float(passive_net), 6),
                "floor_tail_net": round(float(floor_net), 6),
                "passive_edge": round(float(passive_edge), 6),
                "floor_edge": round(float(floor_edge), 6),
                "edge_threshold": float(self.edge_threshold),
                "use_floor": self.use_floor,
            }
        )

    def positions(self, data, start: int, end: int) -> np.ndarray:
        if self.selected is None:
            raise RuntimeError("strategy must be fitted before positions are requested")
        fast, slow = self.selected
        base = _ema_long_cash(data.candles, fast, slow)[start:end]
        if self.use_floor:
            return _floor_positions(base, self.floor)
        return base
