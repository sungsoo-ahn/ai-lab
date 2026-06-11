# Cycle 2 Experiment Summary

Run: `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`
Cell: `btc_benchmark__autoresearch__extended`
Task: `btc_benchmark`
Scheme: `autoresearch`

## Design

The sweep used the Cycle 2 buy-hold-relative decision table. Always-long was treated as the floor, not a win. Candidates were bounded causal overlays: slower EMA long-cash rules, funding stress exits, volatility exits with fold-local thresholds, drawdown-stress exits, and combinations.

Command:

```sh
cd /Users/sungs/ai-lab/sources/checkouts/btc_benchmark
uv run python /Users/sungs/ai-lab/evaluations/active/btc_benchmark__autoresearch__extended/runs/btc-autoresearch-cycle2-20260610T223228Z-autoresearch/run_cycle2_buyhold_relative_sweep.py
```

## Best Confirmed Candidate

`cycle2_bh_ema384_lowvol168_q80`:

- Net `1.8679`, delta versus always-long `+0.3674`
- Max drawdown `-0.3157`, improvement versus always-long `+0.3513`
- Funding-aware net `1.4300`, next-open net `1.8644`, random percentile `1.0`
- Turnover `567.0`, cost2x `0.6252`, cost3x `-0.0795`, cost5x `-0.7052`
- Default gates passed on all 14 folds, future-perturbation cutoff minimum `433`

## Robustness Notes

The best candidate is a real buy-hold-relative development improvement but fails the cost-stress part of the decision table. Its raw net and drawdown are strong, but its turnover makes the 3x and 5x cost cases negative.

Lower-turnover references are weaker but more cost robust:

- `cycle2_bh_funding_le_5bp`: net `1.5744`, turnover `33.0`, cost5x `1.2552`.
- `cycle2_bh_drawdown252_ge_minus20`: net `1.5649`, turnover `33.0`, cost5x `1.2461`.
- `cycle2_ema_72_288_long_cash`: net `1.5591`, turnover `111.0`, cost5x `0.6394`.

## Decision

Promote `cycle2_bh_ema384_lowvol168_q80` as the current best development candidate with a cost-fragility warning. Next work should compress turnover in the slow-regime plus volatility overlay family and compare directly against the cost-surviving funding and drawdown controls.
