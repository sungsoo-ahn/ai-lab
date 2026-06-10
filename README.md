# AI Lab Workspace

This directory is the local-first workspace for developing reusable AI scientist schemes and comparing them across tasks.

An AI scientist scheme is a reusable orchestration pattern for agents. An evaluation cell applies one scheme to one task, owns the task-specific metric and run records, and preserves evidence through work units.

The public GitHub Pages site is built with MkDocs Material from `docs/`. It is a static set of system guides, task pages, scientist scheme pages, evaluation-matrix briefs, and meta-scientist notes.

## Layout

- `catalog/`: broad task descriptions and reusable scientist scheme descriptions.
- `tasks/active/`: active task definitions only.
- `schemes/`: reusable AI scientist scheme definitions.
- `evaluations/active/`: active task-by-scheme evaluation cells.
- `meta/active/`: meta-AI scientists that analyze the overall lab.
- `research/templates/`: reusable Markdown/YAML templates.
- `sources/`: source registry plus ignored shared code checkouts.
- `memory/`: durable system memory, source indexes, and history.
- `policies/`: operating rules for research, privacy, connectors, packages, and approvals.
- `logs/`: local activity notes.
- `docs/`: MkDocs public documentation.
- `reports/system-status.md`: current system status.
- `bin/ai-lab`: canonical AI Lab helper.

## Layer Model

1. Lab: shared catalogs, policies, memory, logs, and scheme knowledge.
2. Task: a broad, under-specified challenge or dataset family.
3. Scheme: a reusable AI scientist orchestration pattern.
4. Evaluation cell: one task-by-scheme application with a concrete metric, run spec, constraints, and evidence.
5. Work unit: a minimal context for one method, ablation, audit, observation, proxy, synthesis, or infrastructure pass.
6. Meta scientist: an analysis/proposal layer for improving the overall lab system.

## Self-Evolution

Work units can propose changes to a cell's target metric, constraints, scheme usage, or next iteration. Accepted proposals are applied by creating a new evaluation-cell version; current cell metrics are not silently mutated in place.

The meta scientist can analyze the overall matrix and write proposals, but it does not mutate tasks, schemes, cells, metrics, or run specs automatically.

## Common Commands

```sh
bin/ai-lab task status btc_benchmark
bin/ai-lab scheme list
bin/ai-lab meta status
uv run python bin/ai-lab cell run-spec validate --all
uv run python bin/ai-lab cell run-all --continuous --dry-run
bin/ai-lab work-unit status <cell_id> <work_unit_id>
bin/ai-lab source status btc_benchmark
bin/ai-lab docs audit
bin/ai-lab memory index
bin/ai-lab memory search btc
bin/ai-lab memory audit
```

## Starting Codex

Use `codex-lab` to start a new session with the account AI Lab prompt and `/Users/sungs` as the working root.

```sh
codex-lab 'Use AI Lab to continue the evaluation matrix.'
```

## Documentation Site

The site is static and deploys to GitHub Pages from the `main` branch.

Install and preview with `uv`:

```sh
uv run --with-requirements requirements.txt mkdocs serve
```

Build locally:

```sh
bin/ai-lab docs audit
uv run --with-requirements requirements.txt mkdocs build
```

Fallback without `uv`:

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
mkdocs serve
```

Deployment uses `.github/workflows/pages.yml`. Push to `main`, then enable GitHub Pages with GitHub Actions as the source if it is not already enabled.

To add or update public documentation, edit the relevant system guide, task page, scheme page, evaluation cell brief, work-unit brief, or meta page under `docs/`. Exact LLM prompts live under evaluation-cell run directories, not under `docs/`.

## Overnight And Runtime Automation

For overnight-scale evaluation work, start from `research/templates/overnight-goal.md` and keep run-specific details in the cell `runs/` directory. Authorized long runs may install missing Python dependencies through local `uv` workflows and may use allowlisted runtime profiles such as `btc-benchmark-python`.

For rigid unattended operation, every active evaluation cell should define `run-spec.yaml`. The run spec is the machine-readable contract for source gates, fixed preflight commands, fixed cycle commands, synthesis commands, timeouts, artifacts, and exit conditions. Validate and dry-run specs before running them:

```sh
uv run python bin/ai-lab cell run-spec validate --all
uv run python bin/ai-lab cell run-all --dry-run --once
```

Runtime profiles are checked or installed with:

```sh
bin/ai-lab runtime check btc-benchmark-python --repo sources/checkouts/btc_benchmark
bin/ai-lab runtime ensure btc-benchmark-python --repo sources/checkouts/btc_benchmark
```

Runtime installs are still bounded by `policies/update-policy.md` and `policies/evaluation-runtime-policy.md`; connector writes, account configuration, Docker, Node, and unlisted OS packages still require explicit approval.
