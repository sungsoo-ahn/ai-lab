# Scientist Components

Date: 2026-06-10
Status: active

## Summary

An AI scientist in this lab is easier to compare when decomposed into separate components:

```text
Scientist = Scheme + Skill Bundle + Research Taste + Hypotheses + Memory
```

This separation keeps reusable capabilities, judgment, and task-specific claims from collapsing into one vague object.

## Component Boundaries

| Component | Question | Example |
| --- | --- | --- |
| Scientist scheme | How is work orchestrated? | AutoResearch loop, AutoScientist team |
| Skill bundle | What can the scientist do? | Run BTC referee, build causal features, audit turnover |
| Research taste | What evidence and risks does it prioritize? | Prefer robust after-cost evidence over raw Sharpe |
| Hypothesis | What claim is being tested? | Funding context improves BTC referee score |
| Memory | What reusable prior knowledge is retained? | Known source refs, previous negative findings |

## Skill Versus Hypothesis

A skill describes **how to do work**. It should be reusable and should not assert that a task claim is true.

A hypothesis describes **what might be true**. It should be falsifiable against a task, metric, or observation.

Examples:

| Skill | Hypothesis |
| --- | --- |
| Run `btc_benchmark.run_benchmark` and parse reports. | A trend-following baseline ladder beats the EMA 12/48 readiness baseline. |
| Build leakage-safe rolling features. | Funding-rate context improves BTC performance after costs. |
| Audit turnover, cost multipliers, next-open score, and random percentile. | Turnover filters preserve more net return under 2x-5x costs. |

## Research Taste

Research taste is the prioritization policy. It is not the ability to execute a method and not a claim to test. It tells the scientist which ideas are worth attention, what evidence is convincing, and which risks should dominate decisions.

For BTC Benchmark, the active taste profile is `btc_robust_alpha_taste_v1`. It prefers causal, low-parameter, after-cost evidence and distrusts results that depend on high turnover, weak gates, poor next-open behavior, or unexplained concentration.

## Active BTC Components

| Component | ID | Local Source |
| --- | --- | --- |
| Skill bundle | `btc_benchmark_core_skills_v1` | `catalog/skill-bundles.yaml` |
| Research taste | `btc_robust_alpha_taste_v1` | `catalog/research-tastes.yaml` |
| Seed hypotheses | BTC trend, cost robustness, funding auxiliary signal | `catalog/hypotheses.yaml` |

The active BTC overnight cells declare these components in `scientist_composition` inside each `evaluation-cell.yaml`.
