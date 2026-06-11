# Maintenance

Before committing changes:

```bash
UV_CACHE_DIR=$PWD/.uv-cache uv run pytest
UV_CACHE_DIR=$PWD/.uv-cache uv run ruff check .
UV_CACHE_DIR=$PWD/.uv-cache uv run mypy .
uv run python bin/ai-lab task validate --all
uv run python bin/ai-lab task run btc_benchmark --once --dry-run
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
