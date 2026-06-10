# Documentation Standards

AI Lab public docs are hand-maintained. These standards are defaults, not rigid schemas: a scientist or work unit may specialize its format when the work requires it.

## Audience Rule

Classify content by audience before publishing it:

- `human`: written for users, maintainers, or reviewers; belongs in public docs when non-sensitive.
- `both`: useful to humans and agents; belongs in public docs when non-sensitive.
- `agent`: operational prompts, logs, caches, or machine-only instructions; keep local and summarize by path when useful.

Public docs should exclude only agent-only or sensitive content. Use [Audience And Terminology](../reference/audience-and-terminology.md) for the canonical labels.

## Core Principle

A user, developer, or maintainer should not need to inspect the repository to understand:

- what the system, scientist, or work unit is for;
- which agents or tools act in the loop;
- what inputs, outputs, and artifacts matter;
- how decisions are made;
- what risks and constraints apply;
- what prompts or prompt artifacts controlled the run;
- how to safely continue the work.

Repository paths are allowed as implementation references and provenance, but the explanation must stand on its own.

## System Guide Checklist

- Purpose and current operating model.
- Layer model and state ownership.
- Policies for packages, connectors, privacy, and proposals.
- Overnight and runtime automation rules, including allowlisted dependency setup.
- Build, validation, and deployment commands.
- Documentation rules and maintenance checklist.
- Current active tasks and scientists.

## Scientist Brief Checklist

Include the following when applicable:

- Identity: task, scientist ID, version, status, date.
- Goal and non-goals.
- Target metric and evaluation context.
- Optimization constraints and safety rules.
- Agent/tool roles and data flow.
- Assets, data, source refs, and implementation references.
- Current result and decision state.
- Prompt provenance for important runs.
- Score-search plot or other evidence visualization.
- Trial or experiment interpretations.
- Active and completed work units.
- Open risks, next actions, and proposal gate.
- Maintenance notes for future developers.

## Work Unit Brief Checklist

Include the following when applicable:

- Identity: task, scientist, work-unit ID, type, status, date.
- Purpose and why the work unit exists.
- Method overview and operational commands.
- Inputs, outputs, artifacts, and provenance paths.
- Prompt artifact path when the work unit was LLM-driven.
- Agent/tool roles.
- Result, decision, and safety checklist.
- Failure modes and suspicious signals.
- How to continue, rerun, close, or promote findings.

## Static Data Checklist

For JSON/YAML assets used by plots or diagrams:

- Keep the file small enough to review by hand.
- Include only public or non-sensitive fields.
- Prefer stable IDs over local machine-specific assumptions.
- Add hover or table fields that explain why a point matters.
- Validate JSON/YAML before committing.

## Prompt Checklist

- Record exact prompts under the owning run directory, not under `docs/`.
- Add or update `prompt-manifest.yaml` when a run has prompt artifacts.
- Link prompt artifacts from scientist or work-unit briefs by local path.
- Do not store secrets, connector-private content, credentials, or unnecessary personal data in prompt artifacts.
- Public pages should summarize prompt purpose and path, not paste long raw prompts.

## Audit Protocol

Run `bin/ai-lab docs audit` whenever system, scientist, work-unit, static asset, or public brief files change. The command is also part of the GitHub Pages workflow, so documentation drift blocks deployment.

## Update Protocol By Level

System maintenance changes should update the relevant System Guide page, `README.md` or `reports/system-status.md` when entry points change, and `logs/activity.md` when the change is significant.

Scientist changes should update the scientist manifest, scientist report or guide, public scientist brief, prompt manifests for new runs, static plot data when the evidence surface changes, and the active/completed work-unit lists.

Work-unit changes should update `work-unit.yaml`, `guide.md`, `report.md`, the public work-unit brief, prompt artifact references when applicable, and the owning scientist brief's work-unit table. When a work unit finishes, close or complete the manifest and keep the report status consistent.

Long-run or overnight changes should update the runbook, prompt artifacts, runtime requirements when used, all touched work-unit reports, the scientist report, source maps, public briefs, and `logs/activity.md`.

## Writing Style

- Use clear academic wording.
- Start with the general system concept before diving into the current example.
- Prefer operational specificity over broad claims.
- Distinguish score-maximizing trials from broader evidence-producing work units.
- Link work-unit briefs from the owning scientist brief to keep global navigation small.
- Explain negative findings and rejected directions as useful evidence.
- Avoid marketing language and hidden assumptions.
