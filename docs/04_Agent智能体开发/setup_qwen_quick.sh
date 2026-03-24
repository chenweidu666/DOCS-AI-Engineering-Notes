#!/bin/bash

# Qwen Code 快速配置脚本 - 简化版
# API Key: sk-sp-e172a79dba3d47a69e349cfad93e344d

set -e

echo "🚀 Qwen Code 快速配置"
echo "===================="
echo ""

# 检测操作系统
if [[ "$OSTYPE" == "darwin"* ]]; then
    CONFIG_DIR="$HOME/.qwen"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    CONFIG_DIR="$HOME/.qwen"
else
    echo "❌ 不支持的操作系统"
    exit 1
fi

CONFIG_FILE="$CONFIG_DIR/settings.json"

# 创建配置目录
mkdir -p "$CONFIG_DIR"

# 备份旧配置
if [ -f "$CONFIG_FILE" ]; then
    BACKUP_FILE="$CONFIG_FILE.backup.$(date +%Y%m%d_%H%M%S)"
    echo "💾 备份旧配置：$BACKUP_FILE"
    cp "$CONFIG_FILE" "$BACKUP_FILE"
fi

# 写入配置
cat > "$CONFIG_FILE" << 'EOF'
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
EOF

echo "✅ 配置完成！"
echo ""
echo "📍 配置文件：$CONFIG_FILE"
echo ""
echo "🎯 下一步:"
echo "   1. 启动 Qwen Code: qwen"
echo "   2. 测试：输入 /help"
echo "   3. 切换模型：输入 /model"
echo ""
echo "💡 提示：运行 'qwen' 开始使用"
echo ""
