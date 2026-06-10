# Fixed Runner Summary: btc_benchmark__autoresearch__overnight_v1

Run ID: `btc-overnight-20260610T151519Z-autoresearch`
Status: completed
Task: `btc_benchmark`
Scheme: `autoresearch`
Started: `2026-06-10T15:15:19.415596+00:00`

## Preflight

- Source status matched registered commit `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`.
- Tracked benchmark files were clean; untracked source-local `uv.lock` was present.
- Runtime check passed.
- Selected referee tests passed: `21 passed`.
- Readiness loaded 56,232 candles and `funding` auxiliary data.
- Preflight EMA baseline passed gates but scored net `-0.8668`, Sharpe `-0.879`, max drawdown `-0.8769`, turnover `1587.0`, funding-aware net `-0.8752`, next-open net `-0.8669`, random percentile `0.21`.

## Work

Created and ran `run_candidate_sweep.py` from the benchmark checkout environment:

```sh
cd /Users/sungs/ai-lab/sources/checkouts/btc_benchmark
uv run python /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__overnight_v1/runs/btc-overnight-20260610T151519Z-autoresearch/run_candidate_sweep.py
```

The sweep evaluated 13 gated candidates and preserved every report under `candidate_reports/`. The best candidate was rerun in `confirm_best_report.json` with the referee default gate budget.

## Result

Best confirmed candidate:

- `candidate_always_long_default_gates`
- Net `1.5005`, Sharpe `0.770`, max drawdown `-0.6670`
- Turnover `1.0`, trades `1`, full exposure
- Cost curve: cost0x `1.5031`, cost2x `1.4980`, cost3x `1.4955`, cost5x `1.4904`
- Funding-aware net `0.9151`, next-open net `1.4982`
- Gates passed on all 14 folds with default future-perturbation cutoff minimum `433`
- Sealed holdout was not used

Best adaptive references:

- `candidate_ema_48_192_funding_le_5bp`: net `0.9021`, max drawdown `-0.4316`, turnover `225.0`, funding-aware net `0.6106`, cost5x `-0.2286`.
- `candidate_ema_48_192_long_cash`: net `0.8433`, max drawdown `-0.4316`, turnover `195.0`, funding-aware net `0.5430`, cost5x `-0.1568`.
- `candidate_ema_24_96_long_cash`: net `0.6632`, max drawdown `-0.4575`, turnover `375.0`, funding-aware net `0.4050`, cost5x `-0.6307`.

## Decision

Always-long is the dev-score floor, not a novel research win. Cycle 2 should evaluate adaptive overlays relative to buy-and-hold and prioritize drawdown reduction, funding-aware net, cost stress, next-open behavior, per-year concentration, and random percentile.

Proposal: `proposals/btc_autoresearch_cycle2_buy_hold_relative.md`.

## Verification

- `uv run python bin/ai-lab docs audit` passed.
- `uv run python -m pytest tests/test_metrics.py tests/test_benchmark_contract.py -q` passed with `21 passed`.

Events: `events.jsonl`
Command logs: `commands/`
Spec snapshot: `run-spec.snapshot.yaml`
Finished: 2026-06-10T15:26:48.655174+00:00
