# Work Unit: BTC Baseline Reproduction

<div class="run-metadata">
<p><strong>Work Unit ID:</strong> baseline_reproduction</p>
<p><strong>Scientist:</strong> btc_autoresearch_v1</p>
<p><strong>Status:</strong> complete</p>
<p><strong>Date:</strong> 2026-06-10 00:27 KST</p>
</div>

## Purpose

This work unit established that the BTC scientist could safely run the inherited research pipeline. It built the required data, ran tests, reproduced the baseline, and executed the M5.5 audit before later work units interpreted new candidates.

## Why It Matters

Without this gate, later score improvements would be hard to trust. The work unit verifies the basic environment, data pipeline, backtester, and baseline comparison point.

## Method

1. Prepare the inherited BTC research environment using scientist-local `uv` workflows.
2. Run the full test suite.
3. Build and validate BTCUSDT futures 1h data.
4. Download funding data.
5. Run the 60-trial baseline search.
6. Run the M5.5 audit for the reproduced baseline.

## Commands

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

## Package And Environment Notes

- The optional `stats` extra could not be resolved because `pypbo` was unavailable.
- Editable install with `uv pip install -e '.[models,plot,dev]'` succeeded in the scientist-local environment.
- XGBoost 3.2.0 failed on macOS due to missing OpenMP runtime. The work unit used `xgboost==1.7.6` as a scientist-local Python workaround.
- No Homebrew, Docker, Node, live-trading, or account-level changes were introduced.

## Outputs

| Output | Result |
| --- | --- |
| Test suite | `163/163` passed |
| Candle data | 56,232 rows, `2020-01-01` through `2026-05-31` |
| Data validation | missing bars `0`, duplicates `0`, irregular gaps `0`, imputed fraction `0.0%` |
| Funding data | 7,367 events |
| 60-trial ledger | `ACCEPT=16`, `NEEDS_REFINEMENT=34`, `REJECT=10` |
| Baseline `t054` | net `+94.0%`, Sharpe `0.71`, max drawdown `-41%`, trades `70` |
| M5.5 audit | `READY_FOR_ONE_SHOT_HOLDOUT`; sealed holdout unused |

## Decision

Use the local reproduced `t054` metrics for comparable follow-up work. Disclose the data-window/version difference when comparing against older documentation.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: yes
- Backtester/accounting rules changed: no
- Live trading/API keys used: no
- Private API keys used: no

## How To Continue

Future work units should compare against the local `t054` baseline, not the older static `+60.0%` reference. If the baseline is rerun, preserve the data range, git ref, package workaround, and test result in this manual.

## Implementation References

- Manifest: `tasks/active/btc/scientists/btc_autoresearch_v1/work_units/baseline_reproduction/work-unit.yaml`
- Source checkout: `sources/checkouts/btc_autoresearch`
- Baseline trial detail in scientist manual: [BTC AutoResearch v1](../index.md)
