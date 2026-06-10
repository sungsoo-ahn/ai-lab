# Evaluation Matrix

Evaluation cells are the operational units of the AI Lab matrix. Each cell applies one reusable scientist scheme to one task.

## Active Cells

No active evaluation cells are initialized after the matrix refactor.

Create one with:

```sh
bin/ai-lab cell init <task_id>__<scheme_id>__v1 <task_id> <scheme_id>
```

Then define its metric, constraints, run spec, and public brief before running unattended work.
