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

This account uses `/Users/sungs/ai-lab` as the local-first workspace for developing reusable AI scientist schemes and comparing them across tasks.

The active model has six layers:

1. Lab memory for shared behavior, policies, catalogs, and scheme knowledge.
2. Task memory for broad challenge or dataset-family context.
3. Scheme memory for reusable AI scientist orchestration patterns.
4. Evaluation-cell memory for one task-by-scheme application, target metric, constraints, runs, and evidence.
5. Work-unit memory for one method, ablation, observation, proxy, synthesis, audit, or infrastructure pass.
6. Meta-scientist memory for system-level analyses and proposals.

Agents should start from this core memory, then follow task, scheme, cell, work-unit, and meta links only as needed.

Do not store secrets or raw private connector content in durable memory, logs, reports, proposals, or asset metadata.
