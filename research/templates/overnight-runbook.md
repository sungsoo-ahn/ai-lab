# Overnight Runbook: <project_id>

Date: <YYYY-MM-DD>
Status: draft

## Goal

<Explain the overnight goal from scratch.>

## Autonomy

- Agents may run a full research loop.
- Agents may silently install missing Python project dependencies using project-local `uv` workflows.
- Agents may not silently install OS-level tools, Node, Docker, connector integrations, shell configuration, or account configuration.

## Gates

1. Verify environment and tests.
2. Verify required assets exist or build them.
3. Reproduce the baseline.
4. Only then launch parallel hypothesis/work units.

## Work Units

| Work Unit | Purpose | Write Scope | Stop Condition |
| --- | --- | --- | --- |
| <id> | <purpose> | <paths> | <condition> |

## Required Final Outputs

- Project report updated.
- Each work unit report updated.
- Run summary written under `runs/`.
- Installed packages and commands recorded.
