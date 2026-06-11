# Proposal: Participant Asset Review Cycle 5

Proposal ID: `btc_autoresearch_cycle5_participant_asset_review`
Parent cell: `btc_benchmark__autoresearch__extended`
Parent run: `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`
Status: proposed

## Rationale

Cycle 4 validated that the Cycle 3 regime overlay is not a single 5 bp funding-threshold optimum. The confirmed best, `cycle4_funding3bp_exit6_min24`, scored net `2.8828`, funding-aware net `2.3155`, next-open net `2.8781`, drawdown `-0.3364`, random percentile `1.0`, and passed default gates. Adjacent variants at 8 bp funding and 5 bp with longer minimum holds also remained strong.

The remaining risks are implementation portability, year concentration, and cost stress. The best raw-net variant still trails always-long under cost5x (`0.3851` versus `1.4904`), while lower-turnover plateau variants such as `cycle4_funding5bp_exit12_min48` improve cost5x to `0.8570` with lower drawdown.

## Proposed Change

Keep the frozen referee target metric and buy-hold-relative decision table unchanged. Review and harden the participant-strategy asset before any external submission or sealed-holdout action.

## Suggested Experiments

1. Port `tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py` into a participant-style strategy module and run the same referee report to confirm identical metrics.
2. Add a parity check between the run-local sweep implementation and the participant asset on fold positions.
3. Compare the raw-net leader `cycle4_funding3bp_exit6_min24` against lower-turnover plateau choices, especially `cycle4_funding8bp_exit6_min24`, `cycle4_funding5bp_exit6_min48`, and `cycle4_funding5bp_exit12_min48`.
4. Promote a submission candidate only after source review confirms no hidden future use, no dependency on mutable run-local state, and no mismatch with participant repo constraints.

## Acceptance Criteria

Cycle 5 should produce a reviewed participant-style strategy asset whose referee metrics match the Cycle 4 report. If portability or position parity fails, do not promote the strategy; preserve the mismatch and revise the asset.
