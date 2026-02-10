---
description: Run a spec-driven autonomous development loop. Reads specs/tasks.md, picks the next task, implements it, verifies, commits, updates progress, and repeats.
---

## Spec-Driven Development Loop

1. Read the project specification at `specs/spec.md` to understand the full project scope, tech stack, and testing strategy.

2. Read `specs/tasks.md` to get the full task list with dependencies and acceptance criteria.

3. Read `specs/progress.txt` to understand what has already been completed.

4. Identify the NEXT uncompleted task from `specs/tasks.md` (status `[ ]`) whose dependencies are ALL marked `[x]` (done). Tasks are ordered by phase, then by ID. If ALL tasks are complete, print a summary of all work done and STOP.

5. Announce: "Starting task [TASK_ID]: [TASK_TITLE]"

6. Read the task's acceptance criteria, files to modify, and verification command carefully.

7. Implement the task:
   - Read any relevant existing code first to understand current patterns
   - Make minimal, focused changes that satisfy the acceptance criteria
   - Follow the project's coding conventions from `specs/spec.md`
   - Add type hints where the spec requires them

8. Run the task's specific verification command (from the task's `Verify` field).

9. If verification fails, analyze the error output and fix the issue. Retry verification up to 3 times. If still failing after 3 retries, update `specs/progress.txt` with a BLOCKED entry and the reason, then move to the next task by calling `/spec-loop`.

// turbo
10. Run the project-wide lint check if one is configured in `specs/spec.md` (e.g. `ruff check src/ tests/`). Fix any lint issues found.

11. Update `specs/tasks.md`: change the task's `Status` from `[ ]` to `[x]` and check off completed acceptance criteria.

// turbo
12. Stage and commit the changes with a descriptive message: `git add -A && git commit -m "feat([TASK_ID]): [brief description of what was implemented]"`

13. Append to `specs/progress.txt` a line in the format: `[YYYY-MM-DD HH:MM] DONE [TASK_ID] - [brief description]`

14. Call `/spec-loop` to continue with the next task.
