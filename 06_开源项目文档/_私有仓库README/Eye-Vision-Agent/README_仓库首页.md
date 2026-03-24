<!-- README 同步自私有仓库 Eye-Vision-Agent（仅首页说明，代码未包含） -->

# Pet Agent（Surface 极简语音助手）

目标：在 `ubuntu-surface` 上实现“Lemon Agent”唤醒 + 豆包语音对话的极简助手应用。

## 当前状态

- Flutter UI 已可运行（Linux）。
- 前端界面为极简待机态：默认黑色背景 + 一对眼睛（不包含宠物功能）。
- `agent-server`（FastAPI）已可运行并支持：
  - `GET /health`
  - `GET /wake/status`
  - `POST /voice/chat`
- 豆包 LLM 已打通。
- 本地唤醒/ASR/TTS 为“可接入骨架 + 配置驱动”，可继续增强为真音频闭环。

## 目录结构

```text
pet-agent/
  lib/
    main.dart
  agent-server/
    .env.example
    main.py
    requirements.txt
    services/
      config.py
      wakeword.py
      doubao.py
      pipeline.py
```

## Surface 部署路径

当前 Surface 使用目录：

- `~/pet_agent`

注意：Dart 包名不支持 `-`，所以 Surface 运行目录统一为 `pet_agent`。

## Surface 一次性准备

### 1) 安装 Linux 构建依赖

```bash
sudo apt update
sudo apt install -y cmake ninja-build pkg-config libgtk-3-dev libblkid-dev liblzma-dev clang
```

### 2) 安装 Flutter（如果未安装）

```bash
cd ~
wget -q https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.24.5-stable.tar.xz
tar xf flutter_linux_3.24.5-stable.tar.xz
echo 'export PATH=$HOME/flutter/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## 更新代码到 Surface

在开发机执行（把当前目录同步到 Surface）：

```bash
rsync -av --delete /home/cw/pet-agent/ ubuntu-surface:/home/chenwei/pet_agent/
```

## 运行 agent-server

```bash
cd ~/pet_agent/agent-server
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

如果机器缺少 `python3-venv`：

```bash
sudo apt install -y python3-venv
```

## 运行 Flutter（Real 模式）

```bash
cd ~/pet_agent
flutter create --platforms=linux .   # 首次或 linux 目录丢失时执行
flutter pub get
flutter run -d linux \
  --dart-define=USE_MOCK_IO=false \
  --dart-define=AGENT_BASE_URL=http://127.0.0.1:8000
```

启动后默认显示黑色背景和一对眼睛（极简待机界面）。

也可直接运行 release 可执行：

```bash
cd ~/pet_agent
flutter build linux
DISPLAY=:0 ./build/linux/x64/release/bundle/pet_agent
```

## 环境变量（只写变量名）

### LLM

- `DOUBAO_API_KEY`
- `DOUBAO_MODEL`（可选）
- `DOUBAO_LLM_URL`（可选）

### ASR/TTS（按需）

- `VOLC_APP_ID`
- `VOLC_ACCESS_TOKEN`
- `VOLC_SECRET_KEY`
- `VOLC_ASR_URL`
- `VOLC_TTS_URL`
- `WAKE_ACK_DEFAULT_AUDIO_PATH`（默认唤醒回复音频文件路径）
- `WAKE_ACK_PREFER_CLOUD_TTS`（1=优先云端 TTS）
- `WAKE_ACK_FALLBACK_LOCAL_TTS`（1=云端失败回退本地 TTS）

### 唤醒词

- `WAKE_WORD`（默认 `Lemon Agent`）
- `PORCUPINE_ACCESS_KEY`

## 快速验收

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/wake/status
curl -X POST http://127.0.0.1:8000/voice/chat \
  -H "Content-Type: application/json" \
  -d '{"text":"Lemon Agent, 介绍一下自己","simulate_wake":true}'
```

## 生成默认唤醒音（使用 1.md 音色）

目标：把“主人，我在。”生成为本地 `mp3`，并作为默认唤醒回复音播放。

### 1) 准备音色与认证信息

- 从 `1.md` 读取 `APP ID`、`Access Token`、`voice_type`（例如：`zh_female_meilinvyou_moon_bigtts`）。
- 确保该应用已开通“语音合成大模型（字符版）”并有对应音色授权。

### 2) 生成 mp3 到默认路径

在 `agent-server` 目录执行：

```bash
mkdir -p assets
python3 - <<'PY'
import base64, uuid
from pathlib import Path
import requests

env = {}
for ln in Path('.env').read_text(encoding='utf-8').splitlines():
    if '=' in ln and not ln.startswith('#'):
        k, v = ln.split('=', 1)
        env[k] = v

payload = {
    "app": {"appid": env["VOLC_APP_ID"], "token": "token", "cluster": "volcano_tts"},
    "user": {"uid": "pet-agent"},
    "audio": {"voice_type": "zh_female_meilinvyou_moon_bigtts", "encoding": "mp3"},
    "request": {
        "reqid": str(uuid.uuid4()),
        "text": "主人，我在。",
        "operation": "query",
    },
}
r = requests.post(
    "https://openspeech.bytedance.com/api/v1/tts",
    headers={"Authorization": f"Bearer;{env['VOLC_ACCESS_TOKEN']}"},
    json=payload,
    timeout=30,
)
data = r.json()
if r.status_code != 200 or data.get("code") != 3000 or not data.get("data"):
    raise SystemExit(f"TTS failed: http={r.status_code} code={data.get('code')} msg={data.get('message')}")
Path("assets/wake_ack_default.mp3").write_bytes(base64.b64decode(data["data"]))
print("OK -> assets/wake_ack_default.mp3")
PY
```

### 3) 指定默认音频并重启服务

`.env` 中确认：

```bash
WAKE_ACK_DEFAULT_AUDIO_PATH=/home/chenwei/pet_agent/agent-server/assets/wake_ack_default.mp3
WAKE_ACK_PREFER_CLOUD_TTS=1
WAKE_ACK_FALLBACK_LOCAL_TTS=1
```

重启：

```bash
cd ~/pet_agent/agent-server
pkill -f "python3 main.py" || true
libcamerify python3 main.py
```

### 4) 验证是否走默认 mp3

```bash
curl -X POST http://127.0.0.1:8000/wake/listen \
  -H "Content-Type: application/json" \
  -d '{"simulate_text":"Lemon Agent"}'
```

返回 `detail` 包含 `wake_ack=default_mp3` 即表示生效。

## 火山语音资源基线（来自 1.md）

以下信息用于记录当前可用的语音合成资源状态，便于后续排查 “requested resource not granted” 或音色回归问题。

### 服务状态

- 服务：`语音合成大模型-字符版`
- 版本：`正式版`
- 实例 ID：`BigTTS2000000627466185538`
- 并发：当前记录为 `10`（可增购）
- 字数包：`20000`（记录时使用 `0/20000`）

### 已验证可用音色（示例）

- `zh_female_meilinvyou_moon_bigtts`（魅力女友，当前默认唤醒语音）
- `zh_female_sajiaonvyou_moon_bigtts`（柔美女友）
- `zh_female_yuanqinvyou_moon_bigtts`（撒娇学妹）
- `zh_male_shenyeboke_moon_bigtts`（深夜播客）
- `zh_male_shaonianzixin_moon_bigtts`（少年梓辛）

### 接入与认证说明

- 接入方式：`API` / `SDK`
- 认证字段：`APP ID`、`Access Token`、`Secret Key`
- 真实值只允许放在 `agent-server/.env`，不要写入文档或代码。

## 安全要求

- 密钥仅放 `.env`，不要提交到仓库。
- 不在日志、README、代码中写入明文密钥。
- 建议定期轮换 API 凭证。
