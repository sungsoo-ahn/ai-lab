# Trial t054: Reproduced Baseline

<div class="run-metadata">
<p><strong>Status:</strong> accepted baseline</p>
<p><strong>Trial ID:</strong> t054_a19bd141e75b</p>
<p><strong>Role:</strong> local comparison baseline</p>
</div>

## Run Summary

`t054` reproduced the documented baseline configuration locally under the current data window and cost-aware evaluation rules.

## Hypothesis

The documented technical-core H=1 long/cash configuration can be reproduced and used as a comparable baseline for later BTC scientist work.

## Config Snippet

```yaml
feature_preset: technical_core
horizon: 1
mode: long_cash
decision: cost_aware
lambda: 3.0
cost_all_in_bps: 10
sealed_holdout_used: false
```

## Raw Agent Trace Excerpt

Readiness and baseline-reproduction gate passed. The local reproduced baseline should be used for comparable follow-up work, with the data-window difference disclosed.

## Metrics

| Metric | Value |
| --- | ---: |
| Net return | +94.0% |
| Sharpe | 0.71 |
| Max drawdown | -41.5% |
| Trades | 70 |
| Fold-positive | 8/14 |
| PBO | 0.4127 |
| Comparable DSR | 0.4570 |

## Interpretation

This is not the highest-return point, but it is the local reference point. It reproduced under preserved accounting, timestamp, split, and holdout rules.

## Decision

Use as the current local baseline.

## Suggested Next Action

Compare follow-up trials against this reproduced result rather than older static documentation.
