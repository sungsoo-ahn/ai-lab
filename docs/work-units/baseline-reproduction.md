# Work Unit: Baseline Reproduction

<div class="run-metadata">
<p><strong>Date:</strong> 2026-06-10 00:27 KST</p>
<p><strong>Status:</strong> complete</p>
<p><strong>Type:</strong> observation</p>
</div>

## Purpose

Build readiness, run tests, build required data, reproduce the 60-trial baseline, and run M5.5 audit.

## Commands Run

```sh
cd sources/checkouts/btc_autoresearch
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
```

## Package Installs

- `uv sync --extra models --extra plot --extra dev` failed because the resolver tried to solve the optional `stats` extra and `pypbo` was unavailable.
- `uv sync --no-extra stats --extra models --extra plot --extra dev` failed for the same resolver issue.
- `uv pip install -e '.[models,plot,dev]'` succeeded in the scientist-local `.venv`.
- The first full test run then failed 6 XGBoost-dependent tests because `xgboost==3.2.0` required a missing macOS OpenMP runtime.
- `uv pip install 'xgboost==1.7.6'` succeeded as a scientist-local Python package workaround.

## Outputs

- Tests: final run passed `163/163`.
- Candle data: `data/processed/BTCUSDT_futures_um_1h.parquet`, 56,232 rows, range `2020-01-01 00:00:00+00:00` through `2026-05-31 23:00:00+00:00`.
- Validation: hard checks passed; missing bars `0`, duplicate timestamps `0`, irregular gaps `0`, imputed fraction `0.0%`.
- Funding data: `data/raw/binance/futures_um/fundingRate/BTCUSDT/BTCUSDT_funding.parquet`, 7,367 events.
- 60-trial reproduction: `results/reports/m5_autoresearch/trial_ledger.parquet` and `.csv`; verdicts `ACCEPT=16`, `NEEDS_REFINEMENT=34`, `REJECT=10`.
- Baseline `t054_a19bd141e75b`: reproduced exactly as `technical_core`, `H=1`, `long_cash`, `cost_aware`, lambda `3.0`; net `+94.0%`, Sharpe `0.71`, max drawdown `-41%`, trades `70`.
- M5.5 audit for `t054`: `READY_FOR_ONE_SHOT_HOLDOUT`; reproduced exactly; sealed holdout unused; comparable DSR `0.4570`; PBO `0.4127`; fold-positive `8/14`; funding-aware net `+72.4%`.

## Result

Readiness and baseline-reproduction gate passed after a scientist-local XGBoost package workaround. The local data build differs from the originally documented baseline metrics: the same `t054` configuration reproduced at `+94.0%` net rather than the scientist note's `+60.0%`.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: yes
- Backtester/accounting rules changed: no
- Live trading/API keys used: no
- Private API keys used: no

## Recommendation

Use the local reproduced `t054` metrics for comparable follow-up work in this workspace, and disclose the data-window/version difference when comparing against the originally documented `+60.0%` baseline.
