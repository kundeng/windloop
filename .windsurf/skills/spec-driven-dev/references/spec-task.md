
## Implement a Single Task

Specify the spec name and task ID (e.g. `/spec-task taskrunner 1.3`).
If only one spec exists, the name can be omitted (e.g. `/spec-task 1.3`).

Let SPEC be the resolved spec name and SPEC_DIR the resolved directory.

1. Read `SPEC_DIR/requirements.md` to understand the requirements and scope. If `steering/` exists (`.windloop/steering/` or `.kiro/steering/`), read it for project-level context.

2. Read `SPEC_DIR/design.md` to understand architecture, tech stack, testing strategy, and correctness properties.

3. Read `SPEC_DIR/tasks.md` and locate the specified task by ID.

4. Verify that all dependencies are satisfied (`[x]` or `[~]`). If not, report which are missing and STOP.

5. Read any existing source files that this task depends on or modifies.

6. Implement the task:
   - Read any relevant existing code first
   - If this is a test task, follow the **Red-Green-Refactor** cycle:
     - **RED**: Write a failing test that describes expected behavior
     - **GREEN**: Write the minimum code to make the test pass
     - **REFACTOR**: Clean up without changing behavior, re-run tests
   - If this is an implementation task, write the code and run existing tests to confirm nothing breaks
   - Follow existing code patterns and conventions

7. Run relevant tests. If failures, analyze and fix. Retry up to 3 times. If still failing, mark as BLOCKED in progress.txt with a clear reason and STOP.

// turbo
8. Run lint if configured in `SPEC_DIR/design.md`.

9. Update `SPEC_DIR/tasks.md`: change the task's checkbox from `[ ]` to `[x]`.

// turbo
10. Commit: `git add -A && git commit -m "feat(SPEC/[TASK_ID]): [description]"`

11. Update `SPEC_DIR/progress.txt`:
    - Append: `[YYYY-MM-DD HH:MM] DONE [TASK_ID] - [description]`
    - Update the `# SUMMARY:` line.

12. Report completion:
    ```
    Task [TASK_ID] complete: [brief description]
    Tests: PASS/FAIL
    Files changed: [list]
    ```
    List any issues encountered or follow-up items discovered.
