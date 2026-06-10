# Work Unit Guide: Regime Filter Probe

Date: 2026-06-10
Status: complete

## Purpose

This work unit probes whether regime or volatility filtering can improve BTC AutoResearch candidates without weakening evaluation discipline.

## Method Overview

The probe searches for candidates whose trading behavior adapts to market conditions, such as volatility or regime filters. It then audits the strongest candidate family, currently `t094`, to see whether the attractive headline return is supported by enough positive folds, reasonable drawdown, cost robustness, and non-concentrated profits.

## Key Terms

- `regime filter`: a rule or feature that changes behavior depending on market state, such as trend or volatility.
- `volatility`: the size and variability of price movement. High volatility can create opportunity and risk.
- `t094`: the strongest headline candidate found in the 100-trial ledger, but not yet robust enough for promotion.
- `fold-positive`: how many walk-forward test folds made money. Low fold-positive counts suggest fragility.
- `Sharpe`: a return-to-risk metric. Higher is generally better, but it can be misleading when trades are sparse or concentrated.
- `max drawdown`: the largest peak-to-trough loss in the backtest.

## Decision Criteria

- A candidate needs more than high net return to advance.
- Weak fold coverage and high profit concentration argue for refinement, not holdout.
- Robustness work should focus on whether the `t094` family can reduce concentration while preserving cost-aware performance.

## Reading Order

1. `guide.md`
2. `report.md`
3. `work unit.yaml`
4. scientist `source-map.md`
5. relevant run records under scientist `runs/`

## How To Continue

Run a narrow robustness work unit around the `t094` family. The candidate is promising on headline metrics but not ready for promotion because fold coverage and profit concentration are weak.

## Evidence And Assets

Reference scientist assets by `asset_id`; this work unit mainly uses the upstream repo, local dataset, search ledger, and custom `t094` audit output.

## Do Not Store

Do not store secrets, raw credentials, private connector content, or unnecessary personal data in this work unit.
