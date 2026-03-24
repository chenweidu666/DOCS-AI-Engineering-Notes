# 站点维护（GitHub Pages / Docsify）

本站根目录即 **`3_技术文档`**，与日常写作目录一致，**不再**使用外层单独拷贝目录。

新增或重命名 `.md` 后，刷新左侧导航：

```bash
cd /path/to/3_技术文档
bash scripts/regen_sidebar.sh
git add _sidebar.md && git commit -m "chore: 更新侧栏" && git push
```

远程仓库：`git@github.com:chenweidu666/chenwei-tech-docs.git`  
线上阅读：<https://chenweidu666.github.io/chenwei-tech-docs/>
