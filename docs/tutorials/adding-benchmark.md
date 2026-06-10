# Adding A Benchmark Or Scientist

Use this pattern when a new task needs static documentation and inspectable results.

## 1. Create The Scientist Files

Add or update the canonical workspace files under `tasks/active/<task_id>/scientists/<scientist_id>/`:

- `scientist.yaml`
- `guide.md`
- `report.md`
- `assets.yaml`
- `work_units/<work_unit_id>/work-unit.yaml`
- `work_units/<work_unit_id>/report.md`

The Markdown and YAML files remain the source of truth. The public site should summarize them rather than invent a separate research record.

## 2. Define A Workflow Asset

Create a static workflow YAML file under `docs/assets/` if the workflow is useful for readers. Keep it small enough to edit by hand.

```yaml
workflow_id: example_scientist_loop_v1
description: Example scientist workflow.
nodes:
  - id: planner
    type: agent
    label: Work Unit Planner
  - id: evaluator
    type: tool
    label: Experiment Evaluator
edges:
  - from: planner
    to: evaluator
    artifact: work-unit.yaml
```

## 3. Add Score Trials As Static JSON

Use a curated static JSON file for plotted score-search trials. Include enough metadata for hover inspection.

```json
{
  "trial_id": "t001_example",
  "parent_trial_id": null,
  "method": "example_method",
  "benchmark": "example_benchmark",
  "gpu_hours": 0.25,
  "net_return": 0.12,
  "sharpe": 0.4,
  "max_drawdown": -0.2,
  "score": 0.8,
  "success_rate": 0.5,
  "status": "needs_refinement",
  "hypothesis": "Short statement of the tested idea.",
  "config_snippet": "Compact settings.",
  "raw_text_snippet": "Short trace or report excerpt.",
  "metric_delta": "Change relative to baseline.",
  "run_page": "../trials/trial_t001/"
}
```

## 4. Create Reader Pages

Add:

- A tutorial page that explains the benchmark.
- A workflow page with Mermaid diagrams.
- Trial detail pages for important examples.
- Work-unit summaries for audits, synthesis, and negative findings.

Update `mkdocs.yml` only for pages that should appear in the main navigation.

## 5. Build And Check

```sh
uv run --with-requirements requirements.txt mkdocs build
```

Confirm that JSON paths resolve from the built tutorial page and that Mermaid diagrams render.
