# Project Report: btc_autoresearch

Date: 2026-06-09
Status: active

## Plain-English Summary

This project is an active research task on a BTC trading AutoResearch repository. The goal is to improve the current backtested BTCUSDT strategy candidate without weakening the evaluation rules.

The project is currently in setup and verification. The repository is cloned, the task constraints are extracted, and the asset registry now records the source repository, expected processed dataset, and baseline result.

## Current Result

No new candidate has been produced yet.

## Baseline To Beat

Candidate `t054` reports +60.0% net return, Sharpe 0.52, max drawdown -46%, and 104 trades under 1x cost assumptions. It has a `NEEDS_REFINEMENT` audit caveat and does not beat buy-and-hold over the same out-of-sample period.

## Hypotheses

| Hypothesis | Status | Result | Next Step |
| --- | --- | --- | --- |
| None yet | not started | No hypothesis workspace exists yet | Inspect and verify the existing pipeline before choosing the first hypothesis |

## Assets

| Asset | Type | Role | Limits |
| --- | --- | --- | --- |
| `upstream_repo` | code_repo | Source code and documentation | Local clone may diverge |
| `btcusdt_futures_1h_dataset` | dataset | Main ML/backtest dataset | May need to be built locally |
| `baseline_t054` | result_bundle | Baseline comparison | Needs refinement and may be overfit |

## Open Questions

- Can the current baseline be reproduced locally without touching sealed holdout data?
- Which first hypothesis should be tested after verifying the pipeline?
