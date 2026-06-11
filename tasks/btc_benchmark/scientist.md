# BTC Benchmark AI Scientist

This task uses the single AI scientist loop for BTC Benchmark. The goal is not to greedily maximize one local score at all costs; the goal is to make an interesting, important, evidence-backed observation that helps improve the metric while preserving the benchmark contract.

## Required Reading

- `~/ai-lab/policies/development-policy.md`
- `~/ai-lab/lab.yaml`
- `~/ai-lab/tasks/btc_benchmark/task.yaml`
- `~/ai-lab/sources/sources.yaml`
- `~/ai-lab/sources/checkouts/btc_benchmark/README.md`

## Loop

1. Inspect the current run directory, especially preflight logs and `preflight_baseline_report.json`.
2. Reconfirm the benchmark Strategy contract, runner, baseline rules, costs, split policy, and causality gates before writing strategy code.
3. Propose one bounded experiment or audit that can change the task understanding.
4. Run local scripts from the benchmark checkout environment, keeping generated code and result files in ignored task artifact directories.
5. Compare candidates against the preflight EMA baseline and passive always-long floor.
6. Preserve weak, failed, or disqualified results when they explain the next decision.
7. Do not commit experiment products. Promote only durable structural changes into task metadata, loop specs, scientist instructions, or maintained helper scripts.

## Evaluation Taste

Prefer robust observations over narrow local overfit:

- delta versus always-long net;
- max drawdown and drawdown improvement;
- funding-aware and next-open robustness;
- cost2x, cost3x, and cost5x survival;
- turnover and per-year concentration;
- random percentile for adaptive strategies;
- implementation portability outside the local run directory.

## Boundaries

- Do not edit tracked files in `sources/checkouts/btc_benchmark`.
- Do not modify referee scoring, costs, splits, causality gates, or sealed-holdout behavior.
- Do not submit externally or write connector state without explicit user approval.
- W&B/Weave observability is handled by the runner; do not add secrets to repo files.

## Final Outputs

Before stopping, update the relevant local run summary. Keep the runner-owned sections intact and fill in:

- `Observation`: the most important evidence-backed result from the cycle, including weak or failed results when they affect the next decision.
- `Next Action`: the next bounded experiment, audit, or stop condition.

Every generated experiment file should live under ignored task artifact directories such as `code/`, `results/`, `plots/`, `reports/`, `runs/`, or `assets/`. If the observation changes the task contract or operating structure, update canonical task metadata, loop specs, scientist instructions, maintained helper scripts, memory, or generated docs.

Run `uv run python bin/ai-lab docs sync`, `uv run python bin/ai-lab docs audit`, and targeted tests when time allows.
