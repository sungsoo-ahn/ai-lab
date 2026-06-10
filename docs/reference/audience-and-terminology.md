---
audience: human
publish: public
---

# Audience And Terminology

AI Lab content is organized by who should read it and what decision it supports.

## Audience Labels

| Label | Meaning | Public docs? |
| --- | --- | --- |
| `human` | Written for users, maintainers, or reviewers. | Yes |
| `both` | Useful to humans and agents. | Yes, if non-sensitive |
| `agent` | Operational instructions, prompts, logs, caches, or machine-only state. | No |

Public documentation should exclude only content that is purely agent-facing or sensitive. It may summarize agent-facing artifacts by path and purpose.

## Preferred Terms

| Use | Avoid |
| --- | --- |
| System Guide | System Manual |
| Scientist Brief | Scientist Manual |
| Work Unit Brief | Work-Unit Manual |
| Run Record | raw run dump |
| Agent Instructions | user guide for agent-only steps |
| State Manifest | YAML report |

## File Roles

| File or directory | Role |
| --- | --- |
| `docs/` | Public human-facing or mixed audience documentation. |
| `tasks/active/.../report.md` | Local current-state evidence summary, usually both-facing. |
| `tasks/active/.../guide.md` | Local continuation guide, usually both-facing. |
| `tasks/active/.../run-spec.yaml` | Agent-facing execution contract, summarized publicly when useful. |
| `tasks/active/.../runs/` | Local run records, logs, prompts, and outputs. |

When a page describes current state or results, call it a brief. Reserve guide for how to operate or understand the system.
