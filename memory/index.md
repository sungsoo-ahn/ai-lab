# Memory Index

This is the durable local memory index for AI Lab.

## Files

- `system/core.md`: tiny shared memory all agents should read first.
- `system/procedures.md`: reusable AI Lab procedures and command conventions.
- `preferences.md`: stable user and system preferences.
- `source-index.md`: reusable source references.
- `research-history.md`: completed research task log.
- `reflections/`: retrospective lessons and proposed self-updates.

Task memory may live under `tasks/<task_id>/memory/` when needed.

The generated SQLite search index is `memory/index.sqlite` and can be rebuilt with:

```bash
bin/ai-lab memory index
```

## Rules

- Store only reusable, non-sensitive information.
- Do not store secrets or raw private connector content.
- Prefer links and short summaries over copied source text.
- Promote task memory to lab memory only when useful beyond one task.

