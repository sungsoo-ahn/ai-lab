# Scientist Manuals

Scientist manuals explain concrete AI scientist versions. A scientist is not just a model or script; it is a versioned research scheme with goals, constraints, prompt/run artifacts, work units, reports, and decision gates.

## What To Look For

| Section | Why it matters |
| --- | --- |
| Purpose and non-goals | Defines what the scientist is allowed to optimize or investigate. |
| Agent and tool roles | Shows how planning, execution, criticism, synthesis, and human review are separated. |
| Prompt provenance | Points to exact local prompts for important LLM runs. |
| Work units | Shows the bounded investigations that produced the current state. |
| Current decision | States what should happen next and what should not be promoted yet. |

## Active Scientists

| Scientist | Task | Role in this manual | Current Decision |
| --- | --- | --- | --- |
| [BTC AutoResearch v1](btc-autoresearch-v1/index.md) | `btc` | Current worked example | Continue with a narrow `t094` robustness work unit before any sealed holdout consideration. |

## Adding Another Scientist

When a new scientist is added, keep its public manual focused on the scheme and decision record. Put detailed work-unit pages under the scientist, but link them from the scientist manual instead of expanding global navigation.
