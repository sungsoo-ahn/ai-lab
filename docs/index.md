# AI Lab

AI Lab is a local-first workspace for comparing reusable AI scientist schemes across tasks.

The system is organized as a matrix:

| Layer | Question | Local source |
| --- | --- | --- |
| Task | What challenge or dataset family is being attempted? | `tasks/active/<task_id>/task.yaml` |
| Scientist scheme | What reusable orchestration pattern is being applied? | `schemes/<scheme_id>/scheme.yaml` |
| Evaluation cell | What happened when one scheme was applied to one task? | `evaluations/active/<cell_id>/evaluation-cell.yaml` |
| Work unit | What focused method, audit, proxy, or synthesis pass produced evidence? | `evaluations/active/<cell_id>/work_units/<work_unit_id>/` |
| Meta scientist | What should improve about the overall lab? | `meta/active/ai_lab_meta_v1/` |

## Current State

The active workspace keeps one benchmark task, reusable schemes, and evaluation cells. Old non-benchmark material, old run history, optional integrations, and legacy plot assets are removed from the tracked tree.

## Start Here

1. Read the [System Guide](system/index.md).
2. Review active [Tasks](tasks/index.md).
3. Review reusable [Scientist Schemes](schemes/index.md).
4. Use the [Evaluation Matrix](evaluations/index.md) to compare task-by-scheme cells.
5. Check [Meta Scientist](meta/ai-lab-meta-v1.md) for system-improvement analysis.
