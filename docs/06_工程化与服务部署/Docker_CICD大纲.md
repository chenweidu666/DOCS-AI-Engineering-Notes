# Docker 与 CI/CD 工程化实践

> 对应简历：Docker · CI/CD · Bazel

## 目录

1. Docker基础与最佳实践（多阶段构建）
2. AI服务容器化（GPU镜像 / 模型挂载 / 资源限制）
3. Bazel构建系统
   - 为什么用Bazel：可重现、增量构建、多语言
   - BUILD文件基础语法
   - C++/Python混合项目实践
4. CI/CD流水线（GitHub Actions）
   - 自动测试 → 构建 → 推送镜像 → 部署
5. 实战：AI服务完整发布流程
6. 踩坑与经验
