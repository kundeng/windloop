
## Plan a Spec

Usage: `/spec-plan <name> [create|refine]`

Modes (auto-detected if not specified):
- **Create**: spec doesn't exist → build from scratch
- **Refine**: spec exists → update requirements, design, or tasks

Let SPEC be the spec name. Resolve SPEC_DIR using the **Spec Resolution** rules in SKILL.md.


### Mode: Create

#### 0. Scaffold

Each spec MUST have its own subdirectory — never put spec files directly in `.windloop/specs/` or `.kiro/specs/`.

**If `.kiro/` exists:**
1. Create `.kiro/specs/` if it doesn't exist
2. Create `.kiro/specs/SPEC/`
3. All spec files go inside `.kiro/specs/SPEC/`

**Otherwise:**
1. Create `.windloop/specs/` if it doesn't exist
2. Create `.windloop/specs/SPEC/`
3. All spec files go inside `.windloop/specs/SPEC/`

If the host project has an `AGENTS.md`, append the windloop snippet from SKILL.md. If not, create it.

#### 1. Scan existing project

Before gathering requirements, understand what already exists:
- Read `README.md`, `AGENTS.md`, `package.json`, `pyproject.toml`, `Cargo.toml`, or any manifest files
- Scan the source directory structure (e.g. `src/`, `lib/`, `app/`)
- Read key source files to understand existing patterns, conventions, and architecture
- Note existing tests, linting config, CI setup
- If steering docs exist (`.windloop/steering/` or `.kiro/steering/`), read `product.md`, `structure.md`, and `tech.md` for project context

The spec should **align with the existing codebase** — preserve conventions, tech stack, and patterns unless the user explicitly asks for a rewrite.

#### 2. Gather requirements

Ask the user to describe the idea, goals, and constraints. If they already provided this in the prompt, proceed.

#### 3. Generate requirements.md

Create `SPEC_DIR/requirements.md` using the template from SKILL.md. This is the *why*.

**Generate first, iterate second** — don't ask a long series of questions before producing anything. Write a complete first draft of requirements based on what you know, then iterate with the user. This is faster and gives the user something concrete to react to.

**EARS format quick reference** (Easy Approach to Requirements Syntax):
- `WHEN [event] THEN [system] SHALL [response]` — Event-driven
- `IF [condition] THEN [system] SHALL [response]` — Conditional
- `WHILE [state] [system] SHALL [response]` — State-driven
- `[system] SHALL [response]` — Unconditional

Requirements structure:
- Each requirement has a **User Story** and **WHEN/SHALL Acceptance Criteria**
- Number hierarchically: `Requirement 1`, criteria `1.1`, `1.2`, etc.
- Include non-functional requirements (`NF 1`, `NF 2`)
- Include a Glossary for shared vocabulary
- Define what is out of scope

Present to the user for review. Iterate until approved.

#### 4. Generate design.md

Create `SPEC_DIR/design.md` using the template from SKILL.md. This is the *what + how*:
- Research technical approaches if the domain is unfamiliar — use available tools (web search, documentation) to inform decisions. Summarize findings in the Architecture or Decisions section, not in a separate file.
- If existing code was found, align tech stack, directory structure, and conventions with it
- Define module architecture and interfaces
- Specify data flow between components
- Define testing strategy with actual commands (test, lint, coverage)
- Write **correctness properties** (Property 1, Property 2, etc.) — each must **validate specific requirements** (e.g. "Validates: Requirement 1.1, 1.2")
- Every requirement should be covered by at least one property
- Document error handling strategy and edge cases

Present to the user for review. Iterate until approved.

#### 5. Generate tasks.md

Create `SPEC_DIR/tasks.md` using the template from SKILL.md:
- Each task completable in a single Cascade session
- Each task lists **Depends**, **Requirements**, and **Properties**
- **Minimize dependencies**: only depend on tasks that produce something this task directly needs
- No circular deps
- Order by phase: Foundation → Core → E2E Tests → Polish
- **Property tests** and **E2E tests** are separate sub-tasks, not embedded in implementation tasks
- Every requirement should be covered by at least one task

#### 6. Create progress.txt

Create `SPEC_DIR/progress.txt` using the template from SKILL.md.

// turbo
#### 7. Commit

```
git add -A && git commit -m "spec(SPEC): create requirements, design, and tasks"
```

#### 8. Report

Print the task summary table:

```
Spec SPEC is ready with N tasks across M phases:

  1.1: [title]  [status]
  1.2: [title]  [status]  (depends: 1.1)
  2.1: [title]  [status]  (depends: 1.1, 1.2)
  ...
```

Then suggest next steps:
- `/spec-go SPEC` for autonomous implementation
- `/spec-task SPEC 1.1` to start with a specific task
- `/spec-status` to see the dashboard


### Mode: Refine

Use when anything in the spec needs to change — broad rethink, targeted fix, or acting on `/spec-audit` findings.

1. Read all spec artifacts: `SPEC_DIR/requirements.md`, `design.md`, `tasks.md`, `progress.txt`.
2. Scan the actual repo structure to detect spec↔disk drift.
3. Ask the user what should change. If they already described changes, proceed. If `/spec-audit` findings are available, use those.
4. Apply the **Spec Refinement Principles** from SKILL.md.
5. Trace changes through the full chain — both directions:

   **Top-down** (requirement changed → design → tasks):
   - Update `requirements.md` with new/modified/removed requirements
   - Propagate to `design.md` — adjust properties, update `Validates:` references
   - Propagate to `tasks.md` — update affected tasks, add new tasks if needed

   **Bottom-up** (implementation revealed something → tasks → design → requirements):
   - Update `requirements.md` with new/modified requirements
   - Update `design.md` — adjust properties
   - Update task acceptance criteria and dependent tasks

6. Update `requirements.md`: merge, remove, or rewrite per the principles.
7. Update `design.md`: merge overlapping properties, renumber, update `Validates:` references.
8. Update `tasks.md`:
   - **Completed tasks** (`[x]`): update references but do NOT uncheck. Add follow-up tasks if needed.
   - **Pending tasks** (`[ ]`): update requirements, properties, criteria as needed.
   - Add new tasks for new requirements. Remove tasks only if requirements were fully removed AND no code was written.
9. Validate traceability: every requirement → ≥1 property → ≥1 task. Flag gaps.
10. Update project documentation files if affected.
11. Present a **change summary**: requirements added/merged/removed, properties added/merged/renumbered, tasks updated/added/removed, traceability gaps.
12. Print the updated task summary table.

// turbo
13. Commit: `git add -A && git commit -m "spec(SPEC): refine — [brief description]"`
