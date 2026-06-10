# BTC Benchmark AutoResearch Overnight v1

Date: 2026-06-10
Status: active, cycle 1 synthesized

## Summary

This evaluation cell applied AutoResearch to BTC Benchmark for a bounded local run. Cycle 1 reproduced the weak EMA preflight baseline, ran a small causal strategy sweep through the frozen referee, confirmed the best local candidate under default gate settings, and concluded that always-long BTC exposure is the current development-score floor.

## Current Run Spec

- Source: `btc_benchmark` at registered commit `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`
- Scheme: AutoResearch
- Skill bundle: `btc_benchmark_core_skills_v1`
- Research taste: `btc_robust_alpha_taste_v1`
- Seed hypotheses: trend-following baseline ladder, cost robustness filter, funding auxiliary signal
- Wall budget: 180 minutes
- Target metric: `referee_dev_score`
- Synthesis prompt: `evaluations/active/btc_benchmark__autoresearch__overnight_v1/synthesis-prompt.md`

## Cycle 1 Run

- Run ID: `btc-overnight-20260610T151519Z-autoresearch`
- Preflight loaded 56,232 candles and `funding` auxiliary data.
- Selected referee tests passed: `21 passed`.
- Generated artifacts are under `evaluations/active/btc_benchmark__autoresearch__overnight_v1/runs/btc-overnight-20260610T151519Z-autoresearch/`.
- The sweep preserved 13 full candidate reports plus `experiment_summary.md`.
- The best candidate was rerun in `confirm_best_report.json` with the referee default gate budget.

## Result

Preflight EMA baseline:

- `ema_baseline_12_48_long_short`
- Net `-0.8668`, Sharpe `-0.879`, max drawdown `-0.8769`
- Turnover `1587.0`, trades `794`, median hold `23` bars
- Funding-aware net `-0.8752`, next-open net `-0.8669`, random percentile `0.21`
- Passed gates across all 14 folds

Best confirmed candidate:

- `candidate_always_long_default_gates`
- Net `1.5005`, Sharpe `0.770`, max drawdown `-0.6670`
- Turnover `1.0`, trades `1`, full exposure
- Cost curve: cost0x `1.5031`, cost2x `1.4980`, cost5x `1.4904`
- Funding-aware net `0.9151`, next-open net `1.4982`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`
- Sealed holdout was not used

Top adaptive references:

- `candidate_ema_48_192_funding_le_5bp`: net `0.9021`, max drawdown `-0.4316`, turnover `225.0`, random percentile `0.95`, funding-aware net `0.6106`, cost5x `-0.2286`.
- `candidate_ema_48_192_long_cash`: net `0.8433`, max drawdown `-0.4316`, turnover `195.0`, random percentile `0.93`, funding-aware net `0.5430`, cost5x `-0.1568`.
- `candidate_ema_24_96_long_cash`: net `0.6632`, max drawdown `-0.4575`, turnover `375.0`, random percentile `0.96`, funding-aware net `0.4050`, cost5x `-0.6307`.

## Plots

The leaderboard makes the main result visually obvious: always-long dominates raw development net, so it should be treated as the floor for Cycle 2.

<div class="ai-lab-vega-plot" data-vega-spec="../../assets/btc-autoresearch-cycle1-leaderboard.vl.json"></div>

The risk-return view shows the tradeoff hidden by the leaderboard. Adaptive variants give up raw net, but several reduce drawdown relative to full BTC exposure.

<div class="ai-lab-vega-plot" data-vega-spec="../../assets/btc-autoresearch-cycle1-risk-return.vl.json"></div>

Cost stress separates passive exposure from active rules. The best adaptive candidates lose much of their appeal under 5x costs.

<div class="ai-lab-vega-plot" data-vega-spec="../../assets/btc-autoresearch-cycle1-cost-stress.vl.json"></div>

The adaptive-only relative plot frames Cycle 2 directly: no adaptive candidate beat always-long net, but some improved drawdown enough to justify overlay experiments.

<div class="ai-lab-vega-plot" data-vega-spec="../../assets/btc-autoresearch-cycle1-adaptive-relative.vl.json"></div>

## Interpretation

The run found a metric improvement over the preflight EMA baseline, but not a novel trading edge. Always-long mostly recovers the benchmark's own buy-and-hold reference after one opening cost. It is robust to cost multipliers and next-open execution because it barely trades, but it has severe drawdown, a weak 2022, and funding drag.

The best adaptive follow-up was an EMA 48/192 long-cash rule with a loose funding filter. It improved raw and funding-aware net over plain EMA 48/192, but higher turnover weakened 5x cost robustness. Future work should treat always-long as the floor and optimize adaptive overlays against buy-and-hold, funding-aware net, drawdown, and cost stress.

## Component Model

See [Scientist Components](../reference/scientist-components.md) for how this cell separates scheme, skills, research taste, and hypotheses.
