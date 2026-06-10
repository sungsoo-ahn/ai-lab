# System Manual

The AI Lab is a local-first workspace for developing AI scientists. It is organized so the reasoning, prompts, artifacts, and decisions behind agentic work remain inspectable after the run is over.

## Core Ideas

| Concept | Meaning |
| --- | --- |
| Scientist | A versioned agent scheme for one task. It owns the goal, metric or decision criteria, constraints, assets, reports, and accepted proposal history. |
| Work unit | The smallest auditable unit of work. A work unit can optimize a metric, test a hypothesis, audit a pipeline, build a proxy, synthesize reports, or document a failure. |
| Run | A concrete execution of prompts, tools, commands, and artifact writes. Runs should preserve enough context to explain what the agent was asked to do. |
| Human gate | The review point where a result is accepted, rejected, rerun, or turned into a next-version proposal. |

## Maintainer Contract

- The manual should explain the system well enough that a reader does not need to inspect source files to understand behavior or decisions.
- Exact prompts are first-class run artifacts. They are stored locally under run directories and summarized, not copied wholesale, in public docs.
- Repository paths may appear as provenance references, but the explanation should stand on its own.
- Secrets, credentials, API keys, tokens, private connector content, and unnecessary personal data must not appear in manuals, prompt artifacts, reports, or logs.
- Scientists and work units are hand-maintained documents. Templates and audit checks keep shape consistent, but each page may specialize for the actual work.
- Work-unit proposals must not silently mutate a current scientist target metric. Accepted proposals create a new scientist version.

## Current System State

| Area | Status |
| --- | --- |
| Active tasks | `btc`, `btc_benchmark` |
| Active scientists | `btc_autoresearch_v1`, `btc_benchmark_v2` |
| Public site | MkDocs Material, deployed to GitHub Pages |
| Static visualization | Vega-Lite from CDN using `docs/assets/btc-trials.json` |
| Prompt provenance | Local run artifacts under `tasks/active/.../runs/.../prompts/` |
| Runtime policy | Prefer Python and `uv`; do not introduce Node or Docker by default |
| Runtime automation | Long runs may use allowlisted runtime profiles such as `xgboost-macos` for XGBoost `libomp` |

## Main Manuals

- [Architecture](architecture.md)
- [Prompt Provenance](prompt-provenance.md)
- [Maintenance](maintenance.md)
- [Documentation Standards](documentation-standards.md)
- [Scientist Manuals](../scientists/index.md)
