# BTC Benchmark v2

<div class="run-metadata">
<p><strong>Scientist ID:</strong> btc_benchmark_v2</p>
<p><strong>Task:</strong> btc_benchmark</p>
<p><strong>Status:</strong> active local solution</p>
<p><strong>Updated:</strong> 2026-06-10 KST</p>
</div>

## One-Screen Summary

BTC Benchmark v2 is a scientist for the frozen BTC 1h benchmark. It treats `btc_benchmark` as the referee and only changes participant strategy code in `btc_agentic_system`.

The current local candidate is reproducible and passes the benchmark gates:

- strategy class: `agentic.strategies.rule_strategies:BestEmaRegimeV2`
- strategy name: `ema_regime_f12_s1440_b0.025_h72_long_cash`
- dev net: `+324.3%`
- Sharpe: `1.453`
- max drawdown: `-25.1%`
- buy-and-hold comparison: `+150.3%`
- causality gates: all 14 folds passed
- exhaustive future-perturbation gate: passed with at least 2,160 cutoffs per fold
- sealed holdout used: no

External submission or upstream GitHub writes remain a human-gated action.

## Purpose And Boundaries

Specific goal: improve participant strategies against the frozen benchmark while preserving the referee's costs, walk-forward splits, backtester, causality gates, random baseline comparison, and sealed-holdout firewall.

This scientist is not a live-trading system. It does not place orders, use exchange credentials, alter account settings, or make external submissions without approval.

## Evaluation Context

| Field | Value |
| --- | --- |
| Referee | `btc_benchmark` version `1.0.0` |
| Participant repo | `btc_agentic_system` |
| Primary metric | official dev `net` from `run_benchmark` |
| Required validity | non-disqualified strategy with causality gates passing |
| Companion evidence | Sharpe, Sortino, max drawdown, cost stress, next-open net, funding-aware net, random percentile, buy-hold comparison, per-year behavior |
| Holdout rule | sealed holdout remains host-owned and unused locally |

## Agent And Tool Roles

| Role | Responsibility | Benchmark example |
| --- | --- | --- |
| Referee Reproduction | Make the frozen benchmark runnable and verify tests. | Repaired the missing local data package from lineage and ran the referee test suite. |
| Baseline Runner | Establish bundled strategy comparisons. | `EmaTrend` lost money; `XgbMomentum` ran after runtime setup but stayed below buy-and-hold. |
| Strategy Search | Explore dependency-light causal rules. | Found the initial gated EMA-regime candidate at `+260.5%`. |
| Robustness Sweeper | Test parameter neighborhoods and gate top variants. | Screened 1,296 EMA variants and gated the top 8. |
| Report Synthesis | Preserve commands, caveats, and submission boundary. | Updated scientist report, source map, and public manual. |

## Work Units

| Work Unit | Status | Result | Manual |
| --- | --- | --- | --- |
| `referee_reproduction` | complete | Local referee tests passed `131 passed, 1 skipped`; data package repair documented. | [Manual](work-units/referee-reproduction.md) |
| `bundled_baselines` | complete | `EmaTrend` lost `-81.7%`; `XgbMomentum` scored `+53.3%` after runtime setup. | [Manual](work-units/bundled-baselines.md) |
| `strategy_search` | complete | Found `BestEmaRegimeV1` at `+260.5%`; superseded by robustness. | [Manual](work-units/strategy-search.md) |
| `ema_regime_robustness` | complete | Promoted `BestEmaRegimeV2` at `+324.3%`; exhaustive gates passed. | [Manual](work-units/ema-regime-robustness.md) |
| `report_synthesis` | active | Maintains local evidence and submission readiness. | [Manual](work-units/report-synthesis.md) |

## Runtime Lessons

The bundled XGBoost baseline exposed a runtime gap: newer XGBoost wheels on macOS can require OpenMP from Homebrew `libomp`, and the sklearn wrapper also needs `scikit-learn`. The AI Lab now has an allowlisted `xgboost-macos` runtime profile for approved long runs:

```sh
bin/ai-lab runtime check xgboost-macos --repo sources/checkouts/btc_agentic_system
bin/ai-lab runtime ensure xgboost-macos --repo sources/checkouts/btc_agentic_system
```

This profile does not authorize broad system changes. It only standardizes the already documented XGBoost runtime dependency.

## Implementation References

- Scientist manifest: `tasks/active/btc_benchmark/scientists/btc_benchmark_v2/scientist.yaml`
- Scientist report: `tasks/active/btc_benchmark/scientists/btc_benchmark_v2/report.md`
- Source map: `tasks/active/btc_benchmark/scientists/btc_benchmark_v2/source-map.md`
- Strategy implementation branch: `sungsoo-ahn/btc_agentic_system`, branch `ai-lab-btc-benchmark-v2`
- Strategy class: `sources/checkouts/btc_agentic_system/agentic/strategies/rule_strategies.py`
