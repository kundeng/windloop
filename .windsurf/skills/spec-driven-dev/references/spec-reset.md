
## Reset a Spec

Pass the spec name (e.g. `/spec-reset taskrunner`).
If omitted, use the **Spec Resolution** rules from SKILL.md.

Let SPEC be the resolved spec name and SPEC_DIR the resolved directory.

**WARNING**: This clears all progress. Ask the user to confirm.

1. Ask: "This will reset all progress for spec **SPEC**. Are you sure? (yes/no)"

2. If confirmed, proceed. Otherwise STOP.

3. Read `SPEC_DIR/tasks.md` and change ALL task checkboxes from `[x]`, `[~]`, or `[!]` back to `[ ]` (preserve `*` on optional tasks).

4. Reset `SPEC_DIR/progress.txt` to just the header:
   ```
   # Progress Log: [SPEC NAME]
   # Auto-updated by spec-go workflow
   # Format: [TIMESTAMP] [STATUS] [TASK_ID] - [DESCRIPTION]
   # STATUS: DONE | BLOCKED | SKIPPED | IN_PROGRESS
   ```

// turbo
5. Commit: `git add -A && git commit -m "chore(SPEC): reset progress for re-run"`

6. Report: "Spec **SPEC** has been reset. Run `/spec-go SPEC` to start fresh."
