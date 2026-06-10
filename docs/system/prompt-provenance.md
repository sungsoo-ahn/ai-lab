# Prompt Provenance

Exact prompts are local evidence. Public docs may summarize them, but should not duplicate long prompt text.

## Storage

Cell run prompts live under:

```text
evaluations/active/<cell_id>/runs/<run_id>/prompts/<prompt_id>.md
```

Each run should also keep:

```text
evaluations/active/<cell_id>/runs/<run_id>/prompt-manifest.yaml
```

The manifest records prompt IDs, paths, source, sensitivity, and related work units.

## Recording Prompts

```sh
bin/ai-lab prompt record <cell_id> <run_id> <prompt_id> \
  --from-file prompt.md \
  --source codex \
  --sensitivity local \
  --work-unit <work_unit_id>
```

Use `--force` only when deliberately replacing an incorrectly recorded prompt.

## Public Docs

Public task, scheme, evaluation, work-unit, and meta pages should summarize:

- what instruction pattern was used;
- which run directory holds the exact prompt;
- whether the prompt contains local-only details;
- what evidence the prompt produced.

Do not publish secrets, credentials, private connector content, or long local prompt transcripts.
