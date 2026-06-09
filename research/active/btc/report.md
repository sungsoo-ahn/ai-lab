# Project Report: btc

Date: 2026-06-09
Status: active

## Plain-English Summary

This is the active BTC research project. The current workstream is a BTC trading AutoResearch repository. The goal of that workstream is to improve the current backtested BTCUSDT strategy candidate without weakening the evaluation rules.

The project is currently prepared for an overnight research run. The AutoResearch repository is cloned, the task constraints are extracted, the asset registry records the source repository, expected processed dataset, and baseline result, and five hypothesis/work-unit folders have been created.

## Current Result

No new candidate has been produced yet.

## Baseline To Beat

Candidate `t054` reports +60.0% net return, Sharpe 0.52, max drawdown -46%, and 104 trades under 1x cost assumptions. It has a `NEEDS_REFINEMENT` audit caveat and does not beat buy-and-hold over the same out-of-sample period.

## Hypotheses

| Hypothesis | Status | Result | Next Step |
| --- | --- | --- | --- |
| `baseline_reproduction` | active | No result yet | Verify environment, build required data, reproduce 60-trial baseline, run M5.5 audit |
| `pipeline_audit` | active | No result yet | Audit leakage, cost, holdout, and reproducibility risks |
| `horizon_h4_audit` | active | No result yet | Investigate H=4 horizon-matched lead after baseline artifacts exist |
| `regime_filter_probe` | active | No result yet | Try bounded volatility/regime-filter workstream after baseline reproduction |
| `report_synthesis` | active | No result yet | Summarize overnight results and update project reports |

## Assets

| Asset | Type | Role | Limits |
| --- | --- | --- | --- |
| `upstream_repo` | code_repo | Source code and documentation | Local clone may diverge |
| `btcusdt_futures_1h_dataset` | dataset | Main ML/backtest dataset | May need to be built locally |
| `baseline_t054` | result_bundle | Baseline comparison | Needs refinement and may be overfit |

## Open Questions

- Can the current baseline be reproduced locally without touching sealed holdout data?
- Which work units should continue after baseline reproduction is known?

## Overnight Run

Run ID: `overnight-2026-06-09`

Runbook: `overnight-runbook.md`

Autonomy: full research loop with silent Python package installs through project-local `uv` workflows. OS-level tools, Node, Docker, connector integrations, shell config, and account config still require explicit approval.
