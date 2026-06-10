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
| 2026-06-09 | Repurposed BTC AutoResearch project as BTC project | Moved active project from `research/active/btc_autoresearch` to `research/active/btc` and treated AutoResearch as the current BTC workstream. |
| 2026-06-09 | Prepared BTC overnight research run | Added overnight run policy, command helper, runbook, work-unit reports, and project status for `overnight-2026-06-09`. Silent Python package installs are allowed for this run through project-local `uv` workflows only. |
| 2026-06-10 | Verified Slack agent bridge prototype | Added unit tests, aligned Codex exec with account approval/search flags, and verified `uv sync`, tests, `py_compile`, and CLI help. |
| 2026-06-10 | Added agent-system dashboard generator | Added a dependency-free Python/`uv` static dashboard, Rowan-inspired CSS, GitHub Pages workflow, and local build docs. Verified build, `py_compile`, link resolution, and generated-output redaction scan. |
| 2026-06-10 | Published tutorial in GitHub Pages output | Added the existing `docs/tutorial.md` to the generated dashboard site and linked it from the Pages navigation. |
| 2026-06-10 | Reframed GitHub Pages home as project page | Shifted the generated home page toward project introduction, workspace purpose, and active project context before the operational status dashboard. |
| 2026-06-10 | Simplified dashboard home hierarchy | Replaced a repeated status block with a four-layer reading guide for projects, work units, evidence, and memory. |
| 2026-06-10 | Clarified project page decisions | Added a project-level current-read and next-step panel, and renamed prominent hypothesis labels to work units. |
| 2026-06-10 | Improved work-unit navigation | Added parent-project links to work-unit pages so individual reports have clearer context and return paths. |
| 2026-06-10 | Polished shared site chrome | Replaced the placeholder brand mark and added a quiet footer explaining the generated public dashboard. |
| 2026-06-10 | Polished source report metadata | Rendered report date and status as compact metadata chips instead of raw Markdown lead-in text. |
| 2026-06-10 | Updated Pages workflow action majors | Moved GitHub Pages workflow actions to current Node 24-compatible major versions to remove Node 20 deprecation noise. |
| 2026-06-10 | Improved empty project sections | Replaced blank work-unit and asset sections with intentional empty states for proposal-stage projects. |
| 2026-06-10 | Curated public activity feed | Filtered dashboard-maintenance entries from the homepage feed so recent changes emphasize research and system work. |
| 2026-06-10 | Polished public status labels | Rendered status values as display labels in badges and metric strips while preserving raw report status values. |
| 2026-06-10 | Polished public evidence labels | Replaced raw report filenames in page metadata and evidence metrics with public-facing labels. |
| 2026-06-10 | Polished homepage metric copy | Replaced internal publication/source-report wording with visitor-facing visibility and report labels. |
| 2026-06-10 | Added per-project and per-hypothesis guide rule | Added `guide.md` as the user-facing guide convention, updated scaffolds/templates/dashboard rendering, and backfilled BTC guides. |
| 2026-06-10 | Reclassified Slack bridge as a service | Moved the Slack bridge proposal under `services/slack-agent-bridge/` and removed it from active research project status. |
| 2026-06-10 | Expanded guide scope to technical explainers | Updated guide policy, templates, scaffolds, and BTC guides so guides explain methods, terminology, assumptions, and decision criteria for unfamiliar users. |
