---
name: spec-driven-dev
description: Guides spec-driven autonomous development. Use when implementing features from a spec, breaking down requirements into tasks, or running the autonomous development loop.
---

## Spec-Driven Development

This project uses a spec-driven development workflow with **multiple specs**:

1. **Specs** are registered in `specs/index.md` and live in `specs/<name>/`
2. Each spec has: `spec.md` (requirements), `tasks.md` (ordered work items), `progress.txt` (log)
3. **Progress** is tracked automatically per spec

## Key Workflows

All workflows accept an optional spec name. If only one spec exists, it can be omitted.

| Command | Purpose |
|---------|---------|
| `/plan-spec <name>` | Generate spec + tasks from a project idea |
| `/spec-loop <name>` | Autonomous loop: pick task → implement → test → commit → repeat |
| `/implement-task <name> T[N]` | Implement a single task by ID (for parallel worktree use) |
| `/verify-all <name>` | Run all tests + lint and report status |
| `/review-merge <name>` | Review progress and validate after merges |

## Task Format

Each task in `specs/<name>/tasks.md` has:
- **ID**: T1, T2, etc.
- **Priority**: P0 (critical), P1 (important), P2 (nice-to-have)
- **Dependencies**: Which tasks must be done first
- **Acceptance criteria**: Checkable items that define "done"
- **Files**: Which files to create/modify
- **Verify**: Command to validate the task
- **Status**: `[ ]` pending, `[x]` done, `[!]` blocked

## Rules for Implementation

1. Always read `specs/index.md` first to find available specs
2. Read the spec before starting any task
3. Check dependencies before implementing — never skip ahead
4. Run the task's verify command after implementation
5. Fix failures up to 3 times before marking BLOCKED
6. Commit after each successful task: `feat(<spec>/T[N]): [description]`
7. Update both `tasks.md` (status) and `progress.txt` (log entry)
8. Follow the tech stack and conventions defined in the spec
9. Keep changes minimal and focused on the current task

## Parallel Execution

For independent tasks (no shared dependencies), use worktree mode:
1. Open a new Cascade in Worktree mode
2. Run `/implement-task <name> T[N]` for the specific task
3. After completion, merge the worktree back

Tasks are independent if they don't share the same `Files` and their dependency chains don't overlap.

## File-Based Coordination (Mailbox)

When running parallel sessions, use `.windsurf/mailbox/` for coordination:
- **`board/claims.json`** — claim tasks before starting (prevents double-work)
- **`board/status.json`** — shared state visible to all sessions
- **`inbox/<session>/`** — messages TO a session
- **`outbox/<session>/`** — completion signals FROM a session

See `.windsurf/mailbox/README.md` for the full protocol.
