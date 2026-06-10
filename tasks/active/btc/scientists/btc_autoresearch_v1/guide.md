# Scientist Guide: BTC Research

Date: 2026-06-10
Status: active

## Purpose

This scientist keeps BTC research restartable and auditable. The current workstream is the BTCUSDT short-horizon AutoResearch pipeline.

## Method Overview

The current method searches for short-horizon BTCUSDT trading candidates in a local AutoResearch repository. A candidate is a specific combination of features, prediction horizon, model settings, trading mode, and cost assumptions. The scientist builds public Binance futures data, trains and evaluates candidates over walk-forward time splits, and compares them against a reproduced baseline before any sealed holdout is touched.

The workflow is intentionally conservative:

1. Reproduce the baseline locally.
2. Audit data, timestamp, cost, and split assumptions.
3. Run bounded searches that keep failed and rejected trials visible.
4. Inspect promising candidates for fold stability, cost sensitivity, random-baseline comparison, drawdown, and profit concentration.
5. Promote nothing to holdout until the report says the candidate is robust enough.

## Key Terms

- `BTCUSDT`: Bitcoin priced against USDT. In this scientist it refers to Binance futures market data, not spot exchange data.
- `AutoResearch`: the local research pipeline that generates features, trains models, runs backtests, and records trial ledgers.
- `candidate`: one tested trading configuration, including feature set, horizon, trade direction rules, cost setting, and model parameters.
- `baseline`: the known comparison configuration. Current reports use reproduced `t054` as the main local baseline.
- `walk-forward split`: a time-series evaluation pattern that trains on earlier data and tests on later data to reduce lookahead bias.
- `sealed holdout`: final reserved data that must not be used during exploratory research.
- `cost-aware`: evaluation that includes transaction-cost assumptions rather than ignoring fees/slippage.
- `fold`: one train/test window in the walk-forward evaluation.
- `profit concentration`: how much of a candidate's result comes from a small number of trades. High concentration means the result may be fragile.

## Assumptions

- Research uses public data and local artifacts only.
- Backtests are research evidence, not live-trading authorization.
- Comparisons are meaningful only when timestamp alignment, split policy, and cost accounting stay comparable.
- A strong headline return is not enough; stability and robustness drive promotion decisions.

## Reading Order

1. `guide.md`
2. `report.md`
3. `source-map.md`
4. `assets.yaml`
5. relevant `work_units/<work_unit_id>/guide.md`

## How To Continue

Start from the current scientist report. The next safe research action is a narrow robustness pass around the `t094` family before any sealed holdout decision.

## Safety Rules

- Do not use the sealed holdout during exploratory research.
- Do not introduce live trading, orders, private API keys, or account credentials.
- Preserve timestamp alignment, split policy, cost accounting, and comparable backtester settings unless the report explicitly scopes an audit.

## Key Places

- `report.md`: current user-facing scientist state.
- `source-map.md`: source and artifact pointers.
- `assets.yaml`: registered datasets, repositories, and result bundles.
- `work_units/`: focused work-unit guides and reports.
- `runs/`: run records for larger research passes.

## Do Not Store

Do not store secrets, raw credentials, private connector content, or unnecessary personal data in this scientist.
