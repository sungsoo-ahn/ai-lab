# Update Policy

## Default Rule

No package, runtime, connector, or account configuration mutation should happen without a written proposal first, unless the user explicitly asks for a specific change and the risk is low.

## Proposal Contents

An update proposal should include:

- purpose;
- exact commands or files to change;
- affected packages, runtimes, policies, or connectors;
- risk and privacy impact;
- rollback path;
- verification commands;
- whether network, elevated permissions, or connector writes are required.

## Package Updates

Use Homebrew for OS-level tools and `uv` for Python tooling. Prefer manifest-backed changes:

- update `agent-system/Brewfile` before installing or removing Homebrew packages;
- run `brew bundle check --file agent-system/Brewfile` before and after installation when Homebrew exists;
- do not use `uv self update` when `uv` is installed by Homebrew;
- keep Python project dependencies in `pyproject.toml` and `uv.lock`.

## Connector And External Writes

Drive, Gmail, Calendar, Slack, and other external writes always require explicit approval. Package update approval does not imply connector write approval.

## Logging

After approved changes, append a short entry to `agent-system/logs/activity.md` with the date, action, and verification result.

