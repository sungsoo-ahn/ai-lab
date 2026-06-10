# AI Lab Status

Date: 2026-06-10

## Current Shape

- Workspace: `/Users/sungs/ai-lab`
- Source registry: `/Users/sungs/ai-lab/sources/sources.yaml`
- Former compatibility symlink `/Users/sungs/agent-system` has been removed.
- Canonical storage: Markdown and YAML
- Prompt provenance: exact prompts are local run artifacts under scientist `runs/<run_id>/prompts/`
- Generated search index: `memory/index.sqlite`
- Memory hierarchy: lab -> task -> scientist -> work unit
- Self-evolution policy: work-unit proposals are gated into new scientist versions

## Active Tasks

- `btc`: broad BTC task.

## Active Scientists

- `btc/btc_autoresearch_v1`: BTCUSDT short-horizon AI scientist built around the inherited `btc_autoresearch` pipeline. Current next step is a narrow robustness pass around the `t094` family before any sealed holdout decision.

## Local Services

- `slack-agent-bridge`: local service scaffold, not a task or scientist.

## User-Facing Entry Points

- `README.md`
- `docs/index.md`
- `docs/system/index.md`
- `docs/system/prompt-provenance.md`
- `docs/scientists/btc-autoresearch-v1/index.md`
- `reports/system-status.md`
- `sources/sources.yaml`
- `catalog/tasks.yaml`
- `catalog/scientist-schemes.yaml`

## Operational Notes

- Package/runtime changes still follow `policies/update-policy.md`.
- Connector writes still require explicit approval.
- Generated indexes can be rebuilt with `bin/ai-lab memory index`.
