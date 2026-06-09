# Project: btc

Date: 2026-06-09
Status: active

## Overview

This is the active BTC research project. It can contain multiple BTC-related research workstreams, assets, hypotheses, and reports.

The current workstream uses a BTC short-horizon trading AutoResearch repository. That repository searches over features, models, and decision rules, then evaluates candidates with walk-forward backtests.

The current workstream is research and backtesting only. It must not implement live trading, place orders, use private API keys, or present results as financial advice.

## Goal

Maintain a restartable BTC research workspace. For the current AutoResearch workstream, find a better backtested BTCUSDT candidate than the current baseline while preserving causal, comparable, cost-correct evaluation.

## Baseline

The current baseline is candidate `t054`: `technical_core`, horizon `H=1`, `long_cash`, `cost_aware`, lambda `3.0`, XGBoost regression, BTCUSDT USD-M futures, 1h timeframe.

Reported baseline metrics:

- Net return: +60.0%
- Sharpe: 0.52
- Max drawdown: -46%
- Trades: 104
- Cost sensitivity: 0x +97%, 1x +60%, 2x +30%, 3x +6%

## Success Criteria

- Candidate beats `t054` under the official backtester and 1x cost assumptions.
- Candidate survives cost sensitivity and random turnover-matched baseline checks.
- Failed trials stay visible in the ledger.
- Sealed holdout is not used during research.
- Evaluation remains causal and leakage-controlled.

## Current State

The AutoResearch source repository has been cloned and the task has been extracted into `task.md`. The next useful step is to inspect and verify the existing implemented search and audit pipeline before modifying strategy logic.
