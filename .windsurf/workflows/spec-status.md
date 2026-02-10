---
description: Dashboard showing progress across all specs, active sessions, and mailbox state. Use to monitor how sub-sessions are doing.
---

## Spec Status Dashboard

1. Read `.windloop/index.md` to get the list of all registered specs.

2. For EACH spec listed in the index:
   a. Read `.windloop/SPEC/tasks.md` and count:
      - Total tasks (required + optional)
      - Done (`[x]`)
      - Partial/skipped (`[~]`)
      - Pending (`[ ]`)
      - Blocked (`[!]`)
      - Optional (any status followed by `*`, e.g. `[ ]*`, `[x]*`)
   b. Read `.windloop/SPEC/progress.txt` and get the last 5 log entries.
   c. Calculate completion percentage: `(done + partial) / required * 100` (exclude optional from denominator)

3. Read `.windloop/dependencies.md` if it exists. Check if any spec's prerequisites are incomplete.

4. Read `.windsurf/mailbox/board/claims.json` to see which tasks are currently claimed by sessions.

5. Read `.windsurf/mailbox/board/status.json` for any shared state.

6. Check `.windsurf/mailbox/outbox/` for any unprocessed completion signals.

7. Check `.windsurf/mailbox/inbox/` for any unread messages.

8. Print a dashboard:

```
╔══════════════════════════════════════════════════╗
║              WINDLOOP STATUS                     ║
╠══════════════════════════════════════════════════╣

Spec: taskrunner
  Progress: ████████░░ 5/7 tasks (71%)
  Status:   T1 ✓  T2 ✓  T3 ~  T4 ✓  T5 ✓  T6 ○  T7○*
  Blocked:  none
  Last:     [2026-02-09 22:30] DONE T5 - Report generator

Spec: auth
  Progress: ██░░░░░░░░ 1/5 tasks (20%)
  Status:   T1 ✓  T2 ○  T3 ○  T4 ○  T5○*
  Blocked:  none
  Depends:  (none)

Active Sessions:
  worker-1: claimed taskrunner/T6 (in progress)
  worker-2: claimed auth/T2 (in progress)

Mailbox:
  Unread messages: 0
  Pending signals: 0

╚══════════════════════════════════════════════════╝
```

9. If any specs have unmet dependencies (from `dependencies.md`), flag them.

10. Suggest next actions based on the current state.
