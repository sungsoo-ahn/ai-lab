# Update Policy

Updates should keep the repo small and understandable.

## Dependency Updates

Use `uv` for Python dependencies. Record why the dependency is needed when it affects task execution or observability.

## Task Updates

Task changes should update the relevant `task.yaml`, reports, docs page, and tests when behavior changes. Raw run output should remain under ignored `tasks/<task_id>/runs/`.

## Approval Boundaries

Connector writes, external submissions, account configuration, Docker, Node, credentials, shell configuration, and unlisted OS packages require explicit approval.

