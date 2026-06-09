# Agent System Status

Date: 2026-06-09

## Current Shape

- Workspace: `/Users/sungs/agent-system`
- Canonical storage: Markdown and YAML
- Generated search index: `memory/index.sqlite`
- Initial trust zone: `/Users/sungs/agent-system`
- Memory hierarchy: system -> project -> hypothesis
- Project restart policy: archive then clean restart

## Active Projects

- `btc_autoresearch`: BTC short-horizon trading AutoResearch task extracted from the local cloned repository.
- `slack-agent-bridge`: setup proposal and local service scaffold.

## User-Facing Entry Points

- `README.md`
- `docs/tutorial.md`
- `reports/system-status.md`

## Operational Notes

- Package/runtime changes still follow `policies/update-policy.md`.
- Connector writes still require explicit approval.
- Generated indexes can be rebuilt with `bin/agent-memory index`.
