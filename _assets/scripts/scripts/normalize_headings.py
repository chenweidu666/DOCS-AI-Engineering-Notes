#!/usr/bin/env python3
"""
[已弃用] 旧版「去数字 + 居中 <h1>」流水线。当前规范见 .cursor/rules/doc-heading-numbering.mdc，
请使用：python3 scripts/apply_doc_format.py

历史行为简述（勿在新稿上执行）：
- 去掉标题前的数字编号（如 1.1.、1.2.1.）。
- 原 ## 级小节 → 一级标题，使用 <h1 align="center">…</h1> 居中。
- 原 ### → ##、#### → ### …（整体少一个 #）。
- 文首 **1. 篇名** → 居中 <p><strong>篇名</strong></p>，去掉篇名前数字。
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"

ATX_RE = re.compile(r"^(#{1,6})\s+((?:\d+\.)+\s*)?(.*)$")
TITLE_LINE_RE = re.compile(r"^\*\*((?:\d+\.\s*)?)(.+?)\*\*\s*$")


def transform_file(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_code = False
    title_consumed = False

    for line in lines:
        s = line.rstrip("\n\r")
        st = s.strip()

        if st.startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue

        if not title_consumed:
            if st == "":
                out.append(line)
                continue
            m = TITLE_LINE_RE.match(s)
            if m:
                raw_title = m.group(2).strip()
                out.append(
                    f'<p align="center"><strong>{html.escape(raw_title)}</strong></p>\n\n'
                )
                title_consumed = True
                continue
            title_consumed = True

        m = ATX_RE.match(s)
        if m:
            hashes = m.group(1)
            rest = (m.group(3) or "").strip()
            old_level = len(hashes)
            new_level = max(1, old_level - 1)
            ending = "\n" if line.endswith("\n") else ""
            if new_level == 1:
                out.append(f'<h1 align="center">{html.escape(rest)}</h1>{ending}')
            else:
                out.append(f"{'#' * new_level} {rest}{ending}")
            continue

        out.append(line)

    return "".join(out)


def main() -> int:
    changed = 0
    for path in sorted(DOCS.rglob("*.md")):
        raw = path.read_text(encoding="utf-8")
        new = transform_file(raw)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            print(f"OK {path.relative_to(DOCS)}")
            changed += 1
    print(f"Done. Updated {changed} files.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
