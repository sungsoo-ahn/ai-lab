---
id: system-core
type: system_memory
created_at: 2026-06-09
updated_at: 2026-06-09
confidence: high
sensitivity: public
status: active
links:
  - /Users/sungs/AGENTS.md
  - /Users/sungs/agent-system/docs/tutorial.md
---

# System Core Memory

This account uses `/Users/sungs/agent-system` as the local-first agent workspace.

Agents should optimize for cited research, local durable memory, targeted connector reads, and safe semi-autonomous organization.

Memory has three levels:

1. System memory for reusable agent-system behavior.
2. Project memory for one research topic.
3. Hypothesis memory for one method, experiment family, or subtask.

Agents should start from this core memory, then follow project and hypothesis links only as needed.

Do not store secrets or raw private connector content in durable memory, logs, reports, or asset metadata.
