# Project Guide: BTC Research

Date: 2026-06-10
Status: active

## Purpose

This project keeps BTC research restartable and auditable. The current workstream is the BTCUSDT short-horizon AutoResearch pipeline.

## Reading Order

1. `guide.md`
2. `report.md`
3. `source-map.md`
4. `assets.yaml`
5. relevant `hypotheses/<hypothesis_id>/guide.md`

## How To Continue

Start from the current project report. The next safe research action is a narrow robustness pass around the `t094` family before any sealed holdout decision.

## Safety Rules

- Do not use the sealed holdout during exploratory research.
- Do not introduce live trading, orders, private API keys, or account credentials.
- Preserve timestamp alignment, split policy, cost accounting, and comparable backtester settings unless the report explicitly scopes an audit.

## Key Places

- `report.md`: current user-facing project state.
- `source-map.md`: source and artifact pointers.
- `assets.yaml`: registered datasets, repositories, and result bundles.
- `hypotheses/`: focused work-unit guides and reports.
- `runs/`: run records for larger research passes.

## Do Not Store

Do not store secrets, raw credentials, private connector content, or unnecessary personal data in this project.
