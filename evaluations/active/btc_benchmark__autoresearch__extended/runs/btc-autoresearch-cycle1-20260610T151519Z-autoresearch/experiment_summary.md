# Experiment Summary

Run ID: `btc-autoresearch-cycle1-20260610T151519Z-autoresearch`
Cycle: 1
Evaluation cell: `btc_benchmark__autoresearch__extended`

## Question

The taste profile ranks low-parameter, causal, after-cost evidence ahead of raw dev-score chasing. The first bounded experiment therefore tested the seed trend-following ladder, simple turnover/cost filters, and one funding-aware filter before considering heavier methods.

## Setup

- Referee: frozen `btc_benchmark` checkout at `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`.
- Data: 56,232 BTCUSDT 1h candles with `funding` auxiliary data.
- Preflight baseline: `ema_baseline_12_48_long_short`.
- Candidate runner: `run_candidate_sweep.py`.
- Sweep reports: `candidate_reports/*.json`.
- Sweep leaderboard: `candidate_leaderboard.jsonl`.
- Confirmed best report: `confirm_best_report.json`.
- Sweep gates: enabled with `gate_max_cutoffs=64`.
- Best confirmation gates: referee default settings, all 14 folds gated, minimum future-perturbation cutoffs `433`.

## Preflight Baseline

`ema_baseline_12_48_long_short` passed gates but is a weak benchmark floor:

- Net `-0.8668`, Sharpe `-0.879`, max drawdown `-0.8769`.
- Turnover `1587.0`, trades `794`, median hold `23` bars.
- Cost curve: cost0x `-0.3479`, cost2x `-0.9729`, cost5x `-0.9998`.
- Funding-aware net `-0.8752`, next-open net `-0.8669`, random percentile `0.21`.

## Candidate Results

| Rank | Strategy | Net | Sharpe | Max DD | Turnover | Cost2x | Cost5x | Next-open | Funding-aware | Random pctile |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `candidate_always_long` | `1.5005` | `0.770` | `-0.6670` | `1.0` | `1.4980` | `1.4904` | `1.4982` | `0.9151` | n/a |
| 2 | `candidate_ema_48_192_funding_le_5bp` | `0.9021` | `0.713` | `-0.4316` | `225.0` | `0.5184` | `-0.2286` | `0.9005` | `0.6106` | `0.95` |
| 3 | `candidate_ema_48_192_long_cash` | `0.8433` | `0.682` | `-0.4316` | `195.0` | `0.5164` | `-0.1568` | `0.8418` | `0.5430` | `0.93` |
| 4 | `candidate_ema_24_96_long_cash` | `0.6632` | `0.595` | `-0.4575` | `375.0` | `0.1423` | `-0.6307` | `0.6614` | `0.4050` | `0.96` |
| 5 | `candidate_ema_48_192_highvol_q60` | `0.2130` | `0.369` | `-0.2413` | `182.0` | `0.0108` | `-0.4157` | `0.2132` | `0.1526` | `0.84` |

All 13 sweep candidates were non-disqualified. Donchian, RSI, fast EMA long-cash, and long-short EMA variants were negative after costs.

## Confirmed Best

`candidate_always_long_default_gates`:

- Net `1.5005`, Sharpe `0.770`, max drawdown `-0.6670`.
- Turnover `1.0`, trades `1`, full exposure.
- Cost curve: cost0x `1.5031`, cost2x `1.4980`, cost3x `1.4955`, cost5x `1.4904`.
- Funding-aware net `0.9151`, next-open net `1.4982`.
- Per-year net: 2022 `-0.6375`, 2023 `1.5718`, 2024 `1.2201`, 2025 `0.2080`.
- Gates passed on all 14 folds with default gate budget; sealed holdout was not used.

## Interpretation

There is a clear metric improvement over the preflight EMA baseline, but it is not evidence of a novel adaptive alpha. The best score is almost identical to the referee buy-and-hold reference (`buy_hold_net=1.5031`) minus one opening transaction cost. It is robust to cost multipliers and next-open execution because it barely trades, but it carries full exposure, a `-0.6670` drawdown, a weak 2022 year, and meaningful funding drag.

The best adaptive result is `candidate_ema_48_192_funding_le_5bp`. It improves raw net and funding-aware net over the plain EMA 48/192 long-cash rule (`0.9021` vs `0.8433` net, `0.6106` vs `0.5430` funding-aware), but uses higher turnover and is worse under 5x costs (`-0.2286` vs `-0.1568`). This is worth a follow-up only as an overlay/exit component, not as a promoted solution.

## Decision

Treat always-long as the development floor, not as an accepted research win. The next cell should optimize adaptive overlays relative to buy-and-hold and report drawdown, funding-aware net, cost stress, next-open execution, and per-year concentration as first-class decision criteria.
