# BTC Benchmark Extended Runbook

Date: 2026-06-10
Status: ready

## Purpose

This runbook explains how to launch the BTC Benchmark AutoResearch extended run with a 180-minute fixed run spec and up to five synthesis cycles. AutoScientist remains an active evaluation cell, but it is run directly when isolating that scheme and is not launched by `bin/run-btc-extended`.

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

Run AutoResearch:

```sh
bin/run-btc-extended
```

Optionally provide a run prefix:

```sh
bin/run-btc-extended btc-extended-20260610
```

That creates run IDs:

- `btc-extended-20260610-autoresearch`

## What Runs

The AutoResearch extended cell executes:

1. source status gate for `btc_benchmark`;
2. `btc-benchmark-python` runtime check;
3. selected referee tests;
4. BTC data-load and EMA baseline reproduction;
5. up to five Codex synthesis cycles using the cell's fixed `synthesis-prompt.md`.

Each AutoResearch cycle should read the Cycle 2 buy-hold-relative proposal and rank candidates against always-long/buy-and-hold evidence, not only against the weak EMA preflight baseline.

## Logs And Outputs

Launcher logs:

```text
logs/extended/<run_id>.log
```

Authoritative run records:

```text
evaluations/active/btc_benchmark__autoresearch__extended/runs/<run_id>/
```

Useful files inside the run directory:

- `run-summary.md`
- `events.jsonl`
- `run-spec.snapshot.yaml`
- `commands/*.stdout.log`
- `commands/*.stderr.log`
- `preflight_baseline_report.json`
- `preflight_leaderboard.jsonl`

## Direct Cell Runs

AutoResearch:

```sh
uv run python bin/ai-lab cell run btc_benchmark__autoresearch__extended --continuous --run-id btc-extended-autoresearch
```

AutoScientist only:

```sh
uv run python bin/ai-lab cell run btc_benchmark__autoscientist__extended --continuous --run-id btc-extended-autoscientist
```

## Stop Or Retry

To prevent a cell from starting its next cycle, create its `STOP` file:

```sh
touch evaluations/active/btc_benchmark__autoresearch__extended/STOP
```

The AutoResearch run spec allows up to five cycles. `STOP` is useful before launching, before a retry, or between cycles if you need the runner to stop before the next cycle starts. Remove the file before rerunning:

```sh
rm evaluations/active/btc_benchmark__autoresearch__extended/STOP
```

Use a new run prefix for a retry so previous run records remain intact.

## Troubleshooting

If the cell passes preflight and fails immediately at `codex_synthesis` with this stderr:

```text
Error: stdin is not a terminal
```

then the synthesis wrapper is launching interactive Codex from a background run. `bin/codex-lab` should use `codex exec` when stdin/stdout are not terminals. Validate the wrapper with:

```sh
sh -n bin/codex-lab
rg -n "codex exec" bin/codex-lab
```

## After The Run

Review the AutoResearch cell report and public brief:

- [BTC Benchmark AutoResearch Extended](btc-benchmark--autoresearch--extended.md)

Then run:

```sh
uv run python bin/ai-lab docs audit
uv run python -m pytest tests -q
```
