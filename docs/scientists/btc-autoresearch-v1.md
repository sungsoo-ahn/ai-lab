# BTC AutoResearch v1

<div class="run-metadata">
<p><strong>Date:</strong> 2026-06-10 00:27 KST</p>
<p><strong>Status:</strong> active</p>
<p><strong>Task:</strong> btc</p>
</div>

## Plain-English Summary

The overnight BTC scientist orchestration completed the readiness and baseline gate, built local BTCUSDT data, reproduced the documented baseline configuration, extended the score-search ledger to 100 trials, and audited the strongest new H=1 candidate.

No sealed holdout was used. No live trading, orders, private API keys, or accounting, cost, timestamp, or split-rule changes were used.

## Current Result

Best headline candidate from the 100-trial ledger:

- `t094_f321ec793728`: `returns_only`, `H=1`, `long_cash`, `cost_aware`, lambda `5.0`
- Net `+231.1%`, Sharpe `1.05`, max drawdown `-38%`, trades `25`
- Beats reproduced `t054` on net return and Sharpe, and beats buy-and-hold over the same OOS window
- Custom pre-holdout audit recommendation: `NEEDS_REFINEMENT`

Reason not promoted: only `6/14` folds were positive and profit concentration top-5 was `0.887`.

## Baseline Status

The baseline configuration `t054` reproduced exactly in the local run as:

- `technical_core`, `H=1`, `long_cash`, `cost_aware`, lambda `3.0`
- Net `+94.0%`, Sharpe `0.71`, max drawdown `-41%`, trades `70`
- M5.5 audit: `READY_FOR_ONE_SHOT_HOLDOUT`
- Funding-aware net: `+72.4%`
- Fold-positive `8/14`; PBO `0.4127`; comparable DSR `0.4570`

This differs from the originally documented `+60.0%` baseline, likely because the local data build now runs through `2026-05-31` while the documentation was static.

## Search Ledger

- 60-trial gate: `ACCEPT=16`, `NEEDS_REFINEMENT=34`, `REJECT=10`
- 100-trial extension: `ACCEPT=29`, `NEEDS_REFINEMENT=56`, `REJECT=15`
- Failed and rejected trials remain in the ledger.
- Main ledger: `sources/checkouts/btc_autoresearch/results/reports/m5_autoresearch/trial_ledger.parquet`
- Main generated report: `sources/checkouts/btc_autoresearch/results/reports/m5_autoresearch/report.md`
- Custom `t094` audit: `sources/checkouts/btc_autoresearch/results_t094_audit/reports/m5_5_audit/report.md`

## Work Units

| Work Unit | Status | Result | Next Step |
| --- | --- | --- | --- |
| [`baseline_reproduction`](../work-units/baseline-reproduction.md) | complete | Readiness gate passed; `t054` reproduced locally at `+94.0%`; audit ready for one-shot holdout | Use local reproduced baseline for comparable research |
| [`pipeline_audit`](../work-units/pipeline-audit.md) | complete | No accounting/split/holdout blocker found; report wording and candidate-dir hygiene caveats recorded | Fix report wording and candidate cleanup before the next long run |
| [`horizon_h4_audit`](../work-units/horizon-h4-audit.md) | complete | H=4 default winners weaken sharply under horizon-matched holding | Integrate horizon-matched H>1 ranking before promoting H>1 |
| [`regime_filter_probe`](../work-units/regime-filter-probe.md) | complete | `t094` has strong net/cost/random metrics but weak fold coverage and high concentration | Run a narrow robustness work unit around `t094` |
| [`report_synthesis`](../work-units/report-synthesis.md) | complete | Reports updated and safety status recorded | Continue with robustness work, not holdout |

## Assets

| Asset | Type | Role | Limits |
| --- | --- | --- | --- |
| `upstream_repo` | code_repo | Source ref and shared checkout for optimized code | Commit SHA is authoritative; checkout may contain ignored generated data/results and a scientist-local `.venv` |
| `btcusdt_futures_1h_dataset` | dataset | Main ML/backtest dataset | Built locally from Binance public data; range starts at 2020-01-01 |
| `baseline_t054` | result_bundle | Baseline comparison | Reproduced locally with updated metrics; still below buy-and-hold |

## Open Questions

- Can a `t094`-family candidate reduce profit concentration while preserving its cost robustness?
- Should H>1 horizon-matched holding become a first-class decision mode in the search grid?
- Should the generated M5 report wording and stale candidate-file cleanup be patched before the next overnight run?

## Overnight Run

Run ID: `overnight-2026-06-09`

Runbook: `overnight-runbook.md`

Safety status: sealed holdout unused; no live trading; no private API keys; no backtester/accounting changes.
