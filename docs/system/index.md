# System Manual

This manual describes how the AI Lab as a whole is maintained. It is for users, developers, and maintainers who need to understand the system without first reading the repository layout.

## System Purpose

The AI Lab is a local-first workspace for developing AI scientists. An AI scientist is an orchestration layer for agents that tackles hard, uncertain work by proposing work units, running bounded investigations, preserving evidence, and evolving only through explicit proposals.

## System Layers

| Layer | Responsibility | Current Example |
| --- | --- | --- |
| Lab | Shared policies, memory, source registry, catalogs, logs, and documentation standards. | This MkDocs site and the AI Lab workspace. |
| Task | Broad challenge or dataset family. | `btc` |
| Scientist | Versioned research scheme with a goal, target metric, constraints, assets, reports, and proposal history. | `btc_autoresearch_v1` |
| Work unit | Smallest auditable unit of work: metric optimization, audit, observation, ablation, synthesis, proxy, or infrastructure pass. | `baseline_reproduction`, `pipeline_audit`, `horizon_h4_audit`, `regime_filter_probe`, `report_synthesis` |

## Maintainer Contract

- The manual must explain the system well enough that a reader does not need to inspect the repo to understand agent behavior or decisions.
- Repository paths may appear as provenance and implementation references.
- Secrets, credentials, API keys, tokens, private connector content, and unnecessary personal data must not appear in manuals.
- Scientists and work units are hand-maintained documents. Templates and checklists keep shape consistent, but each page may specialize for its actual work.
- Work-unit proposals must not silently mutate a current scientist target metric. Accepted proposals create a new scientist version.

## Current System State

| Area | Status |
| --- | --- |
| Active task | `btc` |
| Active scientist | `btc_autoresearch_v1` |
| Public site | MkDocs Material, deployed to GitHub Pages |
| Static visualization | Vega-Lite from CDN using `docs/assets/btc-trials.json` |
| Diagram format | Mermaid in Markdown |
| Runtime policy | Prefer Python and `uv`; do not introduce Node or Docker by default |

## Main Manuals

- [Architecture](architecture.md)
- [Maintenance](maintenance.md)
- [Documentation Standards](documentation-standards.md)
- [BTC AutoResearch v1](../scientists/btc-autoresearch-v1/index.md)
- [BTC Work Units](../work-units/index.md)
