# Work Unit: Horizon H4 Audit

<div class="run-metadata">
<p><strong>Date:</strong> 2026-06-10 00:27 KST</p>
<p><strong>Status:</strong> complete</p>
<p><strong>Type:</strong> observation</p>
</div>

## Purpose

Investigate the documented H=4 horizon-matched lead after baseline artifacts exist.

## Commands Run

```sh
cd sources/checkouts/btc_autoresearch
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

Horizon-matched audit:

| Trial | Default Net | Horizon-Matched Net | Horizon-Matched Sharpe | Trades |
| --- | ---: | ---: | ---: | ---: |
| `t063` | +155.6% | -3.9% | 0.23 | 57 |
| `t096` | +130.6% | +47.9% | 0.48 | 47 |

## Result

H=4 default candidates are not reliable as headline improvements because the default pipeline applies H-bar forecasts to 1-bar-rebalanced positions. Horizon-matched holding materially weakens the lead; `t096` remains positive but no longer beats the reproduced `t054` baseline.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: yes
- Backtester/accounting rules changed: no
- Live trading/API keys used: no

## Recommendation

Do not promote H>1 candidates until horizon-matched holding is part of the primary search and ranking path, not only a post-hoc audit.
