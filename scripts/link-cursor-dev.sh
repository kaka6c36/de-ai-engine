#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$root/.cursor"
ln -sfn "$root/skills" "$root/.cursor/skills"
ln -sfn "$root/agents" "$root/.cursor/agents"
echo "Linked .cursor/skills -> skills"
echo "Linked .cursor/agents -> agents"
