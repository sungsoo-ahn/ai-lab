# Evaluation Runtime Policy

This policy covers runtime support packages that are not Python dependencies but are required for evaluation-cell code to execute correctly.

## Default

Runtime changes follow `policies/update-policy.md`. Do not silently install OS packages during ordinary interactive work.

## Long-Running Runtime Exception

When the user explicitly authorizes an long-running evaluation-cell run with automatic dependency setup, agents may install allowlisted runtime support packages without pausing, subject to all of these limits:

- the package must be listed in `Brewfile`;
- the package must be required by a concrete evaluation cell or work unit;
- the package must be a runtime library or CLI support dependency, not a broad platform such as Docker, Node, a database server, or a credentialed service;
- the command must be manifest-backed, normally `brew bundle --file /Users/sungs/ai-lab/Brewfile --no-upgrade`;
- the exact command, package, reason, and verification result must be recorded in the cell or work-unit report;
- failures must be recorded and should not be hidden by switching evaluation rules.

The active approved runtime profile is `btc-benchmark-python`, which checks the Python imports needed by the BTC Benchmark checkout. It does not require Homebrew packages, so its runtime check should not fail merely because the broader workstation `Brewfile` baseline has unmet optional tools.

## Helper Command

Check the runtime state:

```sh
bin/ai-lab runtime check btc-benchmark-python --repo sources/checkouts/btc_benchmark
```

Ensure the runtime state inside an approved extended run:

```sh
bin/ai-lab runtime ensure btc-benchmark-python --repo sources/checkouts/btc_benchmark
```

## Still Requires Explicit Approval

Connector writes, account configuration, shell startup edits, credentials, Docker, Node, browser drivers, kernels, and external submissions still require explicit approval every time.
