#!/usr/bin/env python3
"""
将 docs 下 Markdown 对齐 canonical；基础层为 `1.1`～`1.4`（`01_基础层/`），KV/推理加速见 `03_部署与推理/3.1_KVCache与推理加速.md`

- 篇名：居中 div + 2rem 粗体（不用 Markdown # 篇名）
- 去掉文首/文末：导航、导读、关键词、本章性质、上一节/下一节/上一章/下一章 等 blockquote；
  去掉文首「上一节/下一节」类导航 Markdown 表（如 5.2 顶部）
- 大节：<h1 align="center">标题</h1> → 按出现顺序 # 1. 标题、# 2. …
- 小节：每个大节下的 ##（非 ###）→ ## N.1.、N.2. …（去掉旧 ## 上的数字前缀）
- **第七章**（`07_项目总结/7.1_CineMaker`、`7.2_OpenClaw-Deployment-Issues`）：先将首行「# 1. 篇名」改为篇名 div 并重编大节号；删文首「返回项目总览 | …」式导航句；围栏外 `# N.` 顺序重编号。

代码围栏内不修改。规范见 .cursor/rules/doc-heading-numbering.mdc
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

TITLE_P = re.compile(
    r'^<p\s+align="center"\s*>\s*<strong>([^<]+)</strong>\s*</p>\s*$',
    re.I,
)
TITLE_DIV = re.compile(
    r'^<div\s+style="text-align:\s*center[^"]*">\s*<strong>([^<]+)</strong>\s*</div>\s*$',
    re.I,
)

H1_CENTER = re.compile(
    r'<h1\s+align="center"\s*>([^<]*)</h1>',
    re.I,
)

META_BQ = re.compile(
    r"^>\s*\*\*(导航|本章导读|关键词|本章性质|下一章|下一节|上一章|上一节)\*\*[:：]"
)

ATX_MAJOR = re.compile(r"^# (\d+)\.\s+(.*)$")
ATX_H2 = re.compile(r"^## (.*)$")

CANONICAL_DIV = (
    '<div style="text-align: center; font-size: 2rem; font-weight: 700; '
    'margin-bottom: 0.5rem;"><strong>{title}</strong></div>'
)

FIRST_MAJOR_H1 = re.compile(r"^# 1\.\s+(.+)$")


def is_chapter7_project_doc(path: Path) -> bool:
    """第七章项目镜像（CineMaker / OpenClaw）：需篇名 div + 顺序大节编号。"""
    try:
        rel = path.relative_to(DOCS)
    except ValueError:
        return False
    if len(rel.parts) < 3:
        return False
    return (
        rel.parts[0] == "07_项目总结"
        and rel.parts[1] in ("7.1_CineMaker", "7.2_OpenClaw-Deployment-Issues")
        and path.suffix.lower() == ".md"
    )


def _skip_html_comments_and_blanks(lines: list[str], start: int) -> int:
    i = start
    while i < len(lines):
        s = lines[i].strip()
        if s == "":
            i += 1
            continue
        if s.startswith("<!--"):
            while i < len(lines) and "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        break
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    return i


def _ch7_unwrap_preamble_until_major(tail: list[str]) -> tuple[list[str], int]:
    """从 tail[0] 起消费文首 blockquote / --- / 空行，直到首个「# N.」大节；返回 (插入段, 余下起始下标)。"""
    j = 0
    while j < len(tail) and tail[j].strip() == "":
        j += 1
    out: list[str] = []
    while j < len(tail):
        raw = tail[j].rstrip("\n\r")
        if raw.strip() == "":
            out.append(tail[j])
            j += 1
            continue
        if raw.startswith("# ") and re.match(r"^# \d+\.\s", raw):
            break
        if raw.startswith(">") or raw.startswith(" >"):
            inner = raw.lstrip()
            if inner.startswith(">"):
                inner = inner[1:].lstrip()
            if "返回" in inner and "项目总览" in inner and "|" in inner:
                j += 1
                continue
            out.append(inner + "\n")
            j += 1
            continue
        if raw.strip() == "---":
            j += 1
            continue
        out.append(tail[j])
        j += 1
    while j < len(tail) and tail[j].strip() == "":
        j += 1
    return out, j


def chapter7_preprocess(text: str) -> str:
    """
    镜像自上游的第七章文档：首行「# 1. 篇名」改为规范篇名 div；文首 blockquote 改为正文段；
    去掉「返回项目总览 | …」式导航句；围栏外所有「# N.」按出现顺序重编为 1..K（不误伤代码块内 #）。
    """
    lines = text.splitlines(keepends=True)
    pos = _skip_html_comments_and_blanks(lines, 0)
    if pos >= len(lines):
        return text

    head = lines[pos].rstrip("\n\r")
    if TITLE_DIV.match(head) or TITLE_P.match(head):
        k = pos + 1
        while k < len(lines) and lines[k].strip() == "":
            k += 1
        prefix = lines[:k]
        tail = lines[k:]
    else:
        m = FIRST_MAJOR_H1.match(head)
        if not m:
            return renumber_h1_sequential_outside_fences(text)
        title = m.group(1).strip()
        div_line = CANONICAL_DIV.format(title=title) + "\n"
        prefix = lines[:pos] + [div_line, "\n"]
        tail = lines[pos + 1 :]

    preamble, j = _ch7_unwrap_preamble_until_major(tail)
    merged = prefix + preamble + tail[j:]
    return renumber_h1_sequential_outside_fences("".join(merged))


def renumber_h1_sequential_outside_fences(text: str) -> str:
    lines = text.splitlines(keepends=True)
    in_fence = False
    n = 0
    out: list[str] = []
    for line in lines:
        st = line.rstrip("\n\r")
        if st.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        m = re.match(r"^# \d+(\.\s+.*)$", st)
        if m:
            n += 1
            out.append(f"# {n}{m.group(1)}\n")
            continue
        out.append(line)
    return "".join(out)


def normalize_title_line(lines: list[str]) -> list[str]:
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines):
        return lines
    raw = lines[i].rstrip("\n\r")
    m = TITLE_P.match(raw) or TITLE_DIV.match(raw)
    if not m:
        return lines
    title = m.group(1).strip()
    new_line = CANONICAL_DIV.format(title=title) + "\n"
    return lines[:i] + [new_line] + lines[i + 1 :]


def strip_after_title(lines: list[str]) -> list[str]:
    """篇名行之后：去掉空行、meta blockquote、---、导航表。"""
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines):
        return lines
    line0 = lines[i].rstrip("\n\r")
    if "</div>" not in line0 or "<strong>" not in line0:
        return lines
    head_end = i + 1
    i = head_end
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    while i < len(lines):
        s = lines[i].rstrip("\n\r")
        if s.strip() == "":
            i += 1
            continue
        if META_BQ.match(s):
            i += 1
            continue
        break
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i < len(lines) and lines[i].strip() == "---":
        i += 1
        while i < len(lines) and lines[i].strip() == "":
            i += 1
    if i < len(lines) and lines[i].lstrip().startswith("|"):
        j = i
        has_nav = False
        while j < len(lines) and lines[j].lstrip().startswith("|"):
            if re.search(r"上一节|下一节|上一章|下一章|\*\*导读\*\*", lines[j]):
                has_nav = True
            j += 1
        if has_nav and j - i >= 2:
            i = j
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            if i < len(lines) and lines[i].strip() == "---":
                i += 1
                while i < len(lines) and lines[i].strip() == "":
                    i += 1
    return lines[:head_end] + lines[i:]


def strip_footer_nav(lines: list[str]) -> list[str]:
    rows = [ln.rstrip("\n\r") for ln in lines]
    while rows and not rows[-1].strip():
        rows.pop()
    while rows and META_BQ.match(rows[-1]):
        rows.pop()
        while rows and not rows[-1].strip():
            rows.pop()
    if rows and rows[-1].strip() == "---":
        rows.pop()
        while rows and not rows[-1].strip():
            rows.pop()
    return [r + "\n" for r in rows]


def convert_h1_blocks(text: str) -> str:
    parts = re.split(r"(```[\s\S]*?```)", text)
    out_parts: list[str] = []
    n = 0
    for k, part in enumerate(parts):
        if k % 2 == 1:
            out_parts.append(part)
            continue
        s = part
        while True:
            m = H1_CENTER.search(s)
            if not m:
                out_parts.append(s)
                break
            inner = m.group(1).strip()
            inner = re.sub(r"^\d+\.\s*", "", inner)
            n += 1
            rep = f"\n\n# {n}. {inner}\n\n"
            s = s[: m.start()] + rep + s[m.end() :]
    return "".join(out_parts)


def renumber_h2_under_major(text: str) -> str:
    def process_segment(segment: str) -> str:
        lines = segment.splitlines(keepends=True)
        major: int | None = None
        sub = 0
        out: list[str] = []
        in_fence = False
        for line in lines:
            st = line.rstrip("\n\r")
            if st.lstrip().startswith("```"):
                in_fence = not in_fence
                out.append(line)
                continue
            if in_fence:
                out.append(line)
                continue
            m_maj = ATX_MAJOR.match(st)
            if m_maj:
                major = int(m_maj.group(1))
                sub = 0
                out.append(line)
                continue
            if major is None:
                out.append(line)
                continue
            m2 = ATX_H2.match(st)
            if not m2:
                out.append(line)
                continue
            rest = m2.group(1).strip()
            if rest.startswith("#"):
                out.append(line)
                continue
            rest = re.sub(r"^\d+\.\d+\.\s*", "", rest)
            sub += 1
            out.append(f"## {major}.{sub}. {rest}\n")
        return "".join(out)

    parts = re.split(r"(```[\s\S]*?```)", text)
    rebuilt = []
    for k, part in enumerate(parts):
        rebuilt.append(process_segment(part) if k % 2 == 0 else part)
    return "".join(rebuilt)


def collapse_extra_blank_lines(text: str) -> str:
    return re.sub(r"\n{4,}", "\n\n\n", text)


def blank_line_after_title_div(text: str) -> str:
    """篇名 </div> 与首个「# 数字.」大节之间保留一空行。"""
    return re.sub(r"(</div>)\n(# \d+\.)", r"\1\n\n\2", text, count=1)


def finalize(lines: list[str]) -> str:
    text = "".join(lines)
    if text and not text.endswith("\n"):
        text += "\n"
    return text


def transform(path: Path, text: str) -> str:
    if is_chapter7_project_doc(path):
        text = chapter7_preprocess(text)
    lines = text.splitlines(keepends=True)
    lines = normalize_title_line(lines)
    lines = strip_after_title(lines)
    body = "".join(lines)

    has_h1 = bool(H1_CENTER.search(body))
    has_numbered_major = bool(re.search(r"(?m)^# \d+\.\s+\S", body))

    if has_h1:
        body = convert_h1_blocks(body)
    elif not has_numbered_major:
        body = collapse_extra_blank_lines(body)
        body = blank_line_after_title_div(body)
        lines = body.splitlines(keepends=True)
        lines = strip_footer_nav(lines)
        return finalize(lines)

    body = renumber_h2_under_major(body)
    body = collapse_extra_blank_lines(body)
    body = blank_line_after_title_div(body)
    lines = body.splitlines(keepends=True)
    lines = strip_footer_nav(lines)
    return finalize(lines)


def main() -> int:
    paths = sorted(DOCS.rglob("*.md"))
    changed = 0
    for p in paths:
        raw = p.read_text(encoding="utf-8")
        new = transform(p, raw)
        if new != raw:
            if len(raw.strip()) > 200 and len(new.strip()) < 30:
                print(f"SKIP suspicious empty output: {p.relative_to(ROOT)}", file=sys.stderr)
                continue
            p.write_text(new, encoding="utf-8")
            print(p.relative_to(ROOT))
            changed += 1
    print(f"updated {changed} file(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
