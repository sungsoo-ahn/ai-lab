# Evaluation Matrix

Evaluation cells bind one task to one scientist scheme. The matrix is the main place to compare whether different scientist designs produce better evidence, better task performance, or better next-step proposals under similar constraints.

## Current Cells

| Cell | Task | Scheme | Status | Latest evidence |
| --- | --- | --- | --- | --- |
| [BTC Benchmark AutoResearch Overnight v1](btc-benchmark--autoresearch--overnight-v1.md) | BTC Benchmark | AutoResearch | active, cycle 1 synthesized | `btc-overnight-20260610T151519Z-autoresearch`: always-long confirmed as dev-score floor, not a novel alpha. |
| [BTC Benchmark AutoScientist Overnight v1](btc-benchmark--autoscientist--overnight-v1.md) | BTC Benchmark | AutoScientist | active | Ready for direct cell run. |
| [BTC Benchmark AutoResearch Smoke](btc-benchmark--autoresearch--smoke.md) | BTC Benchmark | AutoResearch | complete | `smoke-20260610` passed. |

## Latest Matrix Evidence

The latest AutoResearch run completed successfully and is now the strongest BTC Benchmark evidence in the matrix:

- Run ID: `btc-overnight-20260610T151519Z-autoresearch`.
- Best confirmed candidate: `candidate_always_long_default_gates`.
- Confirmed net `1.5005`, Sharpe `0.770`, max drawdown `-0.6670`, turnover `1.0`.
- The result mostly matches buy-and-hold after one opening cost, so it is a development-score floor rather than an accepted adaptive strategy.
- Best adaptive follow-up: `candidate_ema_48_192_funding_le_5bp`, with net `0.9021`, max drawdown `-0.4316`, funding-aware net `0.6106`, but weak 5x cost robustness at `-0.2286`.
- Follow-up proposal: `evaluations/active/btc_benchmark__autoresearch__overnight_v1/proposals/btc_autoresearch_cycle2_buy_hold_relative.md`.

## What A Cell Should Prove

A useful cell should answer:

- which task was attempted;
- which scheme was used;
- which skills, taste profile, and hypotheses were active;
- what metric and constraints governed the run;
- what commands or run specs executed;
- what artifacts support the result;
- what failed or remained unresolved;
- what should change in the next version.

Without those answers, a cell is just a run directory. With those answers, it becomes comparable evidence.

## Run Specs

Active cells use `run-spec.yaml` as their executable contract. Validate them with:

```bash
uv run python bin/ai-lab cell run-spec validate --all
```

Preview all runnable active cells with:

```bash
uv run python bin/ai-lab cell run-all --continuous --dry-run
```

Run specs are intentionally local and conservative. External submissions and connector writes still require explicit approval.

## Comparison Rules

Treat two cells as directly comparable only when:

- they use the same task contract;
- they optimize the same target metric;
- their source gates are equivalent;
- their wall-clock and compute budgets are similar or documented;
- their expected artifacts are similar enough to audit;
- their synthesis summaries identify the scientist composition.

If a cell changes the skill bundle, taste profile, hypotheses, or metric, label the comparison as a component comparison rather than a pure scheme comparison.

## Evidence Quality

The matrix should eventually compare both task score and evidence quality. Evidence quality includes:

- reproducibility of commands;
- completeness of artifacts;
- clarity of failure modes;
- strength of negative-result preservation;
- critique coverage;
- usefulness of next proposals;
- amount of human intervention required.
