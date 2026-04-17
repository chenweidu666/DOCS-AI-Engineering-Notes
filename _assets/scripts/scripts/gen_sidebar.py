#!/usr/bin/env python3
"""
侧栏已由仓库根目录 _sidebar.md 手工维护（七章主线 + 项目总结）。

历史行为：本脚本曾根据 docs/projects/ 生成侧栏，会覆盖 _sidebar.md。
项目镜像已迁至 ../归档/from_3_技术文档/projects/，请勿再运行本脚本覆盖侧栏。

若需重新生成「仅含 projects」的旧式侧栏，请从 git 历史恢复本文件先前版本后自行承担覆盖风险。
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIDEBAR = ROOT / "_sidebar.md"


def main() -> None:
    print("跳过：_sidebar.md 为手工维护（七章结构）。见 scripts/README.md。", file=sys.stderr)
    if not SIDEBAR.is_file():
        raise SystemExit(f"缺少 {SIDEBAR}")
    print(f"当前侧栏文件：{SIDEBAR}（未修改）")


if __name__ == "__main__":
    main()
