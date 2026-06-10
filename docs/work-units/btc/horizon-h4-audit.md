# Work Unit: BTC Horizon H4 Audit

<div class="run-metadata">
<p><strong>Work Unit ID:</strong> horizon_h4_audit</p>
<p><strong>Scientist:</strong> btc_autoresearch_v1</p>
<p><strong>Status:</strong> complete</p>
<p><strong>Date:</strong> 2026-06-10 00:27 KST</p>
</div>

## Purpose

This work unit investigated whether H=4 candidates from the score search remained strong when evaluated with horizon-matched holding.

## Why It Matters

The default pipeline applied H-bar forecasts to 1-bar-rebalanced positions. That is not leakage by itself, but it can make H>1 candidates look stronger than they are under a holding policy that matches the forecast horizon.

## Method

1. Extend the score-search ledger to 100 trials.
2. Select H=4 candidates from the top-ranked set.
3. Run a full candidate audit with `t094` as the primary H=1 comparator and `t063`/`t096` as H=4 secondary candidates.
4. Compare default 1-bar-rebalanced results against H-bar non-overlapping holding.

## Commands

```sh
cd sources/checkouts/btc_autoresearch
uv run --no-sync python -m scripts.run_autoresearch --max-trials 100 --seed 42
uv run --no-sync python - <<'PY'
# Ran src.research.candidate_audit.run_full_audit with primary t094 and H=4 secondary candidates t063/t096.
PY
```

## Results

| Trial | Config | Default Net | Horizon-Matched Net | Horizon-Matched Sharpe | Trades |
| --- | --- | ---: | ---: | ---: | ---: |
| `t063_72e951d8c632` | `volume_core`, H=4, `long_short`, lambda `3.0` | +155.6% | -3.9% | 0.23 | 57 |
| `t096_c1a908fe1a33` | `technical_core`, H=4, `long_cash`, lambda `5.0` | +130.6% | +47.9% | 0.48 | 47 |

## Decision

Do not promote H>1 candidates until horizon-matched holding is part of the primary search and ranking path.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: yes
- Backtester/accounting rules changed: no
- Live trading/API keys used: no

## How To Continue

Integrate horizon-matched H>1 ranking before treating H=4 candidates as comparable to H=1 candidates. Keep `t063` and `t096` as cautionary examples in future scientist manuals.

## Implementation References

- Manifest: `tasks/active/btc/scientists/btc_autoresearch_v1/work_units/horizon_h4_audit/work-unit.yaml`
- Related scientist manual: [BTC AutoResearch v1](../../scientists/btc-autoresearch-v1/index.md)
