# Update Policy

## Default Rule

No package, runtime, connector, or account configuration mutation should happen without a written proposal first, unless the user explicitly asks for a specific change and the risk is low.

## Overnight Research Package Exception

When the user explicitly authorizes an overnight research run with silent package installs, agents may install missing Python scientist dependencies without pausing for approval, subject to all of these limits:

- use scientist-local or inherited repository-local `uv` workflows only (`uv sync`, `uv add`, `uv run`, or equivalent local environment setup);
- keep dependency changes manifest-backed in the relevant `pyproject.toml` and `uv.lock` when the dependency is needed beyond a one-off command;
- do not install into Apple system Python;
- do not use direct `pip` unless maintaining an inherited project command that has no reasonable `uv` equivalent, and record the exception in the run report;
- do not install Homebrew, Node, Docker, system packages, browser drivers, kernels, credentials, or connector/account integrations silently;
- log installed packages, commands, and verification result in the relevant scientist or work-unit report.

This exception applies only to the authorized overnight run scope. It does not authorize connector writes, shell startup changes, account configuration changes, or broad filesystem writes.

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

- update `ai-lab/Brewfile` before installing or removing Homebrew packages;
- run `brew bundle check --file ai-lab/Brewfile` before and after installation when Homebrew exists;
- do not use `uv self update` when `uv` is installed by Homebrew;
- keep Python project dependencies in `pyproject.toml` and `uv.lock`.

## Connector And External Writes

Drive, Gmail, Calendar, Slack, and other external writes always require explicit approval. Package update approval does not imply connector write approval.

## Logging

After approved changes, append a short entry to `ai-lab/logs/activity.md` with the date, action, and verification result.
