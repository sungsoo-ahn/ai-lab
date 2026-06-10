# Overnight Runbook: btc

Date: 2026-06-09
Status: ready
Run ID: overnight-2026-06-09

## Goal

Run a full BTC research loop overnight. First verify environment, data, and baseline reproduction. Then let bounded work unit/work units pursue useful observations or improvements.

## Autonomy

- Agents may run a full research loop.
- Agents may silently install missing Python scientist dependencies using scientist-local `uv` workflows.
- Agents may edit code only in isolated work units, branches, worktrees, or clearly owned file scopes.
- Agents may not silently install Homebrew, Node, Docker, system packages, connector integrations, shell configuration, or account configuration.

## Gates

1. Verify or materialize source `btc_autoresearch` at git ref `ca251130e1f97b6233ceb957cb85e209bc136073`.
2. Run tests or install missing Python deps with `uv` and record the install.
3. Build required BTCUSDT 1h futures candles if missing.
4. Build funding data if needed for audit.
5. Reproduce 60-trial baseline and M5.5 audit.
6. Launch parallel improvement/knowledge work only after baseline status is known.

## Baseline Commands

```sh
/Users/sungs/ai-lab/bin/ai-lab source status btc_autoresearch
cd /Users/sungs/ai-lab/sources/checkouts/btc_autoresearch
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider
python -m src.data.download_binance --market futures_um --symbol BTCUSDT --interval 1h --start 2019-09-01
python -m src.data.impute --market futures_um --symbol BTCUSDT --interval 1h --policy flat_bar_fill
python -m src.data.validate_data --market futures_um --symbol BTCUSDT --interval 1h
python -m src.data.download_derivatives --kind funding --symbol BTCUSDT --start 2019-09-09
python -m scripts.run_autoresearch --max-trials 60 --seed 42
python -m scripts.run_m5_5_audit
```

## Work Units

| Work Unit | Purpose | Write Scope |
| --- | --- | --- |
| `baseline_reproduction` | Build readiness, run tests, build required data, reproduce the 60-trial baseline, and run M5.5 audit. | BTC scientist files, work unit report, and BTC AutoResearch repo generated data/results. |
| `pipeline_audit` | Audit leakage, cost, holdout, and reproducibility risks; produce actionable blockers and safe next steps. | Read-only code inspection plus work unit report updates. |
| `horizon_h4_audit` | Investigate the documented H=4 horizon-matched lead after baseline artifacts exist. | Own work unit report and isolated generated outputs; no core evaluation rule changes. |
| `regime_filter_probe` | Try a bounded volatility/regime-filter workstream after baseline reproduction passes. | Own branch/patch or isolated worktree if code edits are needed. |
| `report_synthesis` | Summarize all overnight results, negative findings, package installs, and next actions for the user. | Scientist report, run summary, and work-unit reports. |

## Required Final Outputs

- Update `tasks/active/btc/scientists/btc_autoresearch_v1/report.md`.
- Update every work-unit `report.md`.
- Write `tasks/active/btc/scientists/btc_autoresearch_v1/runs/overnight-2026-06-09/overnight-summary.md`.
- Record package installs, commands, failures, outputs, and safety status.
