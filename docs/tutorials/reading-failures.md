# Reading Failures And Suspicious Trials

Failed and suspicious trials are useful evidence. A scientist that only preserves winning scores loses the context needed to improve.

## Compare Config Snippets

Start with the smallest differences:

- Feature preset
- Horizon
- Long/cash versus long/short mode
- Lambda or threshold settings
- Cost assumptions
- Split and holdout settings

If a trial improves only after changing accounting, timestamp alignment, or sealed holdout policy, treat the result as invalid until audited.

## Inspect Trace Snippets

Raw agent or report snippets help explain why a point was kept, rejected, or marked for rerun. Look for signs that the score came from an invalid shortcut:

- Too few trades.
- Profit concentrated in a small number of trades.
- H>1 forecasts evaluated with a mismatched holding rule.
- Cost sensitivity that collapses under stress.
- Fold performance that is unstable across time.

## Use Multiple Evidence Surfaces

A high point on the plot is a candidate for investigation, not a conclusion. Read the related work-unit reports:

- Pipeline audits check leakage and accounting.
- Horizon audits check whether the evaluation mode matches the prediction horizon.
- Robustness probes check concentration, fold stability, cost stress, and random baselines.
- Synthesis reports record next actions and negative findings.

## Status Labels

Use status labels as research decisions:

| Status | Meaning |
| --- | --- |
| `accepted_baseline` | A reproduced comparison point for later work. |
| `accepted` | Passed the current ledger filters, but may still need context. |
| `accepted_with_caveat` | Numerically useful but blocked by an audit caveat. |
| `needs_refinement` | Interesting enough to seed more work, not ready to promote. |
| `rejected` | Preserved as negative evidence. |

## Rerun Policy

Before promoting a trial, rerun it with multiple seeds or adjacent settings when possible. Do not use the sealed holdout during exploratory reruns. If a result depends on a small number of trades or a narrow period, mark it `needs_refinement` or `rejected` rather than treating it as progress.
