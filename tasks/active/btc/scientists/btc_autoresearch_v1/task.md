# BTC Scientist AutoResearch Workstream Task Extraction

Date: 2026-06-09
Repository: https://github.com/YoonhoKim0527/btc_autoresearch.git
Source ID: `btc_autoresearch`
Shared checkout: `/Users/sungs/ai-lab/sources/checkouts/btc_autoresearch`
Git ref: `ca251130e1f97b6233ceb957cb85e209bc136073`

## Task

Improve the existing BTC short-horizon trading AutoResearch pipeline to discover a better backtested BTCUSDT candidate than the current baseline, while preserving causal, comparable, cost-correct evaluation.

This is a research and backtesting task only. Do not implement live trading, place orders, use private API keys, or treat results as financial advice.

## Target Setup

- Market: Binance USD-M BTCUSDT perpetual futures.
- Primary timeframe: 1h.
- Evaluation: historical backtest only.
- Information rule: strategies may use only information available up to the current completed candle.
- Position space: long/cash/short depending on experiment config.
- Primary objective: maximize backtested net return under the official backtester and 1x cost assumptions.
- Default AutoResearch budget: 100 trials for comparable main results.

## Baseline To Beat

Current baseline candidate:

- Candidate ID: `t054`
- Feature preset: `technical_core`
- Horizon: `H=1`
- Mode: `long_cash`
- Decision rule: `cost_aware`
- Lambda: `3.0`
- Model: XGBoost regression
- Timeframe: 1h
- Market: BTCUSDT USD-M futures

Reported baseline:

- Net return: +60.0%
- Sharpe: 0.52
- Max drawdown: -46%
- Trades: 104
- Cost sensitivity: 0x +97%, 1x +60%, 2x +30%, 3x +6%

Important caveat: the baseline does not beat buy-and-hold over the same bull-heavy OOS period and has an audit verdict of `NEEDS_REFINEMENT`, with overfit risk after the 60-trial search.

## Valid Change Surface

Allowed areas to modify or extend:

- Feature sets and feature presets
- Model families and hyperparameters
- Search spaces and trial scheduling
- Decision rules, thresholds, cost-aware rules
- Regime, volatility, risk, and drawdown filters
- Position sizing logic
- Ranking/objective functions
- Reviewer/falsifier rules
- Candidate selection logic
- Report generation

Do not modify core evaluation rules to improve reported performance.

## Invalid Or Forbidden Changes

Do not change:

- Backtester accounting logic
- Transaction cost accounting
- Turnover definition
- Return calculation convention
- Data validation or timestamp alignment rules
- Walk-forward split logic, except to make it stricter
- Sealed holdout protection
- Historical candle data to remove bad periods
- Feature or label logic in a way that uses future information

Strictly forbidden:

- Future candles or target labels as features
- Fitting preprocessors on full train+test data
- Using test folds for hyperparameter selection without reporting it
- Deleting failed trials from the trial ledger
- Reporting only winning runs while hiding failed runs
- Reducing transaction costs without clear reporting
- Using sealed holdout data during research

## Recommended First Search Scope

- Timeframe: 1h
- Market: `futures_um BTCUSDT`
- Horizons: `H=1`, `H=4`, `H=12`
- Modes: `long_cash`, `long_short`
- Decision rules: `sign`, `cost_aware`
- Cost-aware lambda: `0.5`, `1.0`, `2.0`, `3.0`, `5.0`
- Feature presets: `returns_only`, `technical_core`, `volume_core`, `derivatives_light` if properly wired and validated
- Models: existing XGBoost; optionally add LightGBM, logistic/classification baselines, or simple ensembles

Avoid expanding the search aggressively before verifying that new degrees of freedom do not introduce overfitting.

## Required Result Summary

Any candidate result should report:

- Candidate name or ID
- Feature preset
- Model
- Horizon
- Decision rule
- Mode
- Lambda or threshold
- Net return
- Sharpe
- Max drawdown
- Calmar if available
- Number of trades
- Turnover
- Cost sensitivity from 0x through 3x
- Random turnover-matched baseline comparison
- Fold-level stability
- Whether sealed holdout was used
- Known limitations

Main reported results should also disclose:

- Number of trials attempted
- Number of accepted candidates
- Number of rejected candidates
- Number of needs-refinement candidates
- Whether failed trials remain in the ledger

## Validity Checklist

Before claiming improvement over the baseline:

- All tests pass.
- Sealed holdout was not used during research.
- No train/test leakage.
- No future feature leakage.
- No target alignment bug.
- No scaler fit on full data.
- No hidden cost reduction.
- No backtester modification.
- Failed trials are preserved.
- Candidate beats turnover-matched random baseline.
- Candidate survives at least 2x cost reasonably.
- Performance is not concentrated in only one or two trades.

## High-Priority Improvement Leads

1. Improve `t054`-style `H=1`, `long_cash`, `cost_aware` strategies.
2. Add or audit `next_open_conservative` robustness.
3. Add funding-aware evaluation.
4. Add volatility or regime filters.
5. Add drawdown kill-switch logic.
6. Add stronger feature presets.
7. Add LightGBM or CatBoost baselines if package changes are approved.
8. Add DSR/PBO or multiple-testing-aware ranking.
9. Improve horizon-matched holding for `H>1`.
10. Add robust candidate audit reports.

## Immediate Research Interpretation

The next useful step is not to invent a single manual strategy. It is to inspect the existing implemented search and audit pipeline, verify its current reproducible baseline, then propose a tightly scoped improvement that stays within the allowed change surface and produces a comparable candidate report.
