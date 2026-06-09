# Activity Log

Use this file for significant local setup, policy, and organization changes.

| Date | Activity | Notes |
| --- | --- | --- |
| 2026-06-09 | Created Codex-native research agent workspace | Initial local-first setup. |
| 2026-06-09 | Added package and update governance | Added Brewfile, uv-first development policy, proposal-first update policy, install checklist, and git ignore rules. |
| 2026-06-09 | Installed lean Homebrew baseline | `brew bundle check` passed; verified Homebrew `uv`, git, gh, rg, fd, jq, yq, shellcheck, shfmt, pre-commit, and Homebrew SQLite. |
| 2026-06-09 | Cleaned redundant setup artifacts | Removed standalone `~/.local/bin/uv`, `~/.local/bin/uvx`, and `/tmp/codex-uv-smoke`; Homebrew `uv` remains first in PATH. Manual `/opt/homebrew` ownership fix still needed for `brew doctor`. |
| 2026-06-09 | Added account-agent launcher | Added `codex-agent` wrapper and put `agent-system/bin` on interactive zsh PATH. |
| 2026-06-09 | Updated account-agent launcher approvals | Added `--ask-for-approval never` to `codex-agent` so sessions started by the wrapper do not prompt for command approval. |
| 2026-06-09 | Scaffolded Slack agent bridge | Added Socket Mode Python service proposal and local `uv` project. `py_compile`, `--help`, and `shellcheck` passed; `uv sync`/`uv lock` could not resolve Slack dependencies because PyPI DNS/network access was blocked in-session. |
| 2026-06-09 | Added `tmux` to Homebrew baseline | Updated `Brewfile`; `brew bundle` could not install `tmux` because `/opt/homebrew` lock/config directories are not writable. Run Homebrew ownership remediation manually, then rerun `brew bundle --file /Users/sungs/agent-system/Brewfile`. |
| 2026-06-09 | Finished Slack agent bridge setup | Slack bridge local verification passed; Slack-side app setup completed by user. |
| 2026-06-09 | Added memory/project/hypothesis system v1 | Added user-facing tutorial/status docs, system memory, project and hypothesis templates, asset registry convention, local command helpers, and BTC project manifests. `py_compile`, command help, indexing, search, and memory audit passed. |
