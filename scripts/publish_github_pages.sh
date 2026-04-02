#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "${ROOT_DIR}"

REPO_NAME="${1:-$(basename "$ROOT_DIR")}"
OWNER="${2:-}"

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI is required." >&2
  exit 1
fi

if ! gh auth status -h github.com >/dev/null 2>&1; then
  echo "GitHub login is required. Run: gh auth login --hostname github.com --git-protocol https --web" >&2
  exit 1
fi

if [ -z "${OWNER}" ]; then
  OWNER="$(gh api user --jq .login)"
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git init
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  gh repo create "${OWNER}/${REPO_NAME}" --public --source=. --remote=origin --push=false
fi

current_branch="$(git branch --show-current || true)"
if [ -z "${current_branch}" ]; then
  git checkout -b main
elif [ "${current_branch}" != "main" ]; then
  git checkout -B main
fi

git add .
if ! git diff --cached --quiet; then
  git commit -m "Set up textbook site deployment and content updates"
fi

git push -u origin main

echo "Requested deployment. Check: https://github.com/${OWNER}/${REPO_NAME}/actions"
echo "Site URL (after Pages deploy): https://${OWNER}.github.io/${REPO_NAME}/"
