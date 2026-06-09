# Development Policy

## Package Ownership

- Homebrew owns OS-level CLI tools.
- `uv` owns Python projects, Python environments, and Python CLI tools.
- Project dependencies belong in project manifests and lockfiles.
- Global installs require a documented reason.

## Python

New Python work must use:

- `pyproject.toml` for project metadata and dependencies;
- `uv.lock` for reproducible dependency resolution;
- `uv sync` for environment setup;
- `uv run` for commands;
- `uv tool install` or `uvx` for Python CLIs.

Do not install packages into Apple system Python. Avoid direct `pip`, manual `venv`, Poetry, Pipenv, and Conda unless maintaining an inherited project that already uses them.

## JavaScript And TypeScript

Do not install Node globally by default. Add Node only when a concrete project needs frontend, TypeScript, or MCP tooling. Prefer a per-project version manager when Node is introduced.

## Containers

Do not install Docker Desktop by default. Add container tooling only when a project, service, or sandboxing workflow justifies the footprint and permissions.

## Shell And Configuration

Keep shell startup changes minimal and documented. Prefer reproducible manifests over one-off install commands. Validate shell scripts with `shellcheck` and format with `shfmt` when scripts are part of maintained tooling.

