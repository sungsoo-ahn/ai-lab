# Memory Index

This is the durable local memory index for the research agent.

## Files

- `system/core.md`: tiny shared memory all agents should read first.
- `system/procedures.md`: reusable system procedures and command conventions.
- `reflections/`: retrospective lessons and proposed self-updates.
- `preferences.md`: stable user and system preferences.
- `source-index.md`: reusable source references.
- `research-history.md`: completed research task log.

Project memory lives under `research/active/<project_id>/memory/`.

Hypothesis memory lives under `research/active/<project_id>/hypotheses/<hypothesis_id>/memory/`.

The generated SQLite search index is `memory/index.sqlite` and can be rebuilt with:

```sh
bin/agent-memory index
```

## Rules

- Store only reusable, non-sensitive information.
- Do not store secrets or raw private connector content.
- Prefer links and short summaries over copied source text.
- Promote hypothesis memory to project memory only when useful beyond the subtask.
- Promote project memory to system memory only through reflection.
