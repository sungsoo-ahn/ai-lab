# Work Unit: BTC Benchmark EMA Regime Robustness

<div class="run-metadata">
<p><strong>Work Unit ID:</strong> ema_regime_robustness</p>
<p><strong>Scientist:</strong> btc_benchmark_v2</p>
<p><strong>Status:</strong> complete</p>
<p><strong>Date:</strong> 2026-06-10 KST</p>
</div>

## Purpose

Check whether the strong EMA-regime result was a narrow search artifact or part of a stable high-performing region.

## Method

The work unit screened 1,296 EMA variants around the initial best family, gated the top 8 candidates, and then verified the exported final class directly through the benchmark runner. A final exhaustive future-perturbation gate run used `gate_max_cutoffs=None`.

## Result

Promoted candidate:

- class: `agentic.strategies.rule_strategies:BestEmaRegimeV2`
- strategy: `ema_regime_f12_s1440_b0.025_h72_long_cash`
- net: `+324.3%`
- Sharpe: `1.453`
- Sortino: `1.291`
- max drawdown: `-25.1%`
- trades: `28`
- turnover: `56`
- exposure: `47.1%`
- 5x-cost net: `+238.9%`
- funding-aware net: `+252.8%`
- random turnover-matched percentile: `0.99`
- buy-hold net: `+150.3%`
- default gates: all 14 folds passed
- exhaustive future-perturbation: passed with at least 2,160 cutoffs per fold

Top gated alternatives also passed, with nets from `+284.6%` to `+310.9%`, so the chosen candidate was not isolated.

## Safety Checklist

- Referee/backtester changed: no
- Failed trials preserved: yes
- Sealed holdout used: no
- Live trading/API keys used: no

## Implementation References

- Work-unit report: `tasks/active/btc_benchmark/scientists/btc_benchmark_v2/work_units/ema_regime_robustness/report.md`
- Robustness script: `sources/checkouts/btc_agentic_system/scripts/ema_robustness.py`
- Result artifacts: `sources/checkouts/btc_agentic_system/results/ema_robustness/`
