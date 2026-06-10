# Work Unit Guide: Report Synthesis

Date: 2026-06-10
Status: complete

## Purpose

This work unit consolidates the overnight BTC research findings into user-facing reports and next actions.

## Method Overview

Report synthesis reads the completed work-unit outputs, source pointers, generated ledgers, and audit results, then updates the scientist-level narrative. Its job is to make the current state understandable without requiring the user to inspect every run artifact. It should preserve negative findings and safety caveats, not only headline winners.

## Key Terms

- `source map`: the file that records source and artifact pointers used to support claims.
- `work unit`: a focused work unit, audit, experiment, or synthesis pass within the scientist.
- `promotion`: moving a candidate or finding to a stronger decision stage, such as holdout review.
- `negative finding`: evidence that something did not work or should not be promoted.

## Decision Criteria

- The synthesized report should state the current best result and why it is or is not promotable.
- Safety status should be explicit, especially sealed holdout, live trading, private keys, and accounting changes.
- Next steps should be operationally specific enough for a future session to continue.

## Reading Order

1. `guide.md`
2. `report.md`
3. `work-unit.yaml`
4. scientist `report.md`
5. scientist `source-map.md`

## How To Continue

Use the synthesized scientist report as the current starting point. Continue with robustness work, not a sealed holdout.

## Evidence And Assets

Reference scientist assets by `asset_id`; this work unit summarizes the reports, ledgers, audit outputs, and run records from the overnight pass.

## Do Not Store

Do not store secrets, raw credentials, private connector content, or unnecessary personal data in this work unit.
