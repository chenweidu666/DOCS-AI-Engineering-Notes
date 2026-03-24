# Qwen Code 配置指南

> 📅 配置时间：2026 年 3 月 13 日  
> 🔑 API Key: `sk-sp-e172a79dba3d47a69e349cfad93e344d`

---

## 🚀 快速开始

### 方法一：CLI 交互式配置（推荐）

1. **启动 Qwen Code**
```bash
qwen
```

2. **进入认证设置**
- 按 `/auth` 命令进入设置界面
- 使用方向键选择 **阿里云百炼 Coding Plan**
- 按回车确认

3. **输入 API Key**
```
sk-sp-e172a79dba3d47a69e349cfad93e344d
```

---

### 方法二：手动配置文件

#### macOS / Linux
编辑文件：`~/.qwen/settings.json`

#### Windows
编辑文件：`C:\Users\你的用户名\.qwen\settings.json`

**配置内容**：
```json
{
  "env": {
    "BAILIAN_CODING_PLAN_API_KEY": "sk-sp-e172a79dba3d47a69e349cfad93e344d"
  },
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3.5-plus",
        "name": "[Bailian Coding Plan] qwen3.5-plus",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "qwen3-coder-plus",
        "name": "[Bailian Coding Plan] qwen3-coder-plus",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY"
      },
      {
        "id": "qwen3-coder-next",
        "name": "[Bailian Coding Plan] qwen3-coder-next",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY"
      },
      {
        "id": "qwen3-max-2026-01-23",
        "name": "[Bailian Coding Plan] qwen3-max-2026-01-23",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "glm-4.7",
        "name": "[Bailian Coding Plan] glm-4.7",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "glm-5",
        "name": "[Bailian Coding Plan] glm-5",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "MiniMax-M2.5",
        "name": "[Bailian Coding Plan] MiniMax-M2.5",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "kimi-k2.5",
        "name": "[Bailian Coding Plan] kimi-k2.5",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      }
    ]
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "codingPlan": {
    "region": "china",
    "version": "f875d4c67d50946244a15d15b2a273a755d0d0c1fef1f4b23d7ee3572884b890"
  },
  "model": {
    "name": "qwen3.5-plus"
  },
  "$version": 3
}
```

---

## 💻 常用命令速查

| 命令 | 说明 | 示例 |
|------|------|------|
| `/model` | 切换模型 | `/model` |
| `/auth` | 更改认证方式 | `/auth` |
| `/init` | 初始化项目上下文 | `/init` |
| `/clear` | 清屏 | `/clear` |
| `/compress` | 压缩对话历史 | `/compress` |
| `/settings` | 打开设置编辑器 | `/settings` |
| `/summary` | 生成项目摘要 | `/summary` |
| `/resume` | 恢复之前对话 | `/resume` |
| `/stats` | 显示会话统计 | `/stats` |
| `/help` | 显示帮助信息 | `/help` |
| `/quit` | 退出 Qwen Code | `/quit` |

---

## 🎯 可用模型列表

### 通义千问系列
- ✅ `qwen3.5-plus` - 默认推荐，综合性能最佳
- ✅ `qwen3-coder-plus` - 代码专用
- ✅ `qwen3-coder-next` - 代码预测
- ✅ `qwen3-max-2026-01-23` - 最强版本（带思考）

### 其他模型
- ✅ `glm-4.7` - 智谱 AI（带思考）
- ✅ `glm-5` - 智谱最新（带思考）
- ✅ `MiniMax-M2.5` - MiniMax 最强（带思考）
- ✅ `kimi-k2.5` - 月之暗面（带思考）

---

## 🔧 VS Code 插件配置

1. **安装插件**
   - 打开 VS Code
   - 扩展市场搜索 `Qwen Code Companion`
   - 点击安装

2. **验证配置**
   - 点击右上角 Qwen 图标
   - 输入 `/model` 查看可用模型
   - 选择需要的模型开始使用

---

## ⚠️ 注意事项

### 安全提醒
- 🔒 **不要将 API Key 上传到 Git 仓库**
- 🔒 定期检查 API Key 使用情况
- 🔒 如怀疑泄露，立即在阿里云百炼控制台重置

### 版本要求
- Qwen Code 版本 ≥ 0.11.1
- VS Code 版本 ≥ 1.85.0

### 网络要求
- Base URL: `https://coding.dashscope.aliyuncs.com/v1`
- 确保网络可以访问阿里云服务

---

## 🆘 故障排查

### 问题 1：无法连接到服务
**解决方案**：
```bash
# 检查网络连接
ping coding.dashscope.aliyuncs.com

# 验证 API Key 格式
echo $BAILIAN_CODING_PLAN_API_KEY
```

### 问题 2：模型列表为空
**解决方案**：
```bash
# 更新 Qwen Code 到最新版本
npm install -g @qwen-code/qwen-code@latest

# 重启 Qwen Code
qwen
```

### 问题 3：认证失败
**解决方案**：
1. 检查 API Key 是否正确复制（无多余空格）
2. 在阿里云百炼控制台验证 API Key 状态
3. 重新执行 `/auth` 命令配置

---

## 📚 学习资源

- 📖 [Qwen Code 官方文档](https://qwenlm.github.io/qwen-code-docs/zh/)
- 🔗 [阿里云百炼控制台](https://bailian.console.aliyun.com/)
- 💬 [常见问题 FAQ](https://help.aliyun.com/zh/model-studio/coding-plan-faq)

---

## 📊 配置完成检查清单

- [ ] Qwen Code 已安装（版本 ≥ 0.11.1）
- [ ] API Key 已配置
- [ ] 能够成功启动对话
- [ ] 可以切换不同模型
- [ ] VS Code 插件（可选）已安装

---

> ✨ **配置完成后，试试输入**: `/help` 查看所有可用命令  
> 🎉 **祝你使用愉快！**
