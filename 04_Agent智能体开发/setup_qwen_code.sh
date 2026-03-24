#!/bin/bash

# Qwen Code 自动配置脚本
# API Key: sk-sp-e172a79dba3d47a69e349cfad93e344d

set -e

API_KEY="sk-sp-e172a79dba3d47a69e349cfad93e344d"
CONFIG_DIR=""
CONFIG_FILE=""

echo "🚀 开始配置 Qwen Code..."
echo ""

# 检测操作系统
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    CONFIG_DIR="$HOME/.qwen"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    CONFIG_DIR="$HOME/.qwen"
else
    echo "❌ 不支持的操作系统：$OSTYPE"
    exit 1
fi

CONFIG_FILE="$CONFIG_DIR/settings.json"

# 创建配置目录（如果不存在）
if [ ! -d "$CONFIG_DIR" ]; then
    echo "📁 创建配置目录：$CONFIG_DIR"
    mkdir -p "$CONFIG_DIR"
fi

# 备份旧配置文件
if [ -f "$CONFIG_FILE" ]; then
    BACKUP_FILE="$CONFIG_FILE.backup.$(date +%Y%m%d_%H%M%S)"
    echo "💾 备份旧配置文件到：$BACKUP_FILE"
    cp "$CONFIG_FILE" "$BACKUP_FILE"
fi

# 创建新配置文件
echo "📝 创建新的配置文件..."

cat > "$CONFIG_FILE" << 'EOF'
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
EOF

echo "✅ 配置文件已创建：$CONFIG_FILE"
echo ""
echo "🎉 配置完成！"
echo ""
echo "📍 下一步:"
echo "   1. 启动 Qwen Code: qwen"
echo "   2. 测试连接：输入 /help"
echo "   3. 切换模型：输入 /model"
echo ""
echo "🔧 常用命令:"
echo "   /model     - 切换模型"
echo "   /auth      - 更改认证方式"
echo "   /init      - 初始化项目"
echo "   /clear     - 清屏"
echo "   /quit      - 退出"
echo ""
echo "⚠️  安全提示:"
echo "   - 请勿将此配置文件提交到 Git 仓库"
echo "   - 定期检查 API Key 使用情况"
echo ""
