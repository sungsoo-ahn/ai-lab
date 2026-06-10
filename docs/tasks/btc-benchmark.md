# BTC Benchmark

Date: 2026-06-10
Status: active

## Summary

BTC Benchmark is the frozen BTC 1h task. It is separate from any scientist scheme that attempts it.

## Candidate Metric

The main metric is the benchmark referee's development score. Scores are valid only when produced without changing referee semantics.

## Constraints

- Do not modify referee scoring, cost model, causality checks, or holdout policy.
- External submissions require explicit user approval.

## Evaluation Cells

- [BTC Benchmark AutoResearch Overnight v1](../evaluations/btc-benchmark--autoresearch--overnight-v1.md)
- [BTC Benchmark AutoScientist Overnight v1](../evaluations/btc-benchmark--autoscientist--overnight-v1.md)
- [BTC Benchmark AutoResearch Smoke](../evaluations/btc-benchmark--autoresearch--smoke.md)

## Scientist Components

- Skill bundle: `btc_benchmark_core_skills_v1`
- Research taste: `btc_robust_alpha_taste_v1`
- Seed hypotheses: `catalog/hypotheses.yaml`

See [Scientist Components](../reference/scientist-components.md).
