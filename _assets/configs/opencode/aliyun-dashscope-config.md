# OpenCode 配置阿里云 DashScope 指南

## 1. 环境准备

### 1.1 系统要求
- macOS / Linux / Windows
- Node.js 18+
- OpenCode CLI 已安装

### 1.2 安装 OpenCode
```bash
npm install -g opencode
```

## 2. 获取阿里云 DashScope API 密钥

### 2.1 申请 API 密钥
1. 访问阿里云 DashScope 控制台：https://dashscope.console.aliyun.com/apiKey
2. 登录阿里云账号
3. 创建新的 API 密钥
4. 复制生成的 `sk-...` 格式的密钥

### 2.2 密钥格式
- DashScope API 密钥格式：`sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
- 注意：这与阿里云 CodePlan 的密钥（`sk-sp-...`）不同

## 3. 配置 OpenCode

### 3.1 配置文件设置

创建或编辑 `~/.config/opencode/opencode.json` 文件：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "alibaba": {
      "options": {
        "apiKey": "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      }
    }
  },
  "model": "alibaba/qwen3.5-plus"
}
```

### 3.2 环境变量设置

添加到你的 `~/.zshrc` 或 `~/.bashrc`：

```bash
# OpenCode Alibaba DashScope
export DASHSCOPE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

然后重新加载配置：
```bash
source ~/.zshrc  # 或 source ~/.bashrc
```

## 4. 验证配置

### 4.1 检查提供商列表
```bash
opencode providers list
```

预期输出：
```
┌  Credentials ~/.local/share/opencode/auth.json
│
└  0 credentials

┌  Environment
│
●  Alibaba DASHSCOPE_API_KEY
│
└  1 environment variable
```

### 4.2 查看可用模型
```bash
opencode models
```

常用阿里云模型：
- `alibaba/qwen3.5-plus` - Qwen 3.5 Plus
- `alibaba/qwen-max` - Qwen Max
- `alibaba/qwen-plus` - Qwen Plus
- `alibaba/qwen-turbo` - Qwen Turbo

### 4.3 测试连接
```bash
opencode run "你好，请介绍一下你自己"
```

## 5. 常用命令

### 5.1 启动 TUI 界面
```bash
opencode
```

### 5.2 运行单次对话
```bash
opencode run "你的问题"
```

### 5.3 指定模型
```bash
opencode run -m alibaba/qwen-max "你的问题"
```

### 5.4 查看版本
```bash
opencode --version
```

## 6. 常见问题排查

### 6.1 API 密钥错误
- 错误信息：`Incorrect API key provided`
- 原因：使用了 CodePlan 的密钥（`sk-sp-...`）而不是 DashScope 的密钥
- 解决方案：申请 DashScope 的 API 密钥（`sk-...`）

### 6.2 模型未找到
- 错误信息：`Model not found: alibaba/xxx`
- 原因：模型名称不正确
- 解决方案：使用 `opencode models` 查看可用模型列表

### 6.3 环境变量未设置
- 错误信息：`Provider not found` 或认证错误
- 原因：`DASHSCOPE_API_KEY` 环境变量未设置
- 解决方案：添加到 shell 配置文件并重新加载

## 7. 配置示例

### 7.1 使用 Qwen 3.5 Plus
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "alibaba": {
      "options": {
        "apiKey": "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      }
    }
  },
  "model": "alibaba/qwen3.5-plus"
}
```

### 7.2 使用 Qwen Max
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "alibaba": {
      "options": {
        "apiKey": "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      }
    }
  },
  "model": "alibaba/qwen-max"
}
```

## 8. 相关资源

- [OpenCode 官方文档](https://opencode.ai/docs)
- [阿里云 DashScope 文档](https://help.aliyun.com/document_detail/611753.html)
- [DashScope API 密钥管理](https://dashscope.console.aliyun.com/apiKey)

## 9. 版本信息

- OpenCode 版本：1.3.17
- 配置日期：2026-04-08
- 测试环境：macOS

---

**注意**：
1. 本配置指南使用的 API 密钥和端点地址仅供参考，请根据实际情况进行修改
2. DashScope 和 CodePlan 是不同的服务，需要不同的 API 密钥
3. 请妥善保管 API 密钥，不要泄露给他人