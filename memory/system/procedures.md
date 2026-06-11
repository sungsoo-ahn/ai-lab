---
id: system-procedures
type: system_memory
created_at: 2026-06-09
updated_at: 2026-06-11
confidence: high
sensitivity: public
status: active
links:
  - /Users/sungs/ai-lab/policies/update-policy.md
  - /Users/sungs/ai-lab/policies/evaluation-runtime-policy.md
  - /Users/sungs/ai-lab/docs/system/maintenance.md
---

# AI Lab Procedures

## Task Runs

Validate task workspaces with:

```bash
uv run python bin/ai-lab task validate --all
```

Preview a loop without W&B or command side effects:

```bash
uv run python bin/ai-lab task run btc_benchmark --once --dry-run
```

Run the active task with W&B observability:

```bash
uv run python bin/ai-lab task run btc_benchmark --continuous
```

Normal runs require `wandb login` or `WANDB_API_KEY`. Tests may use `AI_LAB_DISABLE_WANDB=1` or `--no-wandb`.

## Memory

Use `bin/ai-lab memory index` to rebuild the generated SQLite search index. Use `bin/ai-lab memory search <query>` to search Markdown, YAML, and logs.

## Sources

Use `bin/ai-lab source status <source_id>` before claiming source-backed evidence. External checkouts live under ignored `sources/checkouts/`.

## Runtime Changes

Agents may install missing Python dependencies through local or inherited `uv` workflows when the user authorizes the run or dependency change. Agents must not install Node, Docker, connector integrations, credentials, shell configuration, account configuration, or unlisted OS packages silently.

