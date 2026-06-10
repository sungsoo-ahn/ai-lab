# AI Lab Manual

This site is the operating manual for the AI Lab. A user, developer, or maintainer should be able to understand the system design, each scientist, and each work unit from these pages without opening the repository first.

The repository still contains the implementation and durable artifacts. The manual explains what those artifacts mean, how agents use them, what decisions have been made, and how future work should continue.

## Documentation Families

| Manual family | Purpose |
| --- | --- |
| [System Manual](system/index.md) | Maintains the whole AI Lab: layer model, policies, documentation standards, deployment, and operating procedures. |
| [Scientist Manuals](scientists/index.md) | Explain each scientist end to end: goal, target metric, constraints, agents/tools, workflow, artifacts, decisions, plots, risks, and embedded work-unit manuals. |

## Current Scientist

The active scientist is [BTC AutoResearch v1](scientists/btc-autoresearch-v1/index.md). It studies BTCUSDT short-horizon backtests while preserving causal evaluation, transaction-cost accounting, and sealed holdout protection.

The current recommendation is conservative: continue with a narrow `t094` robustness work unit before any sealed holdout consideration.

## How To Read The Site

1. Start with the [System Manual](system/index.md) to understand the lab model.
2. Read the [BTC scientist manual](scientists/btc-autoresearch-v1/index.md) to understand the current agent scheme and score-search evidence.
3. Use the scientist's embedded work-unit ledger to audit how each result was produced.
4. Treat implementation paths as provenance references. The manual text should be sufficient for understanding; paths are included for audit and maintenance.
