
## Spec Go — Autonomous Implementation

Pass the spec name in your message (e.g. `/spec-go taskrunner`).
Optionally specify a task count (e.g. `/spec-go taskrunner 5` or "implement next 3 tasks"). If a count is given, stop after that many tasks.
If omitted, use the **Spec Resolution** rules from SKILL.md.

Let SPEC be the resolved spec name and SPEC_DIR be the resolved directory.

1. Read `SPEC_DIR/requirements.md` to understand the requirements and scope. If `steering/` exists (`.windloop/steering/` or `.kiro/steering/`), read it for project-level context.

2. Read `SPEC_DIR/design.md` to understand architecture, tech stack, testing strategy, and correctness properties.

3. Read `SPEC_DIR/tasks.md` to get the full task list with dependencies.

4. Read `SPEC_DIR/progress.txt` to understand what has already been completed.

5. Identify the NEXT uncompleted task (`[ ]`) whose dependencies are ALL satisfied (`[x]` or `[~]`). Skip `[ ]*` optional tasks if their dependencies aren't met. If ALL required tasks are done and only optional tasks remain, print a summary and STOP.

6. Announce: "Starting task [TASK_ID]: [TASK_TITLE] (spec: SPEC)"

7. Read the task's description and dependencies.

8. Implement the task:
   - Read any relevant existing code first
   - If this is a test task, write the tests and verify they pass
   - If this is an implementation task, write the code and run existing tests to confirm nothing breaks
   - Follow the coding conventions from `SPEC_DIR/design.md`

9. Run relevant tests. If failures, analyze and fix. Retry up to 3 times. If still failing, update `SPEC_DIR/progress.txt` with a BLOCKED entry and move to the next task.

// turbo
10. Run the lint check if one is configured in `SPEC_DIR/design.md`. Fix any lint issues.

11. Update `SPEC_DIR/tasks.md`: change the task's checkbox from `[ ]` to `[x]`.

// turbo
12. Commit: `git add -A && git commit -m "feat(SPEC/[TASK_ID]): [brief description]"`

13. Update `SPEC_DIR/progress.txt`:
    - Append: `[YYYY-MM-DD HH:MM] DONE [TASK_ID] - [brief description]`
    - Update the `# SUMMARY:` line.

14. If a task count was specified and reached, print a summary and STOP. Otherwise, go back to step 5.
