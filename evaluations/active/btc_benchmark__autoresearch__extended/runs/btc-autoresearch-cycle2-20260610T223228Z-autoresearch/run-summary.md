# Fixed Runner Summary: btc_benchmark__autoresearch__extended

Run ID: btc-autoresearch-cycle2-20260610T223228Z-autoresearch
Status: completed
Task: btc_benchmark
Scheme: autoresearch
Started: 2026-06-10T22:32:28.749829+00:00

## Preflight

- Source status matched commit `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`; tracked files were clean and the only source-local untracked file was `uv.lock`.
- Runtime imports passed for `numpy`, `pandas`, and `scipy`.
- Referee contract tests passed: `21 passed`.
- Benchmark readiness loaded 56,232 candles and `funding` auxiliary data.
- Preflight `ema_baseline_12_48_long_short` passed gates but scored net `-0.8668`, max drawdown `-0.8769`, turnover `1587.0`, funding-aware net `-0.8752`, next-open net `-0.8669`, random percentile `0.21`.

## Experiment

Cycle 2 used the buy-hold-relative decision table from `proposals/btc_autoresearch_cycle2_buy_hold_relative.md`. The run evaluated 18 causal local candidates through `run_benchmark`, including passive always-long, slower EMA long-cash rules, funding exits, drawdown-stress exits, volatility exits, and combinations.

Artifacts:

- Sweep script: `run_cycle2_buyhold_relative_sweep.py`
- Candidate reports: `cycle2_candidate_reports/*.json`
- Leaderboard: `cycle2_candidate_leaderboard.jsonl`
- Ranked summary: `cycle2_candidate_summary.json`
- Confirmed best: `cycle2_confirm_best_report.json`

## Result

Best confirmed candidate:

- `cycle2_bh_ema384_lowvol168_q80`
- Net `1.8679`, delta versus always-long `+0.3674`, Sharpe `1.095`, max drawdown `-0.3157`
- Drawdown improvement versus always-long `+0.3513`
- Turnover `567.0`, trades `284`, exposure `0.506`, median hold `5` bars
- Cost curve: cost0x `4.0577`, cost2x `0.6252`, cost3x `-0.0795`, cost5x `-0.7052`
- Funding-aware net `1.4300`, next-open net `1.8644`, random percentile `1.0`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`

Useful cost-robust references:

- `cycle2_bh_funding_le_5bp`: net `1.5744`, delta versus always-long `+0.0739`, max drawdown `-0.6670`, turnover `33.0`, cost5x `1.2552`, funding-aware net `0.9966`, random percentile `0.93`.
- `cycle2_bh_drawdown252_ge_minus20`: net `1.5649`, delta versus always-long `+0.0644`, max drawdown `-0.6207`, turnover `33.0`, cost5x `1.2461`, funding-aware net `0.9591`, random percentile `0.93`.
- `cycle2_ema_72_288_long_cash`: net `1.5591`, delta versus always-long `+0.0586`, max drawdown `-0.3676`, turnover `111.0`, cost5x `0.6394`, funding-aware net `1.1234`, random percentile `0.93`.

## Decision

Promote `cycle2_bh_ema384_lowvol168_q80` as the current best development candidate, but mark it cost-fragile. The next cycle should search for a lower-turnover regime overlay that preserves the drawdown and funding-aware gains while surviving cost3x and cost5x better.

## Cycle 3 Experiment

Cycle 3 used `proposals/btc_autoresearch_cycle3_cost_robust_regime_overlay.md` and the Cycle 2 buy-hold-relative decision table. The run evaluated 12 causal local candidates through `run_benchmark`: three Cycle 2 cost controls, a retest of the Cycle 2 best, slower volatility windows, persistence/hysteresis variants, and funding or drawdown combinations.

Artifacts:

- Sweep script: `run_cycle3_cost_robust_overlay_sweep.py`
- Candidate reports: `cycle3_candidate_reports/*.json`
- Leaderboard: `cycle3_candidate_leaderboard.jsonl`
- Ranked summary: `cycle3_candidate_summary.json`
- Confirmed best: `cycle3_confirm_best_report.json`

## Cycle 3 Result

Best confirmed candidate:

- `cycle3_ema384_lowvol168_q80_funding5bp_exit6`
- Net `2.6451`, delta versus always-long `+1.1446`, Sharpe `1.271`, max drawdown `-0.3364`
- Drawdown improvement versus always-long `+0.3306`
- Turnover `237.0`, trades `119`, exposure `0.549`, median hold `38` bars
- Cost curve: cost0x `3.6201`, cost2x `1.8751`, cost3x `1.2672`, cost5x `0.4089`
- Funding-aware net `2.0707`, next-open net `2.6407`, random percentile `0.99`
- Per-year nets: 2022 `-0.3101`, 2023 `1.2322`, 2024 `1.0363`, 2025 `0.1624`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`

Useful Cycle 3 references:

- `cycle3_ema384_lowvol168_q80_enter3_exit12_min48`: net `2.4604`, delta versus always-long `+0.9599`, max drawdown `-0.3525`, turnover `157.0`, cost5x `0.8429`, funding-aware net `1.8782`, random percentile `0.99`.
- `cycle3_ema384_lowvol720_q85_exit12_min72`: net `2.1016`, delta versus always-long `+0.6011`, max drawdown `-0.3396`, turnover `167.0`, cost5x `0.5880`, funding-aware net `1.5103`, random percentile `0.99`.
- `cycle3_control_funding_le_5bp`: net `1.5744`, turnover `33.0`, cost5x `1.2552`, funding-aware net `0.9966`, random percentile `0.93`.

## Cycle 3 Decision

Promote `cycle3_ema384_lowvol168_q80_funding5bp_exit6` as the current best development candidate. It improves the Cycle 2 best on raw net, turnover, funding-aware net, next-open net, and cost3x/cost5x survival. It is not final: always-long remains stronger under cost5x, and the positive return is concentrated in 2023 and 2024. The next cycle should validate the funding cap and persistence interaction before packaging a participant-strategy asset.

## Cycle 4 Experiment

Cycle 4 used `proposals/btc_autoresearch_cycle4_validate_funding_persistence_overlay.md` and the Cycle 2 buy-hold-relative decision table. The run evaluated 16 causal local candidates through `run_benchmark`: always-long, funding caps around `0`, `1bp`, `3bp`, `5bp`, and `8bp`, adjacent exit-persistence and minimum-hold variants, price-only controls, and a strict 0 bp funding negative control.

Artifacts:

- Sweep script: `run_cycle4_validate_funding_persistence_overlay.py`
- Candidate reports: `cycle4_candidate_reports/*.json`
- Leaderboard: `cycle4_candidate_leaderboard.jsonl`
- Ranked summary: `cycle4_candidate_summary.json`
- Confirmed best: `cycle4_confirm_best_report.json`
- Participant asset: `/Users/sungs/ai-lab/tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py`

## Cycle 4 Result

Best confirmed candidate:

- `cycle4_funding3bp_exit6_min24`
- Net `2.8828`, delta versus always-long `+1.3823`, Sharpe `1.336`, max drawdown `-0.3364`
- Drawdown improvement versus always-long `+0.3306`
- Turnover `257.0`, trades `129`, exposure `0.540`, median hold `36` bars
- Cost curve: cost0x `4.0209`, cost2x `2.0019`, cost3x `1.3203`, cost5x `0.3851`
- Funding-aware net `2.3155`, next-open net `2.8781`, random percentile `1.0`
- Per-year nets: 2022 `-0.3101`, 2023 `1.3411`, 2024 `1.0682`, 2025 `0.1624`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`

Useful Cycle 4 references:

- `cycle4_funding8bp_exit6_min24`: net `2.8601`, delta versus always-long `+1.3596`, max drawdown `-0.3364`, turnover `223.0`, cost5x `0.5782`, funding-aware net `2.2327`, random percentile `0.98`.
- `cycle4_funding5bp_exit6_min48`: net `2.7832`, delta versus always-long `+1.2827`, max drawdown `-0.3144`, turnover `203.0`, cost5x `0.6760`, funding-aware net `2.1544`, random percentile `1.0`.
- `cycle4_funding5bp_exit12_min48`: net `2.7465`, delta versus always-long `+1.2460`, max drawdown `-0.2901`, turnover `175.0`, cost5x `0.8570`, funding-aware net `2.1179`, random percentile `0.98`.
- Negative control `cycle4_funding0bp_exit6_min24`: net `0.3030`, delta versus always-long `-1.1975`, turnover `182.0`, cost5x `-0.3722`, funding-aware net `0.2957`.

## Cycle 4 Decision

Promote `cycle4_funding3bp_exit6_min24` as the current best development candidate. It improves the Cycle 3 best on raw net, funding-aware net, next-open net, and random percentile while preserving default gate validity and drawdown improvement. The finding is not a final strategy: always-long remains stronger under cost5x, and the leading variants remain negative in 2022. Preserve `cycle4_funding8bp_exit6_min24`, `cycle4_funding5bp_exit6_min48`, and `cycle4_funding5bp_exit12_min48` as lower-turnover or more cost-stress-friendly plateau alternatives.

The next cycle should review, port, and parity-check the participant-style asset before any external submission or sealed-holdout action. Proposal written: `proposals/btc_autoresearch_cycle5_participant_asset_review.md`.

## Cycle 5 Experiment

Cycle 5 used `proposals/btc_autoresearch_cycle5_participant_asset_review.md` and the Cycle 2 buy-hold-relative decision table. The run reviewed `tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py`, compared its fold positions against the Cycle 4 run-local implementation, and evaluated the reviewed asset plus three lower-turnover plateau variants through `run_benchmark` with default gates.

Artifacts:

- Review script: `run_cycle5_participant_asset_review.py`
- Position parity report: `cycle5_position_parity.json`
- Candidate reports: `cycle5_candidate_reports/*.json`
- Leaderboard: `cycle5_candidate_leaderboard.jsonl`
- Ranked summary: `cycle5_candidate_summary.json`

## Cycle 5 Result

Position parity:

- Asset path: `/Users/sungs/ai-lab/tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py`
- All 14 folds matched the Cycle 4 run-local implementation exactly.
- Maximum absolute position difference: `0.0`
- Holdout start index reported by split generation: `51863`

Default-gated participant-style reports:

- `cycle4_funding3bp_exit6_min24`: net `2.8828`, delta versus always-long `+1.3823`, max drawdown `-0.3364`, turnover `257.0`, cost5x `0.3851`, funding-aware net `2.3155`, next-open net `2.8781`, random percentile `1.0`, concentration `0.4654`, gates passed with cutoff minimum `433`.
- `cycle5_asset_funding8bp_exit6_min24`: net `2.8601`, delta `+1.3596`, max drawdown `-0.3364`, turnover `223.0`, cost5x `0.5782`, funding-aware net `2.2327`, next-open net `2.8554`, random percentile `0.98`, concentration `0.4307`, gates passed with cutoff minimum `433`.
- `cycle5_asset_funding5bp_exit6_min48`: net `2.7832`, delta `+1.2827`, max drawdown `-0.3144`, turnover `203.0`, cost5x `0.6760`, funding-aware net `2.1544`, next-open net `2.7787`, random percentile `1.0`, concentration `0.4173`, gates passed with cutoff minimum `433`.
- `cycle5_asset_funding5bp_exit12_min48`: net `2.7465`, delta `+1.2460`, max drawdown `-0.2901`, turnover `175.0`, cost5x `0.8570`, funding-aware net `2.1179`, next-open net `2.7420`, random percentile `0.98`, concentration `0.4688`, gates passed with cutoff minimum `433`.

## Cycle 5 Decision

Promote `cycle4_funding3bp_exit6_min24` as the reviewed current-best development asset. Its participant-style implementation matches the sweep implementation exactly and reproduces the Cycle 4 confirmed report under default gates.

Do not treat it as submission-final yet. Passive exposure remains stronger under cost5x, year returns remain concentrated in 2023 and 2024, and no separate `btc_agentic_system` participant checkout was available to verify external packaging. The next work unit should package the strategy in the participant repo, remove or vendor any benchmark-internal helper dependency if needed, and rerun parity before any external submission or sealed-holdout action.

Proposal written: `proposals/btc_autoresearch_cycle6_participant_repo_packaging.md`.

## Verification

- `uv run python bin/ai-lab docs audit` passed.
- `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed with `21 passed`.
- `uv run python /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__extended/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle3_cost_robust_overlay_sweep.py` completed.
- The Cycle 3 sweep emitted repeated pandas runtime warnings from volatility calculations on invalid log inputs during gate perturbations, but all 12 candidate reports were produced, the ranked best was confirmed with default gates, and all candidates were accepted by the referee gates.
- Cycle 3 verification: `uv run python bin/ai-lab docs audit` passed.
- Cycle 3 verification: `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed with `21 passed`.
- `uv run python /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__extended/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle4_validate_funding_persistence_overlay.py` completed.
- The Cycle 4 sweep emitted repeated pandas runtime warnings from volatility calculations on invalid log inputs during gate perturbations, but all 16 candidate reports were produced, all candidates were accepted by the referee gates, and the ranked best was confirmed with default gates.
- Cycle 4 verification: `uv run python bin/ai-lab docs audit` passed.
- Cycle 4 verification: `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed with `21 passed`.
- Cycle 4 verification: `uv run python -m py_compile /Users/sungs/ai-lab/tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py` passed.
- Cycle 5 first script attempt failed before benchmark execution because the importlib-loaded dataclass module was not registered in `sys.modules`; the script was patched and rerun.
- `uv run python /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__extended/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle5_participant_asset_review.py` completed.
- The Cycle 5 review emitted repeated pandas runtime warnings from volatility calculations on invalid log inputs during gate perturbations, but all 4 participant-style reports were produced, all candidates passed default gates, and fold-position parity passed across all 14 folds.
- Cycle 5 verification: `uv run python bin/ai-lab docs audit` passed.
- Cycle 5 verification: `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed with `21 passed`.
- Cycle 5 verification: `uv run python -m py_compile /Users/sungs/ai-lab/tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__extended/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle5_participant_asset_review.py` passed.

Events: `events.jsonl`
Command logs: `commands/`
Spec snapshot: `run-spec.snapshot.yaml`
Finished: 2026-06-10T23:32:04.807944+00:00
