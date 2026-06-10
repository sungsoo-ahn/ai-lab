# Work Unit: BTC Benchmark Referee Reproduction

<div class="run-metadata">
<p><strong>Work Unit ID:</strong> referee_reproduction</p>
<p><strong>Scientist:</strong> btc_benchmark_v2</p>
<p><strong>Status:</strong> complete</p>
<p><strong>Date:</strong> 2026-06-10 KST</p>
</div>

## Purpose

Make the frozen benchmark checkout runnable and verify that the local referee can be trusted before optimizing strategies.

## Method

The public checkout referenced `btc_benchmark/data` in tests and packaging, but the tracked directory was absent. The local checkout was repaired from the documented `btc_autoresearch` lineage while leaving scoring, gates, costs, splits, and backtester code unchanged.

## Result

- Referee tests passed: `131 passed, 1 skipped`
- Loader saw 56,232 BTCUSDT futures 1h candles
- Data range: 2020-01-01 through 2026-05-31
- Funding events: 7,367
- Sealed holdout: not used

## Safety Checklist

- Referee scoring changed: no
- Causality gates changed: no
- Costs or split policy changed: no
- Live trading/API keys used: no

## Implementation References

- Work-unit report: `tasks/active/btc_benchmark/scientists/btc_benchmark_v2/work_units/referee_reproduction/report.md`
- Referee checkout: `sources/checkouts/btc_benchmark`
