#!/bin/bash

# Cursor IDE Qwen Code 自动配置脚本
# API Key: sk-sp-e172a79dba3d47a69e349cfad93e344d

set -e

echo "🚀 Cursor IDE Qwen Code配置"
echo "=============================="
echo ""

# 检测操作系统
if [[ "$OSTYPE" == "darwin"* ]]; then
    CONFIG_DIR="$HOME/.qwen"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    CONFIG_DIR="$HOME/.qwen"
else
    echo "❌ 不支持的操作系统：$OSTYPE"
    exit 1
fi

CONFIG_FILE="$CONFIG_DIR/settings.json"

# 检查是否安装了 Cursor
CURSOR_INSTALLED=false
if command -v cursor &> /dev/null; then
    CURSOR_INSTALLED=true
    echo "✅ 检测到 Cursor 已安装"
elif [ -d "$HOME/.cursor-server" ]; then
    CURSOR_INSTALLED=true
    echo "✅ 检测到 Cursor 服务器运行中"
else
    echo "⚠️  未检测到 Cursor，将继续配置（可能使用 VS Code）"
fi

echo ""

# 创建配置目录
echo "📁 创建配置目录：$CONFIG_DIR"
mkdir -p "$CONFIG_DIR"

# 备份旧配置
if [ -f "$CONFIG_FILE" ]; then
    BACKUP_FILE="$CONFIG_FILE.backup.cursor.$(date +%Y%m%d_%H%M%S)"
    echo "💾 备份旧配置：$BACKUP_FILE"
    cp "$CONFIG_FILE" "$BACKUP_FILE"
fi

# 写入配置
echo "📝 写入配置文件..."

cat > "$CONFIG_FILE" << 'EOF'
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
      },
      {
        "id": "qwen3-coder-plus",
        "name": "[阿里云百炼] qwen3-coder-plus",
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "envKey": "BAILIAN_CODING_PLAN_API_KEY"
      },
      {
        "id": "kimi-k2.5",
        "name": "[阿里云百炼] kimi-k2.5",
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

# 检查 Qwen Code插件
echo "🔍 检查 Qwen Code插件状态..."

# 尝试查找 Cursor 扩展目录
CURSOR_EXT_DIRS=(
    "$HOME/.cursor-server/extensions"
    "$HOME/.vscode-server/extensions"
    "$HOME/.vscode/extensions"
)

PLUGIN_FOUND=false
for dir in "${CURSOR_EXT_DIRS[@]}"; do
    if [ -d "$dir" ] && ls "$dir" | grep -i "qwen" > /dev/null 2>&1; then
        echo "✅ Qwen Code插件已安装"
        PLUGIN_FOUND=true
        break
    fi
done

if [ "$PLUGIN_FOUND" = false ]; then
    echo "⚠️  未检测到 Qwen Code插件"
    echo ""
    echo "📦 请在 Cursor 中手动安装："
    echo "   1. 按 Ctrl+Shift+X 打开扩展面板"
    echo "   2. 搜索 'Qwen Code Companion'"
    echo "   3. 点击安装"
    echo ""
fi

echo ""
echo "=========================================="
echo "  🎉 配置完成！"
echo "=========================================="
echo ""
echo "📍 配置文件位置：$CONFIG_FILE"
echo ""
echo "🎯 下一步:"
if [ "$CURSOR_INSTALLED" = true ]; then
    echo "   1. 重启 Cursor（如果正在运行）"
    echo "   2. 按 Ctrl+Shift+P"
    echo "   3. 输入 'Qwen Code: Start Chat'"
    echo "   4. 开始使用！"
else
    echo "   1. 安装/打开 Cursor"
    echo "   2. 安装 Qwen Code Companion 插件"
    echo "   3. 按 Ctrl+Shift+P → 'Qwen Code: Start Chat'"
    echo "   4. 开始使用！"
fi
echo ""
echo "🔧 可用模型:"
echo "   ⭐ qwen3.5-plus (默认推荐)"
echo "   ⭐ glm-5 (复杂推理)"
echo "   ⭐ MiniMax-M2.5 (代码生成)"
echo "   ⭐ qwen3-coder-plus (代码专用)"
echo "   ⭐ kimi-k2.5 (长文本)"
echo ""
echo "💡 提示：在对话框中输入 /model 切换模型"
echo ""
