# Evaluation Cell Report: btc_benchmark__autoresearch__extended

Date: 2026-06-11
Status: active, cycle 5 synthesized

## Current State

Cycle 5 completed the AutoResearch participant-asset review for run `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`. The run reproduced the weak EMA preflight baseline, used the Cycle 2 decision table, reviewed the Cycle 4 participant asset, verified exact fold-position parity against the run-local sweep implementation, evaluated the asset plus three lower-turnover plateau variants through the frozen referee with default gates, and preserved all reports in the run directory.

## Fixed Run Contract

- Wall budget: 180 minutes, enforced by `run-spec.yaml` command timeouts and the AI Lab runner wall deadline.
- Source: registered `btc_benchmark` checkout at commit `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`.
- Preflight: source status, runtime check, selected referee tests, data load, and EMA baseline reproduction.
- Synthesis: up to five AutoResearch cycles using `synthesis-prompt.md`.

## Scientist Composition

- Scheme: `autoresearch`
- Skill bundle: `btc_benchmark_core_skills_v1`
- Research taste: `btc_robust_alpha_taste_v1`
- Seed hypotheses:
  - `btc_trend_following_baseline_ladder_v1`
  - `btc_cost_robustness_filter_v1`
  - `btc_funding_auxiliary_signal_v1`

## Preflight Evidence

- Source status matched commit `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`; tracked files were clean and the only untracked source-local file was `uv.lock`.
- Runtime check passed for `numpy`, `pandas`, and `scipy`.
- Referee contract tests passed: `21 passed`.
- Readiness loaded 56,232 candles and `funding` auxiliary data.
- Preflight `ema_baseline_12_48_long_short` passed gates but scored net `-0.8668`, Sharpe `-0.879`, max drawdown `-0.8769`, turnover `1587.0`, funding-aware net `-0.8752`, next-open net `-0.8669`, and random percentile `0.21`.

## Cycle 1 Reference

Cycle 1 established always-long as the development-score floor rather than a completed strategy:

- `candidate_always_long_default_gates`
- Net `1.5005`, Sharpe `0.770`, max drawdown `-0.6670`
- Turnover `1.0`, cost5x `1.4904`, funding-aware net `0.9151`, next-open net `1.4982`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`

## Cycle 2 Result

Artifacts:

- Run summary: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run-summary.md`
- Sweep script: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle2_buyhold_relative_sweep.py`
- Candidate reports: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle2_candidate_reports/*.json`
- Candidate leaderboard: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle2_candidate_leaderboard.jsonl`
- Candidate summary: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle2_candidate_summary.json`
- Confirmed best: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle2_confirm_best_report.json`

Best confirmed candidate:

- `cycle2_bh_ema384_lowvol168_q80`
- Net `1.8679`, delta versus always-long `+0.3674`, Sharpe `1.095`, max drawdown `-0.3157`
- Drawdown improvement versus always-long `+0.3513`
- Turnover `567.0`, trades `284`, exposure `0.506`, median hold `5` bars
- Cost curve: cost0x `4.0577`, cost2x `0.6252`, cost3x `-0.0795`, cost5x `-0.7052`
- Funding-aware net `1.4300`, next-open net `1.8644`, random percentile `1.0`
- Per-year nets: 2022 `-0.2790`, 2023 `0.7829`, 2024 `0.9500`, 2025 `0.1440`
- Per-year absolute net concentration `0.4407`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`
- Sealed holdout was not used

Useful robust references:

- `cycle2_bh_funding_le_5bp`: net `1.5744`, delta versus always-long `+0.0739`, max drawdown `-0.6670`, turnover `33.0`, cost5x `1.2552`, funding-aware net `0.9966`, next-open net `1.5720`, random percentile `0.93`.
- `cycle2_bh_drawdown252_ge_minus20`: net `1.5649`, delta versus always-long `+0.0644`, max drawdown `-0.6207`, turnover `33.0`, cost5x `1.2461`, funding-aware net `0.9591`, next-open net `1.5624`, random percentile `0.93`.
- `cycle2_ema_72_288_long_cash`: net `1.5591`, delta versus always-long `+0.0586`, max drawdown `-0.3676`, turnover `111.0`, cost5x `0.6394`, funding-aware net `1.1234`, next-open net `1.5567`, random percentile `0.93`.

## Interpretation

Cycle 2 found a credible buy-hold-relative development improvement. The confirmed best combines a slow EMA-384 regime gate with a fold-local 168-hour low-volatility threshold. It improves raw net, funding-aware net, next-open net, random percentile, and drawdown relative to always-long.

The best candidate is not yet cost-robust. Its turnover is much higher than passive exposure, and its cost stress collapses from cost2x `0.6252` to cost3x `-0.0795` and cost5x `-0.7052`. This is the main reason not to promote it as final. The lower-turnover funding and drawdown filters are weaker on raw net and drawdown, but they survive cost5x and should anchor the next ablation.

## Decision

Promote `cycle2_bh_ema384_lowvol168_q80` as the current best development candidate, with a cost-fragility warning. The next cycle should keep the buy-hold-relative table and search for a low-turnover version of the same regime idea, using the cost-surviving funding and drawdown filters as controls.

Proposal written: `proposals/btc_autoresearch_cycle3_cost_robust_regime_overlay.md`.

## Cycle 3 Result

Artifacts:

- Sweep script: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle3_cost_robust_overlay_sweep.py`
- Candidate reports: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle3_candidate_reports/*.json`
- Candidate leaderboard: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle3_candidate_leaderboard.jsonl`
- Candidate summary: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle3_candidate_summary.json`
- Confirmed best: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle3_confirm_best_report.json`

Best confirmed candidate:

- `cycle3_ema384_lowvol168_q80_funding5bp_exit6`
- Net `2.6451`, delta versus always-long `+1.1446`, Sharpe `1.271`, max drawdown `-0.3364`
- Drawdown improvement versus always-long `+0.3306`
- Turnover `237.0`, trades `119`, exposure `0.549`, median hold `38` bars
- Cost curve: cost0x `3.6201`, cost2x `1.8751`, cost3x `1.2672`, cost5x `0.4089`
- Funding-aware net `2.0707`, next-open net `2.6407`, random percentile `0.99`
- Per-year nets: 2022 `-0.3101`, 2023 `1.2322`, 2024 `1.0363`, 2025 `0.1624`
- Per-year absolute net concentration `0.4495`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`
- Sealed holdout was not used

Useful Cycle 3 references:

- `cycle3_ema384_lowvol168_q80_enter3_exit12_min48`: net `2.4604`, delta versus always-long `+0.9599`, max drawdown `-0.3525`, turnover `157.0`, cost5x `0.8429`, funding-aware net `1.8782`, next-open net `2.4572`, random percentile `0.99`.
- `cycle3_ema384_lowvol720_q85_exit12_min72`: net `2.1016`, delta versus always-long `+0.6011`, max drawdown `-0.3396`, turnover `167.0`, cost5x `0.5880`, funding-aware net `1.5103`, next-open net `2.0984`, random percentile `0.99`.
- `cycle3_control_funding_le_5bp`: net `1.5744`, delta versus always-long `+0.0739`, max drawdown `-0.6670`, turnover `33.0`, cost5x `1.2552`, funding-aware net `0.9966`, next-open net `1.5720`, random percentile `0.93`.

## Cycle 3 Interpretation

Cycle 3 found a materially better buy-hold-relative development candidate. Adding a causal funding cap and six-bar exit confirmation to the Cycle 2 EMA-384 plus fold-local low-volatility overlay reduced turnover from `567.0` to `237.0`, made cost3x and cost5x positive, improved raw net from `1.8679` to `2.6451`, and improved funding-aware net from `1.4300` to `2.0707`.

The result is still not final. The candidate survives cost5x with net `0.4089`, but always-long remains stronger under cost5x at `1.4904`. The development return is also concentrated in 2023 and 2024, while 2022 remains negative. The next cycle should validate whether the improvement comes from the funding cap, the exit persistence, their interaction, or a lucky parameter pocket.

## Cycle 3 Decision

Promote `cycle3_ema384_lowvol168_q80_funding5bp_exit6` as the current best development candidate, with a remaining high-cost-stress and year-concentration warning. The next cycle should run a narrow validation grid around funding thresholds and persistence settings, confirm top variants with default gates, and prepare a participant-strategy asset only if the candidate remains robust.

Proposal written: `proposals/btc_autoresearch_cycle4_validate_funding_persistence_overlay.md`.

## Cycle 4 Result

Artifacts:

- Sweep script: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle4_validate_funding_persistence_overlay.py`
- Candidate reports: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle4_candidate_reports/*.json`
- Candidate leaderboard: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle4_candidate_leaderboard.jsonl`
- Candidate summary: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle4_candidate_summary.json`
- Confirmed best: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle4_confirm_best_report.json`
- Participant asset: `tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py`

Best confirmed candidate:

- `cycle4_funding3bp_exit6_min24`
- Net `2.8828`, delta versus always-long `+1.3823`, Sharpe `1.336`, max drawdown `-0.3364`
- Drawdown improvement versus always-long `+0.3306`
- Turnover `257.0`, trades `129`, exposure `0.540`, median hold `36` bars
- Cost curve: cost0x `4.0209`, cost2x `2.0019`, cost3x `1.3203`, cost5x `0.3851`
- Funding-aware net `2.3155`, next-open net `2.8781`, random percentile `1.0`
- Per-year nets: 2022 `-0.3101`, 2023 `1.3411`, 2024 `1.0682`, 2025 `0.1624`
- Per-year absolute net concentration `0.4654`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`
- Sealed holdout was not used

Useful Cycle 4 references:

- `cycle4_funding8bp_exit6_min24`: net `2.8601`, delta versus always-long `+1.3596`, max drawdown `-0.3364`, turnover `223.0`, cost5x `0.5782`, funding-aware net `2.2327`, next-open net `2.8554`, random percentile `0.98`, concentration `0.4307`.
- `cycle4_funding5bp_exit6_min48`: net `2.7832`, delta versus always-long `+1.2827`, max drawdown `-0.3144`, turnover `203.0`, cost5x `0.6760`, funding-aware net `2.1544`, next-open net `2.7787`, random percentile `1.0`, concentration `0.4173`.
- `cycle4_funding5bp_exit12_min48`: net `2.7465`, delta versus always-long `+1.2460`, max drawdown `-0.2901`, turnover `175.0`, cost5x `0.8570`, funding-aware net `2.1179`, next-open net `2.7420`, random percentile `0.98`, concentration `0.4688`.
- Negative control `cycle4_funding0bp_exit6_min24`: net `0.3030`, delta versus always-long `-1.1975`, max drawdown `-0.4556`, turnover `182.0`, cost5x `-0.3722`, funding-aware net `0.2957`, random percentile `0.79`.

## Cycle 4 Interpretation

Cycle 4 strengthens the Cycle 3 finding. The best 3 bp funding cap improves raw net from `2.6451` to `2.8828`, funding-aware net from `2.0707` to `2.3155`, and next-open net from `2.6407` to `2.8781`, while preserving the same drawdown improvement and default gate pass. The adjacent 8 bp and 5 bp/min-hold variants remain strong, so the evidence is better described as a funding-and-persistence plateau than a single 5 bp pocket.

The result is still not final. The raw-net leader has turnover `257.0` and cost5x `0.3851`, which remains far below always-long cost5x `1.4904`. The strongest cost-stress plateau reference, `cycle4_funding5bp_exit12_min48`, improves cost5x to `0.8570` with lower drawdown but gives up raw net. Development return also remains concentrated in 2023 and 2024, while 2022 is negative across the leading variants.

## Cycle 4 Decision

Promote `cycle4_funding3bp_exit6_min24` as the current best development candidate, with cost5x and year-concentration warnings. Preserve the lower-turnover plateau variants as credible alternatives for a robustness-first submission choice. A participant-strategy asset has been written under the BTC task workspace, and the next cycle should review, port, and parity-check that asset before any external submission or sealed-holdout action.

Proposal written: `proposals/btc_autoresearch_cycle5_participant_asset_review.md`.

## Cycle 5 Result

Artifacts:

- Review script: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle5_participant_asset_review.py`
- Position parity report: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle5_position_parity.json`
- Candidate reports: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle5_candidate_reports/*.json`
- Candidate leaderboard: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle5_candidate_leaderboard.jsonl`
- Candidate summary: `runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/cycle5_candidate_summary.json`

Participant asset parity:

- Asset: `tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py`
- Exact fold-position parity versus the Cycle 4 run-local implementation: passed across all 14 folds
- Maximum absolute position difference: `0.0`
- Holdout remained structurally unseen; parity split generation reported holdout start index `51863`

Default-gated participant-style candidate results:

- `cycle4_funding3bp_exit6_min24`: net `2.8828`, delta versus always-long `+1.3823`, max drawdown `-0.3364`, turnover `257.0`, cost5x `0.3851`, funding-aware net `2.3155`, next-open net `2.8781`, random percentile `1.0`, concentration `0.4654`, default gates passed with cutoff minimum `433`.
- `cycle5_asset_funding8bp_exit6_min24`: net `2.8601`, delta `+1.3596`, max drawdown `-0.3364`, turnover `223.0`, cost5x `0.5782`, funding-aware net `2.2327`, next-open net `2.8554`, random percentile `0.98`, concentration `0.4307`, default gates passed with cutoff minimum `433`.
- `cycle5_asset_funding5bp_exit6_min48`: net `2.7832`, delta `+1.2827`, max drawdown `-0.3144`, turnover `203.0`, cost5x `0.6760`, funding-aware net `2.1544`, next-open net `2.7787`, random percentile `1.0`, concentration `0.4173`, default gates passed with cutoff minimum `433`.
- `cycle5_asset_funding5bp_exit12_min48`: net `2.7465`, delta `+1.2460`, max drawdown `-0.2901`, turnover `175.0`, cost5x `0.8570`, funding-aware net `2.1179`, next-open net `2.7420`, random percentile `0.98`, concentration `0.4688`, default gates passed with cutoff minimum `433`.

## Cycle 5 Interpretation

Cycle 5 confirms that the participant asset reproduces the Cycle 4 raw-net leader exactly under the frozen referee. The asset's default-gated report matches the Cycle 4 confirmed report on the decision-table metrics, and the fold-by-fold position parity check rules out a packaging mismatch between the sweep implementation and the saved participant-style class.

The lower-turnover plateau variants also passed default gates and reproduced their Cycle 4 metrics. They remain credible robustness alternatives: the 8 bp variant gives up only `0.0227` net versus the raw-net leader while reducing turnover from `257.0` to `223.0` and improving cost5x from `0.3851` to `0.5782`; the 5 bp exit12/min48 variant gives up more raw net but improves max drawdown to `-0.2901`, turnover to `175.0`, and cost5x to `0.8570`.

The result is still not final for external submission. The local asset imports `btc_benchmark.features.technical_indicators`; no separate `btc_agentic_system` participant checkout was available in this workspace, so portability into the actual participant repo was not tested. Source review found no precomputed position arrays, no run-directory reads, no sealed-holdout access, and only fold-local volatility fitting plus backward-asof funding alignment, but the external packaging dependency remains open.

## Cycle 5 Decision

Promote `cycle4_funding3bp_exit6_min24` as the reviewed current-best development asset, with unchanged warnings on high-cost stress, year concentration, and participant-repo packaging. Preserve `cycle5_asset_funding8bp_exit6_min24`, `cycle5_asset_funding5bp_exit6_min48`, and `cycle5_asset_funding5bp_exit12_min48` as submission-choice alternatives if robustness is prioritized over raw development net.

Proposal written: `proposals/btc_autoresearch_cycle6_participant_repo_packaging.md`.

## Verification

- `uv run python /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__extended/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle2_buyhold_relative_sweep.py` completed.
- `uv run python /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__extended/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle3_cost_robust_overlay_sweep.py` completed.
- The sweep emitted repeated pandas runtime warnings from volatility calculations on invalid log inputs, but all 18 candidate reports were produced and all candidates were accepted by the referee gates.
- The Cycle 3 sweep emitted the same warning class during gate perturbations; all 12 candidate reports were produced, the ranked best was confirmed with default gates, and all candidates were accepted by the referee gates.
- Cycle 2 verification: `uv run python bin/ai-lab docs audit` passed.
- Cycle 2 verification: `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed with `21 passed`.
- Cycle 3 verification: `uv run python bin/ai-lab docs audit` passed.
- Cycle 3 verification: `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed with `21 passed`.
- `uv run python /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__extended/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle4_validate_funding_persistence_overlay.py` completed.
- The Cycle 4 sweep emitted repeated pandas runtime warnings from volatility calculations during gate perturbations; all 16 candidate reports were produced, all candidates were accepted by the referee gates, and the ranked best was confirmed with default gates.
- Cycle 4 verification: `uv run python bin/ai-lab docs audit` passed.
- Cycle 4 verification: `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed with `21 passed`.
- Cycle 4 verification: `uv run python -m py_compile /Users/sungs/ai-lab/tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py` passed.
- Cycle 5 first script attempt failed before benchmark execution because the importlib-loaded dataclass module was not registered in `sys.modules`; `run_cycle5_participant_asset_review.py` was patched and rerun.
- `uv run python /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__extended/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle5_participant_asset_review.py` completed.
- The Cycle 5 review emitted repeated pandas runtime warnings from volatility calculations during gate perturbations; all 4 candidate reports were produced, all candidates passed default gates, and fold-position parity passed across all 14 folds.
- Cycle 5 verification: `uv run python bin/ai-lab docs audit` passed.
- Cycle 5 verification: `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed with `21 passed`.
- Cycle 5 verification: `uv run python -m py_compile /Users/sungs/ai-lab/tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__extended/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle5_participant_asset_review.py` passed.
