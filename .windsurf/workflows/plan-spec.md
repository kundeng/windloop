---
description: Generate a spec and task breakdown from a project idea. Use this to bootstrap a new spec-driven project.
---

## Plan a Spec from Requirements

1. Ask the user to describe the project idea, goals, and constraints. If they already provided this in the prompt, proceed.

2. Read `specs/templates/spec-template.md` for the spec format.

3. Generate a comprehensive `specs/spec.md` following the template:
   - Fill in all sections based on the user's description
   - Make concrete tech stack decisions
   - Define clear testing strategy with actual commands
   - List specific data models and interfaces

4. Present the spec to the user for review. Ask if any changes are needed.

5. Once the spec is approved, read `specs/templates/tasks-template.md` for the task format.

6. Break the spec into ordered tasks in `specs/tasks.md`:
   - Each task should be completable in a single Cascade session
   - Include clear acceptance criteria with checkable items
   - Specify exact files to create/modify
   - Include a verification command for each task
   - Set dependencies correctly (no circular deps)
   - Order by phase: Foundation → Core → Integration → Polish

7. Create a fresh `specs/progress.txt` from the template.

8. Report: "Spec and tasks ready. Run `/spec-loop` to begin autonomous implementation, or `/implement-task T[N]` for a specific task."
