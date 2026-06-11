# Extended Runbook: btc_benchmark__autoscientist__extended

Date: 2026-06-10
Status: ready
Run ID: supplied to direct cell runner

## Goal

Run the AutoScientist scheme against BTC Benchmark for a bounded three-hour wall-clock budget, including preflight gates and synthesis.

## Launch

Run this cell directly:

```sh
uv run python bin/ai-lab cell run btc_benchmark__autoscientist__extended --continuous --run-id btc-extended-autoscientist
```

## Gates

1. `source_status`: registered `btc_benchmark` source commit must match and tracked files must be clean.
2. `runtime_check`: `btc-benchmark-python` profile must pass.
3. `referee_contract_tests`: selected metrics and benchmark contract tests must pass.
4. `benchmark_readiness`: data load and EMA baseline reproduction must pass through the referee.
5. `codex_synthesis`: the AutoScientist synthesis prompt runs inside the remaining wall budget.

## Required Final Outputs

- Update `report.md`.
- Update `docs/evaluations/btc-benchmark--autoscientist--extended.md`.
- Keep run artifacts under `runs/<run_id>/`.
- Create or update work units when independent evidence should persist.
- Write proposals under `proposals/` only when the next cell version should change metric, constraints, or scheme use.
- Run `uv run python bin/ai-lab docs audit` and targeted tests if time remains.
