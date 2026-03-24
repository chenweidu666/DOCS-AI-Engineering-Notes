# AI 工程师技术文档库

> 📚 本仓库是陈纬的 AI 工程技术文档知识库，涵盖大模型训练、部署、RAG、Agent 等核心技术领域  
> 📅 最后更新：2026 年 3 月  
> 🌐 在线阅读：<https://chenweidu666.github.io/chenwei-tech-docs/#/>

---

## 📖 文档导航

### 🔧 **01_模型训练与微调**
专注于大模型的训练和参数高效微调技术

**核心内容**：
- ✅ [大模型微调实战指南](./01_模型训练与微调/大模型微调实战指南.md) - LoRA/QLoRA/P-Tuning 等 PEFT 技术详解
- ✅ [常用微调模型架构总结](./01_模型训练与微调/常用微调模型架构总结.md) - 主流微调模型对比
- ✅ [分布式训练框架综述](./01_模型训练与微调/分布式训练框架综述.md) - DeepSpeed/Megatron-LM 等

**前置知识**：Transformer 基础、PyTorch 使用经验  
**学习时长**：约 8-12 小时

---

### 🚀 **02_模型部署与推理**
大模型在生产环境的部署与性能优化

**核心内容**：
- ✅ [vLLM使用指南](./02_模型部署与推理/vLLM使用指南.md) - 高性能推理引擎
- ✅ [云端大模型 8 卡 A100 部署实战](./02_模型部署与推理/云端大模型 8 卡 A100 部署实战.md)
- ✅ [云端大模型部署与运维实践](./02_模型部署与推理/云端大模型部署与运维实践.md)
- ✅ [国产GPU适配vLLM完整指南](./02_模型部署与推理/国产GPU适配vLLM完整指南.md) - 华为昇腾/寒武纪
- ✅ [高通端侧推理框架解析](./02_模型部署与推理/高通端侧推理框架解析.md) - 边缘端部署
- ✅ [LLM压缩工具介绍](./02_模型部署与推理/LLM压缩工具介绍.md) - 量化/剪枝/蒸馏
- ✅ [PaddleOCR 与 LLM文档解析工具](./02_模型部署与推理/PaddleOCR 与 LLM文档解析工具.md)

**前置知识**：Linux 基础、Docker 使用、GPU 硬件基础  
**学习时长**：约 15-20 小时

---

### 🔍 **03_RAG检索增强生成**
RAG 系统从原理到实战的完整技术栈

**核心内容**：
- ✅ [RAG流程与面试问题整理](./03_RAG检索增强生成/RAG流程与面试问题整理.md) - 核心流程 + 面试题库
- ✅ [RAG问答系统设计与实现](./03_RAG检索增强生成/RAG问答系统设计与实现.md)
- ✅ [问答数据集生成工具](./03_RAG检索增强生成/问答数据集生成工具.md)
- ✅ [问答数据集生活记录生成方案](./03_RAG检索增强生成/问答数据集生活记录生成方案.md)

**关键技术**：
- 混合检索（Dense + Sparse）
- Rerank 技术（BGE/Cohere）
- 召回率优化方法
- Agentic RAG / Graph RAG

**前置知识**：向量数据库基础、嵌入模型概念  
**学习时长**：约 12-15 小时

---

### 🤖 **04_Agent智能体开发**
AI Agent 理论基础与平台实践

**核心内容**：

#### Agent 理论基础
- ✅ [Agent技能体系技术说明](./04_Agent智能体开发/Agent技能体系技术说明.md)
- ✅ [车端大模型Agent应用技术路线](./04_Agent智能体开发/车端大模型Agent应用技术路线.md)
- ✅ [Agent写作构想与实践](./04_Agent智能体开发/Agent写作构想与实践.md)
- ✅ [垂直场景 Agent 实践记录](./04_Agent智能体开发/垂直场景 Agent 实践记录.md)

#### Dify平台深度实践
- ✅ [Dify平台技术实践](./04_Agent智能体开发/Dify平台技术实践.md) ⭐ **重点推荐**
- ✅ [MCP技术介绍与实践](./04_Agent智能体开发/MCP技术介绍与实践.md)

#### OpenClaw 二次开发
- ✅ [OpenClaw部署指南](./04_Agent智能体开发/OpenClaw部署指南.md)
- ✅ [OpenClaw工作区使用说明](./04_Agent智能体开发/OpenClaw工作区使用说明.md)
- ✅ [OpenClaw技能系统说明](./04_Agent智能体开发/OpenClaw技能系统说明.md)
- ✅ [OpenClaw 原生工具插件开发](./04_Agent智能体开发/OpenClaw 原生工具插件开发.md)
- ✅ [OpenClaw_Nginx 与 WebUI配置](./04_Agent智能体开发/OpenClaw_Nginx 与 WebUI配置.md)

**前置知识**：Python 编程、API 调用基础、Prompt Engineering  
**学习时长**：约 20-25 小时

---

### ⚙️ **05_AI编译器与底层优化**
AI编译器原理与算子优化技术

**计划内容**（待补充）：
- TVM / MLIR / XLA 编译器原理
- 算子开发与优化
- 硬件感知代码生成
- 显存管理与调度优化

**前置知识**：计算机体系结构、CUDA 编程、编译原理  
**学习时长**：约 15-20 小时

---

### 📦 **06_开源项目文档**
GitHub 产品 / 开源仓 **Markdown 镜像**（无业务代码）：CineMaker、OpenClaw 部署文库、Smart-Wardrobe、IoT 方案及若干私有仓 README 索引。

**入口**：[06_开源项目文档/README.md](./06_开源项目文档/README.md)

**CineMaker 详细文档（与简历项目一致）**  
- [产品工作流](./06_开源项目文档/CineMaker-AI-Platform/docs/guides/1_产品工作流.md)  
- [技术架构](./06_开源项目文档/CineMaker-AI-Platform/docs/guides/2_技术架构.md)  
- [提示词指南](./06_开源项目文档/CineMaker-AI-Platform/docs/guides/3_提示词指南.md)  
- [火山引擎 API 申请](./06_开源项目文档/CineMaker-AI-Platform/docs/guides/4_火山引擎API申请指南.md)  
- [仓库说明](./06_开源项目文档/CineMaker-AI-Platform/README.md) · [剧本格式规范](./06_开源项目文档/CineMaker-AI-Platform/docs/剧本/剧本格式规范.md)

同步更新：`python3 scripts/fetch_github_docs.py` 后执行 `bash scripts/regen_sidebar.sh`。

---

## 🎯 学习路径建议

### 路径 1：大模型部署工程师
```
01_模型训练与微调 (基础) 
  → 02_模型部署与推理 (核心) 
  → 03_RAG检索增强生成 (扩展)
```

### 路径 2：RAG 算法工程师
```
01_模型训练与微调 (基础) 
  → 03_RAG检索增强生成 (核心) 
  → 04_Agent智能体开发 (进阶) 
  → 02_模型部署与推理 (扩展)
```

### 路径 3：AI Agent 开发工程师
```
03_RAG检索增强生成 (基础) 
  → 04_Agent智能体开发 (核心) 
  → 02_模型部署与推理 (扩展)
```

---

## 📊 知识库统计

| 分类 | 文档数量 | 图片资源 | 最后更新 |
|------|---------|---------|---------|
| 01_模型训练与微调 | 3 篇 | 3 张 | 2026-03 |
| 02_模型部署与推理 | 7 篇 | 3 张 | 2026-03 |
| 03_RAG检索增强生成 | 4 篇 | 4 张 | 2026-03 |
| 04_Agent智能体开发 | 11 篇 | 5 张 | 2026-03 |
| 05_AI编译器与底层优化 | 0 篇 | - | - |
| 06_开源项目文档 | 约 36 篇（MD 镜像） | - | 2026-03 |
| **总计** | **约 61 篇** | **15 张** | **2026-03** |

---

## 🔥 重点推荐阅读

### 🏆 Top 5 核心文档
1. ⭐ [Dify平台技术实践](./04_Agent智能体开发/Dify平台技术实践.md) - Agent平台最佳实践
2. ⭐ [RAG流程与面试问题整理](./03_RAG检索增强生成/RAG流程与面试问题整理.md) - RAG 完全指南
3. ⭐ [大模型微调实战指南](./01_模型训练与微调/大模型微调实战指南.md) - PEFT 技术详解
4. ⭐ [云端大模型部署与运维实践](./02_模型部署与推理/云端大模型部署与运维实践.md) - 生产级部署
5. ⭐ [国产GPU适配vLLM完整指南](./02_模型部署与推理/国产GPU适配vLLM完整指南.md) - 国产化方案

---

## 🛠️ 使用建议

### 在线阅读
- 推荐使用支持 Markdown 的编辑器（如 VS Code、Typora）
- 文档中的 Mermaid 流程图可在 GitHub/GitLab 直接渲染
- 图片资源已按专题分类存放

### 本地构建
```bash
# 克隆仓库
git clone <your-repo-url>

# 进入目录
cd 3_技术文档

# 使用 Typora 或 VS Code 打开 README.md
```

### 同步开源仓文档（仅 Markdown）
```bash
python3 scripts/fetch_github_docs.py
bash scripts/regen_sidebar.sh
```

### 引用规范
如需引用本文档内容，请注明：
- 作者：陈纬
- 来源：AI 工程师技术文档库
- 日期：2026 年

---

## 📬 联系与反馈

- 📧 Email：[514351508@qq.com](mailto:514351508@qq.com)
- 💼 简历：<https://chenweidu666.github.io/Resume-Site/>
- 🌐 GitHub：[github.com/chenweidu666](https://github.com/chenweidu666)

---

## 📜 许可证

本文档采用 **CC BY-NC-SA 4.0** 许可协议  
（署名 - 非商业性使用 - 相同方式共享）

---

> **最后更新**: 2026 年 3 月 13 日  
> **维护者**: 陈纬
