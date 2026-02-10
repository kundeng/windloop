---
description: Generate a spec and task breakdown from a project idea. Use this to bootstrap a new spec-driven project.
---

## Plan a Spec from Requirements

Provide a spec name in your message (e.g. `/spec-plan auth`). This becomes the directory name under `.windloop/`.

Let SPEC be the spec name.

1. Ask the user to describe the project idea, goals, and constraints. If they already provided this in the prompt, proceed.

2. Read `.windloop/templates/spec-template.md` for the spec format.

3. Create directory `.windloop/SPEC/` and generate `.windloop/SPEC/spec.md` following the template:
   - Fill in all sections based on the user's description
   - Make concrete tech stack decisions
   - Define clear testing strategy with actual commands
   - List specific data models and interfaces

4. Present the spec to the user for review. Ask if any changes are needed.

5. Once the spec is approved, read `.windloop/templates/tasks-template.md` for the task format.

6. Break the spec into ordered tasks in `.windloop/SPEC/tasks.md`:
   - Each task should be completable in a single Cascade session
   - Include clear acceptance criteria with checkable items
   - Specify exact files to create/modify
   - Include a verification command for each task
   - Set dependencies correctly (no circular deps)
   - Order by phase: Foundation → Core → Integration → Polish

7. Create a fresh `.windloop/SPEC/progress.txt` from the template.

8. Add an entry for this spec in `.windloop/index.md`.

9. If cross-spec dependencies exist, add them to `.windloop/dependencies.md`.

10. Report: "Spec and tasks ready. Run `/spec-loop SPEC` to begin autonomous implementation, or `/spec-task SPEC T[N]` for a specific task."
