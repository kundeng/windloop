
## Spec Status Dashboard

1. Discover all specs: list directories in `.windloop/specs/` and `.kiro/specs/`.

2. For EACH spec (let SPEC_DIR be its directory):
   a. Read `SPEC_DIR/tasks.md` and count:
      - Total tasks (required + optional)
      - Done (`[x]`), Partial/skipped (`[~]`), Pending (`[ ]`), Blocked (`[!]`)
      - Optional (`[ ]*`, `[x]*`)
   b. Read `SPEC_DIR/progress.txt` and get the last 5 log entries.
   c. Completion: `(done + partial) / required * 100` (exclude optional from denominator)

3. Print a dashboard:

```
╔══════════════════════════════════════════════════╗
║              WINDLOOP STATUS                     ║
╠══════════════════════════════════════════════════╣

Spec: taskrunner
  Progress: ████████░░ 5/7 tasks (71%)
  Status:   1.1 ✓  1.2 ✓  1.3 ~  2.1 ✓  2.2 ✓  3.1 ○  3.2○*
  Blocked:  none
  Last:     [2026-02-09 22:30] DONE 2.2 - Report generator

Spec: auth
  Progress: ██░░░░░░░░ 1/5 tasks (20%)
  Status:   1.1 ✓  1.2 ○  2.1 ○  2.2 ○  3.1○*
  Blocked:  none

╚══════════════════════════════════════════════════╝
```

4. Suggest next actions based on the current state.
