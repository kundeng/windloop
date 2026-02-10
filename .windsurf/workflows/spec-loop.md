---
description: Run a spec-driven autonomous development loop. Reads .windloop/<name>/tasks.md, picks the next task, implements it, verifies, commits, updates progress, and repeats.
---

## Spec-Driven Development Loop

This workflow supports multiple specs. Pass the spec name in your message (e.g. `/spec-loop taskrunner`).
If omitted, check `.windloop/index.md` for available specs. If only one active spec exists, use it.

Let SPEC be the resolved spec name. All paths below use `.windloop/SPEC/`.

1. Read `.windloop/SPEC/spec.md` to understand the full project scope, tech stack, and testing strategy.

2. Read `.windloop/SPEC/design.md` (if it exists) to understand architecture, interfaces, and property tests.

3. Read `.windloop/SPEC/tasks.md` to get the full task list with dependencies and acceptance criteria.

4. Read `.windloop/SPEC/progress.txt` to understand what has already been completed.

5. Identify the NEXT uncompleted task from `.windloop/SPEC/tasks.md` (status `[ ]`) whose dependencies are ALL marked `[x]` (done). Tasks are ordered by phase, then by ID. If ALL tasks are complete, print a summary of all work done and STOP.

6. Announce: "Starting task [TASK_ID]: [TASK_TITLE] (spec: SPEC)"

7. Read the task's acceptance criteria, files to modify, and verification command carefully.

8. Implement the task:
   - Read any relevant existing code first to understand current patterns
   - Make minimal, focused changes that satisfy the acceptance criteria
   - Follow the project's coding conventions from `.windloop/SPEC/spec.md`
   - Add type hints where the spec requires them

9. Run the task's specific verification command (from the task's `Verify` field).

10. If verification fails, analyze the error output and fix the issue. Retry verification up to 3 times. If still failing after 3 retries, update `.windloop/SPEC/progress.txt` with a BLOCKED entry and the reason, then move to the next task by calling `/spec-loop SPEC`.

// turbo
11. Run the project-wide lint check if one is configured in `.windloop/SPEC/spec.md` (e.g. `ruff check src/ tests/`). Fix any lint issues found.

12. Update `.windloop/SPEC/tasks.md`: change the task's `Status` from `[ ]` to `[x]` and check off completed acceptance criteria.

// turbo
13. Stage and commit the changes with a descriptive message: `git add -A && git commit -m "feat(SPEC/[TASK_ID]): [brief description of what was implemented]"`

14. Append to `.windloop/SPEC/progress.txt` a line in the format: `[YYYY-MM-DD HH:MM] DONE [TASK_ID] - [brief description]`

15. Call `/spec-loop SPEC` to continue with the next task.
