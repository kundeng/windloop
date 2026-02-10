#!/bin/bash
# Post-write hook: auto-formats files after Cascade edits them.
# Receives JSON on stdin with tool_info.file_path

input=$(cat)

# Extract file path (requires jq; gracefully skip if not available)
if ! command -v jq &> /dev/null; then
    exit 0
fi

file_path=$(echo "$input" | jq -r '.tool_info.file_path // empty')

if [ -z "$file_path" ] || [ ! -f "$file_path" ]; then
    exit 0
fi

# Python files: format with ruff if available
if [[ "$file_path" == *.py ]]; then
    if command -v ruff &> /dev/null; then
        ruff format "$file_path" 2>/dev/null || true
    fi
fi

# JS/TS files: format with prettier if available
if [[ "$file_path" == *.js ]] || [[ "$file_path" == *.ts ]] || [[ "$file_path" == *.tsx ]] || [[ "$file_path" == *.jsx ]]; then
    if command -v prettier &> /dev/null; then
        prettier --write "$file_path" 2>/dev/null || true
    fi
fi

exit 0
