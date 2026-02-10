# Project Specification: Windloop Test Project

## Overview
A small Python utility library used to validate the spec-driven autonomous loop workflow.
The project implements a simple `taskrunner` CLI that reads a JSON task file, executes
shell commands for each task, and reports results. This is intentionally small so the
full spec-loop can be tested end-to-end in minutes.

## Goals
- [ ] Validate that the `/spec-loop` workflow can autonomously implement a multi-task project
- [ ] Demonstrate parallel worktree Cascades on independent tasks
- [ ] Prove the hooks, skills, and workflows integrate correctly

## Architecture

### Tech Stack
- **Language**: Python 3.10+
- **Framework**: None (stdlib only)
- **Testing**: pytest
- **Build**: N/A (pure Python)
- **Lint**: ruff

### Directory Structure
```
src/
├── taskrunner/
│   ├── __init__.py
│   ├── cli.py          # CLI entry point
│   ├── loader.py       # Load tasks from JSON
│   ├── executor.py     # Execute task commands
│   └── reporter.py     # Report results
tests/
├── conftest.py
├── test_loader.py
├── test_executor.py
├── test_reporter.py
└── test_cli.py
```

## Requirements

### Functional Requirements
1. **FR-1**: Load a JSON task file with structure `{"tasks": [{"name": "...", "command": "...", "timeout": N}]}`
2. **FR-2**: Execute each task's command via subprocess with configurable timeout (default 30s)
3. **FR-3**: Capture stdout, stderr, and exit code for each task
4. **FR-4**: Generate a summary report (pass/fail count, duration per task, total duration)
5. **FR-5**: CLI accepts `--file <path>` and `--output <path>` arguments
6. **FR-6**: Exit code 0 if all tasks pass, 1 if any fail

### Non-Functional Requirements
1. **NFR-1**: No external dependencies beyond stdlib + dev deps (pytest, ruff)
2. **NFR-2**: All functions have type hints
3. **NFR-3**: Test coverage for all modules

## Data Models

### Task (input)
```python
@dataclass
class Task:
    name: str
    command: str
    timeout: int = 30
```

### TaskResult (output)
```python
@dataclass
class TaskResult:
    name: str
    success: bool
    exit_code: int
    stdout: str
    stderr: str
    duration: float
```

### Report (output)
```python
@dataclass
class Report:
    results: list[TaskResult]
    total_duration: float
    passed: int
    failed: int
```

## Testing Strategy
- **Unit tests**: pytest, target 100% of loader/executor/reporter
- **Integration test**: CLI end-to-end with a sample task file
- **Verification command**: `python -m pytest tests/ -v`
- **Lint command**: `ruff check src/ tests/`
- **Build command**: N/A

## Constraints & Decisions
- Pure stdlib to keep it simple and dependency-light
- subprocess.run for command execution (not async)
- JSON for task files (not YAML) to avoid external deps

## Out of Scope
- Parallel task execution
- Task dependencies
- Remote execution
