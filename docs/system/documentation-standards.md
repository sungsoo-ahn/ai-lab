# Documentation Standards

AI Lab public docs are hand-maintained summaries for humans and agents. They should explain the current matrix, link to evidence, and avoid exposing local-only execution details.

## Audience Labels

- `human`: written for a user or maintainer.
- `both`: useful to users and agents.
- `agent`: local-only execution material; do not place under `docs/`.

Public documentation should exclude only content that is purely agent-facing or sensitive. A public page may summarize an agent-facing artifact by path, purpose, and evidence value.

## Public Pages

| Page type | Purpose |
| --- | --- |
| Task page | Broad problem, assets, metrics, constraints, and linked cells. |
| Scheme page | Reusable AI scientist orchestration pattern and approval boundaries. |
| Scientist component reference | Skill bundle, research taste, hypothesis, and memory boundaries. |
| Comparable systems reference | External systems and what design lessons they imply for this repo. |
| Evaluation cell brief | Task-by-scheme current state, metric, result, work units, and next step. |
| Work-unit brief | Focused method, result, evidence, and decision. |
| Meta page | System-level analysis state and proposals. |
| Legacy evidence page | Archived reference material and plot assets. |

## Depth Standard

A useful page should answer four questions:

- What is this artifact?
- Why does it exist?
- How does it connect to the rest of the matrix?
- What evidence or command proves the current state?

Short index pages are acceptable, but core concept pages should include enough detail that a new agent can make a safe edit without guessing from YAML alone.

## Update Rules

- Task changes should update `task.yaml` and the public task page.
- Scheme changes should update `scheme.yaml`, `guide.md`, and the public scheme page.
- Skill bundle, research taste, or hypothesis changes should update the relevant catalog file and the scientist component reference when the concept changes.
- Cell changes should update the cell manifest, report, run spec when relevant, public cell brief, and work-unit tables.
- Work-unit changes should update `work-unit.yaml`, `guide.md`, `report.md`, the public work-unit brief, and the owning cell brief.
- Meta analyses should update the meta report or analysis/proposal directories and the public meta page when useful.
- External comparisons should include a source map with source type, relevance, and last-checked date.

## Terminology

Use the vocabulary from [Audience And Terminology](../reference/audience-and-terminology.md). Avoid wording that makes a state summary sound like operating instructions, or makes a scientist scheme sound like a task-specific result.

Preferred distinctions:

- guide: explains how to understand or operate something;
- brief: summarizes current state, evidence, or results;
- manifest: machine-readable state;
- run record: artifacts from one execution;
- work unit: one focused research context.

## Do Not Publish

- Credentials, tokens, private keys, recovery codes, session cookies, or private connector content.
- Long prompt transcripts.
- Raw local logs unless they are intentionally summarized and safe.
- Large generated artifacts that are better referenced by path.
- Purely agent-facing cache, scratch, or source-checkout details.
