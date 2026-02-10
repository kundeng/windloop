#!/bin/bash
# Post-worktree-setup hook: copies env files and installs dev dependencies
# This runs inside the NEW worktree directory.
# $ROOT_WORKSPACE_PATH points to the original workspace.

set -e

echo "=== Setting up worktree ==="

# Copy environment files if they exist
for envfile in .env .env.local .env.development; do
    if [ -f "$ROOT_WORKSPACE_PATH/$envfile" ]; then
        cp "$ROOT_WORKSPACE_PATH/$envfile" "$envfile"
        echo "Copied $envfile"
    fi
done

# Install Python dev dependencies if pyproject.toml exists
if [ -f "pyproject.toml" ]; then
    if command -v pip &> /dev/null; then
        pip install -e ".[dev]" 2>/dev/null || pip install -e . 2>/dev/null || true
        echo "Installed Python dependencies"
    fi
fi

# Install Node dependencies if package.json exists
if [ -f "package.json" ]; then
    if command -v npm &> /dev/null; then
        npm install
        echo "Installed npm dependencies"
    fi
fi

echo "=== Worktree setup complete ==="
exit 0
