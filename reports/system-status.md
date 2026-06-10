# AI Lab Status

Date: 2026-06-10

## Current Shape

- Workspace: `/Users/sungs/ai-lab`
- Source registry: `/Users/sungs/ai-lab/sources/sources.yaml`
- Former compatibility symlink `/Users/sungs/agent-system` has been removed.
- Canonical storage: Markdown and YAML
- Prompt provenance: exact prompts are local run artifacts under scientist `runs/<run_id>/prompts/`
- Generated search index: `memory/index.sqlite`
- Memory hierarchy: lab -> task -> scientist -> work unit
- Self-evolution policy: work-unit proposals are gated into new scientist versions
- Public docs: system guides, scientist briefs, and work-unit briefs
- Rigid runner: active scientists define `run-spec.yaml`

## Active Tasks

- `btc`: broad BTC task.
- `btc_benchmark`: frozen BTC 1h benchmark task.

## Active Scientists

- `btc/btc_autoresearch_v1`: BTCUSDT short-horizon AI scientist built around the inherited `btc_autoresearch` pipeline. Current next step is a narrow robustness pass around the `t094` family before any sealed holdout decision.
- `btc_benchmark/btc_benchmark_v2`: frozen-referee benchmark scientist. Current local candidate is `BestEmaRegimeV2`; external submission remains approval-gated.

## Local Services

- `slack-agent-bridge`: local service scaffold, not a task or scientist.

## User-Facing Entry Points

- `README.md`
- `docs/index.md`
- `docs/system/index.md`
- `docs/system/prompt-provenance.md`
- `docs/scientists/btc-autoresearch-v1/index.md`
- `docs/scientists/btc-benchmark-v2/index.md`
- `reports/system-status.md`
- `sources/sources.yaml`
- `catalog/tasks.yaml`
- `catalog/scientist-schemes.yaml`

## Operational Notes

- Package/runtime changes follow `policies/update-policy.md` and `policies/scientist-runtime-policy.md`.
- Long-running scientists may use `research/templates/overnight-goal.md`, validated `run-spec.yaml` files, and allowlisted runtime profiles.
- Current allowlisted runtime profile: `xgboost-macos`, which installs Homebrew `libomp` for XGBoost.
- Current runtime status: `xgboost-macos` check passes; Brewfile dependencies are satisfied and XGBoost imports as `3.2.0`.
- Connector writes still require explicit approval.
- Generated indexes can be rebuilt with `bin/ai-lab memory index`.
