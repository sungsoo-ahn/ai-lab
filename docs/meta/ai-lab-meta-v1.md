# AI Lab Meta v1

Date: 2026-06-10
Status: active

## Summary

The meta-AI scientist analyzes the overall AI Lab matrix and proposes improvements to tasks, schemes, evaluation cells, automation, and documentation.

The meta scientist is not a stronger version of a task scientist. It studies the lab as a system: whether the artifacts are comparable, whether autonomy is blocked by missing permissions or weak run specs, whether docs explain the current state, and whether new scientist versions should be created.

## Authority

Initial authority is analyze-and-propose only. The meta scientist may write analyses and proposals, but it must not mutate tasks, schemes, cells, metrics, or run specs automatically.

This boundary prevents a meta analysis from corrupting the evidence it is analyzing. A proposal can recommend a new metric, scheme, skill bundle, or run spec, but accepted changes should create a new version when existing evidence depends on the old one.

## Inputs

- `tasks/active/`
- `schemes/`
- `evaluations/active/`
- `reports/system-status.md`
- `logs/activity.md`

## Outputs

- `meta/active/ai_lab_meta_v1/analyses/`
- `meta/active/ai_lab_meta_v1/proposals/`
- `meta/active/ai_lab_meta_v1/report.md`

## Analysis Questions

The meta scientist should ask:

- Are task and scientist concepts still decoupled?
- Are cells comparable, or did hidden component differences make the comparison ambiguous?
- Did automation run without unnecessary human intervention?
- Did run specs preserve enough artifacts to audit success and failure?
- Did docs explain both current operation and deeper design rationale?
- Are skills, research taste, and hypotheses cleanly separated?
- Which proposals should become a new version rather than an in-place edit?

## Proposal Types

| Proposal type | Example |
| --- | --- |
| Task proposal | Add a new benchmark task or clarify BTC constraints. |
| Scheme proposal | Create a search-based scientist scheme inspired by automated evaluator loops. |
| Skill proposal | Add a reusable robustness-audit skill bundle. |
| Taste proposal | Add a conservative evidence profile for high-overfit tasks. |
| Cell proposal | Create a new BTC comparison cell with a changed budget or metric version. |
| Automation proposal | Change a run spec to prevent unattended hangs. |
| Docs proposal | Add a missing guide or clarify a confusing term. |

## Success Criteria

Meta-scientist work is useful when it produces fewer ambiguous runs, cleaner comparisons, better automation, and clearer next experiments. It is not useful if it only summarizes the repo without making a concrete proposal.
