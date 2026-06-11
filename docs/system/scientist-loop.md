# Scientist Loop

AI Lab uses one reusable loop:

1. Read task state, memory, source references, and the current run directory.
2. Propose one bounded experiment, audit, or synthesis step.
3. Execute local commands under the task constraints.
4. Evaluate the result against the task metric and robustness checks.
5. Preserve raw evidence locally in ignored task artifact directories.
6. Update `run-summary.md` with the observation and next action.
7. Update canonical task metadata only when the task contract or operating structure changes.

The loop is intentionally minimal. There are no scheme comparisons, work-unit manifests, or meta-scientist layers.

## Task Workspace Contract

Each task should contain:

- `task.yaml`: goal, metric, constraints, observability, source refs, and canonical task metadata.
- `loop.yaml`: source gates, preflight commands, cycle commands, and AI-agent invocation.
- `scientist.md`: agent-facing task instructions.
- `bin/`: maintained task-specific helper scripts.
- `code/`, `results/`, `plots/`, `reports/`, `runs/`, `assets/`: ignored local experiment workspaces with tracked placeholders.

## Artifact Policy

Experiment products are useful but noisy. They stay local by default. A run directory should be understandable from `run-summary.md`, `events.jsonl`, command logs, and declared artifacts. Promote durable learning by updating task metadata or generated public docs, not by committing local experiment logs.
