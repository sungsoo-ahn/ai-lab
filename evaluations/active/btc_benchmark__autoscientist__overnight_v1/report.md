# Evaluation Cell Report: btc_benchmark__autoscientist__overnight_v1

Date: 2026-06-10
Status: active

## Current State

This cell is ready for the first three-hour AutoScientist overnight run. No overnight result has been recorded yet.

## Fixed Run Contract

- Wall budget: 180 minutes, enforced by `run-spec.yaml` command timeouts and the AI Lab runner wall deadline.
- Source: registered `btc_benchmark` checkout at commit `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`.
- Preflight: source status, runtime check, selected referee tests, data load, and EMA baseline reproduction.
- Synthesis: one AutoScientist loop using `synthesis-prompt.md`.

## Readiness Evidence

Manual setup checks on 2026-06-10:

- `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed with `21 passed`.
- `bin/btc-benchmark-readiness` loaded 56,232 candles, found `funding` auxiliary data, and reproduced `ema_baseline_12_48_long_short` without disqualification.
- `uv run python bin/ai-lab runtime check btc-benchmark-python --repo sources/checkouts/btc_benchmark` passed. Homebrew printed an ownership warning for `/opt/homebrew/Cellar`, but the Brewfile check and Python import checks succeeded.

## Launch

```sh
bin/run-btc-overnight
```
