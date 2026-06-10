# Work Unit Report: regime_filter_probe

Date: 2026-06-10 00:27 KST
Status: complete

## Purpose

Try a bounded volatility/regime-filter workstream after baseline reproduction passes.

## Commands Run

```sh
cd /Users/sungs/ai-lab/sources/checkouts/btc_autoresearch
uv run --no-sync python - <<'PY'
# Ran custom M5.5 audit for t094, including post-hoc regime breakdown and funding sensitivity.
PY
```

## Package Installs

No additional package installs beyond `baseline_reproduction`.

## Outputs

- Custom audit report: `/Users/sungs/ai-lab/sources/checkouts/btc_autoresearch/results_t094_audit/reports/m5_5_audit/report.md`.
- `t094_f321ec793728`: `returns_only`, `H=1`, `long_cash`, `cost_aware`, lambda `5.0`.
- Headline metrics: net `+231.1%`, Sharpe `1.05`, max drawdown `-38%`, trades `25`, turnover `49`.
- Cost stress: `0x +248%`, `0.5x +239%`, `1x +231%`, `2x +215%`, `3x +200%`, `5x +172%`.
- Funding-aware net: `+184.4%` versus `+231.1%` no-funding.
- Random turnover-matched robustness: 500 trials, p95 `+189%`, candidate percentile rank `0.964`.
- Regime breakdown was post-hoc only: bull `+54.5%`, bear `+89.1%`, sideways `+13.4%`, high-vol `+30.8%`, low-vol `+153.2%`.

## Result

No code-level regime filter was promoted. The strongest H=1 candidate (`t094`) is promising on net return, cost stress, random rank, execution-mode robustness, and buy-and-hold comparison, but it remains `NEEDS_REFINEMENT`: fold-positive is only `6/14`, fold Sharpe dispersion is high, and profit concentration top-5 is `0.887`.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: yes
- Backtester/accounting rules changed: no
- Live trading/API keys used: no

## Recommendation

Use `t094` as the next research seed for a narrow robustness work unit: reduce profit concentration and improve fold coverage without changing accounting, costs, timestamps, or split rules.
