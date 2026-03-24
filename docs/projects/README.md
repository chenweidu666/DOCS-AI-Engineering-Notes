# 开源与产品文档（镜像）

本目录文档从 GitHub **仅同步 Markdown**，不包含业务代码。用于技术文档站统一阅读；**正文以各仓库为准**。

| 目录 | 仓库 | 说明 |
|------|------|------|
| [CineMaker-AI-Platform](./CineMaker-AI-Platform/README.md) | [CineMaker-AI-Platform](https://github.com/chenweidu666/CineMaker-AI-Platform) | 短剧 / AI 视频全栈：产品工作流、架构、提示词、火山 API、剧本规范等 |
| [OpenClaw-Deployment-Issues](./OpenClaw-Deployment-Issues/README.md) | [OpenClaw-Deployment-Issues](https://github.com/chenweidu666/OpenClaw-Deployment-Issues) | OpenClaw 自托管部署与排障文库 |
| [Smart-Wardrobe-Web](./Smart-Wardrobe-Web/README.md) | [Smart-Wardrobe-Web](https://github.com/chenweidu666/Smart-Wardrobe-Web) | 智能衣柜全栈：前后端集成与 UI 文档 |
| [IOT-Arduino-BodyWeightMonitor](./IOT-Arduino-BodyWeightMonitor/README.md) | [IOT-Arduino-BodyWeightMonitor](https://github.com/chenweidu666/IOT-Arduino-BodyWeightMonitor) | Arduino 体重监测方案说明 |
| `_私有仓库README/` | （私有） | 各仓 **README 首页** 的只读副本，便于本地与站点索引；**无完整代码与内文档** |

**更新命令**（在 `3_技术文档` 根目录）：

```bash
python3 scripts/fetch_github_docs.py
bash scripts/regen_sidebar.sh
```
