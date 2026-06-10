# System Guide

The AI Lab is organized to compare reusable AI scientist schemes across tasks while keeping evidence, prompts, and operational decisions inspectable. The core discipline is separation: a task is not a scientist, a scientist scheme is not a hypothesis, and a successful run is not automatically a system improvement.

## Design Goals

| Goal | Practical meaning |
| --- | --- |
| Reproducibility | Important work runs from fixed command lines or versioned run specs instead of improvised terminal sessions. |
| Comparability | Different schemes can be applied to the same task with the same target metric, source gates, and artifact expectations. |
| Evidence preservation | Runs keep commands, prompts, outputs, summaries, and failure reasons close to the evaluation cell that produced them. |
| Bounded autonomy | Agents can execute approved local commands and run specs, but connector writes, external submissions, and environment changes stay gated. |
| System learning | The meta scientist looks across cells and proposes improvements without mutating current metrics or constraints in place. |

## Principles

- Tasks describe broad challenge or dataset families.
- Scientist schemes describe reusable orchestration patterns.
- Skill bundles describe reusable capabilities.
- Research taste profiles describe prioritization and judgment.
- Hypotheses describe task-specific claims to test.
- Evaluation cells apply one scheme to one task and own metrics, run specs, work units, prompts, and evidence.
- Work units are the smallest useful research contexts; they can be methods, audits, ablations, observations, proxies, synthesis passes, or infrastructure passes.
- Work-unit proposals create new cell versions instead of silently mutating current metrics or constraints.
- The meta scientist analyzes the matrix and proposes lab improvements; it does not edit the system automatically.

## Current Directories

| Directory | Audience | Purpose |
| --- | --- | --- |
| `docs/` | human-facing | Static guides, task pages, scheme pages, reference material, and evaluation summaries. |
| `tasks/active/` | both | Active task definitions and task-local notes. |
| `schemes/` | both | Reusable AI scientist scheme definitions. |
| `catalog/` | both | Task catalog, scientist scheme catalog, skill bundles, research tastes, and hypotheses. |
| `evaluations/active/` | both | Task-by-scheme operational cells, run specs, prompts, source maps, and run artifacts. |
| `meta/active/` | both | Meta-scientist analyses and improvement proposals. |
| `memory/` | both | Durable non-sensitive preferences, source references, and system memory. |
| `policies/` | both | Connector, privacy, runtime, install, and update policies. |
| `logs/` | agent-facing | Local activity notes and ignored runtime logs. |
| `sources/` | agent-facing | External source checkouts and source registry. |

Docs should expose human-facing and shared concepts. Purely agent-facing runtime noise, transient logs, and cloned source trees should stay out of public docs unless they explain a reproducible workflow.

## Operating Loop

1. Define or select a task.
2. Select a reusable scientist scheme.
3. Attach explicit skills, research taste, and seed hypotheses.
4. Create an evaluation cell that binds the task and scheme under a fixed metric and constraints.
5. Run work units or a run spec.
6. Preserve artifacts and summarize evidence.
7. Compare cells in the evaluation matrix.
8. Let the meta scientist propose changes for the next iteration.

The loop is deliberately slower than a raw agent terminal session. The extra structure makes it possible to answer why a result happened, whether another scheme had the same chance, and what should change next.

## What Counts As Done

A cell or work unit is not done because it ran without crashing. It should leave enough evidence for another agent or human to inspect:

- the exact task, scheme, skills, taste, and hypotheses used;
- the fixed commands or run spec;
- the source and environment gates that passed or failed;
- the artifacts that support the result;
- the failure mode if the run did not complete;
- the next proposal, rejection, or follow-up decision.

## Related Guides

- [Architecture](architecture.md)
- [Comparable Systems](../reference/comparable-systems.md)
- [Scientist Components](../reference/scientist-components.md)
- [Prompt Provenance](prompt-provenance.md)
- [Maintenance](maintenance.md)
- [Documentation Standards](documentation-standards.md)
