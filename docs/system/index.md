# System Guide

The AI Lab is organized to compare reusable AI scientist schemes across tasks.

## Principles

- Tasks describe broad challenge or dataset families.
- Scientist schemes describe reusable orchestration patterns.
- Evaluation cells apply one scheme to one task and own metrics, run specs, work units, prompts, and evidence.
- Work-unit proposals create new cell versions instead of silently mutating current metrics or constraints.
- The meta scientist analyzes the matrix and proposes lab improvements; it does not edit the system automatically.

## Current Directories

| Directory | Purpose |
| --- | --- |
| `tasks/active/` | Active task definitions. |
| `scientists/schemes/` | Reusable AI scientist scheme definitions. |
| `evaluations/active/` | Task-by-scheme operational cells. |
| `meta/active/` | Meta-AI scientist analyses and proposals. |
| `archive/legacy/` | Preserved legacy work used for reference and plots. |

## Related Guides

- [Architecture](architecture.md)
- [Prompt Provenance](prompt-provenance.md)
- [Maintenance](maintenance.md)
- [Documentation Standards](documentation-standards.md)
