# Maintenance

Use this checklist before committing AI Lab changes.

## Matrix Consistency

- Active tasks have `task.yaml` and a public task page.
- Active schemes have `scheme.yaml`, `guide.md`, and a public scheme page.
- Active evaluation cells have `evaluation-cell.yaml`, `guide.md`, `report.md`, `run-spec.yaml`, and a public cell brief.
- Cell `active_work_units` and `completed_work_units` match each work-unit manifest.
- Prompt manifests point to existing prompt files inside the run directory.
- Meta scientists have `meta-scientist.yaml`, `guide.md`, `report.md`, and a public meta page.

## Automation

- Validate run specs with `uv run python bin/ai-lab cell run-spec validate --all`.
- Dry-run unattended work with `uv run python bin/ai-lab cell run-all --once --dry-run`.
- Run `uv run python bin/ai-lab docs audit` before building docs.
- Build public docs with `uv run --with-requirements requirements.txt mkdocs build --strict`.

## Boundaries

- Local writes under `ai-lab` are allowed for task, scheme, cell, work-unit, meta, docs, notes, and source-map files unless the user asks for read-only work.
- Connector writes, external submissions, account configuration changes, Docker, Node, and unlisted OS packages require explicit user approval.
- Long-running cells may install missing Python dependencies only through local or inherited `uv` workflows when the user has authorized automatic dependency setup.
