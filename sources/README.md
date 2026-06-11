# Source Registry

This directory tracks optimized codebases by immutable git reference.

- `sources.yaml`: durable source metadata and current approved refs.
- `checkouts/`: ignored shared materialized clones used for local experiments.

Task runs should record source refs instead of copying external source code into
task folders. Large generated data, virtualenvs, ledgers, and scratch results may
stay beside a shared checkout. Durable source-backed state belongs in canonical
task metadata or generated public docs, not ignored experiment logs.
