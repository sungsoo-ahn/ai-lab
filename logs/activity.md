# Activity Log

Use this file for significant local setup, policy, and organization changes.

| Date | Activity | Notes |
| --- | --- | --- |
| 2026-06-09 | Created Codex-native research agent workspace | Initial local-first setup. |
| 2026-06-09 | Added package and update governance | Added Brewfile, uv-first development policy, proposal-first update policy, install checklist, and git ignore rules. |
| 2026-06-09 | Installed lean Homebrew baseline | `brew bundle check` passed; verified Homebrew `uv`, git, gh, rg, fd, jq, yq, shellcheck, shfmt, pre-commit, and Homebrew SQLite. |
| 2026-06-09 | Cleaned redundant setup artifacts | Removed standalone `~/.local/bin/uv`, `~/.local/bin/uvx`, and `/tmp/codex-uv-smoke`; Homebrew `uv` remains first in PATH. Manual `/opt/homebrew` ownership fix still needed for `brew doctor`. |
