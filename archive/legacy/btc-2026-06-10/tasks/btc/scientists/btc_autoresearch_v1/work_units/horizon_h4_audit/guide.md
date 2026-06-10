# Work Unit Guide: Horizon-Matched H4 Audit

Date: 2026-06-10
Status: complete

## Purpose

This work unit checks whether H=4 candidates remain strong when evaluated with horizon-matched holding logic.

## Method Overview

The audit compares H=4 candidate rankings against evaluation logic that better matches the intended four-hour prediction horizon. A candidate can look strong when the signal horizon and holding behavior are mismatched. This work unit tests whether the apparent advantage survives when the holding period is aligned with the horizon.

## Key Terms

- `H=4`: a prediction horizon four bars ahead. With 1h data, this means a four-hour forward horizon.
- `horizon-matched holding`: holding logic designed to match the prediction horizon instead of treating all horizons like one-bar signals.
- `ranking`: the ordering that decides which candidates look best and deserve deeper review.

## Decision Criteria

- H>1 candidates should not be promoted only because default ranking favors them.
- Horizon-matched results should be reviewed before treating H=4 as a durable improvement.
- If H=4 weakens under matched holding, future search logic should make that evaluation mode first-class.

## Reading Order

1. `guide.md`
2. `report.md`
3. `work-unit.yaml`
4. scientist `source-map.md`
5. relevant run records under scientist `runs/`

## How To Continue

Treat H>1 candidates cautiously until horizon-matched ranking is part of the first-class search and promotion logic.

## Evidence And Assets

Reference scientist assets by `asset_id`; this work unit mainly uses the upstream repo and the local BTCUSDT 1h dataset.

## Do Not Store

Do not store secrets, raw credentials, private connector content, or unnecessary personal data in this work unit.
