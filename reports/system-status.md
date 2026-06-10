# AI Lab Status

Date: 2026-06-10

## Current Shape

- Workspace: `/Users/sungs/ai-lab`
- Source registry: `/Users/sungs/ai-lab/sources/sources.yaml`
- Canonical storage: Markdown and YAML
- Prompt provenance: exact prompts are local run artifacts under evaluation-cell `runs/<run_id>/prompts/`
- Generated search index: `memory/index.sqlite`
- Memory hierarchy: lab -> task -> scheme -> evaluation cell -> work unit -> meta scientist
- Self-evolution policy: work-unit proposals are gated into new evaluation-cell versions
- Public docs: system guides, task pages, scheme pages, evaluation matrix, and meta page
- Rigid runner: active evaluation cells define `run-spec.yaml`

## Active Tasks

- `btc_benchmark`: frozen BTC 1h benchmark task.

## Active Schemes

- `autoresearch`: fixed metric-driven experiment loop.
- `autoscientist`: parallel research-team scheme with critique and synthesis.

## Active Evaluation Cells

One benchmark smoke cell is active and has a passing run: `smoke-20260610`.

## Meta Scientist

- `ai_lab_meta_v1`: analyze-and-propose layer for system improvements.

## User-Facing Entry Points

- `README.md`
- `docs/index.md`
- `docs/system/index.md`
- `docs/tasks/index.md`
- `docs/schemes/index.md`
- `docs/evaluations/index.md`
- `docs/meta/ai-lab-meta-v1.md`
- `reports/system-status.md`
- `sources/sources.yaml`
- `catalog/tasks.yaml`
- `catalog/scientist-schemes.yaml`

## Operational Notes

- Package/runtime changes follow `policies/update-policy.md` and `policies/evaluation-runtime-policy.md`.
- Long-running cells may use `research/templates/overnight-goal.md`, validated `run-spec.yaml` files, and allowlisted runtime profiles.
- Current allowlisted runtime profile: `btc-benchmark-python`, which checks benchmark Python imports in the source checkout.
- Connector writes still require explicit approval.
- Generated indexes can be rebuilt with `bin/ai-lab memory index`.
