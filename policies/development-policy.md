# Development Policy

Keep changes scoped to the task workspace, runner, memory, docs, or policies needed for the work.

## Local Edits

Local writes under `ai-lab` are allowed for task files, docs, notes, memory, and helper tooling unless the user asks for read-only work.

## Generated Output

Do not commit task experiment products by default. Experiment code, assets, reports, plots, results, and runs stay local under ignored task artifact directories.

## Validation

Prefer the smallest validation set that covers the change:

```bash
UV_CACHE_DIR=$PWD/.uv-cache uv run pytest
UV_CACHE_DIR=$PWD/.uv-cache uv run ruff check .
UV_CACHE_DIR=$PWD/.uv-cache uv run mypy .
uv run python bin/ai-lab task validate --all
uv run python bin/ai-lab docs sync --check
uv run python bin/ai-lab docs audit
```

When running Python validation commands, always use the repo-local uv cache form shown above.
