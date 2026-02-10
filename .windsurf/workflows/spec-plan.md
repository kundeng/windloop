---
description: Generate a spec and task breakdown from a project idea. Use this to bootstrap a new spec-driven project.
---

## Plan a Spec

Provide a spec name in your message (e.g. `/spec-plan auth`). Optionally include a description.

This workflow handles three modes:
- **Create**: new spec from scratch (`.windloop/SPEC/` doesn't exist)
- **Refine**: update an existing spec (user says "refine", "update", or "revise")
- **Resume**: pick up where you left off if the spec exists but is incomplete

Let SPEC be the spec name.

### 0. Scaffold `.windloop/` if it doesn't exist

If `.windloop/` directory does not exist, create it with:
- `.windloop/index.md` — use the index.md template from the spec-driven-dev skill
- `.windloop/dependencies.md` — use the dependencies.md template from the skill

If the host project has an existing `AGENTS.md`, read it and check if it already contains a "Windloop" section. If not, append the AGENTS.md snippet from the spec-driven-dev skill. If no `AGENTS.md` exists, create one with just the windloop snippet.

### 1. Gather requirements

Ask the user to describe the project idea, goals, and constraints. If they already provided this in the prompt, proceed.

For **Refine** mode: read the existing `.windloop/SPEC/spec.md` and ask what should change.

### 2. Generate spec.md

Create `.windloop/SPEC/spec.md` using the spec.md template from the spec-driven-dev skill:
- Fill in all sections based on the user's description
- Make concrete tech stack decisions
- Define clear testing strategy with actual commands
- List specific data models and interfaces

Present the spec to the user for review. Ask if any changes are needed. Iterate until approved.

### 3. Generate design.md

Create `.windloop/SPEC/design.md` using the design.md template from the spec-driven-dev skill:
- Define module architecture and interfaces
- Specify data flow between components
- Write **property tests** — invariants that must hold true (these guide implementation and testing)
- Document error handling strategy and edge cases

Present the design to the user for review. Iterate until approved.

### 4. Generate tasks.md

Create `.windloop/SPEC/tasks.md` using the tasks.md template from the spec-driven-dev skill:
- Each task completable in a single Cascade session
- Include clear acceptance criteria with checkable items
- Specify exact files to create/modify
- Include a verification command for each task
- Reference relevant property tests from design.md
- Set dependencies correctly (no circular deps)
- Order by phase: Foundation → Core → Integration → Polish

### 5. Create progress.txt

Create `.windloop/SPEC/progress.txt` using the progress.txt template from the skill.

### 6. Register the spec

Add an entry for SPEC in `.windloop/index.md`.

If cross-spec dependencies exist, add them to `.windloop/dependencies.md`.

// turbo
### 7. Commit

```
git add -A && git commit -m "spec(SPEC): create spec, design, and tasks"
```

### 8. Report

Print: "Spec **SPEC** is ready with [N] tasks across [M] phases."
- Run `/spec-loop SPEC` for autonomous implementation
- Run `/spec-task SPEC T1` to start with the first task
- Run `/spec-status` to see the dashboard
