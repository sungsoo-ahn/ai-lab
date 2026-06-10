# Synthesis Prompt: BTC Benchmark AutoResearch Overnight v1

You are continuing the AI Lab evaluation cell `btc_benchmark__autoresearch__overnight_v1`.

## Required Reading

- `~/AGENTS.md`
- `~/ai-lab/evaluations/active/btc_benchmark__autoresearch__overnight_v1/guide.md`
- `~/ai-lab/evaluations/active/btc_benchmark__autoresearch__overnight_v1/report.md`
- `~/ai-lab/evaluations/active/btc_benchmark__autoresearch__overnight_v1/source-map.md`
- `~/ai-lab/evaluations/active/btc_benchmark__autoresearch__overnight_v1/overnight-runbook.md`
- `~/ai-lab/tasks/active/btc_benchmark/task.yaml`
- `~/ai-lab/schemes/autoresearch/scheme.yaml`
- `~/ai-lab/catalog/skill-bundles.yaml`
- `~/ai-lab/catalog/research-tastes.yaml`
- `~/ai-lab/catalog/hypotheses.yaml`
- `~/ai-lab/sources/checkouts/btc_benchmark/README.md`

## Scope

Use the AutoResearch scheme: propose a bounded local experiment, run it, evaluate the referee report, record evidence, then synthesize the next decision. The target metric is the BTC benchmark development referee report produced by `run_benchmark`.

The scientist composition for this cell is:

- Scheme: `autoresearch`
- Skill bundle: `btc_benchmark_core_skills_v1`
- Research taste: `btc_robust_alpha_taste_v1`
- Seed hypotheses: `btc_trend_following_baseline_ladder_v1`, `btc_cost_robustness_filter_v1`, `btc_funding_auxiliary_signal_v1`

The `btc_benchmark` checkout is frozen referee code. Do not modify tracked files there. Keep generated scripts, reports, and notes in the current run directory supplied by the runner or in this evaluation cell.

## Autonomy

Do not ask the user for permission for declared local commands in this run spec. You may run local `uv` commands inside `/Users/sungs/ai-lab` and the registered benchmark checkout. Do not install Docker, Node, unlisted OS packages, connector integrations, credentials, shell configuration, or account configuration. External submissions and connector writes require explicit user approval and are out of scope for this run.

## Work

1. Inspect the preflight logs and `preflight_baseline_report.json` in the current run directory.
2. Use the skill bundle for execution and robustness audits; do not confuse skills with hypotheses.
3. Use the taste profile to rank which seed hypothesis or quick follow-up is worth testing first.
4. Inspect the benchmark Strategy contract, runner, baseline rules, causality gates, and tests enough to avoid invalid strategy designs.
5. Create local experiment scripts under the current run directory. Use the benchmark source as an importable referee, not as an editable workspace.
6. Run a small sequence of candidate strategy experiments or parameter ablations through `run_benchmark`. Execute run-local scripts from the benchmark checkout environment, for example `cd /Users/sungs/ai-lab/sources/checkouts/btc_benchmark && uv run python /absolute/path/to/run-script.py`, so the benchmark dependencies and package imports are available. Preserve every report, including weak or disqualified results.
7. Compare candidates against the preflight EMA baseline and summarize robustness risks such as turnover, costs, random percentile, gate behavior, funding-aware score, and next-open score.
8. If no credible metric improvement is found, write the negative finding clearly and propose the next cell version or missing participant-strategy asset.

## Final Outputs

Before stopping, update:

- `evaluations/active/btc_benchmark__autoresearch__overnight_v1/report.md`
- `docs/evaluations/btc-benchmark--autoresearch--overnight-v1.md`
- the current run directory `run-summary.md`

Write any next-version proposal under `evaluations/active/btc_benchmark__autoresearch__overnight_v1/proposals/`. Run `uv run python bin/ai-lab docs audit` and targeted tests if time remains.
