# AutoResearch

Date: 2026-06-10
Status: active

## Summary

AutoResearch is a metric-driven experiment loop. It proposes, executes, evaluates, and records bounded experiments against a fixed task-specific metric inside an evaluation cell.

## Operating Model

Use this scheme when the task has a measurable target, reproducible commands, and a useful cycle of proposal, execution, scoring, and synthesis.

Cells using this scheme should define source gates, exact commands, artifact paths, and a synthesis prompt before unattended runs.

## Loop

1. Read the task contract, metric, constraints, skill bundle, taste profile, and seed hypotheses.
2. Propose a small set of candidate methods or audits.
3. Execute the fixed command plan or a bounded work-unit command.
4. Score candidates with the approved evaluator.
5. Record artifacts and negative results.
6. Synthesize what changed relative to the prior state.
7. Propose the next work unit or stop according to exit criteria.

The loop is intentionally narrow. It works best when the scientist can learn from a series of comparable measurements.

## Required Cell Fields

An AutoResearch cell should make these fields easy to inspect:

| Field | Why it matters |
| --- | --- |
| `task_id` | Prevents the scheme from absorbing task identity. |
| `scheme_id` | Makes comparison against other schemes explicit. |
| `scientist_composition` | Records skill bundle, taste, and seed hypotheses. |
| `target_metric` | Prevents post-hoc metric selection. |
| `constraints` | Names disallowed changes and approval boundaries. |
| `run-spec.yaml` | Gives the exact local command contract. |
| `source-map.md` | Identifies external and local sources used by the cell. |

## Strengths

- Fast to operate when scoring is automated.
- Easy to compare across runs because the loop is stable.
- Good at finding incremental improvements and ablations.
- Fits tasks where failure artifacts are cheap to preserve.

## Weaknesses

- Can overfit to a metric if research taste is weak.
- Can miss broad reframings that are not naturally proposed by the loop.
- Can under-invest in critique if the run spec rewards only execution.
- Can produce many small artifacts that need synthesis discipline.

## Good Work Units

- baseline ladder;
- parameter sweep with causal features;
- leakage audit;
- transaction-cost robustness audit;
- source readiness check;
- negative-result synthesis;
- proposal for the next cell version.

## Active BTC Cell

- [BTC Benchmark AutoResearch Extended](../evaluations/btc-benchmark--autoresearch--extended.md)

## Approval Boundaries

External submissions, connector writes, account configuration changes, Docker, Node, and unlisted OS package installs require explicit user approval.
