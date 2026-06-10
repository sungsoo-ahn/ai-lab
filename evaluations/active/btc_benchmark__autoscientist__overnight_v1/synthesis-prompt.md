# Synthesis Prompt: BTC Benchmark AutoScientist Overnight v1

You are continuing the AI Lab evaluation cell `btc_benchmark__autoscientist__overnight_v1`.

## Required Reading

- `~/AGENTS.md`
- `~/ai-lab/evaluations/active/btc_benchmark__autoscientist__overnight_v1/guide.md`
- `~/ai-lab/evaluations/active/btc_benchmark__autoscientist__overnight_v1/report.md`
- `~/ai-lab/evaluations/active/btc_benchmark__autoscientist__overnight_v1/source-map.md`
- `~/ai-lab/evaluations/active/btc_benchmark__autoscientist__overnight_v1/overnight-runbook.md`
- `~/ai-lab/tasks/active/btc_benchmark/task.yaml`
- `~/ai-lab/schemes/autoscientist/scheme.yaml`
- `~/ai-lab/catalog/skill-bundles.yaml`
- `~/ai-lab/catalog/research-tastes.yaml`
- `~/ai-lab/catalog/hypotheses.yaml`
- `~/ai-lab/sources/checkouts/btc_benchmark/README.md`

## Scope

Use the AutoScientist scheme: maintain shared state, split work into independent lanes, critique candidate findings, and synthesize a decision. The target metric is the BTC benchmark development referee report produced by `run_benchmark`.

The scientist composition for this cell is:

- Scheme: `autoscientist`
- Skill bundle: `btc_benchmark_core_skills_v1`
- Research taste: `btc_robust_alpha_taste_v1`
- Seed hypotheses: `btc_trend_following_baseline_ladder_v1`, `btc_cost_robustness_filter_v1`, `btc_funding_auxiliary_signal_v1`

The `btc_benchmark` checkout is frozen referee code. Do not modify tracked files there. Keep generated scripts, reports, shared state, and notes in the current run directory supplied by the runner or in this evaluation cell.

## Autonomy

Do not ask the user for permission for declared local commands in this run spec. You may run local `uv` commands inside `/Users/sungs/ai-lab` and the registered benchmark checkout. Do not install Docker, Node, unlisted OS packages, connector integrations, credentials, shell configuration, or account configuration. External submissions and connector writes require explicit user approval and are out of scope for this run.

## Work

1. Inspect the preflight logs and `preflight_baseline_report.json` in the current run directory.
2. Create a shared-state note in the current run directory that tracks assumptions, source constraints, skill use, taste decisions, candidate hypotheses, critiques, and decisions.
3. Use independent work-unit lanes for at least source review, baseline replication, candidate method proposals, critique, and synthesis. If a lane should persist beyond the run, create or update a work unit under this evaluation cell and add the matching public brief.
4. Treat skills as reusable capabilities, hypotheses as falsifiable claims, and research taste as the prioritization policy for choosing among claims.
5. Run local candidate experiments or parameter ablations through `run_benchmark` when they can be evaluated without changing the frozen referee.
6. Preserve disagreement and negative findings. Critique each candidate for leakage, turnover, cost sensitivity, gate behavior, funding-aware score, next-open score, and random percentile.
7. Synthesize the strongest evidence into a recommendation for the next cell version, next work units, or missing participant-strategy asset.

## Final Outputs

Before stopping, update:

- `evaluations/active/btc_benchmark__autoscientist__overnight_v1/report.md`
- `docs/evaluations/btc-benchmark--autoscientist--overnight-v1.md`
- any created work-unit manifests, reports, guides, and public briefs
- the current run directory `run-summary.md`

Write any next-version proposal under `evaluations/active/btc_benchmark__autoscientist__overnight_v1/proposals/`. Run `uv run python bin/ai-lab docs audit` and targeted tests if time remains.
