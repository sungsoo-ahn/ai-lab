---
id: system-procedures
type: system_memory
created_at: 2026-06-09
updated_at: 2026-06-10
confidence: high
sensitivity: public
status: active
links:
  - /Users/sungs/ai-lab/policies/update-policy.md
  - /Users/sungs/ai-lab/policies/scientist-runtime-policy.md
  - /Users/sungs/ai-lab/docs/system/maintenance.md
  - /Users/sungs/ai-lab/docs/system/documentation-standards.md
---

# AI Lab Procedures

## Tasks

Use `bin/ai-lab task init <task_id>` to create a broad task workspace. A task describes an under-specified challenge or dataset family and may contain multiple scientists with different metrics or schemes.

## Scientists

Use `bin/ai-lab scientist init <task_id> <scientist_id>` to create a concrete scientist version. A scientist owns the specific goal, target metric, optimization constraints, reports, assets, runs, work units, and proposal gate.

Use `bin/ai-lab scientist version <task_id> <old_scientist_id> <new_scientist_id>` when accepted proposals should become the next iteration. Do not silently mutate a current scientist target metric in place.

## Work Units

Use `bin/ai-lab work-unit init <task_id> <scientist_id> <work_unit_id>` to create a minimal agent context. Work units may optimize the target metric, make observations, run ablations, build proxy datasets, test proxy experiments, synthesize results, or improve infrastructure.

Work units should reference scientist assets by `asset_id`, record parallel-safety metadata, and write proposals under the scientist `proposals/` directory when they recommend changing the scientist scheme or target metric.

## Memory

Use `bin/ai-lab memory index` to rebuild the generated SQLite search index. Use `bin/ai-lab memory search <query>` to search Markdown, YAML, and logs.

## Self-Evolution

Low-risk local memory, report, template, and index updates may be applied inside `/Users/sungs/ai-lab`. Package, runtime, shell, connector, account config, and out-of-zone changes require explicit approval or an explicit overnight/long-run authorization and must follow update policy.

## Overnight Research Runs

If the user explicitly authorizes an overnight run with automatic dependency setup, agents may install missing Python scientist dependencies using scientist-local or inherited repository-local `uv` workflows. Allowlisted runtime profiles may be ensured with `bin/ai-lab runtime ensure <profile>`; the first profile is `xgboost-macos` for Homebrew `libomp`. Agents must not install Node, Docker, connector integrations, credentials, shell configuration, account configuration, or unlisted OS packages silently.

For detached account-level `codex exec` runs, pass account-level flags before `exec` and use `--skip-git-repo-check` when launching from `/Users/sungs`. Known-good pattern:

```sh
codex --ask-for-approval never --search exec --cd /Users/sungs --skip-git-repo-check -
```
