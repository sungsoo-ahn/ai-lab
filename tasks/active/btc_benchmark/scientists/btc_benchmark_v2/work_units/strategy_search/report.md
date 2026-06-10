# Work Unit Report: strategy_search

Date: 2026-06-10
Status: complete

## Purpose

Find causal participant strategies that improve the official benchmark dev score without new OS dependencies.

## Commands Run

```sh
cd /Users/sungs/ai-lab/sources/checkouts/btc_agentic_system
BTC_BENCHMARK_REPO=/Users/sungs/ai-lab/sources/checkouts/btc_benchmark uv run --with-editable . --with-editable /Users/sungs/ai-lab/sources/checkouts/btc_benchmark python -m scripts.search_rules --benchmark-repo /Users/sungs/ai-lab/sources/checkouts/btc_benchmark --team ai_lab_v2 --limit 160 --top-gated 5
BTC_BENCHMARK_REPO=/Users/sungs/ai-lab/sources/checkouts/btc_benchmark uv run --with-editable . --with-editable /Users/sungs/ai-lab/sources/checkouts/btc_benchmark python -m scripts.search_rules --benchmark-repo /Users/sungs/ai-lab/sources/checkouts/btc_benchmark --team ai_lab_v2 --offset 160 --top-gated 0 --out-dir results/rule_search_tail
BTC_BENCHMARK_REPO=/Users/sungs/ai-lab/sources/checkouts/btc_benchmark uv run --with-editable . --with-editable /Users/sungs/ai-lab/sources/checkouts/btc_benchmark python -m scripts.run_benchmark --strategy agentic.strategies.rule_strategies:BestEmaRegimeV1 --team ai_lab_v2 --benchmark-repo /Users/sungs/ai-lab/sources/checkouts/btc_benchmark --no-sub-bars
```

## Package Installs

No new OS packages. Used repository-local `uv` environments and existing Python dependencies.

## Files Changed

- Added `/Users/sungs/ai-lab/sources/checkouts/btc_agentic_system/agentic/strategies/rule_strategies.py`.
- Added `/Users/sungs/ai-lab/sources/checkouts/btc_agentic_system/scripts/search_rules.py`.
- Generated `results/rule_search/` and `results/rule_search_tail/` under the strategy checkout.

## Outputs

Best gated candidate:

- class: `agentic.strategies.rule_strategies:BestEmaRegimeV1`
- strategy: `ema_regime_f24_s1440_b0.02_h72_long_cash`
- gates: passed on all 14 folds
- disqualified: false
- net `+260.5%`
- Sharpe `1.295`
- Sortino `1.167`
- max drawdown `-27.4%`
- trades `26`; turnover `52`; exposure `48.5%`
- cost stress: 0x `+279.8%`, 1x `+260.5%`, 2x `+242.3%`, 3x `+224.9%`, 5x `+192.7%`
- next-open net `+260.5%`
- funding-aware net `+198.8%`
- random turnover-matched percentile `0.98`
- buy-hold net `+150.3%`
- sealed holdout used: false

Top gated alternatives from the first screen:

| Strategy | Net | Sharpe | MaxDD | 5x cost | Funding-aware |
| --- | ---: | ---: | ---: | ---: | ---: |
| `ema_regime_f24_s1440_b0.02_h72_long_cash` | `+260.5%` | `1.295` | `-27.4%` | `+192.7%` | `+198.8%` |
| `ema_regime_f24_s1440_b0.01_h1_long_cash` | `+245.1%` | `1.224` | `-24.9%` | `+169.1%` | `+183.5%` |
| `ema_regime_f48_s1440_b0.02_h1_long_cash` | `+232.5%` | `1.217` | `-27.2%` | `+167.7%` | `+175.0%` |
| `ema_regime_f72_s1440_b0.02_h1_long_cash` | `+231.9%` | `1.216` | `-25.6%` | `+176.1%` | `+174.5%` |
| `ema_regime_f24_s1440_b0.01_h24_long_cash` | `+228.8%` | `1.183` | `-28.2%` | `+160.5%` | `+170.0%` |

The tail screen did not beat the current best. Best tail candidate was `donchian_trend_e72_x72_h1` at screened net `+227.5%`, not gated in this pass.

## Result

A simple long/cash EMA-regime strategy beat buy-and-hold and the prior BTC AutoResearch `t094` headline net on dev OOS while passing benchmark gates. This is a strong candidate, but it is selected from a search and needs robustness checks before any external submission.

This work unit is complete and superseded by `ema_regime_robustness`, which promoted `BestEmaRegimeV2` at `+324.3%` net.

## Safety Checklist

- Sealed holdout used: no
- Failed trials preserved: yes, via `screened.csv`, `gated.csv`, and reports
- Backtester/accounting rules changed: no
- Live trading/API keys used: no

## Recommendation

Use this as the initial search ledger; final candidate evidence lives in the robustness and scientist reports.
