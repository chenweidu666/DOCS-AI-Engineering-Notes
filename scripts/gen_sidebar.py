#!/usr/bin/env python3
"""根据当前目录（3_技术文档 根）下的 .md 生成 Docsify 侧栏 _sidebar.md。"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIDEBAR = ROOT / "_sidebar.md"
SKIP_DIRS = {"scripts", ".git"}


def main() -> None:
    md_files: list[Path] = []
    for p in sorted(ROOT.rglob("*.md")):
        if p.name == "_sidebar.md":
            continue
        try:
            rel = p.relative_to(ROOT)
        except ValueError:
            continue
        if rel.parts and rel.parts[0] in SKIP_DIRS:
            continue
        md_files.append(rel)

    lines: list[str] = []
    lines.append("* [首页](/)")
    lines.append("")

    buckets: dict[str, list[Path]] = {}
    for rel in md_files:
        key = rel.parts[0] if len(rel.parts) > 1 else ""
        buckets.setdefault(key, []).append(rel)

    for key in sorted(buckets.keys(), key=lambda k: (k == "", k)):
        items = buckets[key]
        if key == "":
            lines.append("* 根目录")
            for rel in items:
                title = rel.stem.replace("_", " ")
                lines.append(f"  * [{title}]({rel.as_posix()})")
            lines.append("")
            continue
        lines.append(f"* **{key}**")
        for rel in sorted(items):
            title = rel.stem
            lines.append(f"  * [{title}]({rel.as_posix()})")
        lines.append("")

    SIDEBAR.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
