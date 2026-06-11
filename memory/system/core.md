---
id: system-core
type: system_memory
created_at: 2026-06-09
updated_at: 2026-06-11
confidence: high
sensitivity: public
status: active
links:
  - /Users/sungs/ai-lab/policies/development-policy.md
  - /Users/sungs/ai-lab/README.md
  - /Users/sungs/ai-lab/lab.yaml
  - /Users/sungs/ai-lab/docs/index.md
---

# AI Lab Core Memory

This account uses `/Users/sungs/ai-lab` as a local-first workspace for one reusable AI scientist loop.

The active model has four layers:

1. Lab configuration, policies, memory, and source registry.
2. Task workspaces under `tasks/<task_id>/`.
3. Task-local runs under `tasks/<task_id>/runs/`, ignored by Git.
4. Local experiment workspaces for ignored code, reports, assets, results, plots, and runs.

Normal AI scientist runs require W&B/Weave observability through `sungsoo-ahn/ai-lab`. Credentials must stay outside Git.

Do not store secrets or raw private connector content in durable memory, logs, reports, proposals, or asset metadata.
