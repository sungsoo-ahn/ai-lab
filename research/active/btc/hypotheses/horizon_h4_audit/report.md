# Work Unit Report: horizon_h4_audit

Date: 2026-06-10 00:27 KST
Status: complete

## Purpose

Investigate the documented H=4 horizon-matched lead after baseline artifacts exist.

## Commands Run

```sh
cd /Users/sungs/agent-system/inbox/repos/btc_autoresearch
uv run --no-sync python -m scripts.run_autoresearch --max-trials 100 --seed 42
uv run --no-sync python - <<'PY'
# Ran src.research.candidate_audit.run_full_audit with primary t094 and H=4 secondary candidates t063/t096.
PY
```

## Package Installs

No additional package installs beyond `baseline_reproduction`.

## Outputs

- The 100-trial extension found H=4 candidates in the top-ranked set:
  - `t063_72e951d8c632`: `volume_core`, `H=4`, `long_short`, `cost_aware`, lambda `3.0`; default 1-bar-rebalanced net `+155.6%`, Sharpe `0.78`, trades `143`.
  - `t096_c1a908fe1a33`: `technical_core`, `H=4`, `long_cash`, `cost_aware`, lambda `5.0`; default 1-bar-rebalanced net `+130.6%`, Sharpe `0.80`, trades `94`.
- Horizon-matched audit:
  - `t063`: default `+155.6%` collapsed to `-3.9%`, Sharpe `0.23`, trades `57` under H-bar non-overlapping hold.
  - `t096`: default `+130.6%` dropped to `+47.9%`, Sharpe `0.48`, trades `47` under H-bar non-overlapping hold.

## Result

H=4 default candidates are not reliable as headline improvements because the default pipeline applies H-bar forecasts to 1-bar-rebalanced positions. Horizon-matched holding materially weakens the lead; `t096` remains positive but no longer beats the reproduced `t054` baseline.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: yes
- Backtester/accounting rules changed: no
- Live trading/API keys used: no

## Recommendation

Do not promote H>1 candidates until horizon-matched holding is part of the primary search and ranking path, not only a post-hoc audit.
