---
name: spec-driven-dev
description: Guides spec-driven autonomous development. Use when implementing features from a spec, breaking down requirements into tasks, or running the autonomous development loop.
---

## Spec-Driven Development

This skill powers the windloop framework. Specs live in `.windloop/<name>/` and are registered in `.windloop/index.md`.

### Spec Lifecycle

```
idea → spec.md → design.md (with property tests) → tasks.md → [implement loop] → done
```

Each spec directory contains:
- `spec.md` — requirements and constraints
- `design.md` — architecture, interfaces, property tests
- `tasks.md` — ordered work items with dependencies
- `progress.txt` — auto-updated log

### Commands

| Command | Purpose |
|---------|---------|
| `/spec-help` | Onboarding guide |
| `/spec-plan <name>` | Create or refine a spec (idea → spec → design → tasks) |
| `/spec-loop <name>` | Autonomous loop: pick task → implement → test → commit → repeat |
| `/spec-task <name> T[N]` | Implement single task (parallel worktree use) |
| `/spec-verify <name>` | Run all tests + lint |
| `/spec-merge <name>` | Review and validate after merges |
| `/spec-status` | Dashboard: progress, sessions, mailbox |
| `/spec-reset <name>` | Clear progress for re-run |

### Rules

1. Read `.windloop/index.md` first to find specs
2. Read spec.md AND design.md before implementing
3. Check task dependencies — never skip ahead
4. Run verify after implementation; fix up to 3 times before BLOCKED
5. Commit per task: `feat(<spec>/T[N]): [description]`
6. Update `tasks.md` (checkbox) and `progress.txt` (log line) after each task
7. Keep changes minimal and focused

### Scaffolding

When `/spec-plan` runs and `.windloop/` doesn't exist, auto-create:
```
.windloop/
  index.md
  dependencies.md
  <name>/
    spec.md
    design.md
    tasks.md
    progress.txt
```

If the host project already has an `AGENTS.md`, append the windloop snippet (see below). If not, create it.

### AGENTS.md Snippet

When creating or updating AGENTS.md for a host project, append this block:

```markdown
## Windloop (Spec-Driven Development)

This project uses windloop for spec-driven autonomous development.

- Specs live in `.windloop/<name>/` — read `.windloop/index.md` for the registry
- Run `/spec-help` for available commands
- Run `/spec-plan <name>` to create or refine a spec
- Run `/spec-loop <name>` for autonomous implementation
- Run `/spec-status` to check progress across all specs
- Commit format: `feat(<spec>/T[N]): [description]`
```

### Embedded Templates

#### spec.md template

```markdown
# Specification: [PROJECT NAME]

## Overview
<!-- Brief description of what this project does and why -->

## Goals
- [ ] Goal 1
- [ ] Goal 2

## Architecture

### Tech Stack
- **Language**:
- **Framework**:
- **Testing**:
- **Linter**:

### Directory Structure
\```
src/
tests/
\```

## Requirements

### Functional Requirements
1. **FR-1**: [Description]

### Non-Functional Requirements
1. **NFR-1**: [Description]

## Data Models
<!-- Key data structures, schemas, interfaces -->

## Testing Strategy
- **Test command**: `[command]`
- **Lint command**: `[command]`
- **Coverage target**: [percentage]

## Constraints
<!-- Important decisions and constraints -->

## Out of Scope
<!-- What this project explicitly does NOT do -->
```

#### design.md template

```markdown
# Design: [PROJECT NAME]

## Architecture Overview
<!-- High-level component diagram or description -->

## Module Design

### [Module 1]
- **Purpose**: [what it does]
- **Interface**:
  \```
  [function signatures, class interfaces, API endpoints]
  \```
- **Dependencies**: [what it depends on]

## Data Flow
<!-- How data moves through the system -->

## Error Handling Strategy
<!-- How errors are propagated and handled -->

## Property Tests

Properties that must hold true across the system. These guide implementation and serve as invariants for testing.

### [Property 1]: [Name]
- **Statement**: [formal or semi-formal property statement]
- **Example**: [concrete example]
- **Test approach**: [how to verify this property]

### [Property 2]: [Name]
- **Statement**: [property]
- **Example**: [example]
- **Test approach**: [approach]

## Edge Cases
<!-- Known edge cases and how they should be handled -->

## Security Considerations
<!-- If applicable -->
```

#### tasks.md template

```markdown
# Tasks: [PROJECT NAME]

<!--
STATUS: [ ] pending | [x] done | [!] blocked
PRIORITY: P0 critical | P1 important | P2 nice-to-have
DEPENDS: task IDs that must complete first
-->

## Phase 1: Foundation

### T1: [Task title] `P0`
- **Description**: [What to implement]
- **Acceptance criteria**:
  - [ ] Criterion 1
  - [ ] Criterion 2
- **Files**: `src/...`
- **Verify**: `[command]`
- **Status**: [ ]

### T2: [Task title] `P0`
- **Description**: [What to implement]
- **Depends**: T1
- **Acceptance criteria**:
  - [ ] Criterion 1
- **Files**: `src/...`
- **Verify**: `[command]`
- **Status**: [ ]

## Phase 2: Core

### T3: [Task title] `P1`
- **Depends**: T1, T2
- ...

## Phase 3: Polish

### T4: [Task title] `P2`
- **Depends**: T3
- ...
```

#### progress.txt template

```
# Progress Log: [PROJECT NAME]
# Auto-updated by spec-loop workflow
# Format: [TIMESTAMP] [STATUS] [TASK_ID] - [DESCRIPTION]
# STATUS: DONE | BLOCKED | SKIPPED | IN_PROGRESS
```

#### index.md template

```markdown
# Windloop Specs

| Spec | Status | Description |
|------|--------|-------------|
| [name] | active | [description] |
```

#### dependencies.md template

```markdown
# Spec Dependencies

Format: `<spec> -> <prerequisite>` (dependent -> prerequisite)

<!-- Example:
api -> auth
dashboard -> api
-->
```

### Parallel Execution

For independent tasks, use worktree mode:
1. Open a new Cascade in Worktree mode
2. Run `/spec-task <name> T[N]`
3. Merge back when done

### Mailbox Protocol

For parallel session coordination via `.windsurf/mailbox/`:
- `board/claims.json` — task claims (prevents double-work)
- `board/status.json` — shared state
- `inbox/<session>/` — messages TO a session
- `outbox/<session>/` — completion signals FROM a session

See `.windsurf/mailbox/README.md` for details.
