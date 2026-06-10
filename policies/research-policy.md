# Research Policy

## Default Output

Research tasks should produce a concise brief with findings, a source map, confidence, open questions, and reusable local notes when appropriate.

## Source Handling

Prefer primary sources, official documentation, source documents, academic papers, filings, standards, or direct data providers. Use secondary sources for context, discovery, or when primary sources are unavailable.

When information may have changed recently, verify it against current sources before answering. Record source links or connector references clearly enough that the finding can be checked later.

## Evidence Quality

Separate facts from inference. Note weak evidence, conflicts between sources, missing dates, or unclear provenance. Avoid turning a single weak source into a strong conclusion.

## Rigid Evaluation Operation

Unattended or recurring evaluation-cell work should run through a validated `run-spec.yaml`. The run spec must declare source gates, fixed commands, timeouts, artifacts, synthesis behavior, and exit conditions before the loop is started.

## Local Files

Use `tasks/active/` for current task definitions, `schemes/` for reusable schemes, `evaluations/active/` for current task-by-scheme cells, and `meta/active/` for meta-scientist analyses. Add durable, reusable facts to `memory/` only when they are likely to matter again and do not contain secrets.
