
## Implement a Single Task

Specify the spec name and task ID (e.g. `/spec-task taskrunner 1.3`).
If only one spec exists, the name can be omitted (e.g. `/spec-task 1.3`).

Let SPEC be the resolved spec name and SPEC_DIR the resolved directory.

1. Read `SPEC_DIR/requirements.md` to understand the requirements and scope.

2. Read `SPEC_DIR/design.md` to understand architecture, tech stack, testing strategy, and correctness properties.

3. Read `SPEC_DIR/tasks.md` and locate the specified task by ID.

4. Verify that all dependencies are satisfied (`[x]` or `[~]`). If not, report which are missing and STOP.

5. Read any existing source files that this task depends on or modifies.

6. Implement the task (test-first):
   - **Write tests first**: if the task has a Tests field, implement those property tests before production code
   - Then write the production code to make the tests pass
   - For E2E test tasks: implement the test, run it, verify it passes
   - Create or modify only the files listed in the task's Files field
   - Follow existing code patterns and conventions

7. Run the task's verification command (from the Verify field).

8. If verification fails, analyze and fix. Retry up to 3 times.

// turbo
9. Run lint if configured in `SPEC_DIR/design.md`.

10. Update `SPEC_DIR/tasks.md`: change the task's checkbox from `[ ]` to `[x]`.

// turbo
11. Commit: `git add -A && git commit -m "feat(SPEC/[TASK_ID]): [description]"`

12. **Post-commit tracking guard**: For each file in the task's Files field, run `git ls-files <file>`. If untracked, `git add -f <file>` then `git commit --amend --no-edit`.

13. Update `SPEC_DIR/progress.txt`:
    - Append: `[YYYY-MM-DD HH:MM] DONE [TASK_ID] - [description]`
    - Update the `# SUMMARY:` line.

14. Report completion and list any issues encountered.
