# AI Lab Guide

This guide explains how the public MkDocs site maps back to the local AI Lab workspace.

## What You Are Looking At

The workspace lives under `/Users/sungs/ai-lab`. The public site is a generated view of the workspace, not a separate source of truth.

Markdown and YAML are canonical. SQLite indexes, cached environments, and generated Pages output are build products.

## Four Layers

1. Lab: shared catalogs, memory, policies, logs, and scientist scheme knowledge.
2. Task: a broad, under-specified challenge or dataset family.
3. Scientist: a concrete scheme, version, target metric, constraints, reports, assets, runs, and proposals.
4. Work unit: the minimal context for one hypothesis, method, observation, ablation, proxy, synthesis, or infrastructure pass.

## Files Worth Opening First

- `README.md`: workspace overview and command entry points.
- `reports/system-status.md`: current AI Lab status.
- `catalog/tasks.yaml`: broad task catalog.
- `catalog/scientist-schemes.yaml`: reusable scientist scheme catalog.
- `tasks/active/<task_id>/task.yaml`: task manifest.
- `tasks/active/<task_id>/scientists/<scientist_id>/guide.md`: scientist-specific user guide.
- `tasks/active/<task_id>/scientists/<scientist_id>/report.md`: current scientist result and next step.
- `tasks/active/<task_id>/scientists/<scientist_id>/work_units/<work_unit_id>/report.md`: work-unit result, evidence, and recommendation.

## Assets And Evidence

An asset is a material used by a scientist: a repository, dataset, PDF, config, model checkpoint, result bundle, image, spreadsheet, or binary artifact.

Scientists track assets in `assets.yaml`. Work units should reference assets by `asset_id` instead of copying raw paths into every report.

Optimized codebases are tracked separately in `sources/sources.yaml` by immutable git commit SHA. A shared ignored checkout may live under `sources/checkouts/`, but work units should record the `source_id` and `git_ref` as their durable dependency.

## Proposals

Work units may propose changes to the scientist scheme, target metric, constraints, or next iteration. Proposals belong under the scientist `proposals/` directory. Accepted proposals are applied by creating a new scientist version; current scientist metrics are not silently changed in place.

## Common Commands

Run these from `/Users/sungs/ai-lab`:

```sh
bin/ai-lab task status btc
bin/ai-lab scientist status btc btc_autoresearch_v1
bin/ai-lab work-unit status btc btc_autoresearch_v1 regime_filter_probe
bin/ai-lab memory index
bin/ai-lab memory search "query terms"
bin/ai-lab memory audit
```

Compatibility wrappers remain during migration:

```sh
bin/agent-project status btc
bin/agent-hypothesis close btc regime_filter_probe
bin/agent-memory search btc
```

## Privacy Rule

Do not store secrets, API keys, passwords, tokens, private keys, recovery codes, or raw private connector content in memory, logs, reports, proposals, or asset metadata.
