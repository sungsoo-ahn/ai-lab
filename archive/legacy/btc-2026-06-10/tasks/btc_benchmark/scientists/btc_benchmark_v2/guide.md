# Scientist Guide: BTC Benchmark Scientist v2

Date: 2026-06-10
Status: active

## Purpose

Solve the BTC 1h benchmark by improving strategies in `btc_agentic_system` and scoring them with the frozen `btc_benchmark` referee. The scientist must optimize the benchmark score without weakening causality gates, costs, splits, accounting, or holdout protection.

## Method Overview

The referee drives every evaluation. It calls a strategy once per walk-forward fold:

1. `fit(data, train_start, train_end)` may use only training rows.
2. `positions(data, start, end)` returns positions in `[-1, 1]` for the test window.
3. The referee runs determinism, future-perturbation, and prefix-invariance gates.
4. Passing strategies are scored for net return, Sharpe, drawdown, cost stress, execution-mode robustness, funding-aware net, random baseline percentile, and per-year behavior.

The mutable work belongs in the strategy repo. The benchmark repo is treated as a referee; if local repairs are needed to make it runnable, they must preserve scoring semantics and be documented.

## Key Terms

- `btc_benchmark`: frozen referee repository.
- `btc_agentic_system`: participant-owned strategy repository to upgrade.
- `Strategy contract`: Python interface with `fit` and `positions`.
- `causality gates`: checks that strategy output is deterministic, prefix-stable, and invariant to future data perturbations.
- `sealed holdout`: final host-owned period not exposed during development evaluation.
- `official dev score`: `run_benchmark` output on walk-forward folds before sealed holdout.
- `disqualified`: a strategy failed at least one causality gate.

## How To Continue

Current local submission candidate:

- class: `agentic.strategies.rule_strategies:BestEmaRegimeV2`
- strategy: `ema_regime_f12_s1440_b0.025_h72_long_cash`
- dev net: `+324.3%`
- Sharpe: `1.453`
- max drawdown: `-25.1%`
- gates: all 14 folds passed, including exhaustive future-perturbation with at least 2,160 cutoffs per fold
- sealed holdout used: no

To reproduce the main score, run:

```sh
cd /Users/sungs/ai-lab/sources/checkouts/btc_agentic_system
BTC_BENCHMARK_REPO=/Users/sungs/ai-lab/sources/checkouts/btc_benchmark uv run --with-editable . --with-editable /Users/sungs/ai-lab/sources/checkouts/btc_benchmark python -m scripts.run_benchmark --strategy agentic.strategies.rule_strategies:BestEmaRegimeV2 --team ai_lab_v2 --benchmark-repo /Users/sungs/ai-lab/sources/checkouts/btc_benchmark --no-sub-bars
```

The upstream benchmark README describes submission as upgrading/forking `btc_agentic_system`; no GitHub push or external submission should be made without explicit user approval.

## Safety Rules

- Do not change referee scoring, costs, accounting, splits, causality gates, or holdout firewall to improve results.
- Do not use live trading, private API keys, account credentials, or external submissions without explicit user approval.
- Do not read or simulate sealed holdout access during strategy development.
- Keep failed and disqualified runs visible.
- Use `uv` for Python environment commands; do not install into Apple system Python.
