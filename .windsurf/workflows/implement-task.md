---
description: Implement a single task from specs/tasks.md by ID. Use this for parallel worktree execution where each Cascade handles one task.
---

## Implement a Single Task

When invoking this workflow, specify the task ID (e.g. "T3") in your message.

1. Read `specs/spec.md` to understand the project scope and conventions.

2. Read `specs/tasks.md` and locate the specified task by ID.

3. Verify that all dependencies for this task are marked as done (`[x]`). If not, report which dependencies are missing and STOP.

4. Read any existing source files that this task depends on or modifies to understand the current state.

5. Implement the task following the acceptance criteria exactly:
   - Create or modify only the files listed in the task's `Files` field
   - Add type hints where required
   - Follow existing code patterns and conventions

6. Run the task's verification command (from the `Verify` field).

7. If verification fails, analyze and fix. Retry up to 3 times.

// turbo
8. Run lint if configured: check `specs/spec.md` for the lint command.

9. Update `specs/tasks.md`: mark the task status as `[x]` and check off acceptance criteria.

// turbo
10. Commit: `git add -A && git commit -m "feat([TASK_ID]): [description]"`

11. Append to `specs/progress.txt`: `[YYYY-MM-DD HH:MM] DONE [TASK_ID] - [description]`

12. Report completion and list any issues encountered.
