# Memory Index

This is the durable local memory index for AI Lab.

## Files

- `system/core.md`: tiny shared memory all agents should read first.
- `system/procedures.md`: reusable AI Lab procedures and command conventions.
- `reflections/`: retrospective lessons and proposed self-updates.
- `preferences.md`: stable user and system preferences.
- `source-index.md`: reusable source references.
- `research-history.md`: completed research task log.

Task memory may live under `tasks/active/<task_id>/memory/` when needed.

Scheme memory may live under `schemes/<scheme_id>/memory/` when needed.

Evaluation-cell memory lives under `evaluations/active/<cell_id>/memory/`.

Work-unit memory lives under `evaluations/active/<cell_id>/work_units/<work_unit_id>/memory/`.

Meta-scientist memory lives under `meta/active/<meta_id>/memory/` when needed.

The generated SQLite search index is `memory/index.sqlite` and can be rebuilt with:

```sh
bin/ai-lab memory index
```

## Rules

- Store only reusable, non-sensitive information.
- Do not store secrets or raw private connector content.
- Prefer links and short summaries over copied source text.
- Promote work-unit memory to cell memory only when useful beyond the work unit.
- Promote cell or meta memory to lab memory only through reflection.
