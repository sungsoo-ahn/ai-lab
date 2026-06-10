# Work Unit: BTC Regime Filter Probe

<div class="run-metadata">
<p><strong>Work Unit ID:</strong> regime_filter_probe</p>
<p><strong>Scientist:</strong> btc_autoresearch_v1</p>
<p><strong>Status:</strong> complete</p>
<p><strong>Date:</strong> 2026-06-10 00:27 KST</p>
</div>

## Purpose

This work unit audited the strongest H=1 candidate family after baseline reproduction passed. It checked whether the `t094` candidate was robust enough to promote or should instead seed a narrower follow-up.

## Method

The work unit ran a custom M5.5 audit for `t094`, including post-hoc regime breakdown and funding sensitivity. It examined net return, cost stress, random turnover-matched robustness, buy-and-hold comparison, fold coverage, and profit concentration.

## Commands

```sh
cd sources/checkouts/btc_autoresearch
uv run --no-sync python - <<'PY'
# Ran custom M5.5 audit for t094, including post-hoc regime breakdown and funding sensitivity.
PY
```

## Results

| Metric | Value |
| --- | ---: |
| Candidate | `t094_f321ec793728` |
| Config | `returns_only`, H=1, `long_cash`, `cost_aware`, lambda `5.0` |
| Net return | +231.1% |
| Sharpe | 1.05 |
| Max drawdown | -38% |
| Trades | 25 |
| Cost stress 2x | +215% |
| Cost stress 5x | +172% |
| Funding-aware net | +184.4% |
| Random percentile rank | 0.964 |
| Fold-positive | 6/14 |
| Profit concentration top-5 | 0.887 |

Post-hoc regime breakdown: bull `+54.5%`, bear `+89.1%`, sideways `+13.4%`, high-vol `+30.8%`, low-vol `+153.2%`.

## Decision

`t094` is promising but remains `NEEDS_REFINEMENT`. Do not promote it to holdout. Use it as the next robustness seed.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: yes
- Backtester/accounting rules changed: no
- Live trading/API keys used: no

## How To Continue

Search the `t094` family for lower profit concentration and better fold coverage without changing accounting, costs, timestamps, or split rules.

## Implementation References

- Manifest: `tasks/active/btc/scientists/btc_autoresearch_v1/work_units/regime_filter_probe/work-unit.yaml`
- Custom audit report path: `sources/checkouts/btc_autoresearch/results_t094_audit/reports/m5_5_audit/report.md`
