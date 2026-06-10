# Evaluation Matrix

Evaluation cells are the operational units of the AI Lab matrix. Each cell applies one reusable scientist scheme to one task.

## Active Cells

| Evaluation Cell | Task | Scheme | Run Contract |
| --- | --- | --- | --- |
| [BTC Benchmark AutoResearch Overnight v1](btc-benchmark--autoresearch--overnight-v1.md) | BTC Benchmark | AutoResearch | 180-minute fixed run spec |
| [BTC Benchmark AutoScientist Overnight v1](btc-benchmark--autoscientist--overnight-v1.md) | BTC Benchmark | AutoScientist | 180-minute fixed run spec |

## Fixed Launch

Use the [BTC Benchmark Overnight Runbook](btc-benchmark-overnight-runbook.md). The short version is:

```sh
bin/run-btc-overnight
```

The launcher starts both cells in parallel and writes local launcher logs under `logs/overnight/`. Each cell keeps authoritative run records under its own `runs/<run_id>/` directory.

## Completed Reference Cells

| Evaluation Cell | Task | Scheme | Result |
| --- | --- | --- | --- |
| [BTC Benchmark AutoResearch Smoke](btc-benchmark--autoresearch--smoke.md) | BTC Benchmark | AutoResearch | `smoke-20260610` passed |
