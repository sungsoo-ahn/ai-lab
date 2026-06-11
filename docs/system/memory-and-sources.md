# Memory And Sources

`memory/` stores durable non-sensitive context for future AI scientist runs. Keep entries short and link to task artifacts rather than copying large outputs.

Useful commands:

```bash
uv run python bin/ai-lab memory index
uv run python bin/ai-lab memory search btc
uv run python bin/ai-lab memory audit
```

`sources/sources.yaml` tracks external source checkouts. The BTC benchmark checkout is intentionally ignored under `sources/checkouts/`.

```bash
uv run python bin/ai-lab source status btc_benchmark
```

