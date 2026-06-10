# AI Lab

This guide explains the AI Lab system before any specific example. The goal is simple: a user, developer, or maintainer should understand how scientists, work units, prompts, artifacts, and decisions fit together without first reading the repository.

## At A Glance

| Layer | Question it answers | Primary artifact |
| --- | --- | --- |
| Lab | What rules and shared memory govern all work? | System guide, policies, memory, source registry |
| Task | What broad problem family is being studied? | Task manifest and task notes |
| Scientist | Which versioned agent scheme is active for the task? | Scientist manifest, scientist brief, report, assets |
| Work unit | What bounded investigation, audit, ablation, or synthesis was run? | Work-unit manifest, work-unit brief, report, run artifacts |
| Run | What actually happened during one LLM/tool execution? | Run summary, prompt manifest, logs, outputs |

## How The System Works

An AI scientist is a versioned orchestration layer. It proposes bounded work units, runs agents and tools, records evidence, preserves failed directions, and changes its scheme only through explicit proposals.

Not every work unit maximizes a score. Some work units audit the pipeline, build a proxy, explain a failure, improve documentation, or decide that a result is not reliable enough to promote.

## What To Inspect First

1. Read the [System Guide](system/index.md) for the operating model.
2. Read [System Architecture](system/architecture.md) for the artifact flow.
3. Read [Prompt Provenance](system/prompt-provenance.md) to understand how exact LLM prompts are recorded.
4. Open a scientist brief from [Scientists](scientists/index.md).
5. Use the scientist's work-unit table to inspect individual investigations.

## Current Example

The current example scientist is [BTC AutoResearch v1](scientists/btc-autoresearch-v1/index.md). It is useful as a worked example of the system, but it is not the definition of the system. The AI Lab model is intended to support many scientists, tasks, and work-unit types.
