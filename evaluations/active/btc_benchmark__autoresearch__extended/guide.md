# Evaluation Cell Guide: btc_benchmark__autoresearch__extended

Date: 2026-06-10
Status: active

## Purpose

This cell applies AutoResearch to the frozen BTC Benchmark. It is a metric-driven loop for proposing, running, evaluating, and recording bounded local experiments against the benchmark referee.

## Fixed Launch

The AutoResearch three-hour launcher is:

```sh
bin/run-btc-extended
```

Equivalent direct cell command:

```sh
uv run python bin/ai-lab cell run btc_benchmark__autoresearch__extended --continuous --run-id btc-extended-autoresearch
```

## Readiness Gates

The run spec checks the registered source commit, verifies the `btc-benchmark-python` runtime profile, runs selected referee tests, loads the local data bundle, and reproduces an EMA baseline through the referee.

## Operating Rules

- Keep the benchmark checkout read-only except for the known untracked source-local `uv.lock`.
- Write experiment scripts, benchmark reports, and synthesis notes under the current run directory.
- Do not change referee scoring, costs, splits, causality gates, or holdout policy.
- Do not submit externally or write to connectors without explicit user approval.
- Preserve negative results and failed local trials when they explain the next decision.

## Expected Final State

Before the run stops, update `report.md`, the public evaluation brief, and the run summary with the best local evidence, failed directions, and recommended next cell or proposal.
