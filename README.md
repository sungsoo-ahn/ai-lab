# AI Lab

AI Lab is a local-first workspace for one reusable AI scientist loop.

The loop is simple: for a task with a declared metric, an AI agent repeatedly proposes a bounded experiment or audit, runs it, preserves local evidence, and updates canonical task metadata only when the task definition or operating structure changes. The goal is not to compare scientist designs. The goal is to make important observations while keeping enough human-facing state for intervention and review.

## Current Shape

- `lab.yaml`: repo-wide defaults, including W&B/Weave observability.
- `tasks/<task_id>/`: task workspaces with task contract, loop spec, agent instructions, task-local helper scripts, and ignored experiment workspaces.
- `memory/`: durable non-sensitive preferences, source references, and system memory.
- `sources/`: source registry plus ignored external checkouts.
- `policies/`: privacy, connector, runtime, and development boundaries.
- `docs/`: MkDocs dashboard for humans.
- `bin/ai-lab`: small helper for task runs, validation, source checks, memory, and docs audit.

The first active task is `btc_benchmark`.

## W&B Observability

Normal AI scientist runs require W&B/Weave and log full run traces to `sungsoo-ahn/ai-lab`. Configure credentials outside Git:

```bash
wandb login
# or
export WANDB_API_KEY=...
```

Dry runs and tests can opt out explicitly:

```bash
AI_LAB_DISABLE_WANDB=1 uv run python bin/ai-lab task run btc_benchmark --once --no-wandb
```

## Common Commands

```bash
uv run python bin/ai-lab task status btc_benchmark
uv run python bin/ai-lab task validate --all
uv run python bin/ai-lab task run btc_benchmark --once --dry-run
uv run python bin/ai-lab task run btc_benchmark --continuous
uv run python bin/ai-lab task summarize btc_benchmark --run-id <run_id>
uv run python bin/ai-lab memory promote btc_benchmark --run-id <run_id>
uv run python bin/ai-lab source status btc_benchmark
uv run python bin/ai-lab memory search btc
uv run python bin/ai-lab docs sync
uv run python bin/ai-lab docs audit
```

## Documentation

Preview the dashboard:

```bash
uv run --with-requirements requirements.txt mkdocs serve
```

Build it:

```bash
uv run --with-requirements requirements.txt mkdocs build --strict
```

GitHub Pages deploys the MkDocs site from `main`.
