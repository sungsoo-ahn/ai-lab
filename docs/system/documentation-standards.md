# Documentation Standards

AI Lab public docs are hand-maintained summaries for humans and agents. They should explain the current matrix without exposing local-only execution details.

## Audience Labels

- `human`: written for a user or maintainer.
- `both`: useful to users and agents.
- `agent`: local-only execution material; do not place under `docs/`.

## Public Pages

| Page type | Purpose |
| --- | --- |
| Task page | Broad problem, assets, metrics, constraints, and linked cells. |
| Scheme page | Reusable AI scientist orchestration pattern and approval boundaries. |
| Evaluation cell brief | Task-by-scheme current state, metric, result, work units, and next step. |
| Work-unit brief | Focused method, result, evidence, and decision. |
| Meta page | System-level analysis state and proposals. |
| Legacy evidence page | Archived reference material and plot assets. |

## Update Rules

- Task changes should update `task.yaml` and the public task page.
- Scheme changes should update `scheme.yaml`, `guide.md`, and the public scheme page.
- Cell changes should update the cell manifest, report, run spec when relevant, public cell brief, and work-unit tables.
- Work-unit changes should update `work-unit.yaml`, `guide.md`, `report.md`, the public work-unit brief, and the owning cell brief.
- Meta analyses should update the meta report or analysis/proposal directories and the public meta page when useful.

## Do Not Publish

- Credentials, tokens, private keys, recovery codes, session cookies, or private connector content.
- Long prompt transcripts.
- Raw local logs unless they are intentionally summarized and safe.
