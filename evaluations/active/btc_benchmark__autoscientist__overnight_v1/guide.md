# Evaluation Cell Guide: btc_benchmark__autoscientist__overnight_v1

Date: 2026-06-10
Status: active

## Purpose

This cell applies AutoScientist to the frozen BTC Benchmark. It uses independent work-unit lanes, critique, shared evidence, and synthesis to compare candidate methods under the same referee.

## Fixed Launch

The paired three-hour comparison launcher is:

```sh
bin/run-btc-overnight
```

To run only this cell:

```sh
uv run python bin/ai-lab cell run btc_benchmark__autoscientist__overnight_v1 --continuous --run-id btc-overnight-autoscientist
```

## Readiness Gates

The run spec checks the registered source commit, verifies the `btc-benchmark-python` runtime profile, runs selected referee tests, loads the local data bundle, and reproduces an EMA baseline through the referee.

## Operating Rules

- Keep the benchmark checkout read-only except for the known untracked source-local `uv.lock`.
- Use work units for source review, baseline replication, independent method proposals, critique, and synthesis when evidence should persist.
- Keep generated scripts and benchmark reports under the current run directory unless promoting durable notes into work-unit reports.
- Do not change referee scoring, costs, splits, causality gates, or holdout policy.
- Do not submit externally or write to connectors without explicit user approval.

## Expected Final State

Before the run stops, update `report.md`, the public evaluation brief, any created work-unit records and briefs, and the run summary with consensus, disagreements, and the recommended next cell or proposal.
