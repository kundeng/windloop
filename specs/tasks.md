# Tasks: Windloop Test Project

<!--
STATUS KEY:
  - [ ] = pending
  - [x] = done
  - [!] = blocked

DEPENDENCY FORMAT:
  depends: T1, T2  (must be done before this task)

PRIORITY:
  P0 = critical path
  P1 = important
  P2 = nice to have
-->

## Phase 1: Foundation

### T1: Project scaffolding `P0`
- **Description**: Create the project structure with `pyproject.toml`, `src/taskrunner/__init__.py`, empty module files, and `tests/conftest.py`. Configure pytest and ruff in `pyproject.toml`.
- **Acceptance criteria**:
  - [ ] `pyproject.toml` exists with pytest and ruff config
  - [ ] `src/taskrunner/__init__.py` exists
  - [ ] `src/taskrunner/cli.py`, `loader.py`, `executor.py`, `reporter.py` exist (can be empty stubs)
  - [ ] `tests/conftest.py` exists
  - [ ] `python -m pytest tests/ -v` runs without error (0 tests collected is OK)
- **Files**: `pyproject.toml`, `src/taskrunner/*.py`, `tests/conftest.py`
- **Verify**: `python -m pytest tests/ -v`
- **Status**: [ ]

### T2: Data models `P0`
- **Description**: Implement `Task`, `TaskResult`, and `Report` dataclasses in `src/taskrunner/__init__.py` with type hints as specified in the spec.
- **Depends**: T1
- **Acceptance criteria**:
  - [ ] All three dataclasses defined with correct fields and defaults
  - [ ] Type hints on all fields
  - [ ] Can be imported: `from taskrunner import Task, TaskResult, Report`
- **Files**: `src/taskrunner/__init__.py`
- **Verify**: `python -c "from taskrunner import Task, TaskResult, Report; print('OK')"`
- **Status**: [ ]

## Phase 2: Core Features

### T3: Task loader `P0`
- **Description**: Implement `load_tasks(path: str) -> list[Task]` in `loader.py`. Should read a JSON file and return a list of `Task` objects. Raise `FileNotFoundError` if file missing, `ValueError` if JSON is malformed or missing required fields.
- **Depends**: T2
- **Acceptance criteria**:
  - [ ] Loads valid JSON task file into list of Task objects
  - [ ] Raises FileNotFoundError for missing file
  - [ ] Raises ValueError for invalid JSON structure
  - [ ] Tests in `tests/test_loader.py` cover all three cases
- **Files**: `src/taskrunner/loader.py`, `tests/test_loader.py`
- **Verify**: `python -m pytest tests/test_loader.py -v`
- **Status**: [ ]

### T4: Task executor `P0`
- **Description**: Implement `execute_task(task: Task) -> TaskResult` in `executor.py`. Uses `subprocess.run` with the task's command and timeout. Captures stdout, stderr, exit code, and measures duration. Handles `subprocess.TimeoutExpired` by returning a failed result.
- **Depends**: T2
- **Acceptance criteria**:
  - [ ] Executes command and captures output
  - [ ] Measures duration
  - [ ] Handles timeout gracefully (returns failed TaskResult)
  - [ ] Tests in `tests/test_executor.py` cover success, failure, and timeout
- **Files**: `src/taskrunner/executor.py`, `tests/test_executor.py`
- **Verify**: `python -m pytest tests/test_executor.py -v`
- **Status**: [ ]

### T5: Report generator `P1`
- **Description**: Implement `generate_report(results: list[TaskResult]) -> Report` and `format_report(report: Report) -> str` in `reporter.py`. The formatter outputs a human-readable summary with pass/fail counts, per-task details, and total duration.
- **Depends**: T2
- **Acceptance criteria**:
  - [ ] `generate_report` computes passed/failed counts and total duration
  - [ ] `format_report` returns a readable multi-line string
  - [ ] Tests in `tests/test_reporter.py` cover both functions
- **Files**: `src/taskrunner/reporter.py`, `tests/test_reporter.py`
- **Verify**: `python -m pytest tests/test_reporter.py -v`
- **Status**: [ ]

## Phase 3: Integration

### T6: CLI entry point `P1`
- **Description**: Implement the CLI in `cli.py` using `argparse`. Accepts `--file <path>` (required) and `--output <path>` (optional, defaults to stdout). Wires together loader -> executor -> reporter. Exit code 0 if all pass, 1 if any fail.
- **Depends**: T3, T4, T5
- **Acceptance criteria**:
  - [ ] `python -m taskrunner --file tasks.json` works end-to-end
  - [ ] `--output report.txt` writes report to file
  - [ ] Exit code reflects pass/fail
  - [ ] Tests in `tests/test_cli.py` cover the happy path and error cases
- **Files**: `src/taskrunner/cli.py`, `src/taskrunner/__main__.py`, `tests/test_cli.py`
- **Verify**: `python -m pytest tests/test_cli.py -v`
- **Status**: [ ]

### T7: Full test suite + lint pass `P1`
- **Description**: Ensure all tests pass and ruff reports no issues. Fix any remaining lint errors.
- **Depends**: T6
- **Acceptance criteria**:
  - [ ] `python -m pytest tests/ -v` all green
  - [ ] `ruff check src/ tests/` no errors
- **Files**: all
- **Verify**: `python -m pytest tests/ -v && ruff check src/ tests/`
- **Status**: [ ]
