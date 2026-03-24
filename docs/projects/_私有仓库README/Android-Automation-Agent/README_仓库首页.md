<!-- README 同步自私有仓库 Android-Automation-Agent（仅首页说明，代码未包含） -->

# Android Agent（AppAgent 主链路）

本仓库只维护 `third_party/AppAgent-AutoModel` 这一条执行链路，重点用于 Android 端的小红书自动发布与天气海报流程。

## 快速开始

1) 配置环境变量（`~/.aliyun-api.env`）：

```bash
export DASHSCOPE_API_KEY="sk-sp-xxxxx"
export OPENAI_BASE_URL="https://coding.dashscope.aliyuncs.com/v1"
```

2) 默认启动（热更新模式）：

```bash
./start_appagent.sh
```

3) 首次或依赖变更时安装依赖：

```bash
./start_appagent.sh --pip
```

## 启动模式

- `--cli-hot`：默认模式。代码变更后自动重启 worker，无需手动重启整个脚本。
- `--cli`：普通 CLI。
- `--ci "<任务>"`：自动对话 CI 模式。
- `--self-debug`：先自检（ADB/截图/LLM/ChatAgent）再启动。
- `--debug-only`：仅自检不启动。

## 热更新架构（--cli-hot）

`start_appagent.sh` 在 `--cli-hot` 下启动 `third_party/AppAgent-AutoModel/hot_runner.py`：

- Supervisor 常驻进程监听以下目录：
  - `third_party/AppAgent-AutoModel/src`
  - `third_party/AppAgent-AutoModel/config`
- 检测到变更后先执行 `py_compile` 预检：
  - 通过：重启 `cli.py` worker
  - 失败：保留当前 worker，打印错误
- 目标：改代码后自动生效，不需要手动关掉再启动。

## 关键目录

- 启动脚本：`start_appagent.sh`
- 主工程：`third_party/AppAgent-AutoModel`
- 主 Agent：`third_party/AppAgent-AutoModel/src/chat_agent.py`
- skills 主实现：
  - `third_party/AppAgent-AutoModel/src/skills/flows`
  - `third_party/AppAgent-AutoModel/src/skills/registry`
- 天气发布工作流：`third_party/AppAgent-AutoModel/src/workflows/xhs_publish.py`

## 天气发布链路说明（当前实现）

- 城市锁定：天气工具调用时会优先绑定工作流城市，避免漂移到默认城市。
- 相册处理：先清空 `Download` + `DCIM/Camera`，再 push 新图并触发媒体扫描。
- 断点续跑：生成阶段会写 `todo.md` 到 `tmp/xhs_weather_materials/...`，用于恢复执行状态。
- 发布判定：发布后以成功信号确认完成，避免“仅点击发布就算成功”。

## 常见命令

```bash
# 默认热更新
./start_appagent.sh

# CI 自动执行
APPAGENT_AUTO_MAX_TURNS=6 ./start_appagent.sh --ci "帮我发一个南京明天天气的小红书帖子"

# 仅自检
./start_appagent.sh --debug-only
```

## 手机连接前置条件

- 开启开发者模式与 USB 调试
- `adb devices` 返回状态为 `device`

