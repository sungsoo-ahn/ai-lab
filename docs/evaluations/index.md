# Evaluation Matrix

Evaluation cells bind one task to one scientist scheme. The matrix is the main place to compare whether different scientist designs produce better evidence, better task performance, or better next-step proposals under similar constraints.

## Current Cells

| Cell | Task | Scheme | Status | Latest evidence |
| --- | --- | --- | --- | --- |
| [BTC Benchmark AutoResearch Overnight v1](btc-benchmark--autoresearch--overnight-v1.md) | BTC Benchmark | AutoResearch | active, cycle 5 synthesized | `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`: participant-style Cycle 4 asset reviewed, parity-checked, and default-gated. |
| [BTC Benchmark AutoScientist Overnight v1](btc-benchmark--autoscientist--overnight-v1.md) | BTC Benchmark | AutoScientist | active | Ready for direct cell run. |
| [BTC Benchmark AutoResearch Smoke](btc-benchmark--autoresearch--smoke.md) | BTC Benchmark | AutoResearch | complete | `smoke-20260610` passed. |

## Latest Matrix Evidence

The latest AutoResearch run completed five synthesis cycles successfully and is now the strongest BTC Benchmark evidence in the matrix:

- Run ID: `btc-autoresearch-cycle2-20260610T223228Z-autoresearch`.
- Current reviewed raw-net candidate: `cycle4_funding3bp_exit6_min24`.
- Default-gated net `2.8828`, delta versus always-long `+1.3823`, max drawdown `-0.3364`, turnover `257.0`.
- Funding-aware net `2.3155`, next-open net `2.8781`, random percentile `1.0`; all 14 fold gates passed with cutoff minimum `433`.
- Cycle 5 verified exact fold-position parity between the saved participant-style asset and the Cycle 4 run-local implementation.
- Remaining warnings: cost5x remains weaker than passive always-long, returns are concentrated in 2023-2024, and participant-repo packaging is not yet verified.
- Follow-up proposal: `evaluations/active/btc_benchmark__autoresearch__overnight_v1/proposals/btc_autoresearch_cycle6_participant_repo_packaging.md`.

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
