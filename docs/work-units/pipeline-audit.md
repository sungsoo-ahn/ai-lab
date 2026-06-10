# Work Unit: Pipeline Audit

<div class="run-metadata">
<p><strong>Date:</strong> 2026-06-10 00:27 KST</p>
<p><strong>Status:</strong> complete</p>
<p><strong>Type:</strong> observation</p>
</div>

## Purpose

Audit leakage, cost, holdout, and reproducibility risks; produce actionable blockers and safe next steps.

## Commands Run

```sh
cd sources/checkouts/btc_autoresearch
rg -n "sealed|holdout|use_sealed|sealed_holdout|funding|fee_bps|slippage|turnover|timestamp|shift|future|leak|drop_duplicates|searchsorted|embargo|purge" src tests scripts configs README.md competition_guide.md
sed -n '1,300p' src/backtest/backtester.py
sed -n '1,260p' src/backtest/walk_forward.py
sed -n '1,240p' src/labels/fixed_horizon.py
sed -n '1,260p' src/features/feature_builder.py
sed -n '1,220p' src/backtest/cost_model.py
sed -n '1,220p' src/decisions/horizon_matched.py
```

## Findings

- No evaluation/accounting code was modified during the run.
- The test suite covers walk-forward ordering, purge/embargo, sealed holdout exclusion, timestamp uniqueness, cost turnover accounting, funding-event boundary handling, and H>1 horizon-matched holding helpers.
- `generate_splits` carves out the last six months as sealed holdout and caps test label endpoints before the holdout.
- Feature generation uses trailing/causal indicators and does not apply global scaling in the feature builder.
- Fixed-horizon labels use future closes only as labels and drop invalid/no-endpoint rows.
- Backtester charges turnover costs as `abs(p_t - p_{t-1}) * all_in_cost_bps / 10000`, validates sorted unique timestamps, and supports cost multiplier stress.
- Funding in the audit is applied as a secondary sanity check only; the main search still ranks on no-funding cost assumptions.

## Risks And Caveats

- The generated M5 report text still says "capped at 60" even after the 100-trial extension; the ledger and header count show `trials run: 100 / intended grid 108`, so this is a report wording bug, not an evaluation issue.
- The `results/experiments/m5_candidates/` directory retains candidate JSONs from earlier top-5 generations as well as the latest top-ranked candidates. Treat the ledger/report ranking as authoritative.
- H>1 default Mode-A candidates remain a modeling-mismatch risk unless horizon-matched holding is integrated into the main search objective.
- `t094` passes several robustness checks but is not ready because fold coverage and profit concentration are weak.

## Result

No blocker was found in the tested accounting, timestamp, split, or holdout rules. The main blockers are candidate robustness and reporting hygiene, not evidence of leakage or cost weakening in this run.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: yes
- Backtester/accounting rules changed: no
- Live trading/API keys used: no

## Recommendation

Next code work should be narrowly scoped to research-surface improvements: fix generated report wording/cleanup, integrate horizon-matched H>1 ranking, and add a concentration/fold-stability-aware objective for the `t094` family.
