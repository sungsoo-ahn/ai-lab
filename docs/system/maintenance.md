# Maintenance

Use this checklist before committing AI Lab changes. Maintenance is mostly about keeping the matrix inspectable: every human-facing summary should point to the local artifacts that prove it, and every machine-facing artifact should have enough summary context to be reviewed later.

## Matrix Consistency

- Active tasks have `task.yaml` and a public task page.
- Active schemes have `scheme.yaml`, `guide.md`, and a public scheme page.
- Active evaluation cells have `evaluation-cell.yaml`, `guide.md`, `report.md`, `run-spec.yaml`, and a public cell brief.
- Cell `active_work_units` and `completed_work_units` match each work-unit manifest.
- Prompt manifests point to existing prompt files inside the run directory.
- Meta scientists have `meta-scientist.yaml`, `guide.md`, `report.md`, and a public meta page.

## Documentation Checks

Before committing docs:

```bash
uv run python bin/ai-lab docs audit
uv run --with-requirements requirements.txt mkdocs build --strict
```

The audit checks public terminology, broken local links, prompt manifests, and static asset validity. The MkDocs build checks navigation and page rendering.

## Run Spec Checks

Before committing run-spec changes:

```bash
uv run python bin/ai-lab cell run-spec validate --all
uv run python bin/ai-lab cell run-all --once --dry-run
```

Use dry runs to confirm the command plan before launching unattended work. A run spec should be considered incomplete if it lacks source gates, expected artifacts, exit criteria, and a wall-clock bound for long runs.

## Source Checks

Before claiming benchmark evidence:

- verify the source checkout exists;
- record whether it has uncommitted changes;
- run the relevant readiness command;
- preserve the exact command and output artifact paths;
- note any source drift in the cell report.

For BTC Benchmark, use the source status and readiness commands documented on the task and evaluation pages.

## Boundaries

- Local writes under `ai-lab` are allowed for task, scheme, cell, work-unit, meta, docs, notes, and source-map files unless the user asks for read-only work.
- Connector writes, external submissions, account configuration changes, Docker, Node, and unlisted OS packages require explicit user approval.
- Long-running cells may install missing Python dependencies only through local or inherited `uv` workflows when the user has authorized automatic dependency setup.

## Cleanup

Cleanups should preserve decision-making evidence. Before deleting run artifacts, check whether the run produced:

- a failure mode that should be summarized;
- a candidate report or leaderboard that should be retained;
- a prompt or command issue that should update the runbook, source map, or memory;
- a proposal for the next cell version.

When artifacts are safe to remove, remove only the explicit run directories and logs. Do not clean ignored source checkouts or unrelated untracked files as part of docs or catalog maintenance.

## Commit Hygiene

Before committing:

1. Inspect `git status --short`.
2. Separate unrelated user changes from your own edits.
3. Run the smallest validation set that covers the change.
4. Mention any unrun validation in the final note.
5. Leave untracked active run artifacts alone unless the user asked to clean them.
