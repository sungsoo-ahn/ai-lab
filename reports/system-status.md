# AI Lab Status

Date: 2026-06-11

## Current Shape

- Workspace: `/Users/sungs/ai-lab`
- Operating model: one W&B-observed AI scientist loop per task workspace.
- Active task: `btc_benchmark`
- Source registry: `/Users/sungs/ai-lab/sources/sources.yaml`
- Repo config: `/Users/sungs/ai-lab/lab.yaml`
- Public dashboard: `docs/`
- Memory: `memory/`
- Raw run output: `tasks/<task_id>/runs/`, ignored by Git.

## Observability

Normal runs require W&B/Weave and log to `sungsoo-ahn/ai-lab`. Credentials must stay outside Git through `wandb login` or `WANDB_API_KEY`.

## Main Commands

```bash
uv run python bin/ai-lab task status btc_benchmark
uv run python bin/ai-lab task validate --all
uv run python bin/ai-lab task run btc_benchmark --once --dry-run
uv run python bin/ai-lab task run btc_benchmark --continuous
uv run python bin/ai-lab docs audit
```

