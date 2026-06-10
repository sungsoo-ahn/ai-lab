# Work Unit: BTC Benchmark Strategy Search

<div class="run-metadata">
<p><strong>Work Unit ID:</strong> strategy_search</p>
<p><strong>Scientist:</strong> btc_benchmark_v2</p>
<p><strong>Status:</strong> complete</p>
<p><strong>Date:</strong> 2026-06-10 KST</p>
</div>

## Purpose

Search for simple causal strategies that improve official dev score without adding new model or OS dependencies.

## Method

The work unit added dependency-light rule strategies and a bounded search script in the participant checkout. It screened candidates rapidly and gated promoted candidates with the official benchmark runner.

## Result

Initial best gated candidate:

- class: `agentic.strategies.rule_strategies:BestEmaRegimeV1`
- strategy: `ema_regime_f24_s1440_b0.02_h72_long_cash`
- net: `+260.5%`
- Sharpe: `1.295`
- max drawdown: `-27.4%`
- gates: all 14 folds passed

This result was superseded by the EMA robustness work unit, which promoted `BestEmaRegimeV2`.

## Safety Checklist

- Referee/backtester changed: no
- Failed trials preserved: yes
- Sealed holdout used: no
- Live trading/API keys used: no

## Implementation References

- Work-unit report: `tasks/active/btc_benchmark/scientists/btc_benchmark_v2/work_units/strategy_search/report.md`
- Search script: `sources/checkouts/btc_agentic_system/scripts/search_rules.py`
