# BTC Benchmark AutoResearch Overnight v1

Date: 2026-06-11
Status: active, cycle 5 synthesized

## Summary

This evaluation cell applies AutoResearch to BTC Benchmark for bounded local runs. Cycle 1 established always-long BTC exposure as the development-score floor. Cycle 2 found a stronger buy-hold-relative candidate that was cost-fragile. Cycle 3 found a lower-turnover funding-aware persistence overlay. Cycle 4 validated the funding and persistence interaction, found a stronger 3 bp funding-cap variant, and preserved a participant-strategy asset. Cycle 5 reviewed that asset, verified exact fold-position parity, and reran the asset plus three plateau alternatives through default gates.

## Current Run Spec

- Source: `btc_benchmark` at registered commit `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`
- Scheme: AutoResearch
- Skill bundle: `btc_benchmark_core_skills_v1`
- Research taste: `btc_robust_alpha_taste_v1`
- Seed hypotheses: trend-following baseline ladder, cost robustness filter, funding auxiliary signal
- Wall budget: 180 minutes
- Max cycles: 5
- Target metric: `referee_dev_score`
- Synthesis prompt: `evaluations/active/btc_benchmark__autoresearch__overnight_v1/synthesis-prompt.md`
- Cycle 2 target: `evaluations/active/btc_benchmark__autoresearch__overnight_v1/proposals/btc_autoresearch_cycle2_buy_hold_relative.md`
- Cycle 3 target: `evaluations/active/btc_benchmark__autoresearch__overnight_v1/proposals/btc_autoresearch_cycle3_cost_robust_regime_overlay.md`
- Cycle 4 target: `evaluations/active/btc_benchmark__autoresearch__overnight_v1/proposals/btc_autoresearch_cycle4_validate_funding_persistence_overlay.md`
- Cycle 5 target: `evaluations/active/btc_benchmark__autoresearch__overnight_v1/proposals/btc_autoresearch_cycle5_participant_asset_review.md`
- Cycle 6 proposed target: `evaluations/active/btc_benchmark__autoresearch__overnight_v1/proposals/btc_autoresearch_cycle6_participant_repo_packaging.md`

## Cycle 1 Reference

- Run ID: `btc-overnight-20260610T151519Z-autoresearch`
- The best confirmed candidate was `candidate_always_long_default_gates`.
- Net `1.5005`, Sharpe `0.770`, max drawdown `-0.6670`
- Turnover `1.0`, cost5x `1.4904`, funding-aware net `0.9151`, next-open net `1.4982`
- Interpretation: useful floor, not a novel trading edge.

## Cycle 2 Run

- Run ID: `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`
- Preflight loaded 56,232 candles and `funding` auxiliary data.
- Selected referee tests passed: `21 passed`.
- Generated artifacts are under `evaluations/active/btc_benchmark__autoresearch__overnight_v1/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/`.
- The sweep preserved 18 full candidate reports and confirmed the ranked best under default gate settings.

## Cycle 2 Result

Preflight EMA baseline:

- `ema_baseline_12_48_long_short`
- Net `-0.8668`, Sharpe `-0.879`, max drawdown `-0.8769`
- Turnover `1587.0`, funding-aware net `-0.8752`, next-open net `-0.8669`, random percentile `0.21`

Best confirmed candidate:

- `cycle2_bh_ema384_lowvol168_q80`
- Net `1.8679`, delta versus always-long `+0.3674`, Sharpe `1.095`, max drawdown `-0.3157`
- Turnover `567.0`, trades `284`, exposure `0.506`
- Cost curve: cost0x `4.0577`, cost2x `0.6252`, cost3x `-0.0795`, cost5x `-0.7052`
- Funding-aware net `1.4300`, next-open net `1.8644`, random percentile `1.0`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`
- Sealed holdout was not used

Cost-robust references:

- `cycle2_bh_funding_le_5bp`: net `1.5744`, delta versus always-long `+0.0739`, max drawdown `-0.6670`, turnover `33.0`, cost5x `1.2552`.
- `cycle2_bh_drawdown252_ge_minus20`: net `1.5649`, delta versus always-long `+0.0644`, max drawdown `-0.6207`, turnover `33.0`, cost5x `1.2461`.
- `cycle2_ema_72_288_long_cash`: net `1.5591`, delta versus always-long `+0.0586`, max drawdown `-0.3676`, turnover `111.0`, cost5x `0.6394`.

## Cycle 3 Result

- Run ID: `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`
- Sweep: `run_cycle3_cost_robust_overlay_sweep.py`
- The sweep evaluated 12 candidates: Cycle 2 cost controls, a retest of the Cycle 2 best, slower volatility overlays, and persistence/funding variants.
- The ranked best was confirmed with default gates across all 14 folds.

Best confirmed candidate:

- `cycle3_ema384_lowvol168_q80_funding5bp_exit6`
- Net `2.6451`, delta versus always-long `+1.1446`, Sharpe `1.271`, max drawdown `-0.3364`
- Turnover `237.0`, trades `119`, exposure `0.549`, median hold `38` bars
- Cost curve: cost0x `3.6201`, cost2x `1.8751`, cost3x `1.2672`, cost5x `0.4089`
- Funding-aware net `2.0707`, next-open net `2.6407`, random percentile `0.99`
- Per-year nets: 2022 `-0.3101`, 2023 `1.2322`, 2024 `1.0363`, 2025 `0.1624`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`
- Sealed holdout was not used

Useful Cycle 3 references:

- `cycle3_ema384_lowvol168_q80_enter3_exit12_min48`: net `2.4604`, turnover `157.0`, cost5x `0.8429`, funding-aware net `1.8782`.
- `cycle3_ema384_lowvol720_q85_exit12_min72`: net `2.1016`, turnover `167.0`, cost5x `0.5880`, funding-aware net `1.5103`.
- `cycle3_control_funding_le_5bp`: net `1.5744`, turnover `33.0`, cost5x `1.2552`, funding-aware net `0.9966`.

## Cycle 4 Result

- Run ID: `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`
- Sweep: `run_cycle4_validate_funding_persistence_overlay.py`
- The sweep evaluated 16 candidates: funding caps around the Cycle 3 best, adjacent exit persistence and minimum-hold settings, price-only controls, always-long, and a strict 0 bp funding negative control.
- The ranked best was confirmed with default gates across all 14 folds.
- Participant asset: `tasks/active/btc_benchmark/participant-strategies/cycle4_funding3bp_exit6_min24_strategy.py`

Best confirmed candidate:

- `cycle4_funding3bp_exit6_min24`
- Net `2.8828`, delta versus always-long `+1.3823`, Sharpe `1.336`, max drawdown `-0.3364`
- Turnover `257.0`, trades `129`, exposure `0.540`, median hold `36` bars
- Cost curve: cost0x `4.0209`, cost2x `2.0019`, cost3x `1.3203`, cost5x `0.3851`
- Funding-aware net `2.3155`, next-open net `2.8781`, random percentile `1.0`
- Per-year nets: 2022 `-0.3101`, 2023 `1.3411`, 2024 `1.0682`, 2025 `0.1624`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`
- Sealed holdout was not used

Useful Cycle 4 references:

- `cycle4_funding8bp_exit6_min24`: net `2.8601`, turnover `223.0`, cost5x `0.5782`, funding-aware net `2.2327`, concentration `0.4307`.
- `cycle4_funding5bp_exit6_min48`: net `2.7832`, turnover `203.0`, cost5x `0.6760`, funding-aware net `2.1544`, concentration `0.4173`.
- `cycle4_funding5bp_exit12_min48`: net `2.7465`, turnover `175.0`, cost5x `0.8570`, funding-aware net `2.1179`, max drawdown `-0.2901`.
- `cycle4_funding0bp_exit6_min24`: net `0.3030`, turnover `182.0`, cost5x `-0.3722`, funding-aware net `0.2957`.

## Cycle 5 Result

- Run ID: `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`
- Review script: `run_cycle5_participant_asset_review.py`
- Position parity: the participant asset matched the Cycle 4 run-local implementation exactly across all 14 folds; max absolute position difference was `0.0`.
- All four reviewed participant-style variants passed default gates with future-perturbation cutoff minimum `433`.

Default-gated participant-style results:

- `cycle4_funding3bp_exit6_min24`: net `2.8828`, delta versus always-long `+1.3823`, max drawdown `-0.3364`, turnover `257.0`, cost5x `0.3851`, funding-aware net `2.3155`, next-open net `2.8781`, random percentile `1.0`, concentration `0.4654`.
- `cycle5_asset_funding8bp_exit6_min24`: net `2.8601`, delta `+1.3596`, max drawdown `-0.3364`, turnover `223.0`, cost5x `0.5782`, funding-aware net `2.2327`, next-open net `2.8554`, random percentile `0.98`, concentration `0.4307`.
- `cycle5_asset_funding5bp_exit6_min48`: net `2.7832`, delta `+1.2827`, max drawdown `-0.3144`, turnover `203.0`, cost5x `0.6760`, funding-aware net `2.1544`, next-open net `2.7787`, random percentile `1.0`, concentration `0.4173`.
- `cycle5_asset_funding5bp_exit12_min48`: net `2.7465`, delta `+1.2460`, max drawdown `-0.2901`, turnover `175.0`, cost5x `0.8570`, funding-aware net `2.1179`, next-open net `2.7420`, random percentile `0.98`, concentration `0.4688`.

## Plots

The Cycle 1 leaderboard makes the first result visually obvious: always-long dominated raw development net, so Cycle 2 treated it as the floor.

<div class="ai-lab-vega-plot" data-vega-spec="../../assets/btc-autoresearch-cycle1-leaderboard.vl.json"></div>

The Cycle 1 risk-return view shows the tradeoff hidden by the leaderboard. Adaptive variants gave up raw net, but several reduced drawdown relative to full BTC exposure.

<div class="ai-lab-vega-plot" data-vega-spec="../../assets/btc-autoresearch-cycle1-risk-return.vl.json"></div>

Cost stress separated passive exposure from active rules in Cycle 1 and remains the main issue in Cycle 2.

<div class="ai-lab-vega-plot" data-vega-spec="../../assets/btc-autoresearch-cycle1-cost-stress.vl.json"></div>

The adaptive-only relative plot framed the Cycle 2 search: look for a candidate that can beat always-long while preserving robustness.

<div class="ai-lab-vega-plot" data-vega-spec="../../assets/btc-autoresearch-cycle1-adaptive-relative.vl.json"></div>

## Interpretation

Cycle 2 produced a genuine buy-hold-relative development improvement: the best slow-trend plus fold-local low-volatility overlay beat always-long net, improved drawdown, improved funding-aware score, and passed the default causality gate budget. Its weakness was cost robustness: cost3x and cost5x were negative because turnover was much higher than passive exposure.

Cycle 3 materially improved that tradeoff. The best funding-aware persistence overlay reduced turnover from `567.0` to `237.0`, improved net from `1.8679` to `2.6451`, kept a large drawdown improvement, and made cost3x/cost5x positive.

Cycle 4 strengthened the finding. The 3 bp funding cap improved raw net to `2.8828`, funding-aware net to `2.3155`, next-open net to `2.8781`, and passed default gates. Adjacent 8 bp and longer-hold 5 bp variants remained strong, so this looks like a plateau around the funding/persistence interaction rather than a single sharp optimum.

Cycle 5 confirmed the saved participant asset reproduces the Cycle 4 leader exactly. The best raw-net asset remains the current development candidate, while the 8 bp and 5 bp/min-hold variants are better robustness alternatives if cost stress or turnover is weighted more heavily.

The strategy is still not final. Passive exposure remains stronger at cost5x, the positive development return is concentrated in 2023 and 2024, and the local asset still imports a benchmark helper module. No separate `btc_agentic_system` participant checkout was available, so external participant-repo portability remains untested and should be handled before any submission or sealed-holdout action.

## Component Model

See [Scientist Components](../reference/scientist-components.md) for how this cell separates scheme, skills, research taste, and hypotheses.
