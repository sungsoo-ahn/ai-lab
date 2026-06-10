---
id: system-procedures
type: system_memory
created_at: 2026-06-09
updated_at: 2026-06-09
confidence: high
sensitivity: public
status: active
links:
  - /Users/sungs/agent-system/policies/update-policy.md
  - /Users/sungs/agent-system/docs/tutorial.md
---

# System Procedures

## Research Projects

Use `bin/agent-project init <project_id>` to create a project. Use `bin/agent-project restart <project_id>` to archive the current active state and create a clean restarted workspace.

Every project must include a user-facing `guide.md`. The guide should explain, in plain language, how to read the project, where the current report/source map/assets live, what is safe to change, and how to restart or continue the work.

## Hypotheses

Use `bin/agent-hypothesis init <project_id> <hypothesis_id>` to create a hypothesis workspace. Hypotheses should reference project assets by `asset_id`.

Every hypothesis must include a user-facing `guide.md`. The guide should explain the work unit from scratch, point to its report, evidence, runs, and memory, and state the safe next action for a returning user or agent.

## Memory

Use `bin/agent-memory index` to rebuild the generated SQLite search index. Use `bin/agent-memory search <query>` to search Markdown, YAML, and logs.

## Self-Evolution

Low-risk local memory, report, template, and index updates may be applied inside `/Users/sungs/agent-system`. Package, runtime, shell, connector, account config, and out-of-zone changes require explicit approval and must follow update policy.

## Overnight Research Runs

If the user explicitly authorizes an overnight run with silent package installs, agents may install missing Python project dependencies using project-local `uv` workflows. They must not install Homebrew, Node, Docker, system packages, connector integrations, or account configuration silently.

For detached account-level `codex exec` runs, pass account-level flags before `exec` and use `--skip-git-repo-check` when launching from `/Users/sungs`. Known-good pattern:

```sh
codex --ask-for-approval never --search exec --cd /Users/sungs --skip-git-repo-check -
```
