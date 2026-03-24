# AppAgent Android 自动化实践指南

> 对应简历：Android自动化Agent · AppAgent

## 目录

1. AppAgent是什么
   - 基于LLM的Android端任务自动化框架
   - 核心能力：截图 → 视觉理解 → 操作执行
2. 架构设计
   - 感知层（ADB截图）
   - 理解层（LLM/多模态模型）
   - 执行层（ADB控制指令）
3. 环境搭建（ADB + Python + LLM API）
4. 核心代码结构
5. 实战案例：小红书自动发布
6. 热更新架构说明
7. 自检模式（--self-debug）使用指南
8. 踩坑记录
