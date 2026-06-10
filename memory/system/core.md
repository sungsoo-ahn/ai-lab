---
id: system-core
type: system_memory
created_at: 2026-06-09
updated_at: 2026-06-10
confidence: high
sensitivity: public
status: active
links:
  - /Users/sungs/AGENTS.md
  - /Users/sungs/ai-lab/docs/index.md
  - /Users/sungs/ai-lab/docs/system/index.md
---

# AI Lab Core Memory

This account uses `/Users/sungs/ai-lab` as the local-first workspace for developing AI scientists.

An AI scientist is a task-specific orchestration layer for agents. It tries to solve hard, uncertain tasks through versioned schemes, target metrics, work units, evidence preservation, and proposal-gated self-evolution.

Memory has four levels:

1. Lab memory for shared behavior, policies, catalogs, and scheme knowledge.
2. Task memory for broad challenge or dataset-family context.
3. Scientist memory for one task-specific scheme, version, and target metric.
4. Work-unit memory for one hypothesis, method, ablation, observation, proxy, synthesis, or infrastructure pass.

Agents should start from this core memory, then follow task, scientist, and work-unit links only as needed.

Do not store secrets or raw private connector content in durable memory, logs, reports, proposals, or asset metadata.
