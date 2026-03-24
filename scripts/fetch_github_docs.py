#!/usr/bin/env python3
"""
从 GitHub 仅拉取 Markdown 文档到 06_开源项目文档/（不克隆代码）。
公开仓：API 列树 + raw.githubusercontent.com 下载。
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "06_开源项目文档"
OWNER = "chenweidu666"
BRANCH = "main"
UA = "chenwei-tech-docs-fetch/1.0"


def http_get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)


def http_get_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def tree(owner: str, repo: str, branch: str = BRANCH) -> list[dict]:
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    data = http_get_json(url)
    if data.get("truncated"):
        print(f"WARN: tree truncated for {repo}", file=sys.stderr)
    return data.get("tree", [])


def raw_url(repo: str, path: str, branch: str = BRANCH) -> str:
    from urllib.parse import quote

    parts = path.split("/")
    safe = "/".join(quote(p, safe="") for p in parts)
    return f"https://raw.githubusercontent.com/{OWNER}/{repo}/{branch}/{safe}"


def should_skip_path(path: str) -> bool:
    if path in ("CHANGELOG.md", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md"):
        return True
    # 示例剧集正文，体积大且偏内容非工程文档
    if "docs/剧本/AI女性Vlog/剧本/EP" in path and path.endswith(".md"):
        return True
    return False


def _match_prefixes(path: str, prefixes: tuple[str, ...]) -> bool:
    for p in prefixes:
        pn = p.rstrip("/")
        if path == pn or path == p:
            return True
        if path.startswith(pn + "/"):
            return True
    return False


def sync_md_tree(
    repo: str,
    dest_name: str,
    *,
    path_prefixes: tuple[str, ...] | None = None,
) -> int:
    """下载仓库内 .md；path_prefixes 非空时只保留 README 或给定目录下文件。"""
    n = 0
    base = OUT / dest_name
    for item in tree(OWNER, repo):
        if item.get("type") != "blob":
            continue
        path = item["path"]
        if not path.endswith(".md"):
            continue
        if should_skip_path(path):
            continue
        if path_prefixes and not _match_prefixes(path, path_prefixes):
            continue
        url = raw_url(repo, path)
        target = base / path
        target.parent.mkdir(parents=True, exist_ok=True)
        for attempt in range(3):
            try:
                body = http_get_bytes(url)
                note = (
                    f"<!-- 文档同步自 https://github.com/{OWNER}/{repo} 分支 {BRANCH} — 请勿手工与上游长期双轨编辑 -->\n\n"
                )
                text = body.decode("utf-8", errors="replace")
                if not text.lstrip().startswith("<!-- 文档同步自"):
                    text = note + text
                target.write_text(text, encoding="utf-8")
                print(f"OK {repo} {path} ({len(body)} B)")
                n += 1
                time.sleep(0.15)
                break
            except urllib.error.HTTPError as e:
                print(f"HTTP {e.code} {repo} {path}", file=sys.stderr)
                time.sleep(2 * (attempt + 1))
            except Exception as e:
                print(f"ERR {repo} {path}: {e}", file=sys.stderr)
                time.sleep(1)
    return n


def sync_openclaw_style(repo: str, dest_name: str) -> int:
    """README + docs/*.md"""
    return sync_md_tree(
        repo,
        dest_name,
        path_prefixes=("README.md", "docs"),
    )


def sync_cinemaker() -> int:
    """CineMaker-AI-Platform：根 README + docs 下全部 md（排除示例单集剧本）。"""
    return sync_md_tree(
        "CineMaker-AI-Platform",
        "CineMaker-AI-Platform",
        path_prefixes=("README.md", "docs"),
    )


def fetch_private_readme(repo: str, dest_name: str) -> bool:
    """gh api …/readme raw；失败则跳过。"""
    base = OUT / dest_name
    base.mkdir(parents=True, exist_ok=True)
    try:
        p = subprocess.run(
            [
                "gh",
                "api",
                f"repos/{OWNER}/{repo}/readme",
                "-H",
                "Accept: application/vnd.github.raw",
            ],
            capture_output=True,
            timeout=60,
        )
        if p.returncode != 0:
            print(f"SKIP private {repo}: gh exit {p.returncode}", file=sys.stderr)
            return False
        text = p.stdout.decode("utf-8", errors="replace")
        note = f"<!-- README 同步自私有仓库 {repo}（仅首页说明，代码未包含） -->\n\n"
        (base / "README_仓库首页.md").write_text(note + text, encoding="utf-8")
        print(f"OK private README {repo}")
        return True
    except FileNotFoundError:
        print("SKIP: gh not installed", file=sys.stderr)
        return False
    except Exception as e:
        print(f"SKIP private {repo}: {e}", file=sys.stderr)
        return False


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    total += sync_cinemaker()
    total += sync_openclaw_style("OpenClaw-Deployment-Issues", "OpenClaw-Deployment-Issues")
    total += sync_md_tree("Smart-Wardrobe-Web", "Smart-Wardrobe-Web", path_prefixes=("README.md", "docs"))
    total += sync_md_tree(
        "IOT-Arduino-BodyWeightMonitor",
        "IOT-Arduino-BodyWeightMonitor",
        path_prefixes=("README.md",),
    )

    priv = [
        "CineMaker-Core",
        "GateClaw-Bot",
        "Agent-Monitor-Dashboard",
        "Dify-Workflow-Project",
        "Single-Agent-Lab",
        "Eye-Vision-Agent",
        "ComfyUI-Image-Agent",
        "ComfyUI-Workflow-Agent",
        "Picture-Generation-Agent",
        "Android-Automation-Agent",
        "QA-Dataset-Generator",
        "LoRA-Finetune-Lab",
        "Subtitle-SFT-Dataset",
        "AI-Content-Generator",
        "SD-Picture-Generator",
    ]
    for repo in priv:
        fetch_private_readme(repo, f"_私有仓库README/{repo}")

    print(f"\n公开 Markdown 文件合计拉取约 {total} 个（含覆盖）。")


if __name__ == "__main__":
    main()
