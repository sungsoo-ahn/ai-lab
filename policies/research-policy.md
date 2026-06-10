# Research Policy

## Default Output

Research tasks should produce a concise brief with:

- answer or findings;
- source map;
- confidence and open questions;
- reusable local notes when appropriate.

## Source Handling

Prefer primary sources, official documentation, source documents, academic papers, filings, standards, or direct data providers. Use secondary sources for context, discovery, or when primary sources are unavailable.

When information may have changed recently, verify it against current sources before answering. Record source links or connector references clearly enough that the finding can be checked later.

## Evidence Quality

Separate facts from inference. Note weak evidence, conflicts between sources, missing dates, or unclear provenance. Avoid turning a single weak source into a strong conclusion.

## Rigid Scientist Operation

Unattended or recurring scientist work should run through a validated `run-spec.yaml`. The run spec must declare source gates, fixed commands, timeouts, artifacts, synthesis behavior, and exit conditions before the loop is started.

## Local Files

Use `tasks/active/` for current task, scientist, and work-unit state, and `archive/` for completed or superseded packages. Add durable, reusable facts to `memory/` only when they are likely to matter again and do not contain secrets.
