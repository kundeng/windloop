
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

7. Read the task's description, files to modify, and verification command.

8. Implement the task (test-first):
   - Read any relevant existing code first
   - **Write tests first**: if the task has a Tests field, implement those property tests before production code
   - Then write the production code to make the tests pass
   - For E2E test tasks: implement the test, run it, verify it passes
   - Follow the coding conventions from `SPEC_DIR/design.md`

9. Run the task's verification command (from the Verify field).

10. If verification fails, analyze and fix. Retry up to 3 times. If still failing, update `SPEC_DIR/progress.txt` with a BLOCKED entry and move to the next task.

// turbo
11. Run the lint check if one is configured in `SPEC_DIR/design.md`. Fix any lint issues.

12. Update `SPEC_DIR/tasks.md`: change the task's checkbox from `[ ]` to `[x]`.

// turbo
13. Commit: `git add -A && git commit -m "feat(SPEC/[TASK_ID]): [brief description]"`

14. **Post-commit tracking guard**: For each file in the task's Files field, run `git ls-files <file>`. If any file is untracked (likely gitignored), `git add -f <file>` then `git commit --amend --no-edit`.

15. Update `SPEC_DIR/progress.txt`:
    - Append: `[YYYY-MM-DD HH:MM] DONE [TASK_ID] - [brief description]`
    - Update the `# SUMMARY:` line.

16. If a task count was specified and reached, print a summary and STOP. Otherwise, go back to step 5.
