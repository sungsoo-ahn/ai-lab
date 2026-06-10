# Hypothesis Guide: Pipeline Audit

Date: 2026-06-10
Status: complete

## Purpose

This work unit audits leakage, cost, holdout, and reproducibility risks in the BTC AutoResearch pipeline.

## Reading Order

1. `guide.md`
2. `report.md`
3. `hypothesis.yaml`
4. project `source-map.md`
5. relevant run records under project `runs/`

## How To Continue

Use the audit findings as guardrails before running longer searches. Fix report wording and stale candidate cleanup before the next long run if they become operational blockers.

## Evidence And Assets

Reference project assets by `asset_id`; this work unit mainly uses the upstream repo, local dataset, generated reports, and audit outputs.

## Do Not Store

Do not store secrets, raw credentials, private connector content, or unnecessary personal data in this hypothesis.
