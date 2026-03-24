<!-- README 同步自私有仓库 ComfyUI-Image-Agent（仅首页说明，代码未包含） -->

# comfy-image-agent

本项目是基于本机 `ComfyUI` 的图像生成工作流，提供统一测试脚本与多个业务入口。
当前默认模式为本地运行（`127.0.0.1`），不依赖 SSH。

## 快速开始

```bash
bash scripts/setup_project_env.sh
bash scripts/test_full.sh
```

推荐 `.env`：

```env
PROFILE=3060
COMFY_BASE=http://127.0.0.1:18188
COMFY_BASE_3060=http://127.0.0.1:18188
LOCAL_COMFY_ROOT=/home/cw/ComfyUI
LOCAL_COMFY_LOG=/tmp/comfyui_local.log
```

## 入口脚本

- `src/picture_agent.py`：核心执行器（组装 workflow、提交 ComfyUI、下载、评分）
- `src/style_picture_agent.py`：`mode -> prompt` 包装层
- `src/avatar_headshot_agent.py`：头像场景入口
- `src/nsfw_agent.py`：低尺度 tease（soft）
- `src/nsfw_agent_v2.py`：高尺度 tease（hard）

## 统一测试脚本

脚本：`scripts/test_full.sh`

默认行为：

- 按 README 模型清单做校验（文件存在 / 符号链接 / 统一路径）
- 图片模型最小烟测（默认每模型 `1` 张，分辨率 `256x256`）
- 视频模型最小烟测（默认开启，可 `VIDEO_SMOKE=0` 关闭）
- 单模型超时保护（默认 `420s`）

常用示例：

```bash
bash scripts/test_full.sh
VIDEO_SMOKE=0 bash scripts/test_full.sh
VIDEO_WORKFLOW_FILE=/abs/path/to/wan22_i2v_api.json bash scripts/test_full.sh
MODELS="beautifulRealistic_v7.safetensors,Realistic_Vision_V6.0_fp16.safetensors" bash scripts/test_full.sh
```

## 模型存储策略（统一）

- 实体文件统一放在：`/mnt/sdb1/ComfyUI-models`
- `ComfyUI` 模型目录：`/home/cw/ComfyUI/models`（仅符号链接）
- 建议格式：`/mnt/sdb1/ComfyUI-models/<模型类别>/<权重文件>`

## 当前模型清单

来源：`/home/cw/ComfyUI/models`

| 类别 | 组件 | 文件 | 状态 | 位置 | 备注 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 图片模型 | Checkpoint | `beautifulRealistic_v7.safetensors` | 已就绪 | `models/checkpoints` | 符号链接 |
| 图片模型 | Checkpoint | `Counterfeit-V2.5_fp16.safetensors` | 已就绪 | `models/checkpoints` | 符号链接 |
| 图片模型 | Checkpoint | `JuggernautXL_Ragnarok.safetensors` | 已就绪 | `models/checkpoints` | 符号链接 |
| 图片模型 | Checkpoint | `Pony_Realism_v2.2.safetensors` | 已就绪 | `models/checkpoints` | 符号链接 |
| 图片模型 | Checkpoint | `Realistic_Vision_V6.0_fp16.safetensors` | 已就绪 | `models/checkpoints` | 符号链接 |
| 图片模型 | Checkpoint | `RealVisXL_V6.0.safetensors` | 已就绪 | `models/checkpoints` | 符号链接 |
| 图片模型 | Checkpoint | `CyberRealistic_Pony_v8.5.safetensors` | 未就绪 | `models/checkpoints` | `nsfw_agent_v2.py` 随机模型池包含该项 |
| 视频模型（Wan2.2 / I2V） | UNet（高噪） | `wan2.2_i2v_high_noise_14B_Q4_K_M.gguf` | 已就绪 | `models/unet` | 符号链接 |
| 视频模型（Wan2.2 / I2V） | UNet（低噪） | `wan2.2_i2v_low_noise_14B_Q4_K_M.gguf` | 已就绪 | `models/unet` | 符号链接 |
| 视频模型（Wan2.2 / I2V） | VAE | `Wan2.1_VAE.pth` | 已就绪 | `models/vae` | 符号链接 |
| 视频模型（Wan2.2 / I2V） | Text Encoder | `models_t5_umt5-xxl-enc-bf16.pth` | 已就绪 | `models/text_encoders` | 符号链接 |
| 视频模型（Wan2.2 / I2V） | Text Encoder（fp8） | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | 已就绪 | `models/text_encoders/split_files/text_encoders` | 符号链接 |
| 视频模型（Wan2.2 / I2V） | CLIP Vision | `clip_vision_h.safetensors` | 未就绪 | `models/clip_vision` | 当前仅占位文件 |

说明：

- `test_full.sh` 会读取本表作为默认测试清单。
- 标记为 `已就绪` 的图片模型会进入 checkpoint 烟测。
- 标记为 `未就绪` 的模型仅统计告警，不进入图片烟测。

## 常用脚本

- `scripts/test_full.sh`：统一最小测试（默认图片 + 视频）
- `scripts/setup_project_env.sh`：创建/固定项目 Python 环境
- `scripts/ensure_3060_service.sh`：历史远端脚本，本地模式通常不需要
- `scripts/lock_3060_env.sh`：历史远端脚本，本地模式通常不需要

## 目录结构

```text
archive_projects/comfy-image-agent/
├── src/
│   ├── pipeline/main.py
│   ├── picture_agent.py
│   ├── style_picture_agent.py
│   ├── avatar_headshot_agent.py
│   ├── nsfw_agent.py
│   ├── nsfw_agent_v2.py
│   └── shared/
│       ├── comfy_runtime.py
│       └── model_manager.py
├── config/
├── scripts/
├── output/
├── workspace/
└── README.md
```

# comfy-image-agent

本项目是基于本机 `ComfyUI` 的图像生成工作流，提供统一测试脚本与多个业务入口。
当前默认模式为本地运行（`127.0.0.1`），不依赖 SSH。

## 快速开始

```bash
# 1) 初始化环境
bash scripts/setup_project_env.sh

# 2) 统一最小测试（默认图片 + 视频）
bash scripts/test_full.sh
```
