# Work Unit Report: referee_reproduction

Date: 2026-06-10
Status: complete

## Purpose

Make the frozen referee locally runnable and trustworthy before scoring strategies.

## Commands Run

```sh
cd /Users/sungs/ai-lab
git clone https://github.com/YoonhoKim0527/btc_benchmark.git sources/checkouts/btc_benchmark
cd /Users/sungs/ai-lab/sources/checkouts/btc_benchmark
git rev-parse HEAD
uv run --with-editable . --extra dev pytest
```

## Package Installs

Attempted local `uv run --with-editable . --extra dev pytest`. It created a repository-local `.venv` but failed before installing the package because the package manifest references a missing directory.

After local repair, reran:

```sh
uv run --with-editable . --extra dev pytest
uv run --with-editable . --extra dev python - <<'PY'
from btc_benchmark import load_benchmark_data, BENCHMARK_VERSION
data = load_benchmark_data('.', include_sub_bars=False)
print(BENCHMARK_VERSION, len(data.candles), {k: len(v) for k, v in data.aux.items()})
PY
```

## Files Changed

- `/Users/sungs/ai-lab/sources/checkouts/btc_benchmark/.venv` was created by `uv` during the failed install attempt.
- `/Users/sungs/ai-lab/sources/checkouts/btc_benchmark/btc_benchmark.egg-info` was partially generated during the failed build attempt.
- `/Users/sungs/ai-lab/sources/checkouts/btc_benchmark/btc_benchmark/data/` was restored locally from `/Users/sungs/ai-lab/sources/checkouts/btc_autoresearch/src/data/`.
- `/Users/sungs/ai-lab/sources/checkouts/btc_benchmark/data/processed/BTCUSDT_futures_um_1h.parquet` and funding aux parquet were copied from the existing BTC AutoResearch data bundle.

## Outputs

- Benchmark git ref: `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`.
- Install failure: `error: package directory 'btc_benchmark/data' does not exist`.
- Referee tests after repair: `131 passed, 1 skipped`.
- Loader after data copy: benchmark version `1.0.0`, candles `56232`, aux `{'funding': 7367}`.

## Result

The public benchmark checkout is not installable as-is, but the local referee is now runnable after a lineage repair. No scoring, gate, backtester, cost, split, or holdout code was changed.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: not applicable
- Backtester/accounting rules changed: no
- Live trading/API keys used: no

## Recommendation

Use this local repaired referee for dev scoring. Treat the upstream missing data package as an open source-integrity question.
