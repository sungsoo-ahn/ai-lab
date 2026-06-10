# Trial t094: Strong Candidate, Needs Refinement

<div class="run-metadata">
<p><strong>Status:</strong> needs refinement</p>
<p><strong>Trial ID:</strong> t094_f321ec793728</p>
<p><strong>Role:</strong> next robustness seed</p>
</div>

## Run Summary

`t094` is the strongest H=1 candidate from the 100-trial ledger after rejecting a more extreme too-few-trades point. It beats the reproduced baseline on headline return and Sharpe, but it is not ready for promotion.

## Hypothesis

A sparse returns-only H=1 long/cash candidate can preserve signal under transaction-cost stress while avoiding the fragility of long/short overtrading.

## Config Snippet

```yaml
feature_preset: returns_only
horizon: 1
mode: long_cash
decision: cost_aware
lambda: 5.0
trades: 25
sealed_holdout_used: false
```

## Raw Agent Trace Excerpt

The candidate is promising on net return, cost stress, random rank, execution-mode robustness, and buy-and-hold comparison, but it remains `NEEDS_REFINEMENT`: fold-positive is only `6/14`, fold Sharpe dispersion is high, and profit concentration top-5 is `0.887`.

## Metrics

| Metric | Value |
| --- | ---: |
| Net return | +231.1% |
| Sharpe | 1.05 |
| Max drawdown | -37.9% |
| Trades | 25 |
| Cost 2x net | +215.2% |
| Funding-aware net | +184.4% |
| Random percentile rank | 0.964 |
| Profit concentration top-5 | 0.887 |

## Interpretation

This point is valuable because it identifies a research direction, not because it is ready to ship. The key risk is concentration: too much of the result may come from a few trades or narrow regimes.

## Decision

Do not promote to holdout. Use as the next narrow robustness seed.

## Suggested Next Action

Search the `t094` family for lower concentration and better fold coverage without changing accounting, cost, timestamp, or split rules.
