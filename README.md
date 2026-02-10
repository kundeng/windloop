# Windloop

A spec-driven autonomous development framework for [Windsurf](https://windsurf.com). Uses workflows, skills, hooks, and git worktrees to enable near-intervention-free cascaded agent loops.

## What Is This?

Windloop provides a reusable scaffold that turns Windsurf's Cascade into an autonomous development loop:

```
spec.md → tasks.md → [pick task → implement → test → commit → update progress → repeat]
```

It leverages Windsurf's native features:
- **Workflows** — sequenced multi-step instructions (`/spec-loop`, `/implement-task`, etc.)
- **Skills** — bundled knowledge for spec-driven development
- **Hooks** — lifecycle scripts for worktree setup, auto-formatting, and audit logging
- **Git Worktrees** — parallel isolated workspaces for concurrent Cascade sessions
- **Turbo Mode + Auto-Continue** — minimal human intervention

## Quick Start

### 1. Bootstrap a new project from an idea

```
/plan-spec
```

Describe your project. Cascade generates `specs/spec.md` and `specs/tasks.md`.

### 2. Run the autonomous loop

```
/spec-loop
```

Cascade reads the spec, picks the next task, implements it, runs tests, commits, and repeats.

### 3. Or implement a single task (great for parallel worktrees)

```
/implement-task T3
```

Open multiple Cascade sessions in Worktree mode, each assigned a different task.

### 4. Verify everything

```
/verify-all
```

### 5. Review after parallel work

```
/review-merge
```

## Settings for Maximum Autonomy

| Setting | Value | Where |
|---------|-------|-------|
| Auto-Execution | **Turbo** | Windsurf Settings (bottom-right) |
| Auto-Continue | **Enabled** | Windsurf Settings |
| Worktree Mode | **On** | Cascade input (bottom-right toggle) |

## Project Structure

```
specs/
├── spec.md              # Project specification
├── tasks.md             # Ordered task list with dependencies
├── progress.txt         # Auto-updated progress log
└── templates/           # Reusable templates for new projects
    ├── spec-template.md
    ├── tasks-template.md
    └── progress-template.txt

.windsurf/
├── workflows/
│   ├── spec-loop.md     # Main autonomous loop
│   ├── implement-task.md # Single task implementation
│   ├── plan-spec.md     # Bootstrap spec from idea
│   ├── verify-all.md    # Run all checks
│   └── review-merge.md  # Post-merge review
├── skills/
│   └── spec-dev/
│       └── SKILL.md     # Spec-driven dev skill
├── hooks.json           # Hook configuration
└── hooks/
    ├── auto-format.sh   # Auto-format after edits
    └── log_cascade.py   # Audit log of Cascade responses

hooks/
└── setup_worktree.sh    # Worktree initialization

AGENTS.md                # Agent instructions (auto-discovered by Cascade)
```

## How It Works

### The Loop

1. `/spec-loop` reads `specs/tasks.md` and finds the next uncompleted task with all dependencies met
2. Implements the task following acceptance criteria
3. Runs the task's verification command
4. On failure: retries up to 3 times, then marks BLOCKED and moves on
5. On success: commits, updates progress, calls `/spec-loop` again
6. Stops when all tasks are done

### Parallel Execution

For independent tasks (no overlapping files or dependencies):

1. Open Cascade #1 in Worktree mode → `/implement-task T3`
2. Open Cascade #2 in Worktree mode → `/implement-task T4`
3. Both run in isolated git worktrees
4. Merge each back when done
5. Run `/review-merge` to validate

### Hooks

- **`post_setup_worktree`** — Copies `.env` files, installs dependencies in new worktrees
- **`post_write_code`** — Auto-formats edited files (ruff for Python, prettier for JS/TS)
- **`post_cascade_response`** — Logs Cascade responses to `.windsurf/cascade_log.jsonl`

## Using Templates for New Projects

The `specs/templates/` directory contains blank templates. To start a fresh project:

1. Copy this repo's `.windsurf/`, `hooks/`, `specs/templates/`, and `AGENTS.md` into your project
2. Run `/plan-spec` and describe your project
3. Run `/spec-loop` to build it

## Testing This Repo

This repo includes a test project (a simple Python `taskrunner` CLI) defined in `specs/spec.md` and `specs/tasks.md`. To test the full loop:

1. Open a Cascade session
2. Type `/spec-loop`
3. Watch it implement T1 through T7 autonomously
4. Check `specs/progress.txt` for the log

## License

MIT
