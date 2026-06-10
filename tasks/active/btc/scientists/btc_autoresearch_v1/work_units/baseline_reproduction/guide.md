# Work Unit Guide: Baseline Reproduction

Date: 2026-06-10
Status: complete

## Purpose

This work unit verifies that the BTC AutoResearch baseline and readiness gates can be reproduced locally before comparing new candidates.

## Method Overview

Baseline reproduction reruns the documented BTC AutoResearch setup in the current local environment. It checks whether required data can be built, tests pass, and the known baseline configuration can be evaluated with the same decision machinery used for future candidates. The goal is not to discover a new winner; it is to establish a trustworthy comparison point.

## Key Terms

- `readiness gate`: a pre-search check that verifies the pipeline is healthy enough to run comparisons.
- `baseline_t054`: the reproduced reference candidate used as the local comparison target.
- `M5.5 audit`: the audit step that reviews candidate robustness before any one-shot holdout decision.
- `funding-aware net`: performance adjusted for futures funding effects, when available.

## Decision Criteria

- The baseline should reproduce under the official pipeline without private data or accounting changes.
- The run should preserve sealed-holdout protection.
- Future candidates should be compared against the reproduced local baseline, not only against old static documentation.

## Reading Order

1. `guide.md`
2. `report.md`
3. `work unit.yaml`
4. scientist `source-map.md`
5. relevant run records under scientist `runs/`

## How To Continue

Use the reproduced local baseline as the comparison point for future BTC AutoResearch work. Do not rerun the sealed holdout from this work unit.

## Evidence And Assets

The main assets are `upstream_repo`, `btcusdt_futures_1h_dataset`, and the reproduced `baseline_t054` result bundle.

## Do Not Store

Do not store secrets, raw credentials, private connector content, or unnecessary personal data in this work unit.
