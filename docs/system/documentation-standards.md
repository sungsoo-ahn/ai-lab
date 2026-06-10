# Documentation Standards

The AI Lab manuals are hand-maintained. These standards are defaults, not rigid schemas: a scientist or work unit may specialize its format when the work requires it.

## Core Principle

A user, developer, or maintainer should not need to inspect the repository to understand:

- what the system, scientist, or work unit is for;
- which agents or tools act in the loop;
- what inputs, outputs, and artifacts matter;
- how decisions are made;
- what risks and constraints apply;
- how to safely continue the work.

Repository paths are allowed as implementation references and provenance, but the explanation must stand on its own.

## System Manual Checklist

- Purpose and current operating model.
- Layer model and state ownership.
- Policies for packages, connectors, privacy, and proposals.
- Build, validation, and deployment commands.
- Documentation rules and maintenance checklist.
- Current active tasks and scientists.

## Scientist Manual Checklist

Include the following when applicable:

- Identity: task, scientist ID, version, status, date.
- Goal and non-goals.
- Target metric and evaluation context.
- Optimization constraints and safety rules.
- Agent/tool roles and data flow.
- Assets, data, source refs, and implementation references.
- Current result and decision state.
- Score-search plot or other evidence visualization.
- Trial or experiment interpretations.
- Active and completed work units.
- Open risks, next actions, and proposal gate.
- Maintenance notes for future developers.

## Work-Unit Manual Checklist

Include the following when applicable:

- Identity: task, scientist, work-unit ID, type, status, date.
- Purpose and why the work unit exists.
- Method overview and operational commands.
- Inputs, outputs, artifacts, and provenance paths.
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

## Audit Protocol

Run `bin/ai-lab docs audit` whenever system, scientist, work-unit, static asset, or public manual files change. The command is also part of the GitHub Pages workflow, so documentation drift blocks deployment.

## Update Protocol By Level

System maintenance changes should update the relevant System Manual page, `README.md` or `reports/system-status.md` when entry points change, and `logs/activity.md` when the change is significant.

Scientist changes should update the scientist manifest, scientist report or guide, public scientist manual, static plot data when the evidence surface changes, and the active/completed work-unit lists.

Work-unit changes should update `work-unit.yaml`, `guide.md`, `report.md`, the public work-unit manual, and the owning scientist manual's work-unit table. When a work unit finishes, close or complete the manifest and keep the report status consistent.

## Writing Style

- Use clear academic wording.
- Prefer operational specificity over broad claims.
- Distinguish score-maximizing trials from broader evidence-producing work units.
- Link work-unit manuals from the owning scientist manual to keep global navigation small.
- Explain negative findings and rejected directions as useful evidence.
- Avoid marketing language and hidden assumptions.
