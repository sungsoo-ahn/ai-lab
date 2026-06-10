# AutoResearch

Date: 2026-06-10
Status: active

## Summary

AutoResearch is a metric-driven experiment loop. It proposes, executes, evaluates, and records bounded experiments against a fixed task-specific metric inside an evaluation cell.

## Operating Model

Use this scheme when the task has a measurable target, reproducible commands, and a useful cycle of proposal, execution, scoring, and synthesis.

Cells using this scheme should define source gates, exact commands, artifact paths, and a synthesis prompt before unattended runs.

## Active BTC Cell

- [BTC Benchmark AutoResearch Overnight v1](../evaluations/btc-benchmark--autoresearch--overnight-v1.md)

## Approval Boundaries

External submissions, connector writes, account configuration changes, Docker, Node, and unlisted OS package installs require explicit user approval.
