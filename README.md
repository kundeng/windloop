# Windloop

A spec-driven autonomous development framework for [Windsurf](https://windsurf.com). Copy one directory into any project and get an AI-powered development loop that turns ideas into working code.

**Kiro-compatible specs** — Windloop uses the same `requirements.md` → `design.md` → `tasks.md` spec format and EARS acceptance criteria as [Kiro](https://kiro.dev). Specs created in Windloop work in Kiro and vice versa — switch IDEs without losing your planning artifacts.

**Best-of-breed design** — We studied the top spec-driven skills on [skills.sh](https://skills.sh/?q=spec+driven) (including [jasonkneen/kiro](https://skills.sh/jasonkneen/kiro/spec-driven-development), [feiskyer/kiro-skill](https://skills.sh/feiskyer/claude-code-settings/kiro-skill), [xbklairith/kisune](https://skills.sh/xbklairith/kisune/spec-driven-planning), and [obra/superpowers](https://skills.sh/obra/superpowers)) and incorporated the strongest patterns: phase gate protocols, resume detection, quality checklists, decision documentation, and common-pitfall guardrails — on top of Windloop's unique autonomous implement loop, correctness properties, spec refinement engine, and parallel worktree execution.

## Install

**Option A — Copy into your project:**
```bash
cp -r path/to/windloop/.windsurf/ your-project/.windsurf/
```

**Option B — Install via [skills.sh](https://skills.sh):**
```bash
npx skills add https://github.com/kundeng/windloop/tree/main/.windsurf/skills/spec-driven-dev
```

Then open your project in Windsurf and type `/spec-help`.

## What It Does

```
idea → spec.md (why) → design.md (what + how) → tasks.md (steps) → [implement → test → commit → repeat]
```

Windloop turns Windsurf's Cascade into an autonomous development loop:

1. **`/spec-plan myfeature`** — Describe your idea. Cascade generates a spec, design (with property tests), and task breakdown. Auto-scaffolds `.windloop/` and `AGENTS.md`.
2. **`/spec-go myfeature`** — Cascade picks the next task, implements it, runs tests, commits, and repeats until done.
3. **`/spec-status`** — See progress across all specs and parallel sessions.

## Commands

| Command | Purpose |
|---------|---------|
| `/spec-help` | Onboarding guide |
| `/spec-plan <name> [create\|refine]` | Create or refine a spec (auto-detected) |
| `/spec-audit <name>` | Validate spec consistency: traceability, redundancy, drift |
| `/spec-go <name>` | Autonomous loop: pick task → implement → test → commit → repeat. Also resumes work. |
| `/spec-task <name> T[N]` | Implement a single task (for parallel worktree use) |
| `/spec-merge <name>` | Merge parallel branches/worktrees, resolve conflicts, verify |
| `/spec-status` | Dashboard: progress across all specs |
| `/spec-reset <name>` | Reset a spec for re-run |

> If only one spec exists, the `<name>` can be omitted.

## Spec Lifecycle

`/spec-plan` walks you through each stage interactively:

1. **spec.md** — The *why*: requirements as numbered user stories (R1.1, R1.2, NF1)
2. **design.md** — The *what + how*: architecture, tech stack, constraints, testing strategy, **property tests** that validate requirements ("P1 validates R1.1, R1.2")
3. **tasks.md** — Tasks reference requirements + properties they fulfill (`Requirements: R1.1` / `Properties: P1`)
4. **progress.txt** — Auto-updated log

Each stage is reviewed with you before proceeding.

**Modes**: `/spec-plan <name> create` (new) or `refine` (change anything — broad rethink or targeted fix). Auto-detected if omitted.

## What Gets Created

When you run `/spec-plan`, windloop auto-scaffolds:

```
.windloop/                      # Auto-created (not shipped)
├── index.md                    # Registry of all specs
├── dependencies.md             # Cross-spec dependency graph
└── <name>/                     # One directory per spec
    ├── spec.md                 # Requirements (why)
    ├── design.md               # Architecture, tech stack, constraints, properties (what + how)
    ├── tasks.md                # Task breakdown
    └── progress.txt            # Progress log

AGENTS.md                       # Windloop snippet appended (or created)
```

## What You Ship (the `.windsurf/` directory)

```
.windsurf/
├── skills/
│   └── spec-driven-dev/            # Portable skill (agentskills.io compatible)
│       ├── SKILL.md                # Core: rules, lifecycle, templates
│       └── references/             # Detailed workflow instructions
│           ├── spec-plan.md
│           ├── spec-audit.md
│           ├── spec-go.md
│           ├── spec-task.md
│           ├── spec-merge.md
│           ├── spec-status.md
│           ├── spec-reset.md
│           └── spec-help.md
├── workflows/                      # Thin wrappers for Windsurf slash commands
│   ├── spec-plan.md                # → references/spec-plan.md
│   ├── spec-audit.md
│   ├── spec-go.md
│   ├── spec-task.md
│   ├── spec-merge.md
│   ├── spec-status.md
│   ├── spec-reset.md
│   └── spec-help.md
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

**Option A — Windsurf Worktree Mode** (if available):
1. Toggle **Worktree Mode** in the Cascade input bar
2. Each worktree Cascade gets its own isolated copy of the repo
3. Assign tasks: `/spec-task myfeature T3` in one, `/spec-task myfeature T4` in another
4. When done, merge back with `/spec-merge myfeature`

**Option B — Manual worktrees** (always works):
```bash
git worktree add ../myproject-T2 main
git worktree add ../myproject-T3 main
# Open each in a separate Windsurf window, run /spec-task in each
# Merge back when done, then: git worktree remove ../myproject-T2
```

**Option C — Feature branches** (simplest):
```bash
git checkout -b task/T2 main   # open in Windsurf window 1
git checkout -b task/T3 main   # open in Windsurf window 2
# Merge branches when done
```

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
Cascade #1 (worktree) → /spec-go auth
Cascade #2 (worktree) → /spec-go api
Cascade #3 (worktree) → /spec-go dashboard
```

Cross-spec dependencies are declared in `.windloop/dependencies.md`. Use `/spec-status` to monitor everything.

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
/spec-go calculator
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
