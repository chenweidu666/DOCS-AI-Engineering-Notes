# 站点维护（GitHub Pages / Docsify）

本站根目录即 **`3_技术文档`**，与日常写作目录一致，**不再**使用外层单独拷贝目录。

侧栏与搜索**不包含** `github文档仓库/`（已迁至 `1_陈纬简历/归档/github文档快照/`）、**不包含** `99_面试与学习资源/`（已迁至 `1_陈纬简历/归档/99_面试与学习资源/`）；`gen_sidebar.py` 的 `SKIP_DIRS` 已包含二者。

**从 GitHub 拉取公开/私有 README 文档镜像**（不克隆代码）：

```bash
python3 scripts/fetch_github_docs.py
bash scripts/regen_sidebar.sh
```

依赖：`gh` CLI（用于私有仓 README）；仅公开仓时可不用。

新增或重命名 `.md` 后，刷新左侧导航：

```bash
cd /path/to/3_技术文档
bash scripts/regen_sidebar.sh
git add _sidebar.md && git commit -m "chore: 更新侧栏" && git push
```

远程仓库：`git@github.com:chenweidu666/chenwei-tech-docs.git`  
线上阅读：<https://chenweidu666.github.io/chenwei-tech-docs/>
