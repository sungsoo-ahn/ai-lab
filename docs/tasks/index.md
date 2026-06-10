# Tasks

Tasks define broad challenge or dataset families. They are deliberately separate from AI scientist schemes so the same scheme can be compared across multiple tasks.

## Active Tasks

| Task | Category | Status | Notes |
| --- | --- | --- | --- |
| [BTC Benchmark](btc-benchmark.md) | financial backtesting | active | Frozen referee benchmark task. |

## What Belongs In A Task

A task should describe the problem space and the contract for attempting it. It should not describe the orchestration pattern of a particular scientist.

Task-level material includes:

- dataset family or source;
- allowed and disallowed data use;
- benchmark or evaluator contract;
- candidate metrics;
- approval boundaries;
- known baselines;
- task-specific risks;
- active evaluation cells.

Scheme-level material belongs under [Scientist Schemes](../schemes/index.md). Skill, taste, and hypothesis material belongs under [Scientist Components](../reference/scientist-components.md).

## Task Readiness Checklist

Before adding serious evaluation cells, a task should have:

- a `task.yaml` manifest;
- a human-facing task page under `docs/tasks/`;
- at least one metric or decision criterion;
- source and data references;
- a list of disallowed shortcuts;
- a baseline or readiness command when possible;
- enough constraints to prevent a scientist from changing the task while optimizing it.

## Comparison Discipline

The same task can host many cells. The comparison is meaningful only when the task contract is stable. If the benchmark, data split, cost model, evaluator, or target metric changes, create a new task version or a clearly versioned cell instead of silently changing the old comparison.

## Adding Another Task

When adding a new task:

1. Add the catalog entry.
2. Create `tasks/active/<task_id>/task.yaml`.
3. Add a task page under `docs/tasks/`.
4. Add or reuse a skill bundle.
5. Add seed hypotheses only after the task contract is clear.
6. Create one smoke evaluation cell before creating larger cells.
7. Update this index and the evaluation matrix.
