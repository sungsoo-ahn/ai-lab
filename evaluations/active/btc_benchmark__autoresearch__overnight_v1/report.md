# Evaluation Cell Report: btc_benchmark__autoresearch__overnight_v1

Date: 2026-06-10
Status: active, cycle 1 synthesized

## Current State

Cycle 1 executed the AutoResearch loop for run `btc-overnight-20260610T151519Z-autoresearch`. The run reproduced the weak EMA preflight baseline, evaluated 13 local candidates through the frozen referee, confirmed the best candidate with default gate settings, and preserved all reports in the run directory.

## Fixed Run Contract

- Wall budget: 180 minutes, enforced by `run-spec.yaml` command timeouts and the AI Lab runner wall deadline.
- Source: registered `btc_benchmark` checkout at commit `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`.
- Preflight: source status, runtime check, selected referee tests, data load, and EMA baseline reproduction.
- Synthesis: one AutoResearch loop using `synthesis-prompt.md`.

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

## Cycle 1 Result

Artifacts:

- Run summary: `runs/btc-overnight-20260610T151519Z-autoresearch/run-summary.md`
- Experiment notes: `runs/btc-overnight-20260610T151519Z-autoresearch/experiment_summary.md`
- Sweep script: `runs/btc-overnight-20260610T151519Z-autoresearch/run_candidate_sweep.py`
- Candidate reports: `runs/btc-overnight-20260610T151519Z-autoresearch/candidate_reports/*.json`
- Candidate leaderboard: `runs/btc-overnight-20260610T151519Z-autoresearch/candidate_leaderboard.jsonl`
- Confirmed best: `runs/btc-overnight-20260610T151519Z-autoresearch/confirm_best_report.json`

Best confirmed candidate:

- `candidate_always_long_default_gates`
- Net `1.5005`, Sharpe `0.770`, max drawdown `-0.6670`
- Turnover `1.0`, trades `1`, full exposure
- Cost curve: cost0x `1.5031`, cost2x `1.4980`, cost3x `1.4955`, cost5x `1.4904`
- Funding-aware net `0.9151`, next-open net `1.4982`
- Passed all 14 fold gates with default future-perturbation cutoff minimum `433`
- Sealed holdout was not used

Best adaptive references:

- `candidate_ema_48_192_funding_le_5bp`: net `0.9021`, max drawdown `-0.4316`, turnover `225.0`, funding-aware net `0.6106`, next-open net `0.9005`, random percentile `0.95`, but cost5x `-0.2286`.
- `candidate_ema_48_192_long_cash`: net `0.8433`, max drawdown `-0.4316`, turnover `195.0`, funding-aware net `0.5430`, next-open net `0.8418`, random percentile `0.93`, cost5x `-0.1568`.
- `candidate_ema_24_96_long_cash`: net `0.6632`, max drawdown `-0.4575`, turnover `375.0`, funding-aware net `0.4050`, next-open net `0.6614`, random percentile `0.96`, cost5x `-0.6307`.

## Interpretation

The run found a large metric improvement over the preflight EMA baseline, but the best result is not a novel trading edge. Always-long mostly recovers the benchmark buy-and-hold reference after one opening cost. It is robust to cost multipliers and next-open execution because turnover is almost zero, but it has severe drawdown, a weak 2022, and material funding drag.

The best adaptive follow-up signal is the loose funding filter on EMA 48/192. It modestly improves net and funding-aware net over plain EMA 48/192, but its higher turnover hurts 5x cost robustness. It should be tested next as an overlay component against the always-long floor.

## Decision

Treat always-long as the dev-score floor. Do not promote it as a completed BTC strategy. The next cell should rank candidates against buy-and-hold-relative evidence: drawdown reduction, funding-aware net, cost stress, next-open execution, per-year concentration, and random percentile.

Proposal written: `proposals/btc_autoresearch_cycle2_buy_hold_relative.md`.

## Verification

- `uv run python /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__overnight_v1/runs/btc-overnight-20260610T151519Z-autoresearch/run_candidate_sweep.py` completed.
- `uv run python bin/ai-lab docs audit` passed.
- `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed after synthesis with `21 passed`.
