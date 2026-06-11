# Memory And Sources

`memory/` stores durable non-sensitive context for future AI scientist runs. Keep entries short and link to task artifacts rather than copying large outputs.

Task-local curated memory lives under `tasks/<task_id>/memory/`:

- `insights.yaml`: durable lessons that should affect future runs.
- `negative-results.yaml`: failed or weak approaches worth remembering.
- `candidates.yaml`: notable candidate strategies or implementations.
- `runs.yaml`: promoted run index for generated user-facing docs.

Useful commands:

```bash
uv run python bin/ai-lab memory index
uv run python bin/ai-lab memory search btc
uv run python bin/ai-lab memory audit
uv run python bin/ai-lab memory promote btc_benchmark --run-id <run_id>
```

`sources/sources.yaml` tracks external source checkouts. The BTC benchmark checkout is intentionally ignored under `sources/checkouts/`.

```bash
uv run python bin/ai-lab source status btc_benchmark
```
