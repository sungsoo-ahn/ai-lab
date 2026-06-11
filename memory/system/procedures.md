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
  - /Users/sungs/ai-lab/policies/evaluation-runtime-policy.md
  - /Users/sungs/ai-lab/docs/system/maintenance.md
  - /Users/sungs/ai-lab/docs/system/documentation-standards.md
---

# AI Lab Procedures

## Tasks

Use `bin/ai-lab task init <task_id>` to create a broad task definition. A task describes an under-specified challenge or dataset family and links to evaluation cells.

## Scientist Schemes

Use `bin/ai-lab scheme init <scheme_id>` to create a reusable AI scientist scheme. A scheme describes orchestration, autonomy, work-unit style, and evidence discipline.

## Evaluation Cells

Use `bin/ai-lab cell init <cell_id> <task_id> <scheme_id>` to apply one scheme to one task. A cell owns the specific goal, target metric, constraints, run spec, reports, assets, runs, work units, and proposal gate.

Use `bin/ai-lab cell version <old_cell_id> <new_cell_id>` when accepted proposals should become the next iteration. Do not silently mutate a current cell target metric in place.

Validate fixed command loops with:

```sh
uv run python bin/ai-lab cell run-spec validate --all
```

## Work Units

Use `bin/ai-lab work-unit init <cell_id> <work_unit_id>` to create a minimal agent context. Work units may optimize the target metric, make observations, run ablations, build proxy datasets, test proxy experiments, synthesize results, or improve infrastructure.

Work units should reference cell assets by `asset_id`, record parallel-safety metadata, and write proposals under the cell `proposals/` directory when they recommend changing metric, constraints, scheme usage, or next work.

## Meta Scientist

Use `bin/ai-lab meta status` to read current system-level analysis state. Use `bin/ai-lab meta analyze` or `bin/ai-lab meta propose` only when intentionally creating local analysis or proposal artifacts.

## Memory

Use `bin/ai-lab memory index` to rebuild the generated SQLite search index. Use `bin/ai-lab memory search <query>` to search Markdown, YAML, and logs.

## Extended Research Runs

If the user explicitly authorizes an extended run with automatic dependency setup, agents may install missing Python dependencies using cell-local or inherited repository-local `uv` workflows. Allowlisted runtime profiles may be ensured with `bin/ai-lab runtime ensure <profile>`; the active profile is `btc-benchmark-python` for benchmark checkout import checks. Agents must not install Node, Docker, connector integrations, credentials, shell configuration, account configuration, or unlisted OS packages silently.

For detached account-level `codex exec` runs, pass account-level flags before `exec` and use `--skip-git-repo-check` when launching from `/Users/sungs`. Known-good pattern:

```sh
codex --ask-for-approval never --search exec --cd /Users/sungs --skip-git-repo-check -
```
