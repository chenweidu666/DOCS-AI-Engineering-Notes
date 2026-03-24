# 🔧 Qwen Code配置 - 3 分钟快速开始

> ⚡ 超简单的配置指南，3 分钟搞定一切  
> 📅 更新时间：2026 年 3 月 13 日

---

## 🎯 配置目标

使用你的 API Key **`sk-sp-e172a79dba3d47a69e349cfad93e344d`** 配置阿里云百炼 Coding Plan

---

## ⚡ 方法一：一键脚本（推荐⭐⭐⭐⭐⭐）

### Step 1: 运行脚本

```bash
# 进入目录
cd /home/cw/For-Work/1_简历/1_陈纬简历/3_技术文档/04_Agent智能体开发

# 运行快速配置脚本
./setup_qwen_quick.sh
```

### Step 2: 验证安装

```bash
# 启动 Qwen Code
qwen

# 测试连接
/help
```

**完成！** 🎉 就是这么简单！

---

## 📝 方法二：手动配置

### Step 1: 创建配置文件

```bash
mkdir -p ~/.qwen
nano ~/.qwen/settings.json
```

### Step 2: 粘贴配置

```json
{
  "env": {
    "BAILIAN_CODING_PLAN_API_KEY": "sk-sp-e172a79dba3d47a69e349cfad93e344d"
  },
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3.5-plus",
        "name": "[Bailian] qwen3.5-plus",
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
        "name": "[Bailian] glm-5",
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
        "name": "[Bailian] MiniMax-M2.5",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY"
      }
    ]
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "codingPlan": {
    "region": "china"
  },
  "model": {
    "name": "qwen3.5-plus"
  },
  "$version": 3
}
```

### Step 3: 保存并测试

```bash
# 保存文件（Ctrl+X, Y, Enter）
# 启动 Qwen Code
qwen
```

---

## 🚀 开始使用

### 基本命令

```bash
# 启动对话
qwen

# 查看帮助
/help

# 切换模型
/model

# 清屏
/clear

# 退出
/quit
```

### 可用模型

| 模型 | 特点 | 推荐场景 |
|------|------|---------|
| **qwen3.5-plus** ⭐ | 默认推荐，均衡 | 通用编程 |
| **glm-5** | 智谱最新，带思考 | 复杂推理 |
| **MiniMax-M2.5** | MiniMax 最强 | 代码生成 |

---

## 💡 实用技巧

### 技巧 1：快速切换模型

```bash
# 在对话中输入
/model

# 然后选择：
# 0: qwen3.5-plus
# 1: glm-5
# 2: MiniMax-M2.5
```

### 技巧 2：项目初始化

```bash
# 在项目目录下运行
cd your-project
qwen
/init

# 会自动创建 QWEN.md 上下文文件
```

### 技巧 3：压缩对话历史

```bash
# 当对话太长时
/compress

# 自动摘要历史记录，节省 Token
```

---

## 🆘 故障排查

### 问题 1：找不到 `qwen` 命令

**解决方案**:
```bash
# 检查是否已安装
which qwen

# 如果没安装，先安装
npm install -g @qwen-code/qwen-code@latest

# 或者使用完整路径
~/.nvm/versions/node/v20.0.0/bin/qwen
```

---

### 问题 2：认证失败

**解决方案**:
```bash
# 检查配置文件
cat ~/.qwen/settings.json

# 确认 API Key 正确
# sk-sp-e172a79dba3d47a69e349cfad93e344d

# 重新运行配置脚本
./setup_qwen_quick.sh
```

---

### 问题 3：无法连接到服务

**解决方案**:
```bash
# 检查网络
ping coding.dashscope.aliyuncs.com

# 检查防火墙
sudo ufw status

# 如果是公司网络，可能需要代理
export https_proxy=http://proxy-server:port
```

---

## 📚 进阶阅读

需要更详细的配置说明？查看完整文档：

- 📄 [Qwen_Code配置指南.md](./Qwen_Code配置指南.md) - 完整版配置手册
- 📄 [README.md](../../README.md) - 技术文档总导航

---

## 🎁 额外福利

### VS Code 插件配置

如果你喜欢用 IDE：

1. **安装插件**
   ```
   扩展市场搜索：Qwen Code Companion
   点击安装
   ```

2. **自动同步配置**
   ```
   插件会自动读取 ~/.qwen/settings.json
   无需额外配置！
   ```

3. **开始使用**
   ```
   Ctrl+Shift+P → Qwen Code: Start Chat
   ```

---

## ✅ 配置检查清单

- [ ] Qwen Code 已安装
- [ ] 运行了配置脚本
- [ ] 配置文件在 `~/.qwen/settings.json`
- [ ] API Key 正确（`sk-sp-e172a79dba3d47a69e349cfad93e344d`）
- [ ] 能够成功启动 `qwen`
- [ ] 可以使用 `/help` 查看帮助
- [ ] 可以切换模型 `/model`

**全部打勾？** 🎉 恭喜，你已经配置完成！

---

## 📞 需要帮助？

遇到问题？

1. **查看完整文档**: [Qwen_Code配置指南.md](./Qwen_Code配置指南.md)
2. **检查常见问题**: 本文档的故障排查章节
3. **联系作者**: 见下方联系方式

---

> **配置完成时间**: 2026 年 3 月 13 日  
> **维护者**: 陈纬  
> **API Key**: `sk-sp-e172a79dba3d47a69e349cfad93e344d`

**祝你使用愉快！** 🚀
