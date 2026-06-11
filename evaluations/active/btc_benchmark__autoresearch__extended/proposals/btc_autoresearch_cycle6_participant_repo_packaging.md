# Proposal: Participant Repo Packaging Cycle 6

Proposal ID: `btc_autoresearch_cycle6_participant_repo_packaging`
Parent cell: `btc_benchmark__autoresearch__extended`
Parent run: `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`
Status: proposed

## Rationale

Cycle 5 verified that `tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py` matches the Cycle 4 run-local implementation exactly across all 14 development folds and reproduces the confirmed default-gated report: net `2.8828`, funding-aware net `2.3155`, next-open net `2.8781`, max drawdown `-0.3364`, turnover `257.0`, random percentile `1.0`, and future-perturbation cutoff minimum `433`.

The remaining blocker is participant-repo portability. The local asset imports `btc_benchmark.features.technical_indicators`, and no separate `btc_agentic_system` participant checkout was available in the workspace. The current evidence supports the strategy logic, but not external packaging or participant-runtime constraints.

## Proposed Change

Keep the frozen referee target metric and buy-hold-relative decision table unchanged. Create a packaging work unit that uses an actual participant-style repository layout, vendors or replaces benchmark-internal helper dependencies as needed, and reruns the same parity and referee checks before any external submission or sealed-holdout action.

## Suggested Experiments

1. Materialize or locate the participant repo expected by BTC Benchmark submissions.
2. Port the reviewed `cycle4_funding3bp_exit6_min24` asset into that repo without reading run-local files or importing benchmark-internal helper modules unless the participant runtime explicitly allows them.
3. Add a parity check between the participant-repo strategy and the reviewed task-workspace asset on all development folds.
4. Rerun `run_benchmark` with default gates for the raw-net leader and, if packaging time allows, the lower-turnover alternatives `cycle5_asset_funding8bp_exit6_min24`, `cycle5_asset_funding5bp_exit6_min48`, and `cycle5_asset_funding5bp_exit12_min48`.
5. Preserve source-review notes for causal data access, fold-local fitting, funding alignment, dependencies, and absence of precomputed positions.

## Acceptance Criteria

The packaged participant strategy should match the reviewed task-workspace asset's fold positions exactly and reproduce the default-gated referee report. If packaging parity fails or the participant runtime cannot support the dependency set, do not submit; preserve the mismatch and revise the asset.
