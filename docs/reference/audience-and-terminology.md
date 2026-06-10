---
audience: human
publish: public
---

# Audience And Terminology

AI Lab content is organized by audience and by layer in the matrix.

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
| Scientist Scheme | task-specific scientist |
| Evaluation Cell | scientist version |
| Evaluation Cell Brief | Scientist Manual |
| Work Unit Brief | Work-Unit Manual |
| Run Record | raw run dump |
| Agent Instructions | user guide for agent-only steps |
| State Manifest | YAML report |
| Meta Scientist | meta-analysis notes |

## File Roles

| File or directory | Role |
| --- | --- |
| `docs/` | Public human-facing or mixed-audience documentation. |
| `tasks/active/<task_id>/task.yaml` | Task definition and constraints. |
| `scientists/schemes/<scheme_id>/scheme.yaml` | Reusable scientist scheme definition. |
| `evaluations/active/<cell_id>/evaluation-cell.yaml` | Task-by-scheme operational state. |
| `evaluations/active/<cell_id>/run-spec.yaml` | Agent-facing execution contract, summarized publicly when useful. |
| `evaluations/active/<cell_id>/runs/` | Local run records, logs, prompts, and outputs. |
| `meta/active/<meta_id>/` | System-level analyses and proposals. |

When a page describes current state or results, call it a brief. Reserve guide for how to operate or understand the system.
