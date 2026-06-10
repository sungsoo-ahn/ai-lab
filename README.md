# AI Lab Workspace

This directory is the local-first workspace for developing AI scientists on this account.

An AI scientist is a task-specific orchestration layer for agents. It tries to solve a hard, uncertain task by running work units, preserving evidence, and evolving its scheme and target metric over versions.

## Layout

- `catalog/`: broad task descriptions and reusable scientist scheme descriptions.
- `tasks/active/`: active task, scientist, and work-unit workspaces.
- `research/templates/`: reusable Markdown/YAML templates.
- `sources/`: source registry plus ignored shared code checkouts.
- `memory/`: durable system memory, reflections, source indexes, and history.
- `policies/`: operating rules for research, privacy, connectors, packages, and approvals.
- `archive/`: completed or superseded tasks, scientists, and packages.
- `logs/`: local activity notes.
- `docs/tutorial.md`: beginner walkthrough.
- `reports/system-status.md`: current system status.
- `bin/ai-lab`: canonical AI Lab helper.

## Layer Model

1. Lab: shared catalogs, policies, memory, logs, and scheme knowledge.
2. Task: a broad, under-specified challenge or dataset family.
3. Scientist: a concrete task-specific scheme, version, target metric, and constraints.
4. Work unit: a minimal agent context for one hypothesis, method, ablation, observation, proxy, synthesis, or infrastructure pass.

## Self-Evolution

Work units can propose changes to a scientist scheme, target metric, constraints, or next iteration. Accepted proposals are applied by creating a new scientist version; current scientist metrics are not silently mutated in place.

## Common Commands

```sh
bin/ai-lab task status btc
bin/ai-lab scientist status btc btc_autoresearch_v1
bin/ai-lab work-unit status btc btc_autoresearch_v1 regime_filter_probe
bin/ai-lab source status btc_autoresearch
bin/ai-lab memory index
bin/ai-lab memory search btc
bin/ai-lab memory audit
```

Compatibility wrappers remain for one migration cycle:

```sh
bin/agent-project status btc
bin/agent-hypothesis close btc regime_filter_probe
bin/agent-memory search btc
```

## Starting Codex

Use `codex-agent` to start a new session with the account AI Lab prompt and `/Users/sungs` as the working root.

```sh
codex-agent 'Use AI Lab to continue btc.'
```
