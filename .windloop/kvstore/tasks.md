# Tasks: kvstore

<!--
STATUS: [ ] pending | [x] done | [!] blocked
PRIORITY: P0 critical | P1 important | P2 nice-to-have
DEPENDS: task IDs that must complete first
-->

## Phase 1: Foundation

### T1: Project setup and store I/O `P0`
- **Description**: Create `pyproject.toml` with ruff + pytest config, and implement `kv.py` with `load_store()` and `save_store()` functions. No CLI yet.
- **Acceptance criteria**:
  - [ ] `pyproject.toml` exists with ruff and pytest-cov configuration
  - [ ] `load_store(path)` returns `{}` when file is missing
  - [ ] `load_store(path)` returns parsed dict when file exists
  - [ ] `save_store(path, store)` writes valid JSON to disk
  - [ ] Round-trip: save then load returns identical dict
- **Files**: `kv.py`, `pyproject.toml`
- **Verify**: `python -c "from kv import load_store, save_store; print('OK')"`
- **Properties**: P1 (round-trip), P4 (empty store on missing file)
- **Status**: [ ]

## Phase 2: Core

### T2: CLI commands and argument parsing `P0`
- **Description**: Add argparse-based CLI with `set`, `get`, `delete` subcommands. Wire up `cmd_set`, `cmd_get`, `cmd_delete`, and `main()`. Use `sys.exit()` in `__main__` block.
- **Depends**: T1
- **Acceptance criteria**:
  - [ ] `python kv.py set foo bar` stores `{"foo": "bar"}` in `data.json`
  - [ ] `python kv.py get foo` prints `bar` to stdout, exits 0
  - [ ] `python kv.py get missing` prints error to stderr, exits 1
  - [ ] `python kv.py delete foo` removes key, exits 0
  - [ ] `python kv.py delete missing` exits 0 (silent no-op)
  - [ ] Running with no args prints usage
- **Files**: `kv.py`
- **Verify**: `python kv.py set test_key test_val && python kv.py get test_key && python kv.py delete test_key`
- **Properties**: P1, P2, P3, P5
- **Status**: [ ]

## Phase 3: Polish

### T3: Full test suite with 100% coverage + lint `P0`
- **Description**: Write comprehensive pytest tests covering all commands, edge cases, and property tests from design.md. Ensure 100% line coverage and zero ruff violations.
- **Depends**: T2
- **Acceptance criteria**:
  - [ ] `tests/test_kv.py` exists with tests for all 5 properties (P1–P5)
  - [ ] Tests cover: set, get (found + not found), delete (found + not found), missing data.json, overwrite
  - [ ] `pytest --cov=kv --cov-report=term-missing --cov-fail-under=100` passes
  - [ ] `ruff check .` passes with zero violations
- **Files**: `tests/test_kv.py`
- **Verify**: `pytest --cov=kv --cov-report=term-missing --cov-fail-under=100 && ruff check .`
- **Properties**: P1, P2, P3, P4, P5
- **Status**: [ ]
