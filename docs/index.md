# AI Lab Manual

This site is a static manual for inspecting an AI Lab: a local-first workspace for developing AI scientists. The current concrete example is the BTC scientist, which studies BTCUSDT short-horizon backtests while preserving causal evaluation, transaction-cost accounting, and sealed holdout protection.

The site is intentionally simple. Markdown pages explain methods and decisions, Mermaid diagrams show agentic flow, Vega-Lite plots make score-search trials inspectable, and static JSON/YAML files keep examples editable by hand.

## What An AI Scientist Is

An AI scientist is an orchestration layer around uncertain research work. It proposes work units, runs bounded investigations, preserves evidence, and updates its scheme only through explicit proposals.

The AI Lab model has four layers:

| Layer | Role |
| --- | --- |
| Lab | Shared catalogs, policies, memory, logs, and scheme knowledge. |
| Task | A broad challenge or dataset family, such as BTC. |
| Scientist | A task-specific scheme with target metrics, constraints, reports, assets, and proposal history. |
| Work unit | A focused context for one hypothesis, audit, ablation, synthesis pass, proxy, or infrastructure pass. |

## Trials Are Not The Whole Scientist

The BTC scientist has score-maximizing candidate trials, but not every useful work unit tries to maximize score. A pipeline audit, horizon-matched evaluation, report synthesis pass, or robustness check can improve the scientist even when it does not produce a higher return.

The performance plot is therefore one evidence surface. It helps inspect candidate trials from the BTC score search, while work-unit reports explain why a high-return point may still be unsafe to promote.

## Mental Model

Markdown tutorials + Mermaid workflows + Vega-Lite trial plots + static run artifacts.

In practice:

1. Read the workflow to understand which agent or tool produced each artifact.
2. Inspect the score plot to find promising, rejected, or suspicious BTC trials.
3. Open a trial detail page to see the hypothesis, config, trace excerpt, metrics, and decision.
4. Read work-unit summaries to understand audits and negative findings that do not appear as score improvements.

## Current BTC Scientist

The active BTC scientist is `btc_autoresearch_v1`. It reproduced the local `t054` baseline, extended a score-search ledger to 100 trials, audited the strongest H=1 candidate `t094`, found caveats in H=4 default candidates, and preserved rejected or suspicious results.

The current recommendation is conservative: continue with a narrow `t094` robustness work unit before any sealed holdout consideration.

## Start Here

- [First BTC trial inspection](tutorials/first-btc-trial.md)
- [AI Lab scientist loop](workflows/ai-lab-loop.md)
- [BTC AutoResearch v1 scientist report](scientists/btc-autoresearch-v1.md)
- [BTC trial index](trials/index.md)
- [Work unit index](work-units/index.md)
