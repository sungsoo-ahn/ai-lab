# Comparable Systems

Date: 2026-06-11
Status: active

This page compares AI Lab with related AI scientist, research-agent, and agent-evaluation systems. The goal is not to copy any one system. The goal is to make the local design choices explicit: AI Lab is a local-first platform for comparing scientist schemes across tasks, preserving evidence, and letting a meta scientist improve the lab.

## Summary

| System | Primary emphasis | Strong idea to learn from | Difference from AI Lab |
| --- | --- | --- | --- |
| The AI Scientist | End-to-end idea generation, experiment execution, paper writing, and review for constrained ML research domains. | Treat the scientific loop as a complete pipeline, not just coding. | AI Lab focuses on local evidence and cross-scheme comparison rather than autonomous paper production as the main output. |
| AI Scientist-v2 | A later open-source AI scientist framework with more advanced autonomous research workflow support. | Keep the workflow inspectable as the system becomes more capable. | AI Lab decomposes scientist identity into scheme, skills, taste, hypotheses, and evaluation cell. |
| AutoScientists | A runbook-oriented scientist workflow with fixed command entry points. | A concrete CLI entry point can make agent work easier to launch and repeat. | AI Lab generalizes this into task-by-scheme cells and reusable component catalogs. |
| Agent Laboratory / AgentRxiv-style systems | Multi-agent research assistance from literature review through experimentation and report writing. | Role separation and staged research can improve coverage. | AI Lab keeps task, scientist scheme, and work-unit evidence as first-class local artifacts. |
| MLAgentBench | Benchmarking LLM agents on machine learning experimentation tasks. | Agent evaluation should include realistic ML experimentation loops, not only code puzzles. | AI Lab is a platform for running and improving scientist schemes, not only a benchmark suite. |
| MLE-bench | Measuring AI agents on Kaggle-style machine learning engineering tasks. | Strong task packaging and scoring discipline make comparisons credible. | AI Lab can use benchmark tasks, but also tracks hypotheses, taste, and meta-scientist proposals. |
| AlphaEvolve | Evolutionary coding agent for discovering algorithms using LLM-generated programs and automated evaluators. | Automated evaluators plus search can produce useful discoveries in tightly scored domains. | AI Lab supports search-like schemes, but also needs research memory, work units, and cross-task scientist comparison. |

## What Existing Systems Suggest

### End-To-End Autonomy Is Useful But Too Coarse

The AI Scientist line of work shows that a system can automate a broad scientific workflow: proposing ideas, running experiments, producing writeups, and reviewing results. This is valuable because it treats research as a loop rather than a single model call.

AI Lab should borrow the full-loop ambition but avoid making "paper produced" the only success state. For this repo, the more useful intermediate objects are work units, falsified hypotheses, reusable skills, preserved failed runs, and concrete proposals for the next scientist version.

### Fixed Entrypoints Matter

AutoScientists and similar runbook-driven systems are useful because a fixed command such as `autoscientist` gives the human a clear operational handle. AI Lab should keep this property through `run-spec.yaml`, `bin/ai-lab`, and task-specific launchers.

The difference is that AI Lab should not let the command hide the scientist composition. The run should declare the task, scheme, skill bundle, research taste, hypotheses, target metric, and exit criteria.

### Multi-Agent Roles Need Shared State

Agent Laboratory-style systems show the value of separating roles such as literature review, experimentation, critique, and writing. The local AutoScientist scheme follows the same broad idea.

The practical risk is role theater: multiple agents can produce more text without producing better evidence. AI Lab should judge a multi-agent scheme by whether it leaves stronger work-unit evidence, better critiques, or better next-step proposals than a simpler loop.

### Benchmarks Need Contract Discipline

MLAgentBench and MLE-bench are reminders that benchmark packaging matters. If the task, scoring code, data splits, and allowed actions are unclear, scientist comparison becomes anecdotal.

AI Lab's task manifests and evaluation cells should therefore document:

- what score is being optimized;
- what source code or data is frozen;
- which actions are disallowed;
- what artifacts prove a score;
- what makes two cells comparable.

### Search Works Best With Automated Evaluators

AlphaEvolve is a strong example of pairing LLM-generated code with automated evaluation and iterative search. This maps naturally to domains where candidate quality can be scored cheaply and repeatedly.

AI Lab should use this idea where the task supports it, but it should keep the search loop as one possible scientist scheme rather than the definition of an AI scientist. Some work units will be observational, diagnostic, or proposal-oriented instead of direct metric optimization.

## Design Implications For This Repo

| Implication | Repo design response |
| --- | --- |
| Scientist identity becomes ambiguous if everything lives in one prompt. | Store scheme, skills, taste, hypotheses, and memory separately. |
| Autonomy stalls when every local action asks for permission. | Use approved local run specs with explicit gates and exit criteria. |
| Autonomy becomes unsafe when external writes are hidden. | Keep connector writes, external submissions, and environment changes gated. |
| Benchmarks are easy to overfit. | Preserve source gates, referee constraints, holdout rules, and negative results. |
| Multi-agent systems can generate unreviewable volume. | Require work-unit evidence and synthesis summaries tied to artifacts. |
| Meta-improvement can corrupt comparisons if it mutates current cells. | Route system changes through proposals and new versions. |

## Source Map

| Source | Type | Relevance | Last checked |
| --- | --- | --- | --- |
| [The AI Scientist](https://sakana.ai/ai-scientist/) | Official project page | End-to-end AI scientist workflow for ideation, experimentation, paper writing, and review. | 2026-06-11 |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | GitHub repository | Open-source implementation and examples for the original AI Scientist framework. | 2026-06-11 |
| [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | GitHub repository | Later AI Scientist implementation for comparison with the local platform model. | 2026-06-11 |
| [mims-harvard/AutoScientists runbook](https://github.com/mims-harvard/AutoScientists/blob/main/runbook.md) | GitHub runbook | Example of a fixed-entrypoint scientist workflow. | 2026-06-11 |
| [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) | GitHub repository | Multi-agent research workflow from literature review through experimentation and report writing. | 2026-06-11 |
| [MLAgentBench](https://github.com/snap-stanford/MLAgentBench) | GitHub repository | Benchmark for agents performing machine learning experimentation. | 2026-06-11 |
| [OpenAI MLE-bench](https://github.com/openai/mle-bench) | GitHub repository | Benchmark suite for ML engineering agents on Kaggle-style tasks. | 2026-06-11 |
| [AlphaEvolve](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) | Official project page | Example of LLM-generated code search combined with automated evaluators. | 2026-06-11 |

## Open Questions

- Should AI Lab add a dedicated "search scientist" scheme inspired by AlphaEvolve-style program evolution?
- Should benchmark cells include a standard anti-overfitting checklist for every task?
- Should the meta scientist score scientist schemes on evidence quality separately from task metric improvement?
- Should role-based schemes require independent work-unit manifests for each role to prevent untraceable shared state?
