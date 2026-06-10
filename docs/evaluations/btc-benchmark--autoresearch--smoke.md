# BTC Benchmark AutoResearch Smoke

Date: 2026-06-10
Status: active

## Summary

This evaluation cell applies the AutoResearch scheme to the BTC Benchmark task only as a short smoke check. It verifies that the registered benchmark checkout can pass a bounded referee test module through the AI Lab fixed runner.

## Current Run Spec

- Source: `btc_benchmark`
- Command: `uv run python -m pytest tests/test_metrics.py -q`
- Timeout: 120 seconds
- Target metric: `smoke_test_pass`

## Result

Run `smoke-20260610` passed on 2026-06-10.

- Source gate: registered `btc_benchmark` commit matched.
- Tracked source edits: none.
- Command result: `6 passed`.
