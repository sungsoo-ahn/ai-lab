# Activity Log

Use this file for significant local setup, policy, and organization changes.

| Date | Activity | Notes |
| --- | --- | --- |
| 2026-06-09 | Created Codex-native research agent workspace | Initial local-first setup. |
| 2026-06-09 | Added package and update governance | Added Brewfile, uv-first development policy, proposal-first update policy, install checklist, and git ignore rules. |
| 2026-06-09 | Installed lean Homebrew baseline | `brew bundle check` passed; verified Homebrew `uv`, git, gh, rg, fd, jq, yq, shellcheck, shfmt, pre-commit, and Homebrew SQLite. |
| 2026-06-09 | Cleaned redundant setup artifacts | Removed standalone `~/.local/bin/uv`, `~/.local/bin/uvx`, and `/tmp/codex-uv-smoke`; Homebrew `uv` remains first in PATH. Manual `/opt/homebrew` ownership fix still needed for `brew doctor`. |
| 2026-06-09 | Added account-agent launcher | Added `codex-lab` wrapper and put `ai-lab/bin` on interactive zsh PATH. |
| 2026-06-09 | Updated account-agent launcher approvals | Added `--ask-for-approval never` to `codex-lab` so sessions started by the wrapper do not prompt for command approval. |
| 2026-06-09 | Scaffolded Slack agent bridge | Added Socket Mode Python service proposal and local `uv` project. `py_compile`, `--help`, and `shellcheck` passed; `uv sync`/`uv lock` could not resolve Slack dependencies because PyPI DNS/network access was blocked in-session. |
| 2026-06-09 | Added `tmux` to Homebrew baseline | Updated `Brewfile`; `brew bundle` could not install `tmux` because `/opt/homebrew` lock/config directories are not writable. Run Homebrew ownership remediation manually, then rerun `brew bundle --file /Users/sungs/ai-lab/Brewfile`. |
| 2026-06-09 | Finished Slack agent bridge setup | Slack bridge local verification passed; Slack-side app setup completed by user. |
| 2026-06-09 | Added memory/project/hypothesis system v1 | Added user-facing tutorial/status docs, system memory, project and hypothesis templates, asset registry convention, local command helpers, and BTC project manifests. `py_compile`, command help, indexing, search, and memory audit passed. |
| 2026-06-09 | Repurposed BTC AutoResearch project as BTC project | Moved active project from `research/active/btc_autoresearch` to `research/active/btc` and treated AutoResearch as the current BTC workstream. |
| 2026-06-09 | Prepared BTC overnight research run | Added overnight run policy, command helper, runbook, work-unit reports, and project status for `overnight-2026-06-09`. Silent Python package installs are allowed for this run through project-local `uv` workflows only. |
| 2026-06-10 | Verified Slack agent bridge prototype | Added unit tests, aligned Codex exec with account approval/search flags, and verified `uv sync`, tests, `py_compile`, and CLI help. |
| 2026-06-10 | Added ai-lab dashboard generator | Added a dependency-free Python/`uv` static dashboard, Rowan-inspired CSS, GitHub Pages workflow, and local build docs. Verified build, `py_compile`, link resolution, and generated-output redaction scan. |
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
| 2026-06-10 | Migrated workspace to AI Lab | Renamed the workspace concept and local path to `/Users/sungs/ai-lab`, added task/scientist/work-unit manifests, migrated BTC to `tasks/active/btc/scientists/btc_autoresearch_v1`, and kept compatibility wrappers/symlinks for old agent-system commands and paths. |
| 2026-06-10 | Renamed GitHub repo to AI Lab | Renamed the GitHub repository from `agent-system` to `ai-lab`, updated the local `origin`, and removed the local `/Users/sungs/agent-system` compatibility symlink. |
| 2026-06-10 | Expanded guide scope to technical explainers | Updated guide policy, templates, scaffolds, and BTC guides so guides explain methods, terminology, assumptions, and decision criteria for unfamiliar users. |
| 2026-06-10 | Added source-ref registry | Moved optimized BTC code to an ignored shared checkout under `sources/checkouts`, added `sources/sources.yaml`, and updated BTC work units to depend on immutable git refs instead of duplicated codebases. |
| 2026-06-10 | Replaced Pages dashboard with MkDocs manual | Added a MkDocs Material AI Lab Manual with BTC trial plots, Mermaid workflows, static JSON/YAML assets, and a GitHub Pages workflow that deploys `site/`. Verified with `uv run --with-requirements requirements.txt mkdocs build --strict`. |
| 2026-06-10 | Removed obsolete dashboard generator | Migrated the old dashboard's system, scientist, and work-unit report content into MkDocs pages, then removed the tracked `dashboard/` generator and local ignored dashboard artifacts. |
| 2026-06-10 | Reorganized MkDocs into manuals | Refactored public documentation into System, Scientist, and Work Unit manual families, folded tutorial/workflow/trial content into the BTC scientist and work-unit manuals, and added documentation standards/checklists for hand-maintained manuals. |
| 2026-06-10 | Cleaned AI Lab manual maintenance drift | Kept work-unit manuals linked from scientist pages instead of global nav, closed completed BTC work-unit manifests, refreshed stale manual references, and preserved backwards-compatible plot hooks. |
| 2026-06-10 | Added documentation audit protocol | Added `bin/ai-lab docs audit` to check static assets, Markdown links, scientist manuals, work-unit manuals, and manifest/report status consistency before GitHub Pages builds. |
| 2026-06-10 | Generalized manual and added prompt provenance | Reworked the public manual around the AI Lab system first, made BTC the worked example, added local prompt artifact conventions, and backfilled the BTC overnight orchestration prompt. |
| 2026-06-10 | Started BTC benchmark scientist v2 | Registered `btc_benchmark` and `btc_agentic_system`, repaired the local referee data package from lineage, verified referee tests (`131 passed, 1 skipped`), and found a gated dependency-light EMA-regime candidate with `+260.5%` dev net and Sharpe `1.295`. |
| 2026-06-10 | Promoted BTC benchmark EMA candidate | Screened 1,296 EMA-regime variants, gated the top 8, and promoted `BestEmaRegimeV2` with `+324.3%` dev net, Sharpe `1.453`, max drawdown `-25.1%`, all 14 default gates passing, and exhaustive future-perturbation passing with at least 2,160 cutoffs per fold. |
| 2026-06-10 | Added overnight runtime automation | Added `libomp` to the Brewfile, `policies/scientist-runtime-policy.md`, `bin/ai-lab runtime check/ensure xgboost-macos`, overnight goal/runtime templates, and missing BTC benchmark public manuals. After `libomp` was installed, `runtime check xgboost-macos` passed and `XgbMomentum` scored `+53.3%` with a transient `scikit-learn` uv overlay. |
| 2026-06-10 | Added rigid scientist runner | Added uv-managed PyYAML tooling, fixed `run-spec.yaml` contracts for both active scientists, runner validation/dry-run/execution/synthesis commands, tests, and documentation. Verified run-spec validation, dry-run, pytest, docs audit, and MkDocs strict build. |
