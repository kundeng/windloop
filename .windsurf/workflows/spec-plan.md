---
description: Generate a spec and task breakdown from an idea. Use when you want to plan a feature, design a system, create requirements, break down work into tasks, start a new project, or refine an existing spec. Keywords: plan, design, feature, idea, requirements, tasks, breakdown, create, build, new, refine, update, spec, windloop.
---

## Plan a Spec

Usage: `/spec-plan <name> [create|refine|update]`

Modes (auto-detected if not specified):
- **Create**: `.windloop/SPEC/` doesn't exist → build from scratch
- **Refine**: spec exists, user wants to rethink requirements or design (broader changes)
- **Update**: spec exists, user wants to adjust specific items discovered during implementation (targeted back-propagation)

Let SPEC be the spec name.

---

### Mode: Create

#### 0. Scaffold `.windloop/` if it doesn't exist

If `.windloop/` directory does not exist, create it with:
- `.windloop/index.md` — use the index.md template from the spec-driven-dev skill
- `.windloop/dependencies.md` — use the dependencies.md template from the skill

If the host project has an existing `AGENTS.md`, read it and check if it already contains a "Windloop" section. If not, append the AGENTS.md snippet from the spec-driven-dev skill. If no `AGENTS.md` exists, create one with just the windloop snippet.

#### 1. Scan existing project

Before gathering requirements, understand what already exists:
- Read `README.md`, `AGENTS.md`, `package.json`, `pyproject.toml`, `Cargo.toml`, or any manifest files
- Scan the source directory structure (e.g. `src/`, `lib/`, `app/`)
- Read key source files to understand existing patterns, conventions, and architecture
- Note existing tests, linting config, CI setup

The spec should **align with the existing codebase** — preserve conventions, tech stack, and patterns unless the user explicitly asks for a rewrite or drastic change.

#### 2. Gather requirements

Ask the user to describe the idea, goals, and constraints. If they already provided this in the prompt, proceed.

#### 3. Generate spec.md

Create `.windloop/SPEC/spec.md` using the spec.md template from the spec-driven-dev skill:
- If existing code was found, align tech stack, directory structure, and conventions with it
- Frame requirements as **numbered user stories** (R1.1, R1.2, etc.): "As a [role], I should be able to [action] so that [benefit]"
- Group requirements hierarchically by feature area (R1: Feature, R1.1, R1.2, R2: Feature, etc.)
- Include non-functional requirements (NF1, NF2, etc.)
- Define clear testing strategy with actual commands
- List specific data models and interfaces

Present the spec to the user for review. Iterate until approved.

#### 4. Generate design.md

Create `.windloop/SPEC/design.md` using the design.md template from the spec-driven-dev skill:
- If existing code was found, reflect the actual architecture (don't redesign what works)
- Define module architecture and interfaces
- Specify data flow between components
- Write **property tests** (P1, P2, etc.) — each property must **validate specific requirements** from spec.md (e.g. "Validates: R1.1, R1.2")
- Every requirement should be covered by at least one property
- Document error handling strategy and edge cases

Present the design to the user for review. Iterate until approved.

#### 5. Generate tasks.md

Create `.windloop/SPEC/tasks.md` using the tasks.md template from the spec-driven-dev skill:
- Each task completable in a single Cascade session
- Each task lists which **requirements** it fulfills (e.g. `Requirements: R1.1, R1.2`)
- Each task lists which **properties** it should satisfy (e.g. `Properties: P1`)
- Include clear acceptance criteria with checkable items
- Specify exact files to create/modify
- Include a verification command for each task
- **Minimize dependencies**: only depend on tasks that produce something this task directly needs. Avoid chaining tasks sequentially when they can run in parallel. More independent tasks = more parallelism.
- No circular deps
- Order by phase: Foundation → Core → E2E Tests → Polish
- **Property tests** go inline with implementation tasks (in the `Tests` field)
- **E2E tests** are separate tasks in their own phase, each validating a user story end-to-end
- Every requirement from spec.md should be covered by at least one task

#### 6. Create progress.txt

Create `.windloop/SPEC/progress.txt` using the progress.txt template from the skill.

#### 7. Register the spec

Add an entry for SPEC in `.windloop/index.md`.

If cross-spec dependencies exist, add them to `.windloop/dependencies.md`.

// turbo
#### 8. Commit

```
git add -A && git commit -m "spec(SPEC): create spec, design, and tasks"
```

#### 9. Report

Print the task summary table:

```
Spec SPEC is ready with N tasks across M phases:

  T1: [title]  [status]
  T2: [title]  [status]  (depends: T1)
  T3: [title]  [status]  (depends: T1, T2)
  ...
```

Then suggest next steps:
- `/spec-loop SPEC` for autonomous implementation
- `/spec-task SPEC T1` to start with a specific task
- `/spec-status` to see the dashboard

---

### Mode: Refine

Use when rethinking requirements or design more broadly (e.g. "we need to change the approach to auth").

1. Read all existing spec artifacts: `.windloop/SPEC/spec.md`, `design.md`, `tasks.md`, `progress.txt`
2. Ask the user what should change. If they already described changes in the prompt, proceed.
3. Identify which **requirements** (R-numbers) are affected.
4. Update `spec.md` — add, modify, or remove requirements. Preserve unchanged requirements and their numbering.
5. Update `design.md` — adjust affected modules and properties. For each changed requirement, check that its validating properties (P-numbers) still hold. Add/update properties as needed.
6. Update `tasks.md`:
   - For **completed tasks** (`[x]`): do NOT uncheck them. If their requirements changed, add a new follow-up task to reconcile.
   - For **pending tasks** (`[ ]`): update requirements, properties, acceptance criteria, and files as needed.
   - Add new tasks if new requirements were introduced.
   - Remove tasks only if their requirements were fully removed AND no code was written for them.
7. Present a **change summary** showing: requirements changed → properties affected → tasks added/modified.

8. Print the updated task summary table (all tasks with IDs, titles, status, and dependencies).

// turbo
9. Commit: `git add -A && git commit -m "spec(SPEC): refine requirements and propagate to design/tasks"`

---

### Mode: Update

Use for targeted adjustments discovered during implementation (e.g. "T3 revealed we need an extra API endpoint" or "the data model needs a new field").

1. Read all existing spec artifacts: `.windloop/SPEC/spec.md`, `design.md`, `tasks.md`, `progress.txt`
2. Ask the user what was discovered. If they already described it in the prompt, proceed.
3. Trace the change through the chain:

   **If the change starts from a task** (bottom-up):
   - Identify which requirements the task references
   - Determine if the requirement needs updating or a new sub-requirement (e.g. R1.3)
   - Update `spec.md` with the new/modified requirement
   - Update `design.md` — adjust the relevant property or add a new one, with `Validates:` reference
   - Update the task's acceptance criteria and any dependent tasks

   **If the change starts from a requirement** (top-down):
   - Update `spec.md`
   - Propagate to `design.md` (properties)
   - Propagate to `tasks.md` (affected tasks)

4. For completed tasks: do NOT uncheck. Add follow-up tasks if reconciliation is needed.
5. Present a **change summary**: what changed at each level (spec → design → tasks).

6. Print the updated task summary table (all tasks with IDs, titles, status, and dependencies).

// turbo
7. Commit: `git add -A && git commit -m "spec(SPEC): update — [brief description of what changed]"`
