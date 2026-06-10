# Proposal: Buy-Hold-Relative AutoResearch Cycle 2

Proposal ID: `btc_autoresearch_cycle2_buy_hold_relative`
Parent cell: `btc_benchmark__autoresearch__overnight_v1`
Parent run: `btc-overnight-20260610T151519Z-autoresearch`
Status: proposed

## Rationale

Cycle 1 beat the weak preflight EMA baseline, but the best candidate was always-long BTC exposure. That result is a useful floor, not a robust adaptive strategy. The best adaptive candidate, EMA 48/192 with a loose funding filter, improved raw and funding-aware net over plain EMA but gave up 5x cost robustness.

## Proposed Change

Create a cycle 2 work unit that keeps the frozen referee target metric unchanged but ranks candidates against an internal decision table with:

- delta versus always-long buy-and-hold net;
- max drawdown improvement;
- funding-aware net;
- cost2x, cost3x, and cost5x survival;
- next-open net;
- per-year concentration;
- random percentile for adaptive strategies.

## Suggested Experiments

1. Test long-only overlay exits around `candidate_always_long`: EMA regime filter, high-volatility cash filter, and funding stress filter.
2. Sweep slower EMA windows around 48/192 and funding thresholds around 0 to 5 bps.
3. Promote only candidates that either beat always-long net with acceptable drawdown or materially reduce drawdown/funding drag while preserving enough net return.

## Acceptance Criteria

A cycle 2 candidate should not be called a win solely for beating `ema_baseline_12_48_long_short`. It should improve the buy-and-hold-relative decision table or clearly explain why the benchmark target rewards passive exposure.
