# Proposal: Validate Funding Persistence Overlay Cycle 4

Proposal ID: `btc_autoresearch_cycle4_validate_funding_persistence_overlay`
Parent cell: `btc_benchmark__autoresearch__overnight_v1`
Parent run: `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`
Status: proposed

## Rationale

Cycle 3 found `cycle3_ema384_lowvol168_q80_funding5bp_exit6`, a buy-hold-relative improvement with net `2.6451`, drawdown `-0.3364`, funding-aware net `2.0707`, next-open net `2.6407`, turnover `237.0`, and positive cost3x/cost5x results. It passed default gates on all 14 folds.

The result should not be treated as final yet. Always-long remains stronger under cost5x stress, and the development return is concentrated in 2023 and 2024. The improvement may depend on a narrow interaction between the funding threshold and exit persistence.

## Proposed Change

Keep the frozen referee target metric and buy-hold-relative decision table unchanged. Run a narrow validation work unit around the Cycle 3 candidate before packaging any participant-strategy asset.

## Suggested Experiments

1. Sweep funding caps around `0`, `1bp`, `3bp`, `5bp`, and `8bp` while holding EMA-384, low-volatility 168/q80, and exit persistence fixed.
2. Sweep persistence settings around exit confirmation `3`, `6`, `12`, enter confirmation `1` or `3`, and minimum hold `24` or `48`.
3. Confirm top variants with default gates and compare against `cycle3_ema384_lowvol168_q80_enter3_exit12_min48`, `cycle3_control_funding_le_5bp`, and always-long.
4. If a plateau remains, write a participant-strategy asset under the appropriate AI Lab task or inbox path without modifying the frozen referee checkout.

## Acceptance Criteria

A Cycle 4 candidate should only be promoted if it preserves most of the Cycle 3 raw-net and drawdown improvement while showing robustness across adjacent funding and persistence settings. Prefer a slightly lower-net plateau candidate over a single sharp optimum.
