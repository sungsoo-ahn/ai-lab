# Work Unit Guide: Pipeline Audit

Date: 2026-06-10
Status: complete

## Purpose

This work unit audits leakage, cost, holdout, and reproducibility risks in the BTC AutoResearch pipeline.

## Method Overview

The audit inspects whether the pipeline can accidentally overstate performance. It looks for lookahead leakage, timestamp mistakes, inconsistent cost accounting, unsafe holdout use, stale candidate files, and report wording that could mislead a future reader. The output is a set of blockers, caveats, and safe operating rules for future runs.

## Key Terms

- `leakage`: information from the future or test window accidentally entering training or features.
- `timestamp alignment`: making sure features, labels, predictions, and trades line up in causal time order.
- `cost accounting`: how fees, slippage, and related trading frictions are represented in backtests.
- `candidate-dir hygiene`: whether generated candidate artifacts are current, traceable, and not mixed with stale outputs.
- `blocker`: an issue serious enough to stop promotion or long runs until addressed.

## Decision Criteria

- Any leakage, holdout misuse, or accounting inflation is a blocker.
- Ambiguous report wording should be fixed before it becomes operationally misleading.
- Non-blocking hygiene issues should still be recorded so future runs do not inherit confusion.

## Reading Order

1. `guide.md`
2. `report.md`
3. `work-unit.yaml`
4. scientist `source-map.md`
5. relevant run records under scientist `runs/`

## How To Continue

Use the audit findings as guardrails before running longer searches. Fix report wording and stale candidate cleanup before the next long run if they become operational blockers.

## Evidence And Assets

Reference scientist assets by `asset_id`; this work unit mainly uses the upstream repo, local dataset, generated reports, and audit outputs.

## Do Not Store

Do not store secrets, raw credentials, private connector content, or unnecessary personal data in this work unit.
