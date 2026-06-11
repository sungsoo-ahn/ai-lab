# Memory And Sources

`memory/` stores durable non-sensitive context for future AI scientist runs. Keep entries short and link to task artifacts rather than copying large outputs.

Task-local curated memory lives under `tasks/<task_id>/memory/`:

- `insights.yaml`: durable lessons that should affect future runs.
- `negative-results.yaml`: failed or weak approaches worth remembering.
- `candidates.yaml`: notable candidate strategies or implementations.
- `runs.yaml`: promoted run index and compact telemetry for generated user-facing docs.

Promoted run entries should contain enough non-sensitive structure for CI to rebuild the public run explorer without ignored raw logs: run status, timestamps, W&B URL, command/artifact/observation counts, agent cycle durations, and cycle-level metrics when available.
Runs may be promoted for telemetry even when they do not contain a durable observation; in that case `runs.yaml` is updated without adding an insight or negative result.

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
