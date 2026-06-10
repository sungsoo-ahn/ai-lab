# BTC Benchmark Overnight Runbook

Date: 2026-06-10
Status: ready

## Purpose

This runbook explains how to launch the paired BTC Benchmark overnight comparison. The run starts the AutoResearch and AutoScientist evaluation cells in parallel, each with a 180-minute fixed run spec.

## Start From Repo Root

```sh
cd /Users/sungs/ai-lab
```

## Preflight Check

Before a real run, validate the fixed specs and print the command plan:

```sh
uv run python bin/ai-lab cell run-spec validate --all
uv run python bin/ai-lab cell run-all --continuous --dry-run
```

## Launch The Experiment

Run both schemes in parallel:

```sh
bin/run-btc-overnight
```

Optionally provide a run prefix:

```sh
bin/run-btc-overnight btc-overnight-20260610
```

That creates run IDs:

- `btc-overnight-20260610-autoresearch`
- `btc-overnight-20260610-autoscientist`

## What Runs

Each active overnight cell executes:

1. source status gate for `btc_benchmark`;
2. `btc-benchmark-python` runtime check;
3. selected referee tests;
4. BTC data-load and EMA baseline reproduction;
5. one Codex synthesis loop using the cell's fixed `synthesis-prompt.md`.

## Logs And Outputs

Launcher logs:

```text
logs/overnight/<run_id>.log
```

Authoritative run records:

```text
evaluations/active/btc_benchmark__autoresearch__overnight_v1/runs/<run_id>/
evaluations/active/btc_benchmark__autoscientist__overnight_v1/runs/<run_id>/
```

Useful files inside each run directory:

- `run-summary.md`
- `events.jsonl`
- `run-spec.snapshot.yaml`
- `commands/*.stdout.log`
- `commands/*.stderr.log`
- `preflight_baseline_report.json`
- `preflight_leaderboard.jsonl`

## Run One Cell Only

AutoResearch only:

```sh
uv run python bin/ai-lab cell run btc_benchmark__autoresearch__overnight_v1 --continuous --run-id btc-overnight-autoresearch
```

AutoScientist only:

```sh
uv run python bin/ai-lab cell run btc_benchmark__autoscientist__overnight_v1 --continuous --run-id btc-overnight-autoscientist
```

## Stop Or Retry

To prevent a cell from starting its next cycle, create its `STOP` file:

```sh
touch evaluations/active/btc_benchmark__autoresearch__overnight_v1/STOP
touch evaluations/active/btc_benchmark__autoscientist__overnight_v1/STOP
```

The current run specs use one cycle, so `STOP` is mainly useful before launching or before a retry. Remove the file before rerunning:

```sh
rm evaluations/active/btc_benchmark__autoresearch__overnight_v1/STOP
rm evaluations/active/btc_benchmark__autoscientist__overnight_v1/STOP
```

Use a new run prefix for a retry so previous run records remain intact.

## Troubleshooting

If both cells pass preflight and fail immediately at `codex_synthesis` with this stderr:

```text
Error: stdin is not a terminal
```

then the synthesis wrapper is launching interactive Codex from a background run. `bin/codex-lab` should use `codex exec` when stdin/stdout are not terminals. Validate the wrapper with:

```sh
sh -n bin/codex-lab
rg -n "codex exec" bin/codex-lab
```

## After The Run

Review both cell reports and public briefs:

- [BTC Benchmark AutoResearch Overnight v1](btc-benchmark--autoresearch--overnight-v1.md)
- [BTC Benchmark AutoScientist Overnight v1](btc-benchmark--autoscientist--overnight-v1.md)

Then run:

```sh
uv run python bin/ai-lab docs audit
uv run python -m pytest tests -q
```
