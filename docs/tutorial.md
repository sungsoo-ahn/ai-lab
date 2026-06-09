# Agent System Tutorial

This is the local-first research agent workspace for this account. It is designed so a user can return after forgetting the details and still understand what exists, what is active, and how to restart safely.

## What This System Does

The system keeps research work under `/Users/sungs/agent-system`.

It separates:

- user-facing files: tutorials, overviews, reports, and status pages;
- agent-facing files: logs, memory, run metadata, indexes, and reflections.

The canonical files are Markdown and YAML. SQLite files are generated search indexes and can be rebuilt.

## Memory Hierarchy

Agents use three memory levels:

1. System memory: reusable knowledge about the agent system itself.
2. Project memory: knowledge for one research topic.
3. Hypothesis memory: knowledge for one method, experiment family, or subtask.

Agents should read memory in this order:

1. `memory/system/core.md`
2. the active project files
3. the active hypothesis files, if a hypothesis is selected
4. linked deeper records only when needed

## Important User-Facing Files

- `README.md`: system overview.
- `docs/tutorial.md`: this tutorial.
- `reports/system-status.md`: current system status.
- `research/active/<project_id>/README.md`: project overview.
- `research/active/<project_id>/project.md`: project description.
- `research/active/<project_id>/report.md`: current project status and results.
- `research/active/<project_id>/hypotheses/<hypothesis_id>/README.md`: hypothesis overview.
- `research/active/<project_id>/hypotheses/<hypothesis_id>/report.md`: hypothesis result summary.

## Important Agent-Facing Files

- `memory/system/`: shared system memory.
- `memory/reflections/`: retrospective lessons and proposed self-updates.
- `logs/`: append-only activity and execution notes.
- `research/active/<project_id>/memory/`: project memory.
- `research/active/<project_id>/runs/`: project run records and artifacts.
- `research/active/<project_id>/state/`: generated project state.
- `research/active/<project_id>/hypotheses/<hypothesis_id>/memory/`: hypothesis memory.
- `research/active/<project_id>/hypotheses/<hypothesis_id>/runs/`: hypothesis run records.

## Assets

An asset is any non-description material used by a project: a dataset, repository, PDF, config, model checkpoint, result bundle, image, spreadsheet, or binary artifact.

Each project has an `assets.yaml` registry. Hypotheses should reference assets by `asset_id`, not by raw path. For ML work, datasets are `type: dataset` assets with extra details such as schema, split policy, target definition, leakage constraints, preprocessing, and time range.

## Common Commands

From `/Users/sungs/agent-system`:

```sh
bin/agent-project init my_project
bin/agent-project status my_project
bin/agent-hypothesis init my_project first_method
bin/agent-hypothesis close my_project first_method
bin/agent-memory index
bin/agent-memory search "query terms"
bin/agent-memory audit
bin/agent-project restart my_project
bin/agent-project archive my_project
```

## Restarting A Project

Restart means archive then clean restart:

1. The current project folder is moved to `archive/projects/<project_id>/<timestamp>/`.
2. A new clean `research/active/<project_id>/` folder is created from templates.
3. The new project links back to the archive as historical context.
4. Agents use the latest system memory, policies, templates, and tools.

## What Is Safe To Edit

User-facing files are safe to edit when you want to clarify intent:

- project `README.md`
- `project.md`
- `project.yaml`
- `assets.yaml`
- hypothesis `README.md`
- `hypothesis.yaml`

Avoid manual edits to generated SQLite indexes. Rebuild them with `bin/agent-memory index`.

## Privacy Rule

Do not store secrets, API keys, passwords, tokens, private keys, recovery codes, or raw private connector content in memory, logs, reports, or asset metadata.
