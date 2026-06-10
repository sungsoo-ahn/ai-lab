# System Maintenance

This page describes routine maintenance of the AI Lab public docs and site.

## Local Preview

Use `uv` from the repository root:

```sh
uv run --with-requirements requirements.txt mkdocs serve
```

Build locally:

```sh
uv run --with-requirements requirements.txt mkdocs build --strict
```

The generated `site/` directory is a build artifact and is not committed.

## Documentation Audit

Run the AI Lab documentation audit before publishing changes:

```sh
bin/ai-lab docs audit
```

The audit checks that:

- static JSON assets parse;
- prompt manifests point at existing local prompt files;
- Markdown links under `docs/` resolve locally;
- active scientists have public scientist briefs;
- every work unit has `work-unit.yaml`, `guide.md`, `report.md`, and a linked public work-unit brief;
- `active_work_units` and `completed_work_units` match the statuses in each work-unit manifest;
- work-unit report status lines match their manifests.

## Deployment

GitHub Pages deploys from `.github/workflows/pages.yml` on pushes to `main`.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs `requirements.txt`.
4. Runs `python bin/ai-lab docs audit`.
5. Runs `mkdocs build --strict`.
6. Uploads `site/` to GitHub Pages.

## Package And Runtime Rules

- Use Homebrew for OS-level tools and keep the approved baseline in `Brewfile`.
- Use `uv` for Python project, environment, and command execution.
- Do not install packages into Apple system Python.
- Authorized overnight or long-running scientist runs may install missing Python dependencies through local `uv` workflows.
- Allowlisted runtime profiles may install narrow Homebrew runtime support through `bin/ai-lab runtime ensure <profile>`. The current `xgboost-macos` profile installs `libomp` for XGBoost.
- Do not add Node, Docker, connector integrations, shell/account configuration, or a backend service unless a concrete scientist or workflow requires it and an update proposal is accepted.
- Before package, runtime, connector, or account configuration changes, follow `policies/update-policy.md`.

## Privacy And Connector Rules

- Never store credentials, API keys, tokens, passwords, private keys, recovery codes, or session cookies in public docs, reports, memory, or logs.
- Connector reads should be targeted and minimal.
- Connector writes always require explicit user approval.
- Local writes under `ai-lab` are allowed for public docs, scientist state, work-unit state, notes, and source maps unless the user asks for read-only work.

## Maintenance Checklist

- Run `mkdocs build --strict` before committing site changes.
- Run `bin/ai-lab docs audit` before committing system, scientist, work-unit, or public brief changes.
- Run `bin/ai-lab runtime check <profile>` before a long run when a known runtime such as XGBoost is expected.
- Record important LLM prompts with `bin/ai-lab prompt record` and reference the prompt manifest from the relevant run, scientist, or work-unit page.
- Confirm new guides and briefs are linked from the relevant System or Scientist index. Work-unit briefs should be linked from their owning scientist brief instead of listed in the global navigation.
- Confirm pages explain behavior and decisions directly instead of only pointing to implementation files.
- Confirm implementation paths are accurate when used as provenance.
- Confirm static JSON/YAML assets validate if edited.
- Add a short entry to `logs/activity.md` for significant system documentation or deployment changes.
