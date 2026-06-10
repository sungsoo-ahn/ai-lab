Use the account agent setup. Read ~/AGENTS.md and continue from ~/agent-system.

/goal Run the overnight BTC research orchestration for active project `btc`.

Read:
- /Users/sungs/agent-system/research/active/btc/project.md
- /Users/sungs/agent-system/research/active/btc/project.yaml
- /Users/sungs/agent-system/research/active/btc/assets.yaml
- /Users/sungs/agent-system/research/active/btc/task.md
- /Users/sungs/agent-system/research/active/btc/overnight-runbook.md

Operate as the orchestration agent. Use hypothesis/work-unit folders under `/Users/sungs/agent-system/research/active/btc/hypotheses`. First complete the readiness and baseline-reproduction gate. If missing Python dependencies block progress, install them silently with project-local uv workflows and record the exact command. Do not install Homebrew, Node, Docker, connector integrations, shell config, or account config silently.

After baseline status is known, run bounded work units. Preserve failed trials, never touch sealed holdout during research, never place live orders or use private API keys, and never weaken accounting/cost/timestamp/split rules to improve results.

Before stopping, update `/Users/sungs/agent-system/research/active/btc/report.md`, each work-unit report, and the active overnight summary under `/Users/sungs/agent-system/research/active/btc/runs`.
