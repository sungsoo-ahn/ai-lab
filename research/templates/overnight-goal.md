# Overnight Scientist Goal Template

Use this when assigning a scientist to run at overnight scale.

```text
/goal Use the account AI Lab setup from ~/AGENTS.md. In ~/ai-lab, continue task <task_id> and scientist <scientist_id>. Work nonstop at overnight scale until the run is complete, reproducible, or blocked by an approval-only external action.

Read the scientist guide, report, source map, current runbook, package/runtime policies, and relevant work-unit records. Run readiness gates first: source status, environment check, tests or smoke tests, data availability, and baseline reproduction. If missing Python dependencies block progress, install them through scientist-local or inherited repo-local uv workflows and record the command. If an allowlisted runtime profile blocks progress, run bin/ai-lab runtime ensure <profile> and record the command. Do not silently install Docker, Node, connector integrations, credentials, shell/account configuration, or unlisted OS packages.

Spawn focused work units for independent hypotheses, audits, ablations, infrastructure, and synthesis. Preserve failed trials, negative findings, package/runtime exceptions, commands, source refs, and artifacts. Do not weaken evaluation rules, costs, leakage gates, split policy, or holdout protection. Before stopping, update scientist/work-unit manifests and reports, source maps, run summary, memory index, and public manuals when applicable. Run bin/ai-lab docs audit and relevant tests/builds.
```
