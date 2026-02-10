# Windloop Agent Instructions

## Project Overview
This is a spec-driven autonomous development framework for Windsurf. It uses workflows, skills, and hooks to enable near-intervention-free cascaded agent loops.

## Development Workflow
1. Specs live in `specs/<name>/` — always read `specs/index.md` to find available specs
2. Read `specs/<name>/spec.md` and `specs/<name>/tasks.md` before implementing anything
3. Use `/spec-loop <name>` for autonomous task-by-task implementation
4. Use `/implement-task <name> T[N]` for single-task execution (ideal for parallel worktrees)
5. Use `/verify-all <name>` to run the full test + lint suite
6. Use `/plan-spec <name>` to bootstrap a new spec from requirements
7. If only one spec exists, the name can be omitted

## Conventions
- Always check task dependencies before starting implementation
- Run the task's verification command after every implementation
- Commit after each completed task with message format: `feat(<spec>/T[N]): [description]`
- Update both `specs/<name>/tasks.md` (status checkbox) and `specs/<name>/progress.txt` (log line) after each task
- Keep changes minimal and focused — one task per commit
- Follow the tech stack and patterns defined in `specs/<name>/spec.md`

## Multi-Spec Structure
```
specs/
  index.md                # Registry of all specs
  templates/              # Reusable templates for new specs
  <name>/                 # One directory per spec
    spec.md               # Full project specification
    tasks.md              # Ordered task list with dependencies
    progress.txt          # Auto-updated progress log
```

## File-Based Coordination (Mailbox Protocol)
When running parallel Cascade sessions, use the mailbox for coordination:
```
.windsurf/mailbox/
  board/status.json       # Shared state visible to all sessions
  board/claims.json       # Task claim registry (prevents double-work)
  inbox/<session>/        # Messages TO a session
  outbox/<session>/       # Completion signals FROM a session
```
See `.windsurf/mailbox/README.md` for the full protocol.

## File Structure
```
specs/                    # Project specifications and progress
.windsurf/
  workflows/              # Cascade workflow definitions
  skills/                 # Cascade skill bundles
  hooks.json              # Lifecycle hook configuration
  hooks/                  # Hook scripts
  mailbox/                # File-based inter-session coordination
hooks/                    # Worktree setup scripts
```

## Testing
- Run tests: check `specs/<name>/spec.md` for the exact command (typically `python -m pytest tests/ -v`)
- Run lint: check `specs/<name>/spec.md` for the lint command (typically `ruff check src/ tests/`)
- Never skip verification after implementation
