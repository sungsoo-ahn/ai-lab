# System Maintenance

This page describes routine maintenance of the AI Lab manual and site.

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

## Deployment

GitHub Pages deploys from `.github/workflows/pages.yml` on pushes to `main`.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs `requirements.txt`.
4. Runs `mkdocs build --strict`.
5. Uploads `site/` to GitHub Pages.

## Package And Runtime Rules

- Use Homebrew for OS-level tools and keep the approved baseline in `Brewfile`.
- Use `uv` for Python project, environment, and command execution.
- Do not install packages into Apple system Python.
- Do not add Node, Docker, or a backend service unless a concrete scientist or workflow requires it and an update proposal is accepted.
- Before package, runtime, connector, or account configuration changes, follow `policies/update-policy.md`.

## Privacy And Connector Rules

- Never store credentials, API keys, tokens, passwords, private keys, recovery codes, or session cookies in manuals, reports, memory, or logs.
- Connector reads should be targeted and minimal.
- Connector writes always require explicit user approval.
- Local writes under `ai-lab` are allowed for manuals, scientist state, work-unit state, notes, and source maps unless the user asks for read-only work.

## Maintenance Checklist

- Run `mkdocs build --strict` before committing site changes.
- Confirm new manuals are linked from the relevant System or Scientist index. Work-unit manuals should be embedded under their owning scientist.
- Confirm pages explain behavior and decisions directly instead of only pointing to implementation files.
- Confirm implementation paths are accurate when used as provenance.
- Confirm static JSON/YAML assets validate if edited.
- Add a short entry to `logs/activity.md` for significant system documentation or deployment changes.
