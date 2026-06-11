# AutoScientist

Date: 2026-06-10
Status: active

## Summary

AutoScientist is a shared-state, parallel research-team scheme. It emphasizes independent work units, critique, evidence sharing, and synthesis.

## Operating Model

Use this scheme when a task benefits from multiple parallel attempts rather than a single metric loop.

Cells using this scheme should define shared state, work-unit ownership, proposal review rules, and a synthesis cadence.

## Roles

AutoScientist should make roles explicit enough that the cell can be audited later. Typical roles are:

| Role | Responsibility | Evidence expected |
| --- | --- | --- |
| Planner | Selects hypotheses and allocates work units. | Work-unit plan and rationale. |
| Builder | Implements candidates, scripts, or analysis code. | Commands, diffs, reports, and artifacts. |
| Critic | Checks leakage, metric gaming, weak assumptions, and missing baselines. | Critique notes tied to evidence. |
| Synthesizer | Consolidates results into decisions and next proposals. | Summary, accepted/rejected hypotheses, proposal records. |

A role can be performed by the same underlying model or process, but the artifact should still identify which function was being performed.

## Shared State

AutoScientist needs shared state because independent work units otherwise drift. The shared state should include:

- task contract and constraints;
- scientist composition;
- active hypotheses;
- current best evidence;
- known failed ideas;
- approved command surfaces;
- open questions;
- next synthesis deadline.

Shared state should be concise. If it grows into a transcript dump, the scheme becomes hard to review and compare.

## Strengths

- Better coverage of broad search spaces than a single loop.
- More natural home for critique and adversarial checks.
- Can separate domain work from infrastructure work.
- Can compare independent hypotheses before committing to one path.

## Weaknesses

- More coordination overhead.
- Harder to judge whether improvement came from the scheme or from more total effort.
- Can generate redundant work units unless the planner is strict.
- Needs stronger synthesis to avoid scattered evidence.

## Good Work Units

- independent candidate families;
- adversarial benchmark audit;
- proxy dataset construction;
- critique of top candidates;
- literature or source scan;
- meta-analysis of why the scheme stalled;
- proposal for a new scheme or taste version.

## Active BTC Cell

- [BTC Benchmark AutoScientist Extended](../evaluations/btc-benchmark--autoscientist--extended.md)

## Approval Boundaries

External submissions, connector writes, account configuration changes, Docker, Node, and unlisted OS package installs require explicit user approval.
