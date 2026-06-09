---
id: system-procedures
type: system_memory
created_at: 2026-06-09
updated_at: 2026-06-09
confidence: high
sensitivity: public
status: active
links:
  - /Users/sungs/agent-system/policies/update-policy.md
  - /Users/sungs/agent-system/docs/tutorial.md
---

# System Procedures

## Research Projects

Use `bin/agent-project init <project_id>` to create a project. Use `bin/agent-project restart <project_id>` to archive the current active state and create a clean restarted workspace.

## Hypotheses

Use `bin/agent-hypothesis init <project_id> <hypothesis_id>` to create a hypothesis workspace. Hypotheses should reference project assets by `asset_id`.

## Memory

Use `bin/agent-memory index` to rebuild the generated SQLite search index. Use `bin/agent-memory search <query>` to search Markdown, YAML, and logs.

## Self-Evolution

Low-risk local memory, report, template, and index updates may be applied inside `/Users/sungs/agent-system`. Package, runtime, shell, connector, account config, and out-of-zone changes require explicit approval and must follow update policy.
