#!/usr/bin/env python3
"""修复 OpenClaw 实战系列文档格式，符合 Cursor rules"""

import os
import re

docs_dir = "/root/.openclaw/workspace/AI-Engineering-Docs/docs/08_OpenClaw 实战"

for filename in sorted(os.listdir(docs_dir)):
    if not filename.endswith('.md'):
        continue
    
    filepath = os.path.join(docs_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取原标题（第一个 # 标题）
    match = re.match(r'^# (.+?)\n', content)
    if not match:
        continue
    
    old_title = match.group(1).strip()
    
    # 提取副标题（> 📅 那行）
    subtitle_match = re.search(r'^> 📅 (.+?)\n', content, re.MULTILINE)
    subtitle = subtitle_match.group(1) if subtitle_match else "2026-03-25 | 🦞 双龙虾架构实战系列"
    
    # 提取目录（## 📋 目录部分）
    toc_match = re.search(r'## 📋 目录\n\n(.*?)(?=\n---\n\n## )', content, re.DOTALL)
    toc = toc_match.group(1) if toc_match else ""
    
    # 提取正文（从第一个 ## 开始）
    body_match = re.search(r'\n---\n\n(## .*)', content, re.DOTALL)
    body = body_match.group(1) if body_match else content
    
    # 重新编号大节（# 1. # 2. ...）
    body = re.sub(r'^## (.*?)$', lambda m: f'# 1. {m.group(1)}' if m.group(1).startswith('背景') else m.group(0), body, flags=re.MULTILINE)
    
    # 构建新内容
    new_content = f'''<div style="text-align: center; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;"><strong>{old_title}</strong></div>

> {subtitle}

---

{toc}

---

{body}
'''
    
    # 写回
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ 修复：{filename}")

print("\n✅ 所有文档格式已修复")
