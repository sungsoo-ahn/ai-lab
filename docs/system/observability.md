# W&B Observability

Normal AI scientist runs require W&B/Weave observability. The repo default target is configured in `lab.yaml`:

```yaml
observability:
  provider: wandb_weave
  entity: sungsoo-ahn
  project: ai-lab
  required: true
  payload: full_trace
```

Configure credentials outside Git:

```bash
wandb login
# or
export WANDB_API_KEY=...
```

The runner logs run starts, source gate state, prompts, command metadata, command outputs, declared artifacts, failures, and finish status. Secret-like environment values are redacted before logging.

Each local run directory also contains `run-summary.md`, `events.jsonl`, command logs, the loop snapshot, and task-local launcher output when launched through `tasks/<task_id>/bin/`.

Dry-runs and tests may opt out explicitly with `--dry-run`, `--no-wandb`, or `AI_LAB_DISABLE_WANDB=1`.
