#!/usr/bin/env bash
# 文档已在当前目录维护，仅需刷新 Docsify 侧栏。
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/gen_sidebar.py
