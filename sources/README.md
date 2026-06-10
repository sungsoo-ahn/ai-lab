# Source Registry

This directory tracks optimized codebases by immutable git reference.

- `sources.yaml`: durable source metadata and current approved refs.
- `checkouts/`: ignored shared materialized clones used for local experiments.

Work units should record source refs instead of copying code into their folders.
Large generated data, virtualenvs, ledgers, and scratch results may stay beside a
shared checkout. Durable summaries and result pointers belong under the relevant
scientist, run, or work-unit report.
