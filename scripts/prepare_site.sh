#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DIST_DIR="${ROOT_DIR}/dist"
SRC_DIR="${ROOT_DIR}/textbooks"

rm -rf "${DIST_DIR}"
mkdir -p "${DIST_DIR}"

# Publish textbooks as a static website root.
cp -R "${SRC_DIR}/." "${DIST_DIR}/"
touch "${DIST_DIR}/.nojekyll"

echo "Prepared static site in ${DIST_DIR}"
