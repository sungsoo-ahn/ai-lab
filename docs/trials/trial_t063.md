# Trial t063: H4 Candidate With Horizon Caveat

<div class="run-metadata">
<p><strong>Status:</strong> accepted with caveat</p>
<p><strong>Trial ID:</strong> t063_72e951d8c632</p>
<p><strong>Role:</strong> H&gt;1 evaluation warning</p>
</div>

## Run Summary

`t063` looks strong under the default H=4 score-search evaluation, but the horizon-matched audit changes the interpretation.

## Hypothesis

A volume-core H=4 long/short candidate can improve the BTC score search by using a longer forecast horizon.

## Config Snippet

```yaml
feature_preset: volume_core
horizon: 4
mode: long_short
decision: cost_aware
lambda: 3.0
default_execution: 1_bar_rebalanced
sealed_holdout_used: false
```

## Raw Agent Trace Excerpt

H=4 default candidates are not reliable as headline improvements because the default pipeline applies H-bar forecasts to 1-bar-rebalanced positions. Horizon-matched holding materially weakens the lead.

## Metrics

| Metric | Default Evaluation | Horizon-Matched Audit |
| --- | ---: | ---: |
| Net return | +155.6% | -3.9% |
| Sharpe | 0.78 | 0.23 |
| Trades | 143 | 57 |

## Interpretation

The default plot point is useful as a warning. It shows why score-search plots need companion audit work units. A point can look attractive under one evaluation mode and fail once the holding rule matches the forecast horizon.

## Decision

Do not promote H>1 candidates until horizon-matched holding is part of the primary ranking path.

## Suggested Next Action

Integrate horizon-matched H>1 ranking before treating H=4 candidates as comparable to H=1 candidates.
