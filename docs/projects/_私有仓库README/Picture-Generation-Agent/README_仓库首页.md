<!-- README 同步自私有仓库 Picture-Generation-Agent（仅首页说明，代码未包含） -->

# picture_agent

`picture_agent` 是一条自动化出图链路：

1. 用 Qwen 直接生成英文提示词
2. 调用 ComfyUI 批量推理
3. 自动评分并选择最佳结果

## 推荐：Docker 运行

### 前置条件

- 已安装 Docker / Docker Compose
- 本机 ComfyUI 已启动（默认 `http://127.0.0.1:8188`）
- 已准备模型目录（默认 `/home/cw/桌面/ComfyUI/models/checkpoints`）
- 已设置 `DASHSCOPE_API_KEY`

### 启动

```bash
cd /home/cw/Agent-Project/Picture_Agent
docker compose up --build -d
```

启动后访问：`http://127.0.0.1:7861`

### 常用环境变量

- `DASHSCOPE_API_KEY`: Qwen API Key（必填）
- `COMFY_BASE`: ComfyUI 地址（默认 `http://host.docker.internal:8188`）
- `CKPT_DIR_HOST`: 主机模型目录（默认 `/home/cw/桌面/ComfyUI/models/checkpoints`）
- `SKIP_LOCAL_MODEL_CHECK`: 默认 `1`，跳过本地 checkpoint 存在性检查
- `PREFERRED_MODEL`: 默认 `Counterfeit-V2.5_fp16.safetensors`，页面默认选中该模型

示例：

```bash
export DASHSCOPE_API_KEY="你的key"
export COMFY_BASE="http://host.docker.internal:8188"
export CKPT_DIR_HOST="/home/cw/桌面/ComfyUI/models/checkpoints"
docker compose up --build -d
```

### 停止

```bash
docker compose down
```

### 萌图专用程序（独立）

- 程序路径：`src/cute_picture_agent.py`
- 网页入口：创建任务区域的 `萌图生成一次`
- 数据展示：与普通任务共用同一任务列表、画廊、日志

命令行示例：

```bash
python3 src/cute_picture_agent.py --request "猫耳少女在樱花树下微笑" -n 2
```

## 本地直跑（可选）

```bash
python3 src/picture_agent.py --request "写实风格街头人像，夜景霓虹，电影感" -n 4
```

## 挑图后美化 + 超分链路

用于“手机/相册挑图后再精修”的批处理脚本：`src/retouch_upscale_agent.py`

示例：

```bash
python3 src/retouch_upscale_agent.py \
  --input-dir "/home/cw/Agent-Project/Picture_Agent/output/run_xxx" \
  --auto-repair \
  --repair-strength 0.55 \
  --preset anime_soft \
  --upscale-scale 2.0 \
  --max-side 2048
```

可选参数：

- `--output-dir`: 自定义输出目录（默认自动新建 `*_retouch_时间戳`）
- `--preset`: `anime_soft` / `anime_pop` / `realistic_clean`
- `--auto-repair`: 自动局部修复（轻量 inpaint 思路）
- `--repair-strength`: 自动修复强度（0~1，建议 `0.45~0.7`）
- `--no-upscale`: 只美化不超分
- `--limit`: 仅处理前 N 张（便于快速测试）

## Qwen + 万象超分（云端）

脚本：`src/wanx_enhance_agent.py`  
用途：先让 Qwen 自动设计“细节修复 + 超清”提示词，再调用万象 `super_resolution` 处理图片。

示例（处理两张）：

```bash
python3 src/wanx_enhance_agent.py \
  --images \
    "/home/cw/Agent-Project/Picture_Agent/output/run_20260225_063611/candidate_001_Counterfeit-V2.png" \
    "/home/cw/Agent-Project/Picture_Agent/output/run_20260225_063611/candidate_002_Counterfeit-V2.png" \
  --upscale-factor 2
```

## 生成后自动万象修复（style 一条龙）

本地直跑 `style_picture_agent.py` 时可直接开启：

```bash
python3 src/style_picture_agent.py \
  --mode cute \
  --request "可爱少女头像，干净背景" \
  -n 2 \
  --internal-run \
  --wanx-enhance \
  --wanx-upscale-factor 2
```
