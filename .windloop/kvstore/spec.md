# Specification: kvstore

## Overview
<!-- Brief description of what this project does and why -->
A tiny Python CLI key-value store. Three commands (`get`, `set`, `delete`) persist data to a local JSON file. Zero external dependencies beyond the standard library.

## Goals
- [ ] Provide a simple CLI for key-value CRUD operations
- [ ] Persist data reliably to `data.json`
- [ ] 100% test coverage
- [ ] Clean, lint-free code

## Architecture

### Tech Stack
- **Language**: Python 3.11+
- **Framework**: None (stdlib only — `argparse`, `json`, `pathlib`)
- **Testing**: pytest + pytest-cov
- **Linter**: ruff

### Directory Structure
```
kv.py              # CLI entry point + all logic
data.json          # persisted key-value data (created at runtime)
tests/
  test_kv.py       # all tests
pyproject.toml     # project config (ruff + pytest settings)
```

## Requirements

### Functional Requirements
1. **FR-1**: `python kv.py set <key> <value>` — stores key-value pair in `data.json`
2. **FR-2**: `python kv.py get <key>` — prints value to stdout; exits with code 1 if key not found
3. **FR-3**: `python kv.py delete <key>` — removes key from `data.json`; no error if key missing

### Non-Functional Requirements
1. **NFR-1**: No external runtime dependencies (stdlib only)
2. **NFR-2**: 100% line coverage via pytest-cov
3. **NFR-3**: Zero ruff lint violations

## Data Models
<!-- Key data structures, schemas, interfaces -->
- **Store**: A flat `dict[str, str]` serialized as JSON in `data.json`
- Keys and values are always strings

## Testing Strategy
- **Test command**: `pytest --cov=kv --cov-report=term-missing --cov-fail-under=100`
- **Lint command**: `ruff check .`
- **Coverage target**: 100%

## Constraints
<!-- Important decisions and constraints -->
- Single-file implementation (`kv.py`) — keep it simple
- `data.json` is created on first write if it doesn't exist
- Reading a missing `data.json` is treated as an empty store
- All keys and values are strings (no type coercion)

## Out of Scope
<!-- What this project explicitly does NOT do -->
- Nested values or complex data types
- Concurrent access / file locking
- Remote storage or networking
- Shell completion
