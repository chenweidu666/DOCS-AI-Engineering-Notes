# FastAPI 服务化部署指南

> 对应简历：FastAPI · Python工程化

## 目录

1. 为什么用FastAPI（异步、自动文档、类型安全）
2. 核心概念（路由 / 依赖注入 / Pydantic / async）
3. LLM推理服务封装
   - 流式响应（SSE/StreamingResponse）
   - 并发控制与请求队列
4. 生产部署（Uvicorn + Gunicorn + Nginx + Docker）
5. 接口设计最佳实践
6. 性能压测与优化
