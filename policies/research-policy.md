# Research Policy

AI Lab uses one task-local AI scientist loop.

## Evidence

Every durable claim should point to canonical task metadata, a source reference, W&B run, or local run directory. Experiment products under `tasks/<task_id>/` are ignored by Git by default.

## Task Workspaces

Use `tasks/<task_id>/` for task contracts and AI-scientist operating structure. A task workspace owns the task contract, metric, constraints, loop spec, agent instructions, maintained helper scripts, and ignored local experiment workspaces.

## Changes

Do not weaken task metrics, referee rules, source gates, privacy policy, or approval boundaries silently. If a task definition changes after evidence exists, update the task report and observation log so old evidence remains interpretable.

## External Actions

External submissions, connector writes, account configuration changes, Docker, Node, credentials, and unlisted OS packages require explicit user approval.
