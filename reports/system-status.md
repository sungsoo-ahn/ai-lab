# AI Lab Status

Date: 2026-06-10

## Current Shape

- Workspace: `/Users/sungs/ai-lab`
- Compatibility symlink: `/Users/sungs/agent-system`
- Canonical storage: Markdown and YAML
- Generated search index: `memory/index.sqlite`
- Memory hierarchy: lab -> task -> scientist -> work unit
- Self-evolution policy: work-unit proposals are gated into new scientist versions

## Active Tasks

- `btc`: broad BTC task.

## Active Scientists

- `btc/btc_autoresearch_v1`: AutoResearch-style BTCUSDT short-horizon backtesting scientist. Current next step is a narrow robustness pass around the `t094` family before any sealed holdout decision.

## Local Services

- `slack-agent-bridge`: local service scaffold, not a task or scientist.

## User-Facing Entry Points

- `README.md`
- `docs/tutorial.md`
- `reports/system-status.md`
- `catalog/tasks.yaml`
- `catalog/scientist-schemes.yaml`

## Operational Notes

- Package/runtime changes still follow `policies/update-policy.md`.
- Connector writes still require explicit approval.
- Generated indexes can be rebuilt with `bin/ai-lab memory index`.
