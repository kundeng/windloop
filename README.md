# Windloop

A spec-driven autonomous development framework for [Windsurf](https://windsurf.com). Copy one directory into any project and get an AI-powered development loop that turns ideas into working code.

## Install

```bash
# Copy .windsurf/ into your project (that's it — everything else is auto-created)
cp -r path/to/windloop/.windsurf/ your-project/.windsurf/
```

Then open your project in Windsurf and type `/spec-help`.

## What It Does

```
idea → spec.md → design.md (with property tests) → tasks.md → [implement → test → commit → repeat]
```

Windloop turns Windsurf's Cascade into an autonomous development loop:

1. **`/spec-plan myfeature`** — Describe your idea. Cascade generates a spec, design (with property tests), and task breakdown. Auto-scaffolds `.windloop/` and `AGENTS.md`.
2. **`/spec-loop myfeature`** — Cascade picks the next task, implements it, runs tests, commits, and repeats until done.
3. **`/spec-status`** — See progress across all specs and parallel sessions.

## Commands

| Command | Purpose |
|---------|---------|
| `/spec-help` | Onboarding guide |
| `/spec-plan <name> [create\|refine\|update]` | Create, refine, or update a spec (auto-detected) |
| `/spec-loop <name>` | Autonomous loop: pick task → implement → test → commit → repeat |
| `/spec-task <name> T[N]` | Implement a single task (for parallel worktree use) |
| `/spec-verify <name>` | Run all tests + lint |
| `/spec-merge <name>` | Review and merge after parallel work |
| `/spec-status` | Dashboard: progress, sessions, mailbox state |
| `/spec-reset <name>` | Reset a spec for re-run |

> If only one spec exists, the `<name>` can be omitted.

## Spec Lifecycle

`/spec-plan` walks you through each stage interactively:

1. **spec.md** — Requirements as numbered user stories (R1.1, R1.2, NF1), tech stack, testing strategy
2. **design.md** — Architecture, module interfaces, **property tests** that validate requirements ("P1 validates R1.1, R1.2")
3. **tasks.md** — Tasks reference requirements + properties they fulfill (`Requirements: R1.1` / `Properties: P1`)
4. **progress.txt** — Auto-updated log

Each stage is reviewed with you before proceeding.

**Modes**: `/spec-plan <name> create` (new), `refine` (broad rethink), `update` (targeted back-propagation from implementation). Auto-detected if omitted.

## What Gets Created

When you run `/spec-plan`, windloop auto-scaffolds:

```
.windloop/                      # Auto-created (not shipped)
├── index.md                    # Registry of all specs
├── dependencies.md             # Cross-spec dependency graph
└── <name>/                     # One directory per spec
    ├── spec.md                 # Requirements
    ├── design.md               # Architecture + property tests
    ├── tasks.md                # Task breakdown
    └── progress.txt            # Progress log

AGENTS.md                       # Windloop snippet appended (or created)
```

## What You Ship (the `.windsurf/` directory)

```
.windsurf/
├── workflows/                  # All /spec-* commands
│   ├── spec-help.md
│   ├── spec-plan.md
│   ├── spec-loop.md
│   ├── spec-task.md
│   ├── spec-verify.md
│   ├── spec-merge.md
│   ├── spec-status.md
│   └── spec-reset.md
├── skills/
│   └── spec-dev/
│       └── SKILL.md            # Embedded templates + rules
├── hooks.json                  # Lifecycle hooks
├── hooks/
│   ├── setup_worktree.sh       # Worktree init
│   ├── auto-format.sh          # Auto-format on save
│   └── log_cascade.py          # Audit log
└── mailbox/                    # Inter-session coordination
    ├── README.md
    ├── board/
    │   ├── status.json
    │   └── claims.json
    ├── inbox/
    └── outbox/
```

Templates are embedded in `SKILL.md` — no separate template files to copy.

## Settings for Maximum Autonomy

| Setting | Value | Where |
|---------|-------|-------|
| Auto-Execution | **Turbo** | Windsurf Settings |
| Auto-Continue | **Enabled** | Windsurf Settings |
| Worktree Mode | **On** | Cascade input toggle |

## Parallel Work & Worktrees

> **Rule #1: One Cascade session per working tree.** Sessions sharing a branch will overwrite each other's changes. Always use worktrees or branches for parallel work.

### How to run parallel sessions

1. Toggle **Worktree Mode** on in the Cascade input bar
2. Each worktree Cascade gets its own isolated copy of the repo
3. Assign tasks: `/spec-task myfeature T3` in one, `/spec-task myfeature T4` in another
4. When done, merge back with `/spec-merge myfeature`

### Multiple specs

Break large efforts into independent specs:

```
.windloop/
├── auth/        # Authentication module
├── api/         # REST API endpoints
└── dashboard/   # Frontend dashboard
```

Each spec has its own lifecycle. Run them in parallel with worktree Cascades:

```
Cascade #1 (worktree) → /spec-loop auth
Cascade #2 (worktree) → /spec-loop api
Cascade #3 (worktree) → /spec-loop dashboard
```

Cross-spec dependencies are declared in `.windloop/dependencies.md`. Use `/spec-status` to monitor everything.

## Parallel Coordination (Mailbox Protocol)

Parallel Cascade sessions coordinate via `.windsurf/mailbox/`:

- **`board/claims.json`** — claim tasks to prevent double-work
- **`board/status.json`** — shared state visible to all sessions
- **`inbox/<session>/`** — messages TO a session
- **`outbox/<session>/`** — completion signals FROM a session

Patterns: Lead-Worker, Claim Board, Pipeline. See `.windsurf/mailbox/README.md`.

## Try It: Example Spec

Test the full loop end-to-end in any empty git repo:

```bash
# 1. Create a test repo
mkdir test-project && cd test-project && git init

# 2. Install windloop
cp -r path/to/windloop/.windsurf/ .windsurf/

# 3. Open in Windsurf
windsurf .
```

Then in Cascade:

```
/spec-plan calculator
```

Describe something simple like: *"A Python CLI calculator that supports add, subtract, multiply, divide. Use pytest for testing."*

Cascade will:
1. Create `.windloop/calculator/spec.md` — review and approve
2. Create `.windloop/calculator/design.md` — review and approve
3. Create `.windloop/calculator/tasks.md` — review and approve
4. Auto-scaffold `.windloop/index.md`, `AGENTS.md`, etc.

Then:

```
/spec-loop calculator
```

Watch Cascade implement each task autonomously: create files, write tests, run verification, commit, and move to the next task.

Check progress anytime:

```
/spec-status
```

## Hooks

- **`post_setup_worktree`** — copies `.env`, installs deps in new worktrees
- **`post_write_code`** — auto-formats (ruff for Python, prettier for JS/TS)
- **`post_cascade_response`** — logs responses to `.windsurf/cascade_log.jsonl`

## License

MIT
