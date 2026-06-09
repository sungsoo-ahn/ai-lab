# Agent Research Log Guide

This guide explains how the public dashboard maps back to the local research workspace. It is meant for a future reader who wants to know what is active, what evidence exists, and how to restart without digging through the repository first.

## What You Are Looking At

The workspace keeps research under `/Users/sungs/agent-system`. The public site is a generated view of that workspace, not a separate source of truth.

The split is simple:

- reports and guides explain the current state in plain language;
- memory and logs preserve reusable context for future agent sessions;
- generated indexes and site files can be rebuilt.

Markdown and YAML are the canonical files. SQLite indexes, cached environments, and the generated Pages output are build products.

## How Memory Is Organized

The workspace uses three levels of memory:

1. System memory for account-level behavior and policies.
2. Project memory for one research topic.
3. Hypothesis memory for one method, experiment, or work unit.

When restarting work, read in this order:

1. `memory/system/core.md`
2. the active project report and source map
3. the relevant hypothesis report, if one is selected
4. deeper memory only when the current report points there

## Files Worth Opening First

- `README.md`: workspace overview and command entry points.
- `reports/system-status.md`: current account-level status.
- `research/active/<project_id>/report.md`: current project result and next step.
- `research/active/<project_id>/source-map.md`: sources and evidence pointers.
- `research/active/<project_id>/hypotheses/<hypothesis_id>/report.md`: work-unit result, evidence, and recommendation.

## Files Agents Use Behind The Scenes

- `memory/system/`: shared system memory.
- `memory/reflections/`: retrospective lessons and proposed self-updates.
- `logs/`: append-only activity and execution notes.
- `research/active/<project_id>/memory/`: project memory.
- `research/active/<project_id>/runs/`: project run records and artifacts.
- `research/active/<project_id>/state/`: generated project state.
- `research/active/<project_id>/hypotheses/<hypothesis_id>/memory/`: hypothesis memory.
- `research/active/<project_id>/hypotheses/<hypothesis_id>/runs/`: hypothesis run records.

## Assets And Evidence

An asset is a material used by the research: a repository, dataset, PDF, config, model checkpoint, result bundle, image, spreadsheet, or binary artifact.

Each project tracks assets in `assets.yaml`. Hypotheses should reference assets by `asset_id` instead of copying raw paths into every report. For ML work, dataset assets should record the schema, split policy, target definition, leakage constraints, preprocessing, and time range.

## Common Commands

Run these from `/Users/sungs/agent-system`:

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

## Restarting Work

Restarting means archive first, then create a clean active project:

1. The current project folder is moved to `archive/projects/<project_id>/<timestamp>/`.
2. A new clean `research/active/<project_id>/` folder is created from templates.
3. The new project links back to the archive as historical context.
4. Agents use the latest system memory, policies, templates, and tools.

## What To Edit By Hand

These files are intended for clarification and should stay readable:

- project `README.md`
- `project.md`
- `project.yaml`
- `assets.yaml`
- hypothesis `README.md`
- `hypothesis.yaml`

Avoid manual edits to generated SQLite indexes. Rebuild them with `bin/agent-memory index`.

## Privacy Rule

Do not store secrets, API keys, passwords, tokens, private keys, recovery codes, or raw private connector content in memory, logs, reports, or asset metadata.
