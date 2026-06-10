# Overnight Runbook: <cell_id>

Date: <YYYY-MM-DD>
Status: ready
Run ID: <run_id>

## Goal

<Run a full evaluation-cell loop after readiness gates pass.>

## Autonomy

- Agents may run bounded work units.
- Agents may silently install missing Python dependencies only through cell-local or inherited repository-local `uv` workflows when explicitly authorized.
- Agents may use allowlisted runtime profiles, such as `bin/ai-lab runtime ensure btc-benchmark-python --repo sources/checkouts/btc_benchmark`, when explicitly authorized.
- Agents may not silently install Node, Docker, unlisted system packages, connector integrations, credentials, shell configuration, or account configuration.

## Gates

1. Verify environment, tests, data, and baseline.
2. Record package installs and failures.
3. Check expected runtime profiles before model-heavy work.
4. Launch parallel-ready work units only after baseline state is known.
5. Preserve failed trials and negative findings.

## Required Final Outputs

- Update the evaluation cell `report.md`.
- Update every work-unit `report.md`.
- Write a run summary under cell `runs/`.
- Record proposals under cell `proposals/` if the next version should change task-specific metric, constraints, or scheme usage.
