# Maintenance

Before committing changes:

```bash
UV_CACHE_DIR=$PWD/.uv-cache uv run pytest
UV_CACHE_DIR=$PWD/.uv-cache uv run ruff check .
UV_CACHE_DIR=$PWD/.uv-cache uv run mypy .
uv run python bin/ai-lab task validate --all
uv run python bin/ai-lab task run btc_benchmark --once --dry-run
uv run python bin/ai-lab task run-publish btc_benchmark --continuous
uv run python bin/ai-lab docs sync --check
uv run python bin/ai-lab docs audit
uv run --with-requirements requirements.txt mkdocs build --strict
```

## Rules

- Keep task experiment products under ignored task artifact directories.
- Commit task contracts, loop specs, scientist instructions, maintained helper scripts, placeholders, and generated public docs.
- Do not store W&B API keys or connector secrets in repo files.
- Connector writes, external submissions, Docker, Node, and unlisted OS packages still require explicit approval.
- Preserve user changes; do not reset the worktree to clean up unrelated files.

## First Run Checklist

1. Confirm the source checkout is present and pinned:

```bash
uv run python bin/ai-lab source status btc_benchmark
```

2. Confirm W&B credentials are available outside Git through `wandb login`, netrc, or `WANDB_API_KEY`.
3. Run the dry run and docs audit:

```bash
uv run python bin/ai-lab task run btc_benchmark --once --dry-run
uv run python bin/ai-lab docs audit
```

4. Launch, promote, sync, commit, and push a full run:

```bash
uv run python bin/ai-lab task run-publish btc_benchmark --continuous
```

5. For manual recovery or older runs, summarize and review the run:

```bash
uv run python bin/ai-lab task summarize btc_benchmark --run-id <run_id>
```

Review `tasks/btc_benchmark/runs/<run_id>/run-summary.md`, `run.json`, `events.jsonl`, `observations.jsonl`, `artifacts.jsonl`, `launcher.log`, and W&B.

6. Promote durable findings only after review:

```bash
uv run python bin/ai-lab memory promote btc_benchmark --run-id <run_id>
uv run python bin/ai-lab docs sync
```
