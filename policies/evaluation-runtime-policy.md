# Evaluation Runtime Policy

This policy covers runtime support packages that are not Python dependencies but are required for evaluation-cell code to execute correctly.

## Default

Runtime changes follow `policies/update-policy.md`. Do not silently install OS packages during ordinary interactive work.

## Overnight Runtime Exception

When the user explicitly authorizes an overnight or long-running evaluation-cell run with automatic dependency setup, agents may install allowlisted runtime support packages without pausing, subject to all of these limits:

- the package must be listed in `Brewfile`;
- the package must be required by a concrete evaluation cell or work unit;
- the package must be a runtime library or CLI support dependency, not a broad platform such as Docker, Node, a database server, or a credentialed service;
- the command must be manifest-backed, normally `brew bundle --file /Users/sungs/ai-lab/Brewfile --no-upgrade`;
- the exact command, package, reason, and verification result must be recorded in the cell or work-unit report;
- failures must be recorded and should not be hidden by switching evaluation rules.

The first approved runtime profile is `xgboost-macos`, which uses Homebrew `libomp` so XGBoost wheels can load OpenMP on macOS.

## Helper Command

Check the runtime state:

```sh
bin/ai-lab runtime check xgboost-macos --repo /path/to/python/project
```

Ensure the runtime state inside an approved overnight run:

```sh
bin/ai-lab runtime ensure xgboost-macos --repo /path/to/python/project
```

## Still Requires Explicit Approval

Connector writes, account configuration, shell startup edits, credentials, Docker, Node, browser drivers, kernels, and external submissions still require explicit approval every time.
