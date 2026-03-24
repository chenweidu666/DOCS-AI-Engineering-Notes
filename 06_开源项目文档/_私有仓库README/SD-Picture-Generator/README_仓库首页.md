<!-- README 同步自私有仓库 SD-Picture-Generator（仅首页说明，代码未包含） -->

# AI Picture Generator

AI 图片批量生成工具集，包含云端 API 版和本地推理版两套方案，用于游戏项目 *Midnight Stories* 的素材生产。

## 项目结构

```
1_AI_Picture_Generator/
├── 1_AI_Picture_Generator_API/     # 云端 API 版（火山引擎 / 阿里云）
└── 2_AI_Picture_Generator_Local/   # 本地推理版（ComfyUI 双后端）
```

---

## 1_AI_Picture_Generator_API — 云端 API 版

调用商业 API 生成高质量图片及 3D 资产。

### 后端服务

| 服务 | 模型 | 用途 |
|------|------|------|
| 火山引擎 | Seedream 4.0 | 文生图（2K 分辨率） |
| 阿里云通义万相 | wan2.6 | 文生图（国内访问备选） |
| 火山引擎 | Seed3D 1.0 | 图生 3D（输出 PBR/RGB GLB） |

### 主要功能

- **文生图**：支持 12 种风格预设（角色立绘、场景、UI 等）
- **换装生成**：以参考图 + 服装描述生成角色变体
- **图生 3D**：将 2D 立绘转为 GLB 三维模型（PBR/RGB 双格式）
- **批量预设**：内置游戏项目批量任务配置

### 快速使用

```bash
cd 1_AI_Picture_Generator_API

# 文生图
python generate.py image --prompt "anime girl, office outfit" --style char_front

# 换装
python generate.py outfit --base chinatsu_base.jpg --outfit "office suit"

# 图生3D
python generate.py 3d --image chinatsu_outfit_office.jpg
```

---

## 2_AI_Picture_Generator_Local — 本地推理版

基于 ComfyUI 的双后端批量推理系统，支持自动提示词生成与图片质量评分。

### 架构

```
Qwen 生成提示词 → ComfyUI 批量推理 → 自动评分选最佳图
```

### 双后端配置

| 后端 | 设备 | 端口 | Checkpoint 数量 |
|------|------|------|----------------|
| 3060 | RTX 3060 (CUDA) | 18188 | 5 个 |
| mac  | MacBook Air (MPS) | 28188 | 1 个 |

连接方式：SSH 隧道转发，`dispatch.sh` 按 8:1 速度比自动分配任务。

### 模型池（SD Checkpoints）

- `Counterfeit-V2.5`（动漫风）
- `Realistic_Vision_V5.1`（写实风）
- `chilloutmix`（混合风）
- `majicmixRealistic_v7`（写实风）
- `deliberate_v2`（写实风）

### 生成模式

| 模式 | 说明 |
|------|------|
| `cute` | 萌系风格 |
| `lingerie` | 内衣写真 |
| `adult` | 成人内容（需解锁模型） |
| `couple` | 双人场景 |
| `tease` | 擦边写真 |
| `abstract` | 抽象艺术 |

### 快速使用

```bash
cd 2_AI_Picture_Generator_Local

# 配置环境
cp .env.example .env
# 编辑 .env，填写 DASHSCOPE_API_KEY

# 安装依赖
pip install -r requirements.txt

# 单机运行（自动选后端）
python src/style_picture_agent.py --mode cute --count 5

# 双后端并行调度
bash scripts/dispatch.sh --mode nsfw_boudoir
```

### 环境变量（.env）

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `DASHSCOPE_API_KEY` | 阿里云 API Key（Qwen 提示词生成） | — |
| `PROFILE` | 后端选择 `3060 / mac / auto` | `auto` |
| `COMFY_BASE` | 手动指定 ComfyUI 地址 | — |
| `PICTURE_AGENT_UPSCALE` | 开启超分后处理 | `true` |

---

## 输出

所有生成图片保存至各子项目的 `output/` 目录（已加入 `.gitignore`）。

每次运行生成 JSON 清单（`output/*/manifests/`），记录：
- 提示词、seed、模型、后端
- 亮度 / 色彩 / 锐度三维质量评分
- 最终入选图片路径
