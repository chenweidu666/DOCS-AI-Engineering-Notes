<!-- README 同步自私有仓库 ComfyUI-Workflow-Agent（仅首页说明，代码未包含） -->

# ComfyUI_Agent

5 模型 × 100 题材批量测试，结果自动拼图对比与表格汇总。

## 项目结构

```
ComfyUI_Agent/
├── model_theme_research/     # 实验目录（单文件整合）
│   ├── model_theme_research.py  # 主程序（子命令: check|run|collages|table|rerun|cleanup|all）
│   ├── experiment_prompts.json
│   ├── output/               # 生成图片、拼图
│   └── results/              # CSV、metadata
├── agent/                    # 图片、关键帧 Agent
├── video_agent/              # 视频测试（分镜→逐帧→ffmpeg）
└── docs/                     # 文档
```

## 使用

```bash
# 1. 启动 ComfyUI（在 ComfyUI_Workflow 运行 ./scripts/run_all.sh）

# 2. 运行实验
cd /home/cw/桌面/ComfyUI_Agent/model_theme_research
python3 model_theme_research.py all
```

流程：检查模型 → 运行实验 → 生成拼图 → 更新表格。

## 模型池

- Counterfeit-V2.5_fp16.safetensors
- Realistic_Vision_V5.1.safetensors
- chilloutmix_NiPrunedFp32Fix.safetensors
- majicmixRealistic_v7.safetensors
- deliberate_v2.safetensors

模型需放在 `/home/cw/桌面/ComfyUI/models/checkpoints`，至少 1.5GB 视为可用。
