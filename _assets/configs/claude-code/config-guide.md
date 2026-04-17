# Claude Code 配置指南

## 配置信息

### API 信息
- **API 密钥**: `sk-sp-4a72cbac7f5d407eb9e0041e234fb563`
- **Anthropic 兼容接口**: `https://coding.dashscope.aliyuncs.com/apps/anthropic/v1`
- **模型**: `qwen3.5-plus` / `QwQ Plus`

## 1. Claude Code 安装位置

```bash
/Users/chenwei/.local/bin/claude
```

版本: `2.1.96 (Claude Code)`

## 2. 环境变量配置

在 `~/.zshrc` 中配置:

```bash
# Claude Code / Anthropic Configuration
export ANTHROPIC_API_KEY=sk-sp-4a72cbac7f5d407eb9e0041e234fb563
export ANTHROPIC_BASE_URL=https://coding.dashscope.aliyuncs.com/apps/anthropic/v1

# Claude Code specific
export CLAUDE_API_KEY=sk-sp-4a72cbac7f5d407eb9e0041e234fb563
export CLAUDE_BASE_URL=https://coding.dashscope.aliyuncs.com/apps/anthropic/v1
```

## 3. 使用方法

### 启动 Claude Code
```bash
claude
```

### 运行单次命令
```bash
claude "你好，请介绍一下你自己"
```

### 使用特定模型
```bash
claude --model qwen3.5-plus "你好"
```

## 4. 已知问题

### API 密钥错误

如果遇到 "Incorrect API key provided" 错误：

1. **检查 API 密钥格式**
   - CodePlan 密钥格式: `sk-sp-xxx`
   - DashScope 密钥格式: `sk-xxx`

2. **验证环境变量**
   ```bash
   echo $ANTHROPIC_API_KEY
   echo $CLAUDE_API_KEY
   ```

3. **确保 Base URL 包含 /v1**
   - ❌ 错误: `https://coding.dashscope.aliyuncs.com/apps/anthropic`
   - ✅ 正确: `https://coding.dashscope.aliyuncs.com/apps/anthropic/v1`

## 5. 测试命令

### 测试 API 连接
```bash
curl -s "https://coding.dashscope.aliyuncs.com/apps/anthropic/v1/messages" \
  -H "Content-Type: application/json" \
  -H "x-api-key: sk-sp-4a72cbac7f5d407eb9e0041e234fb563" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "qwen3.5-plus",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

### 检查 Claude Code 版本
```bash
claude --version
```

## 6. 资源链接

- [阿里云 CodePlan 文档](https://help.aliyun.com/zh/model-studio/coding-plan-faq)
- [Claude Code 文档](https://docs.anthropic.com/claude-code)
- [Anthropic API 文档](https://docs.anthropic.com/)

## 7. 版本信息

- **配置日期**: 2026-04-08
- **Claude Code 版本**: 2.1.96
- **测试状态**: ⚠️ 需要验证

## 8. 故障排除

### 如果遇到认证错误

1. 确认 API 密钥是否有效
2. 检查密钥是否有足够的配额
3. 确认 Base URL 是否正确
4. 重启终端使环境变量生效
5. 如果问题持续，尝试重新生成 API 密钥