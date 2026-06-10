# Scientist Components

Date: 2026-06-10
Status: active

## Summary

An AI scientist in this lab is easier to compare when decomposed into separate components:

```text
Scientist = Scheme + Skill Bundle + Research Taste + Hypotheses + Memory
```

This separation keeps reusable capabilities, judgment, and task-specific claims from collapsing into one vague object.

The decomposition also makes comparisons less slippery. If two cells use the same scheme but different skill bundles, the result is not a pure scheme comparison. If two cells use the same skills but different research taste, the result is partly a judgment-policy comparison. The cell should state these differences explicitly.

## Component Boundaries

| Component | Question | Example |
| --- | --- | --- |
| Scientist scheme | How is work orchestrated? | AutoResearch loop, AutoScientist team |
| Skill bundle | What can the scientist do? | Run BTC referee, build causal features, audit turnover |
| Research taste | What evidence and risks does it prioritize? | Prefer robust after-cost evidence over raw Sharpe |
| Hypothesis | What claim is being tested? | Funding context improves BTC referee score |
| Memory | What reusable prior knowledge is retained? | Known source refs, previous negative findings |

## Component Tests

Use these tests when deciding where something belongs:

| Question | If yes, likely component |
| --- | --- |
| Would this still matter on another task? | Scheme, skill, taste, or memory |
| Does it describe control flow, roles, or cadence? | Scientist scheme |
| Does it describe an ability or procedure? | Skill bundle |
| Does it rank what evidence is convincing? | Research taste |
| Does it assert something about the world or task? | Hypothesis |
| Does it summarize a previous result that should inform future work? | Memory |
| Does it bind task, scheme, metric, and run artifacts? | Evaluation cell |

## Skill Versus Hypothesis

A skill describes **how to do work**. It should be reusable and should not assert that a task claim is true.

A hypothesis describes **what might be true**. It should be falsifiable against a task, metric, or observation.

Examples:

| Skill | Hypothesis |
| --- | --- |
| Run `btc_benchmark.run_benchmark` and parse reports. | A trend-following baseline ladder beats the EMA 12/48 readiness baseline. |
| Build leakage-safe rolling features. | Funding-rate context improves BTC performance after costs. |
| Audit turnover, cost multipliers, next-open score, and random percentile. | Turnover filters preserve more net return under 2x-5x costs. |

Bad component boundaries:

| Bad wording | Problem | Better placement |
| --- | --- | --- |
| "Skill: funding improves BTC." | This is a claim, not an ability. | Hypothesis |
| "Hypothesis: run the referee." | This is an action, not a falsifiable claim. | Skill |
| "Taste: use EMA 24/96." | This is a method choice, not a judgment policy. | Hypothesis or work unit |
| "Scheme: BTC robust alpha." | This mixes orchestration with domain preference. | Research taste plus task constraints |

## Research Taste

Research taste is the prioritization policy. It is not the ability to execute a method and not a claim to test. It tells the scientist which ideas are worth attention, what evidence is convincing, and which risks should dominate decisions.

For BTC Benchmark, the active taste profile is `btc_robust_alpha_taste_v1`. It prefers causal, low-parameter, after-cost evidence and distrusts results that depend on high turnover, weak gates, poor next-open behavior, or unexplained concentration.

Research taste should be explicit because many research disagreements are not about the command that ran. They are about which evidence should count. Two scientists can see the same leaderboard and make different decisions if one prioritizes raw score and another prioritizes cost robustness.

## Memory

Memory is durable, non-sensitive prior knowledge. It can include:

- source references that future work should reuse;
- known failed ideas;
- task-specific gotchas;
- user preferences;
- stable terminology decisions;
- accepted proposals and why they were accepted.

Memory should not include credentials, private raw connector content, or large artifact dumps. A memory note should be useful to future work without becoming a hidden dependency that replaces task manifests or run evidence.

## Evaluation Cells

An evaluation cell is where the components become operational. A cell should declare:

- the task;
- the scientist scheme;
- the skill bundle;
- the research taste profile;
- seed hypotheses;
- target metric and constraints;
- source maps and expected artifacts;
- run specs and evidence.

This makes it possible to compare AutoResearch versus AutoScientist on BTC Benchmark without pretending that the task, skills, and taste are part of the scheme itself.

## Active BTC Components

| Component | ID | Local Source |
| --- | --- | --- |
| Skill bundle | `btc_benchmark_core_skills_v1` | `catalog/skill-bundles.yaml` |
| Research taste | `btc_robust_alpha_taste_v1` | `catalog/research-tastes.yaml` |
| Seed hypotheses | BTC trend, cost robustness, funding auxiliary signal | `catalog/hypotheses.yaml` |

The active BTC cells declare these components in `scientist_composition` inside each `evaluation-cell.yaml`.

## Maintenance Rules

- Add a new skill when the lab gains a reusable ability.
- Add a new hypothesis when there is a falsifiable task claim.
- Add a new taste profile when the judgment policy changes.
- Add a new scheme when the orchestration pattern changes.
- Add a new evaluation cell version when the binding of task, scheme, metric, constraints, or major components changes.
- Preserve old component versions when existing evidence depends on them.
