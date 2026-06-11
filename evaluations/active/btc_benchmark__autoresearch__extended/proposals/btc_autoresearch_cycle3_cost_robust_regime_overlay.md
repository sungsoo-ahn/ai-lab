# Proposal: Cost-Robust Regime Overlay Cycle 3

Proposal ID: `btc_autoresearch_cycle3_cost_robust_regime_overlay`
Parent cell: `btc_benchmark__autoresearch__extended`
Parent run: `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`
Status: proposed

## Rationale

Cycle 2 found `cycle2_bh_ema384_lowvol168_q80`, a buy-hold-relative improvement with net `1.8679`, drawdown `-0.3157`, funding-aware net `1.4300`, next-open net `1.8644`, and default gates passed. The weakness is turnover: cost3x fell to `-0.0795` and cost5x to `-0.7052`.

## Proposed Change

Keep the frozen referee target metric and the buy-hold-relative decision table unchanged, but prioritize a low-turnover version of the slow-regime plus volatility overlay before broader feature search.

## Suggested Experiments

1. Add hysteresis or persistence to the EMA-384 and low-volatility overlay so exits require multi-bar confirmation.
2. Sweep slower volatility windows and higher quantiles to reduce churn while preserving the drawdown benefit.
3. Compare directly against the low-turnover controls from Cycle 2: `cycle2_bh_funding_le_5bp`, `cycle2_bh_drawdown252_ge_minus20`, and `cycle2_ema_72_288_long_cash`.
4. Promote only candidates that preserve positive delta versus always-long or materially improve drawdown while improving cost3x and cost5x survival.

## Acceptance Criteria

A Cycle 3 candidate should improve the Cycle 2 decision table by either:

- preserving positive delta versus always-long while making cost3x and cost5x materially less fragile; or
- giving up only modest raw net while preserving strong drawdown improvement, funding-aware net, next-open net, and random percentile.
