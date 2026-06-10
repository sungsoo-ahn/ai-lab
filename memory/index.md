# Memory Index

This is the durable local memory index for AI Lab.

## Files

- `system/core.md`: tiny shared memory all agents should read first.
- `system/procedures.md`: reusable AI Lab procedures and command conventions.
- `reflections/`: retrospective lessons and proposed self-updates.
- `preferences.md`: stable user and system preferences.
- `source-index.md`: reusable source references.
- `research-history.md`: completed research task log.

Task memory lives under `tasks/active/<task_id>/memory/` when needed.

Scientist memory lives under `tasks/active/<task_id>/scientists/<scientist_id>/memory/`.

Work-unit memory lives under `tasks/active/<task_id>/scientists/<scientist_id>/work_units/<work_unit_id>/memory/`.

The generated SQLite search index is `memory/index.sqlite` and can be rebuilt with:

```sh
bin/ai-lab memory index
```

## Rules

- Store only reusable, non-sensitive information.
- Do not store secrets or raw private connector content.
- Prefer links and short summaries over copied source text.
- Promote work-unit memory to scientist memory only when useful beyond the work unit.
- Promote scientist memory to lab memory only through reflection.
