---
description: Reset a spec by clearing progress, unchecking all tasks, and clearing mailbox claims. Use to re-run the loop from scratch.
---

## Reset a Spec

Pass the spec name in your message (e.g. `/spec-reset taskrunner`).
If omitted, check `.windloop/index.md`. If only one active spec exists, use it.

Let SPEC be the resolved spec name.

**WARNING**: This will clear all progress for the spec. Ask the user to confirm before proceeding.

1. Ask: "This will reset all progress for spec **SPEC**. Are you sure? (yes/no)"

2. If confirmed, proceed. Otherwise STOP.

3. Read `.windloop/SPEC/tasks.md` and change ALL task statuses from `[x]`, `[~]`, or `[!]` back to `[ ]` (preserve `*` on optional tasks). Uncheck all acceptance criteria checkboxes.

4. Reset `.windloop/SPEC/progress.txt` to just the header:
   ```
   # Progress Log: [SPEC NAME]
   # Auto-updated by spec-loop workflow
   # Format: [TIMESTAMP] [STATUS] [TASK_ID] - [DESCRIPTION]
   # STATUS: DONE | BLOCKED | SKIPPED | IN_PROGRESS
   ```

5. If `.windsurf/mailbox/board/claims.json` has claims for this spec, remove them.

6. If `.windsurf/mailbox/outbox/` has completion signals for this spec's tasks, remove them.

// turbo
7. Commit: `git add -A && git commit -m "chore(SPEC): reset progress for re-run"`

8. Report: "Spec **SPEC** has been reset. Run `/spec-loop SPEC` to start fresh."
