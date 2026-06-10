# AI Lab

AI Lab is a local-first workspace for developing and comparing AI scientist systems. It treats an AI scientist as an orchestration layer: a repeatable way to propose ideas, run bounded work, preserve evidence, and improve the research system over time.

The repo is intentionally organized around comparison. A task should stay separate from the scientist scheme that attempts it, and a scientist scheme should stay separate from the domain skills, judgment policy, and hypotheses it happens to use in one evaluation.

## Mental Model

| Layer | Question | Human-facing page | Local source |
| --- | --- | --- | --- |
| Lab | What rules, catalogs, and durable memory govern the workspace? | [System Guide](system/index.md) | `catalog/`, `memory/`, `policies/` |
| Task | What challenge or dataset family is being attempted? | [Tasks](tasks/index.md) | `tasks/active/<task_id>/task.yaml` |
| Scientist scheme | What reusable orchestration pattern is being applied? | [Scientist Schemes](schemes/index.md) | `schemes/<scheme_id>/scheme.yaml` |
| Skill bundle | What reusable capabilities can the scientist use? | [Scientist Components](reference/scientist-components.md) | `catalog/skill-bundles.yaml` |
| Research taste | What judgment policy ranks evidence and hypotheses? | [Scientist Components](reference/scientist-components.md) | `catalog/research-tastes.yaml` |
| Hypothesis | What task-specific claim is under test? | [Scientist Components](reference/scientist-components.md) | `catalog/hypotheses.yaml` |
| Evaluation cell | What happened when one scheme was applied to one task? | [Evaluation Matrix](evaluations/index.md) | `evaluations/active/<cell_id>/evaluation-cell.yaml` |
| Work unit | What focused method, audit, proxy, or synthesis pass produced evidence? | [Evaluation Matrix](evaluations/index.md) | `evaluations/active/<cell_id>/work_units/<work_unit_id>/` |
| Meta scientist | What should improve about the overall lab? | [Meta Scientist](meta/ai-lab-meta-v1.md) | `meta/active/ai_lab_meta_v1/` |

## What This Repo Is For

AI Lab is not just a benchmark runner. It is meant to answer questions such as:

- Which AI scientist scheme works best on a fixed task under the same constraints?
- Which task skills are reusable across schemes?
- Which hypotheses were tried, rejected, revived, or promoted?
- Which failures came from the scientist design rather than the domain task?
- What should the meta scientist change before the next generation of experiments?

The current active task is BTC Benchmark. It is deliberately narrow because the platform work is still early: the repo should first make one task reproducible, auditable, and comparable before adding many domains.

## Current State

The active workspace keeps one benchmark task, reusable scientist schemes, component catalogs, and evaluation cells. BTC Benchmark has paired AutoResearch and AutoScientist cells plus a completed smoke reference cell. Old non-benchmark material, optional integrations, and legacy plot assets were removed from the tracked tree so the repo can act as a cleaner platform baseline.

Important current boundaries:

- BTC Benchmark is the task, not the scientist.
- AutoResearch and AutoScientist are reusable schemes, not BTC-specific implementations.
- Skills, research taste, and seed hypotheses are explicit catalogs so they can be reused or swapped.
- Evaluation cells are the operational comparison surface.
- The meta scientist analyzes evidence and proposes improvements; it does not silently rewrite current tasks, metrics, or run specs.

## Start Here

1. Read the [System Guide](system/index.md) for the operating model and directory roles.
2. Read [Architecture](system/architecture.md) for the artifact lifecycle and execution contract.
3. Review [Scientist Components](reference/scientist-components.md) to understand scheme, skill, taste, hypothesis, and memory boundaries.
4. Compare this lab to external systems in [Comparable Systems](reference/comparable-systems.md).
5. Review active [Tasks](tasks/index.md), starting with [BTC Benchmark](tasks/btc-benchmark.md).
6. Review reusable [Scientist Schemes](schemes/index.md), especially [AutoResearch](schemes/autoresearch.md) and [AutoScientist](schemes/autoscientist.md).
7. Use the [Evaluation Matrix](evaluations/index.md) to inspect task-by-scheme cells.
8. Check [Meta Scientist](meta/ai-lab-meta-v1.md) for system-improvement analysis.
