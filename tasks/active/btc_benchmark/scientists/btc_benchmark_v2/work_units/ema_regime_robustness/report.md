# Work Unit Report: ema_regime_robustness

Date: 2026-06-10
Status: complete

## Purpose

Check whether the current best EMA-regime candidate is robust or a narrow search artifact.

## Commands Run

```sh
cd /Users/sungs/ai-lab/sources/checkouts/btc_agentic_system
BTC_BENCHMARK_REPO=/Users/sungs/ai-lab/sources/checkouts/btc_benchmark uv run --with-editable . --with-editable /Users/sungs/ai-lab/sources/checkouts/btc_benchmark python -m scripts.ema_robustness --benchmark-repo /Users/sungs/ai-lab/sources/checkouts/btc_benchmark --team ai_lab_v2 --top-gated 8
BTC_BENCHMARK_REPO=/Users/sungs/ai-lab/sources/checkouts/btc_benchmark uv run --with-editable . --with-editable /Users/sungs/ai-lab/sources/checkouts/btc_benchmark python -m scripts.run_benchmark --strategy agentic.strategies.rule_strategies:BestEmaRegimeV2 --team ai_lab_v2 --benchmark-repo /Users/sungs/ai-lab/sources/checkouts/btc_benchmark --no-sub-bars
```

## Package Installs

None.

## Files Changed

- Added `agentic.strategies.rule_strategies:BestEmaRegimeV2`.
- Added `scripts/ema_robustness.py`.
- Generated `results/ema_robustness/screened.csv`, `gated.csv`, `gated.json`, `gated_leaderboard.jsonl`, and `best_fold_attribution.csv`.

## Outputs

- Screened 1,296 EMA variants around the initial best family.
- Gated the top 8 candidates with the official benchmark gates.
- Directly verified exported class `BestEmaRegimeV2`.

## Result

Best candidate:

- class: `agentic.strategies.rule_strategies:BestEmaRegimeV2`
- strategy: `ema_regime_f12_s1440_b0.025_h72_long_cash`
- gates: passed on all 14 folds
- exhaustive future-perturbation gate: passed; minimum 2,160 cutoffs per fold
- disqualified: false
- net `+324.3%`
- Sharpe `1.453`; Sortino `1.291`
- max drawdown `-25.1%`
- trades `28`; turnover `56`; exposure `47.1%`
- cost stress: 0x `+348.8%`, 1x `+324.3%`, 2x `+301.2%`, 3x `+279.3%`, 5x `+238.9%`
- next-open net `+324.3%`
- funding-aware net `+252.8%`
- random turnover-matched percentile `0.99`
- buy-hold net `+150.3%`
- sealed holdout used: false

Top gated alternatives also passed, with nets from `+284.6%` to `+310.9%`, so the promoted candidate sits in a stable high-performing region rather than an isolated single point.

Fold attribution for V2 shows losses in early 2022 and mid-2024, but strong positive folds in 2023, Q1 2024, and late 2024; this is consistent with a long/cash trend regime filter rather than a uniformly profitable oracle-like profile.

The final V2 class also passed an exhaustive future-perturbation gate run via `run_benchmark(..., gate_max_cutoffs=None)`, reporting `future_perturbation_exhaustive: true` and `future_perturbation_cutoffs_min: 2160`.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: not applicable yet
- Backtester/accounting rules changed: no
- Live trading/API keys used: no

## Recommendation

Promote `BestEmaRegimeV2` as the current submission candidate. No external submission or GitHub write should be made without explicit user approval.
