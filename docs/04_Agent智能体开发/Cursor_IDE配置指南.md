# 🚀 Cursor IDE Qwen Code配置指南

> 💻 专为 Cursor IDE 用户准备的配置方案  
> 📅 更新时间：2026 年 3 月 13 日

---

## 🎯 配置目标

在 Cursor IDE 中配置阿里云百炼 Coding Plan，使用 API Key: `sk-sp-e172a79dba3d47a69e349cfad93e344d`

---

## ⚡ 快速配置（推荐）

### Step 1: 运行自动配置脚本

```bash
cd /home/cw/For-Work/1_简历/1_陈纬简历/3_技术文档/04_Agent智能体开发
./setup_qwen_quick.sh
```

这个脚本会自动：
- ✅ 创建配置文件 `~/.qwen/settings.json`
- ✅ 配置 API Key
- ✅ 设置 3 个主流模型
- ✅ 备份旧配置

### Step 2: 重启 Cursor

```bash
# 完全退出 Cursor
# 重新打开 Cursor
```

### Step 3: 验证配置

在 Cursor 中：
1. 按 `Ctrl+Shift+P` (或 `Cmd+Shift+P`)
2. 输入 `Qwen Code: Start Chat`
3. 如果能正常启动，说明配置成功！

---

## 🔧 手动配置（如果自动配置失败）

### Step 1: 创建配置目录

```bash
mkdir -p ~/.qwen
```

### Step 2: 创建配置文件

编辑 `~/.qwen/settings.json`:

```bash
nano ~/.qwen/settings.json
```

粘贴以下内容：

```json
{
  "env": {
    "BAILIAN_CODING_PLAN_API_KEY": "sk-sp-e172a79dba3d47a69e349cfad93e344d"
  },
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3.5-plus",
        "name": "[阿里云百炼] qwen3.5-plus",
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
        "name": "[阿里云百炼] glm-5",
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
        "name": "[阿里云百炼] MiniMax-M2.5",
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
    "region": "china",
    "version": "f875d4c67d50946244a15d15b2a273a755d0d0c1fef1f4b23d7ee3572884b890"
  },
  "model": {
    "name": "qwen3.5-plus"
  },
  "$version": 3
}
```

保存文件（`Ctrl+O`, `Enter`, `Ctrl+X`）

---

## 💡 Cursor 中使用技巧

### 1. 启动对话

**方法 1**: 快捷键
```
Ctrl+Shift+P → 输入 "Qwen Code" → Enter
```

**方法 2**: 侧边栏
```
点击左侧活动栏的 Qwen Code 图标
```

### 2. 切换模型

在对话框中输入：
```
/model
```

然后选择：
- `qwen3.5-plus` - 日常编码（推荐）
- `glm-5` - 复杂推理
- `MiniMax-M2.5` - 代码生成

### 3. 常用命令

| 命令 | 作用 | 示例 |
|------|------|------|
| `/init` | 初始化项目上下文 | `/init` |
| `/clear` | 清空对话历史 | `/clear` |
| `/compress` | 压缩对话节省 Token | `/compress` |
| `/help` | 查看帮助 | `/help` |
| `/quit` | 退出对话 | `/quit` |

---

## 🎨 Cursor 专属优化

### 集成终端配置

在 Cursor 的设置中添加：

```json
// settings.json
{
  "terminal.integrated.env.linux": {
    "BAILIAN_CODING_PLAN_API_KEY": "sk-sp-e172a79dba3d47a69e349cfad93e344d"
  }
}
```

### 自动补全增强

如果你使用 Qwen Coder 模型进行代码补全：

```json
{
  "editor.inlineSuggest.enabled": true,
  "editor.suggestOnTriggerCharacters": true,
  "editor.quickSuggestions": {
    "other": true,
    "comments": true,
    "strings": true
  }
}
```

---

## 🔍 故障排查

### 问题 1: 找不到 Qwen Code插件

**解决方案**:

1. 打开扩展面板 (`Ctrl+Shift+X`)
2. 搜索 `Qwen Code Companion`
3. 点击安装
4. 重启 Cursor

### 问题 2: 认证失败

**检查清单**:

```bash
# 1. 检查配置文件是否存在
ls -la ~/.qwen/settings.json

# 2. 查看配置内容
cat ~/.qwen/settings.json

# 3. 确认 API Key 正确
grep "BAILIAN_CODING_PLAN_API_KEY" ~/.qwen/settings.json
```

应该看到：
```json
"BAILIAN_CODING_PLAN_API_KEY": "sk-sp-e172a79dba3d47a69e349cfad93e344d"
```

### 问题 3: 无法连接服务

**网络检查**:

```bash
# 测试连接
ping coding.dashscope.aliyuncs.com

# 如果是 Linux，检查防火墙
sudo ufw status

# 如果需要代理
export https_proxy=http://你的代理服务器：端口
```

---

## 🆚 Cursor vs VS Code配置对比

| 特性 | Cursor | VS Code |
|------|--------|---------|
| **配置方式** | 相同（~/.qwen/settings.json） | 相同 |
| **插件名称** | Qwen Code Companion | Qwen Code Companion |
| **启动方式** | Ctrl+Shift+P | Ctrl+Shift+P |
| **AI 特性** | 原生集成更好 | 需要插件 |
| **推荐度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 🎁 Cursor 专属技巧

### 技巧 1: 项目级配置

在项目根目录创建 `.qwen/` 文件夹：

```bash
your-project/
├── .qwen/
│   └── settings.json  # 项目专属配置
├── src/
└── README.md
```

这样不同项目可以用不同的模型和配置。

### 技巧 2: 智能提交信息

使用 Qwen Code 自动生成 Git 提交信息：

```
/commit

# Qwen 会分析你的代码变更并生成提交信息
```

### 技巧 3: 代码审查

选中代码后问：

```
请审查这段代码，找出潜在问题并提出改进建议
```

### 技巧 4: 单元测试生成

```
为这个函数生成单元测试，覆盖所有边界情况
```

---

## 📊 性能优化建议

### 1. 选择合适的模型

| 场景 | 推荐模型 | 理由 |
|------|---------|------|
| 日常编码 | qwen3.5-plus | 速度快，准确率高 |
| 复杂算法 | glm-5 | 推理能力强 |
| 大量代码生成 | MiniMax-M2.5 | 代码质量高 |

### 2. 合理设置参数

```json
{
  "generationConfig": {
    "temperature": 0.7,  // 创造性与准确性平衡
    "max_tokens": 2048,  // 输出长度限制
    "top_p": 0.9         // 采样策略
  }
}
```

### 3. 定期清理历史

```bash
# 每周清理一次
/compress

# 或者开始新话题时
/clear
```

---

## 📚 相关资源

- 📘 [完整配置指南](./Qwen_Code配置指南.md)
- 📗 [3 分钟快速配置](./Qwen_Code快速配置.md)
- 📙 [04_Agent智能体开发导航](./README.md)
- 🔗 [Cursor 官方文档](https://cursor.sh/docs)

---

## ✅ 配置检查清单

完成以下检查确保配置成功：

- [ ] Cursor 已安装
- [ ] Qwen Code Companion 插件已安装
- [ ] 配置文件 `~/.qwen/settings.json` 存在
- [ ] API Key 正确（`sk-sp-e172a79dba3d47a69e349cfad93e344d`）
- [ ] 能够启动 Qwen Code 对话
- [ ] 可以切换模型
- [ ] 至少完成一次成功对话

**全部打勾？** 🎉 恭喜，你已经成功配置完成！

---

## 🎯 下一步

配置完成后，试试这些实用场景：

1. **代码解释** - 选中代码问"这段代码做了什么？"
2. **Bug 修复** - 粘贴错误信息问"如何修复？"
3. **重构建议** - "如何优化这段代码的性能？"
4. **文档生成** - "为这个函数写文档注释"
5. **学习新技术** - "用 Python 实现一个快速排序"

---

> **配置时间**: 2026 年 3 月 13 日  
> **维护者**: 陈纬  
> **API Key**: `sk-sp-e172a79dba3d47a69e349cfad93e344d`  
> **IDE**: Cursor (Linux ARM64)

**祝你编码愉快！** 🚀
