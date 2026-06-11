# Extended Evaluation Cell Goal Template

Use this when assigning an evaluation cell to run as an extended evaluation.

```text
/goal Use the account AI Lab setup from ~/AGENTS.md. In ~/ai-lab, continue evaluation cell <cell_id>. Work nonstop at extended scale until the run is complete, reproducible, or blocked by an approval-only external action.

Read the cell guide, report, source map, current runbook, package/runtime policies, and relevant work-unit records. Run readiness gates first: source status, environment check, tests or smoke tests, data availability, and baseline reproduction. If missing Python dependencies block progress, install them through cell-local or inherited repo-local uv workflows and record the command. If an allowlisted runtime profile blocks progress, run bin/ai-lab runtime ensure <profile> and record the command. Do not silently install Docker, Node, connector integrations, credentials, shell/account configuration, or unlisted OS packages.

Spawn focused work units for independent methods, audits, ablations, infrastructure, and synthesis. Preserve failed trials, negative findings, package/runtime exceptions, commands, source refs, and artifacts. Do not weaken evaluation rules, costs, leakage gates, split policy, or holdout protection. Before stopping, update cell/work-unit manifests and reports, source maps, run summary, memory index, and public briefs when applicable. Run bin/ai-lab docs audit and relevant tests/builds.
```
