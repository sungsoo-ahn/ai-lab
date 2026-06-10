# System Architecture

The AI Lab stores research state as Markdown, YAML, JSON, and static assets. The public site renders that state as a manual, not as a separate application.

## Agentic Flow

```mermaid
flowchart LR
  L[Lab Policies And Memory] --> T[Task]
  T --> S[Scientist Version]
  S --> W[Work Unit]
  W --> E[Evidence And Artifacts]
  E --> R[Reports And Manuals]
  R --> G[Human Gate]
  G -->|accept / reject / rerun| S
  G -->|accepted proposal| N[Next Scientist Version]
```

## Scientist Loop

```mermaid
sequenceDiagram
  participant State as Scientist State
  participant Planner as Work Unit Planner
  participant Source as Source Checkout
  participant Eval as Experiment Evaluator
  participant Audit as Critic/Auditor
  participant Report as Report Synthesis
  participant Human as Human Reviewer

  State->>Planner: goal, constraints, prior evidence
  Planner->>Source: source_id and immutable git_ref
  Source->>Eval: reproducible code, configs, data contracts
  Eval->>Audit: metrics, trial ledger, artifacts
  Audit->>Report: caveats, negative findings, next actions
  Report->>Human: updated scientist and work-unit manuals
  Human->>State: accept, reject, rerun, or propose next version
```

## Canonical Artifact Types

| Artifact | Purpose | Typical Location |
| --- | --- | --- |
| Task manifest | Broad task state and active scientists. | `tasks/active/<task_id>/task.yaml` |
| Scientist manifest | Versioned scientist goal, metric, constraints, assets, and reports. | `tasks/active/<task_id>/scientists/<scientist_id>/scientist.yaml` |
| Scientist manual | Human-readable operating manual for a scientist. | `docs/scientists/<scientist_id>/` |
| Work-unit manifest | Work-unit scope, method, source refs, and decision state. | `tasks/active/<task_id>/scientists/<scientist_id>/work_units/<work_unit_id>/work-unit.yaml` |
| Work-unit manual | Human-readable operating manual for a work unit. | `docs/scientists/<scientist_id>/work-units/` |
| Source registry | Durable identity and immutable refs for external codebases. | `sources/sources.yaml` |
| Static plot data | Public, curated visualization dataset. | `docs/assets/*.json` |

## Why Static Documentation

The site uses MkDocs, Mermaid, Vega-Lite, and static files because lab members should be able to inspect and edit the manual without running a backend or frontend application. Static documentation is also easier to review, deploy, archive, and reproduce.
