# Agent System Workspace

This directory is the local-first workspace for the Codex-native research agent on this account.

## Layout

- `inbox/`: unprocessed inputs from the user.
- `research/active/`: working research briefs and source maps.
- `research/templates/`: reusable output templates.
- `memory/`: durable local notes, preferences, source indexes, and history.
- `policies/`: operating rules for research, privacy, connectors, and approvals.
- `archive/`: completed research packages.
- `logs/`: local activity notes for significant setup and maintenance.

## Operating Defaults

- Keep canonical memory local.
- Use connectors for targeted reads when useful.
- Require approval for connector writes or external messages.
- Do not store secrets or raw sensitive values.
- Use `Brewfile` for OS-level package state.
- Use `uv` as the base Python package, project, and tool manager.
- Follow `policies/update-policy.md` before mutating packages, runtimes, connectors, or account configuration.

## Package Baseline

The lean package baseline is recorded in `Brewfile`. Homebrew owns OS-level CLI tools; `uv` owns Python environments and Python CLIs.

## Starting Codex

Use `codex-agent` to start a new session with the account-agent prompt and `/Users/sungs` as the working root.

You can pass an initial task:

```sh
codex-agent 'Use $research-agent to research <topic>.'
```
