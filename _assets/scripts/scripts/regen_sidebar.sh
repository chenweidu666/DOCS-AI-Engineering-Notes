#!/usr/bin/env bash
# 侧栏由根目录 _sidebar.md 手工维护；本脚本仅调用 gen_sidebar.py 打印提示，不覆盖侧栏。
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/gen_sidebar.py
