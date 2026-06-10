# Scientist Report: btc_benchmark_v2

Date: 2026-06-10
Status: active

## Plain-English Summary

This scientist is assigned to solve the frozen BTC 1h benchmark. The benchmark is split across two repositories: `btc_benchmark` is the frozen referee, while `btc_agentic_system` is the mutable participant strategy package.

Initial source discovery found a setup blocker in the benchmark checkout: `pyproject.toml` lists `btc_benchmark.data`, tests import `btc_benchmark.data.*`, and `scripts/bootstrap_data.py` calls `btc_benchmark.data.*`, but the tracked repository at git `166a99f0e915ba1aaaaa6da9451dfa90c49032a6` does not include `btc_benchmark/data`. The local checkout has been repaired by transplanting the missing data package from the documented `btc_autoresearch` lineage while leaving benchmark scoring, gates, backtester, costs, and splits unchanged.

## Current Result

Current best gated candidate:

- `agentic.strategies.rule_strategies:BestEmaRegimeV2`
- strategy name: `ema_regime_f12_s1440_b0.025_h72_long_cash`
- benchmark version: `1.0.0`
- gates: passed on all 14 folds; not disqualified
- exhaustive future-perturbation gate: passed; minimum 2,160 cutoffs per fold
- dev OOS: 2022-04-01 00:00 UTC to 2025-09-30 23:00 UTC
- net `+324.3%`, Sharpe `1.453`, Sortino `1.291`, max drawdown `-25.1%`
- trades `28`, turnover `56`, exposure `47.1%`
- cost stress: 0x `+348.8%`, 1x `+324.3%`, 2x `+301.2%`, 3x `+279.3%`, 5x `+238.9%`
- next-open net `+324.3%`, funding-aware net `+252.8%`
- random turnover-matched percentile `0.99`
- buy-and-hold over same dev OOS: `+150.3%`
- sealed holdout used: `False`

## Target Metric

Primary metric: official benchmark dev `net` from `btc_benchmark.benchmark.runner.run_benchmark`, maximized only among non-disqualified strategies.

Required companion evidence for any promoted candidate:

- causality gates passed on all folds
- Sharpe, max drawdown, turnover, trades, exposure, and buy-hold comparison
- cost stress at 0x, 1x, 2x, 3x, and 5x
- next-open net and funding-aware net when funding data exists
- random turnover-matched percentile
- per-year metrics
- `sealed_holdout_used: False`

## Work Units

| Work Unit | Status | Result | Next Step |
| --- | --- | --- | --- |
| `referee_reproduction` | complete | Local referee repaired; test suite passes `131 passed, 1 skipped`; loader sees 56,232 candles and 7,367 funding events | Keep scoring/gates unchanged |
| `bundled_baselines` | complete | `EmaTrend` gates passed but loses `-81.7%`; `XgbMomentum` blocked by missing OS `libomp.dylib` | Avoid XGBoost unless user approves Homebrew `libomp` install |
| `strategy_search` | complete | First dependency-light search found gated `BestEmaRegimeV1` at `+260.5%` net | Superseded by robustness-promoted V2 |
| `ema_regime_robustness` | complete | 1,296 EMA variants screened; top 8 gated; `BestEmaRegimeV2` verified at `+324.3%` net | Use V2 for submission preparation and final evidence |
| `report_synthesis` | active | Current report updated with best candidate | Keep reports and source map current |

## Commands Run

```sh
git clone https://github.com/YoonhoKim0527/btc_benchmark.git sources/checkouts/btc_benchmark
git clone https://github.com/YoonhoKim0527/btc_agentic_system.git sources/checkouts/btc_agentic_system
cd /Users/sungs/ai-lab/sources/checkouts/btc_benchmark
uv run --with-editable . --extra dev pytest
cd /Users/sungs/ai-lab/sources/checkouts/btc_agentic_system
BTC_BENCHMARK_REPO=/Users/sungs/ai-lab/sources/checkouts/btc_benchmark uv run --with-editable . --with-editable /Users/sungs/ai-lab/sources/checkouts/btc_benchmark python -m scripts.search_rules --benchmark-repo /Users/sungs/ai-lab/sources/checkouts/btc_benchmark --team ai_lab_v2 --limit 160 --top-gated 5
BTC_BENCHMARK_REPO=/Users/sungs/ai-lab/sources/checkouts/btc_benchmark uv run --with-editable . --with-editable /Users/sungs/ai-lab/sources/checkouts/btc_benchmark python -m scripts.run_benchmark --strategy agentic.strategies.rule_strategies:BestEmaRegimeV1 --team ai_lab_v2 --benchmark-repo /Users/sungs/ai-lab/sources/checkouts/btc_benchmark --no-sub-bars
BTC_BENCHMARK_REPO=/Users/sungs/ai-lab/sources/checkouts/btc_benchmark uv run --with-editable . --with-editable /Users/sungs/ai-lab/sources/checkouts/btc_benchmark python -m scripts.ema_robustness --benchmark-repo /Users/sungs/ai-lab/sources/checkouts/btc_benchmark --team ai_lab_v2 --top-gated 8
BTC_BENCHMARK_REPO=/Users/sungs/ai-lab/sources/checkouts/btc_benchmark uv run --with-editable . --with-editable /Users/sungs/ai-lab/sources/checkouts/btc_benchmark python -m scripts.run_benchmark --strategy agentic.strategies.rule_strategies:BestEmaRegimeV2 --team ai_lab_v2 --benchmark-repo /Users/sungs/ai-lab/sources/checkouts/btc_benchmark --no-sub-bars
# Also verified by direct Python call with run_benchmark(..., gate_max_cutoffs=None): exhaustive gates passed, future_perturbation_cutoffs_min=2160.
```

## Setup Evidence

The original referee install failed with:

```text
error: package directory 'btc_benchmark/data' does not exist
```

After local data-package repair from lineage, referee verification passed:

```text
131 passed, 1 skipped
```

## Open Questions

- Does the upstream benchmark repo intentionally omit data modules, or is the public checkout incomplete?
- What is the benchmark host's submission mechanism? No external submission will be attempted without explicit user approval.
- Should we install Homebrew `libomp` to evaluate the bundled XGBoost baseline and possible XGBoost-derived strategies?
