# BTC Benchmark AutoScientist Overnight v1

Date: 2026-06-10
Status: active

## Summary

This evaluation cell applies AutoScientist to BTC Benchmark for a bounded three-hour local run. It uses a fixed run spec with source gates, runtime checks, selected referee tests, data-load verification, EMA baseline reproduction, and one Codex synthesis loop that maintains shared state and independent work-unit lanes.

## Current Run Spec

- Source: `btc_benchmark` at registered commit `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`
- Scheme: AutoScientist
- Skill bundle: `btc_benchmark_core_skills_v1`
- Research taste: `btc_robust_alpha_taste_v1`
- Seed hypotheses: trend-following baseline ladder, cost robustness filter, funding auxiliary signal
- Wall budget: 180 minutes
- Target metric: `referee_dev_score`
- Preflight artifacts: `preflight_baseline_report.json` and `preflight_leaderboard.jsonl` in the run directory
- Synthesis prompt: `evaluations/active/btc_benchmark__autoscientist__overnight_v1/synthesis-prompt.md`

## Launch

Run this cell directly:

```sh
uv run python bin/ai-lab cell run btc_benchmark__autoscientist__overnight_v1 --continuous --run-id btc-overnight-autoscientist
```

## Readiness

Setup checks on 2026-06-10 confirmed selected referee tests pass, local data loads, and the EMA baseline reproduces without disqualification. The runtime profile passes while Homebrew prints an ownership warning for `/opt/homebrew/Cellar`.

## Expected Result

The first overnight run should update the cell report, this brief, any created work-unit briefs, and the run summary with consensus, disagreements, robustness risks, and next-version proposals if needed.

## Component Model

See [Scientist Components](../reference/scientist-components.md) for how this cell separates scheme, skills, research taste, and hypotheses.
