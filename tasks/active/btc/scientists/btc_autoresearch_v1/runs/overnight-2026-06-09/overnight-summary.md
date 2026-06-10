# Overnight Summary: btc

Date: 2026-06-10 00:27 KST
Run ID: overnight-2026-06-09
Status: complete

## Summary

The overnight orchestration completed the readiness and baseline-reproduction gate, then ran bounded follow-up work units. The local repo now has built BTCUSDT 1h futures candles, funding data, a 100-trial AutoResearch ledger, the official `t054` M5.5 audit, and a separate audit for the strongest new H=1 candidate `t094`.

No sealed holdout was touched. No live orders, live trading code, private API keys, or evaluation-rule changes were used.

## Commands

```sh
cd /Users/sungs/ai-lab/sources/checkouts/btc_autoresearch
uv sync --extra models --extra plot --extra dev
uv sync --no-extra stats --extra models --extra plot --extra dev
uv pip install -e '.[models,plot,dev]'
PYTHONDONTWRITEBYTECODE=1 uv run --no-sync pytest -q -p no:cacheprovider
uv pip install 'xgboost==1.7.6'
PYTHONDONTWRITEBYTECODE=1 uv run --no-sync pytest -q -p no:cacheprovider
uv run --no-sync python -m src.data.download_binance --market futures_um --symbol BTCUSDT --interval 1h --start 2019-09-01
uv run --no-sync python -m src.data.impute --market futures_um --symbol BTCUSDT --interval 1h --policy flat_bar_fill
uv run --no-sync python -m src.data.validate_data --market futures_um --symbol BTCUSDT --interval 1h
uv run --no-sync python -m src.data.download_derivatives --kind funding --symbol BTCUSDT --start 2019-09-09
uv run --no-sync python -m scripts.run_autoresearch --max-trials 60 --seed 42
uv run --no-sync python -m scripts.run_m5_5_audit
uv run --no-sync python -m scripts.run_autoresearch --max-trials 100 --seed 42
```

## Package Installs

- `uv pip install -e '.[models,plot,dev]'`
- `uv pip install 'xgboost==1.7.6'`

Notes:

- `uv sync` was attempted first but failed because the resolver tried to solve the unused optional `stats` extra containing unavailable `pypbo`.
- `xgboost==3.2.0` installed initially but failed at runtime due missing `libomp.dylib`; Homebrew install was not allowed silently, so XGBoost was downgraded locally to `1.7.6`.

## Data And Tests

- Final tests passed: `163/163`.
- Processed candles: 56,232 rows, `2020-01-01 00:00:00+00:00` through `2026-05-31 23:00:00+00:00`.
- Data validation hard checks passed with zero missing bars and zero duplicate timestamps.
- Funding data: 7,367 events.

## Work Units

- `baseline_reproduction`: complete. `t054` reproduced exactly at net `+94.0%`, Sharpe `0.71`, max drawdown `-41%`, trades `70`; M5.5 audit `READY_FOR_ONE_SHOT_HOLDOUT`.
- `pipeline_audit`: complete. No accounting, timestamp, split, cost, or holdout blocker found in the run; caveats recorded.
- `horizon_h4_audit`: complete. H=4 candidates weakened under horizon-matched holding; `t063` fell from `+155.6%` to `-3.9%`, `t096` from `+130.6%` to `+47.9%`.
- `regime_filter_probe`: complete. `t094` audited as `NEEDS_REFINEMENT` despite strong headline results because of `6/14` positive folds and `0.887` top-5 profit concentration.
- `report_synthesis`: complete. Scientist and work-unit reports updated.

## Main Results

- 100-trial ledger verdicts: `ACCEPT=29`, `NEEDS_REFINEMENT=56`, `REJECT=15`.
- Best headline candidate: `t094_f321ec793728`, `returns_only`, `H=1`, `long_cash`, `cost_aware`, lambda `5.0`.
- `t094` metrics: net `+231.1%`, Sharpe `1.05`, max drawdown `-38%`, trades `25`, turnover `49`.
- `t094` robustness: cost stress survives through 5x; funding-aware net `+184.4%`; random turnover-matched percentile rank `0.964`; PBO `0.2262`; comparable DSR `0.4432`.
- `t094` blocker: `NEEDS_REFINEMENT`, fold-positive `6/14`, profit concentration top-5 `0.887`.

## Files

- Main ledger: `/Users/sungs/ai-lab/sources/checkouts/btc_autoresearch/results/reports/m5_autoresearch/trial_ledger.parquet`
- Main AutoResearch report: `/Users/sungs/ai-lab/sources/checkouts/btc_autoresearch/results/reports/m5_autoresearch/report.md`
- Official `t054` audit: `/Users/sungs/ai-lab/sources/checkouts/btc_autoresearch/results/reports/m5_5_audit/report.md`
- Custom `t094` audit: `/Users/sungs/ai-lab/sources/checkouts/btc_autoresearch/results_t094_audit/reports/m5_5_audit/report.md`

## Safety Status

- Sealed holdout used: no
- Failed trials preserved: yes
- Backtester/accounting/cost/timestamp/split rules changed: no
- Live trading/API keys/orders used: no

## Recommended Next Step

Run a narrow robustness work unit around `t094`: keep `H=1`, `long_cash`, and official accounting fixed, then try concentration and fold-stability controls. Do not use sealed holdout yet.
