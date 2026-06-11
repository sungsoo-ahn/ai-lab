# Runtime Policy

This policy covers runtime support packages and environment checks needed by task-local AI scientist loops.

## Python Dependencies

When the user explicitly authorizes a run or dependency change, agents may use local or inherited `uv` workflows such as `uv sync`, `uv add`, and `uv run`.

## OS Packages

Only allowlisted runtime support may be installed without a new approval. Docker, Node, connector integrations, credentials, shell configuration, account configuration, and unlisted OS packages require explicit approval.

## Evidence

Record runtime changes and verification results in the relevant task report or run summary. Do not hide dependency drift in raw logs only.

