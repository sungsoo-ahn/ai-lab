# System Guide

The AI Lab is organized to compare reusable AI scientist schemes across tasks.

## Principles

- Tasks describe broad challenge or dataset families.
- Scientist schemes describe reusable orchestration patterns.
- Skill bundles describe reusable capabilities.
- Research taste profiles describe prioritization and judgment.
- Hypotheses describe task-specific claims to test.
- Evaluation cells apply one scheme to one task and own metrics, run specs, work units, prompts, and evidence.
- Work-unit proposals create new cell versions instead of silently mutating current metrics or constraints.
- The meta scientist analyzes the matrix and proposes lab improvements; it does not edit the system automatically.

## Current Directories

| Directory | Purpose |
| --- | --- |
| `tasks/active/` | Active task definitions. |
| `schemes/` | Reusable AI scientist scheme definitions. |
| `catalog/skill-bundles.yaml` | Reusable scientist capabilities. |
| `catalog/research-tastes.yaml` | Scientist judgment profiles. |
| `catalog/hypotheses.yaml` | Task-specific claims under consideration. |
| `evaluations/active/` | Task-by-scheme operational cells. |
| `meta/active/` | Meta-AI scientist analyses and proposals. |

## Related Guides

- [Architecture](architecture.md)
- [Prompt Provenance](prompt-provenance.md)
- [Maintenance](maintenance.md)
- [Documentation Standards](documentation-standards.md)
