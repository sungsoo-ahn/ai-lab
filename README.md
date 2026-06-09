# Agent System Workspace

This directory is the local-first workspace for the Codex-native research agent on this account.

## Layout

- `inbox/`: unprocessed inputs from the user.
- `research/active/`: active research projects, reports, assets, hypotheses, and run records.
- `research/templates/`: reusable output templates.
- `memory/`: durable system/project/hypothesis memory, reflections, source indexes, and history.
- `policies/`: operating rules for research, privacy, connectors, and approvals.
- `archive/`: completed research packages.
- `logs/`: local activity notes for significant setup and maintenance.
- `docs/tutorial.md`: beginner walkthrough for using the system.
- `reports/system-status.md`: user-facing current system status.
- `bin/agent-memory`: memory indexing, search, audit, and reflection helper.
- `bin/agent-project`: project init/status/restart/archive helper.
- `bin/agent-hypothesis`: hypothesis init/close helper.

## Memory Hierarchy

The system uses three memory levels:

1. System memory for reusable agent-system behavior.
2. Project memory for one research topic.
3. Hypothesis memory for one method, experiment family, or subtask.

Agents should start from `memory/system/core.md`, then read the active project and hypothesis context. User-facing reports should explain current state from scratch so the maintainer does not need to inspect internal files.

## Assets

Projects track non-description materials in `assets.yaml`. Assets can be datasets, repositories, PDFs, configs, models, checkpoints, images, spreadsheets, result bundles, or other artifacts. Hypotheses should reference assets by `asset_id` rather than raw paths.

## Operating Defaults

- Keep canonical memory local.
- Keep Markdown/YAML canonical and treat SQLite indexes as generated.
- Use connectors for targeted reads when useful.
- Require approval for connector writes or external messages.
- Do not store secrets or raw sensitive values.
- Use `Brewfile` for OS-level package state.
- Use `uv` as the base Python package, project, and tool manager.
- Follow `policies/update-policy.md` before mutating packages, runtimes, connectors, or account configuration.

## Common Commands

```sh
bin/agent-project init <project_id>
bin/agent-project status <project_id>
bin/agent-project restart <project_id>
bin/agent-hypothesis init <project_id> <hypothesis_id>
bin/agent-hypothesis close <project_id> <hypothesis_id>
bin/agent-memory index
bin/agent-memory search <query>
bin/agent-memory audit
```

## Package Baseline

The lean package baseline is recorded in `Brewfile`. Homebrew owns OS-level CLI tools; `uv` owns Python environments and Python CLIs.

## Starting Codex

Use `codex-agent` to start a new session with the account-agent prompt and `/Users/sungs` as the working root.

You can pass an initial task:

```sh
codex-agent 'Use $research-agent to research <topic>.'
```
