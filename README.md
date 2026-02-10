# Windloop

A spec-driven autonomous development framework for [Windsurf](https://windsurf.com). Uses workflows, skills, hooks, git worktrees, and a file-based coordination protocol to enable near-intervention-free cascaded agent loops.

## What Is This?

Windloop provides a reusable scaffold that turns Windsurf's Cascade into an autonomous development loop:

```
specs/<name>/spec.md → tasks.md → [pick task → implement → test → commit → update progress → repeat]
```

It leverages Windsurf's native features:
- **Workflows** — sequenced multi-step instructions (`/spec-loop`, `/implement-task`, etc.)
- **Skills** — bundled knowledge for spec-driven development
- **Hooks** — lifecycle scripts for worktree setup, auto-formatting, and audit logging
- **Git Worktrees** — parallel isolated workspaces for concurrent Cascade sessions
- **Turbo Mode + Auto-Continue** — minimal human intervention
- **Mailbox Protocol** — file-based coordination between parallel Cascade sessions

## Quick Start

### 1. Bootstrap a new spec from an idea

```
/plan-spec myproject
```

Describe your project. Cascade generates `specs/myproject/spec.md` and `specs/myproject/tasks.md`.

### 2. Run the autonomous loop

```
/spec-loop myproject
```

Cascade reads the spec, picks the next task, implements it, runs tests, commits, and repeats.

### 3. Or implement a single task (great for parallel worktrees)

```
/implement-task myproject T3
```

Open multiple Cascade sessions in Worktree mode, each assigned a different task.

### 4. Verify everything

```
/verify-all myproject
```

### 5. Review after parallel work

```
/review-merge myproject
```

> **Note**: If only one spec exists, the spec name can be omitted from all commands.

## Settings for Maximum Autonomy

| Setting | Value | Where |
|---------|-------|-------|
| Auto-Execution | **Turbo** | Windsurf Settings (bottom-right) |
| Auto-Continue | **Enabled** | Windsurf Settings |
| Worktree Mode | **On** | Cascade input (bottom-right toggle) |

## Project Structure

```
specs/
├── index.md                # Registry of all specs
├── templates/              # Reusable templates for new specs
│   ├── spec-template.md
│   ├── tasks-template.md
│   └── progress-template.txt
└── <name>/                 # One directory per spec
    ├── spec.md             # Full project specification
    ├── tasks.md            # Ordered task list with dependencies
    └── progress.txt        # Auto-updated progress log

.windsurf/
├── workflows/
│   ├── spec-loop.md        # Main autonomous loop
│   ├── implement-task.md   # Single task implementation
│   ├── plan-spec.md        # Bootstrap spec from idea
│   ├── verify-all.md       # Run all checks
│   └── review-merge.md     # Post-merge review
├── skills/
│   └── spec-dev/
│       └── SKILL.md        # Spec-driven dev skill (auto-invoked)
├── hooks.json              # Hook configuration
├── hooks/
│   ├── auto-format.sh      # Auto-format after edits
│   └── log_cascade.py      # Audit log of Cascade responses
└── mailbox/                # File-based inter-session coordination
    ├── README.md           # Full protocol documentation
    ├── board/
    │   ├── status.json     # Shared state
    │   └── claims.json     # Task claim registry
    ├── inbox/              # Messages TO sessions
    └── outbox/             # Completion signals FROM sessions

hooks/
└── setup_worktree.sh       # Worktree initialization

AGENTS.md                   # Agent instructions (auto-discovered by Cascade)
```

## How It Works

### The Loop

1. `/spec-loop <name>` reads `specs/<name>/tasks.md` and finds the next uncompleted task with all dependencies met
2. Implements the task following acceptance criteria
3. Runs the task's verification command
4. On failure: retries up to 3 times, then marks BLOCKED and moves on
5. On success: commits, updates progress, calls `/spec-loop <name>` again
6. Stops when all tasks are done

### Multiple Specs

Break large projects into independent specs:

```
specs/
├── auth/        # Authentication module
├── api/         # REST API endpoints
├── dashboard/   # Frontend dashboard
└── infra/       # Infrastructure & deployment
```

Each spec has its own task list, progress log, and can be implemented independently — even in parallel by different Cascade sessions.

### Parallel Execution

For independent tasks (no overlapping files or dependencies):

1. Open Cascade #1 in Worktree mode → `/implement-task myproject T3`
2. Open Cascade #2 in Worktree mode → `/implement-task myproject T4`
3. Both run in isolated git worktrees
4. Merge each back when done
5. Run `/review-merge myproject` to validate

For independent specs, run entire loops in parallel:

1. Cascade #1 (worktree) → `/spec-loop auth`
2. Cascade #2 (worktree) → `/spec-loop api`
3. Cascade #3 (worktree) → `/spec-loop dashboard`

### File-Based Coordination (Mailbox Protocol)

Parallel Cascade sessions can't communicate directly. The mailbox protocol uses the shared filesystem as a message bus:

```
.windsurf/mailbox/
├── board/claims.json    # Claim tasks to prevent double-work
├── board/status.json    # Shared state visible to all sessions
├── inbox/<session>/     # Messages TO a session
└── outbox/<session>/    # Completion signals FROM a session
```

**Patterns supported**:
- **Lead-Worker** — one session orchestrates, others implement
- **Claim Board** — self-organizing: sessions claim tasks from a shared board
- **Pipeline** — sequential handoff between sessions

See `.windsurf/mailbox/README.md` for the full protocol.

### Hooks

- **`post_setup_worktree`** — Copies `.env` files, installs dependencies in new worktrees
- **`post_write_code`** — Auto-formats edited files (ruff for Python, prettier for JS/TS)
- **`post_cascade_response`** — Logs Cascade responses to `.windsurf/cascade_log.jsonl`

## Using Templates for New Projects

The `specs/templates/` directory contains blank templates. To start a fresh project:

1. Copy this repo's `.windsurf/`, `hooks/`, `specs/templates/`, and `AGENTS.md` into your project
2. Run `/plan-spec myfeature` and describe your project
3. Run `/spec-loop myfeature` to build it

## Testing This Repo

This repo includes a test spec (`taskrunner` — a simple Python CLI) in `specs/taskrunner/`. To test the full loop:

1. Open a Cascade session
2. Type `/spec-loop taskrunner`
3. Watch it implement T1 through T7 autonomously
4. Check `specs/taskrunner/progress.txt` for the log

## Windsurf CLI & API Status

Windsurf has a basic CLI (`windsurf .` to open a folder) but **no headless/programmatic API** for driving Cascade sessions externally. This means:
- You cannot spawn Cascade sessions from a script
- You cannot inject prompts programmatically
- The mailbox protocol is the best available workaround for inter-session coordination

If Windsurf adds a CLI/API for Cascade in the future, this framework can be extended with a true outer-loop orchestrator (similar to Claude Code's agent teams).

## License

MIT
