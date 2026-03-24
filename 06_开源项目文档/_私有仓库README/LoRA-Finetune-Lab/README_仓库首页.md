<!-- README 同步自私有仓库 LoRA-Finetune-Lab（仅首页说明，代码未包含） -->

# lora-finetune-lab

LoRA/QLoRA 微调实践项目。基于 LLaMA-Factory + Qwen3-4B，在 RTX 3060 12GB 上完成 QLoRA SFT 微调全流程。

> **当前版本**：V2 训练流程进行中 — 使用 vLLM + Qwen3-8B-AWQ 对训练数据进行剧本风格扩写，扩写完成后将进行第二轮微调。

---

## 0. V2 训练流程（进行中）

### 0.1 问题分析

V1 训练完成后，微调模型存在 **回复过短** 的问题（仅一两句话）。原因分析：

| 问题 | 原因 | 影响 |
|------|------|------|
| 训练数据回复短 | 原始多轮对话中每轮 gpt 回复仅 50-200 字 | 模型学习了「简短回复」的模式 |
| 多轮合并为单轮 | rebuild_longform.py 拼接后仍偏短 | 平均长度不足 300 字 |
| 缺乏结构化格式 | 原始数据无场景/动作/心理等描写 | 模型输出缺乏层次感 |

### 0.2 数据演化路径

```
nsfw-sft-data/raw_pairs.jsonl (89,937条, 字幕原始句对)
  ↓ 场景聚合 + 改写
nsfw-sft-data/dataset_sharegpt.jsonl (3,391条, 多轮短对话, ~20字/回复)
  + nsfw-sft-data/rewritten.jsonl (3,491条, 场景描述)
  ↓ rebuild_longform.py — 合并多轮为单轮 + 插入动作描写
nsfw-sft-longform/dataset_sharegpt.jsonl (3,391条, 单轮, ~150字/条)  ← V1 训练数据
  ↓ expand_longform.py + vLLM (Qwen3-8B-AWQ)
nsfw-sft-longform/dataset_expanded.jsonl (3,391条, ~500字/条)  ← V2 训练数据
```

> 注：`nsfw-sft-data/dataset_alpaca.jsonl` (24,238条) 是 Alpaca 单轮指令格式的备用数据，不参与扩写流程。

### 0.3 V2 数据扩写方案

使用 **vLLM + Qwen3-8B-AWQ** 对 V1 数据集（`nsfw-sft-longform/dataset_sharegpt.jsonl`）进行 **剧本风格扩写**：

- 保留原始 `id`、`system`（角色设定）、`conversations[0]`（用户消息）
- 仅扩写 `conversations[1]`（gpt 回复）为结构化剧本
- 目标长度：400-800 字/条（原始 ~150 字/条）

**扩写格式示例**：
```
（场景描写）午后的阳光透过半掩的百叶窗洒进房间...
（动作指示）她轻轻侧过头，指尖划过桌面...
（对白台词）"今天...好像特别安静呢～" 她低声说道
「心理旁白」明明只是普通的一天，心跳却快了半拍...
```

### 0.4 V2 运行环境

| 组件 | 配置 |
|------|------|
| 推理引擎 | vLLM 0.15.1 (conda: `vllm-env`) |
| 模型 | Qwen3-8B-AWQ (4-bit AWQ 量化) |
| 模型位置 | 3060 HDD `/mnt/hdd/ai-models/modelscope/Qwen/Qwen3-8B-AWQ` |
| 服务端口 | `http://localhost:8101/v1` |
| pip 源 | 清华镜像 (`pypi.tuna.tsinghua.edu.cn`) |
| 扩写脚本 | `../1_数据工程/2_subtitle-sft-dataset/scripts/expand_longform.py` |

**启动 vLLM 服务**：
```bash
# 激活 conda 环境
conda activate vllm-env

# 启动 vLLM API (Qwen3-8B-AWQ)
python -m vllm.entrypoints.openai.api_server \
  --model /mnt/hdd/ai-models/modelscope/Qwen/Qwen3-8B-AWQ \
  --quantization awq_marlin \
  --served-model-name qwen3-8b \
  --max-model-len 4096 \
  --gpu-memory-utilization 0.90 \
  --host 0.0.0.0 --port 8101 \
  --dtype half --enforce-eager
```

**运行数据扩写**：
```bash
cd /tmp/expand-work  # 或项目 scripts/ 目录
PYTHONUNBUFFERED=1 python scripts/expand_longform.py
# 输出: datasets/nsfw-sft-longform/dataset_expanded.jsonl
# 进度: datasets/nsfw-sft-longform/.expand_progress.json (支持断点续跑)
```

### 0.5 V2 训练计划

扩写完成后的操作步骤：

1. **停止 vLLM 服务**，释放 GPU 显存
2. **复制扩写数据** 到 `data/` 目录，注册到 `dataset_info.json`
3. **调整训练配置**：增大 `cutoff_len`（1024 → 2048），适配更长文本
4. **启动 V2 QLoRA 训练**
5. **评测对比**：V1 vs V2 模型效果

### 0.6 V1 → V2 对比

| 维度 | V1 | V2 (规划) |
|------|-----|-----------|
| 训练数据 | 多轮合并，50-200字/条 | 剧本扩写，400-800字/条 |
| 数据格式 | 拼接文本 | 结构化剧本（场景/动作/台词/心理） |
| cutoff_len | 1024 | 2048 |
| 扩写模型 | — | Qwen3-8B-AWQ (vLLM) |
| 预期效果 | 回复简短 | 回复丰富、有层次感 |

---

## 1. V1 训练结果

### 1.1 模型产物

| 文件 | 位置 | 大小 | 说明 |
|------|------|------|------|
| `adapter_model.safetensors` | `output/qlora-sft/` | 127MB | LoRA 适配器权重 |
| `adapter_config.json` | `output/qlora-sft/` | 1KB | LoRA 配置（r=16, alpha=32, target=all） |
| `checkpoint-400/` | `output/qlora-sft/` | — | 最优 checkpoint（eval_loss=1.2368） |
| `checkpoint-600/` | `output/qlora-sft/` | — | epoch 3 checkpoint |
| `checkpoint-624/` | `output/qlora-sft/` | — | 最终 checkpoint |
| `model-00001-of-00002.safetensors` | `output/merged-model/` | 4.7GB | 合并后完整模型 (shard 1) |
| `model-00002-of-00002.safetensors` | `output/merged-model/` | 2.9GB | 合并后完整模型 (shard 2) |
| `generated_predictions.jsonl` | `output/eval-results/` | — | 测试集评测输出 |

**合并模型信息**：
- 架构：`Qwen3ForCausalLM`
- 精度：`bfloat16`
- 总大小：~7.6GB（2 个 safetensors 文件）
- 可独立部署：transformers / vLLM / GGUF 转换 / Ollama

### 1.2 训练数据来源

| 项目 | 说明 |
|------|------|
| 数据工程项目 | `../1_数据工程/2_subtitle-sft-dataset/`（git 分支: `v1`） |
| 训练集文件 | `datasets/nsfw-sft-data/dataset_sharegpt.jsonl` |
| 训练集条数 | 3,391 条多轮对话（ShareGPT 格式） |
| 测试集文件 | `data/test_sharegpt.jsonl`（100 条，seed=42 随机抽取） |
| 数据内容 | 240 部影片字幕 → 场景切分 → Qwen3-8B 改写 → 5 种角色人设 |
| 平均回复长度 | ~20 字/轮（多轮对话，4-8 轮/条） |

### 1.3 训练指标

| 指标 | 数值 |
|------|------|
| 基座模型 | Qwen3-4B (4-bit 量化) |
| 微调方法 | QLoRA SFT |
| 可训练参数 | 33,030,144 (33M) |
| 训练时长 | 1 小时 27 分 55 秒 |
| 训练 Loss | 1.2474 |
| 验证 Loss | 1.2488 |
| Epoch | 3.0 |
| LoRA 适配器大小 | 127 MB |
| GPU 峰值显存 | ~9.8 GB / 12 GB |

### 1.4 验证 Loss 变化

| Checkpoint | Epoch | Eval Loss | 趋势 |
|-----------|-------|-----------|------|
| step-200 | ~1.0 | 1.2823 | — |
| step-400 | ~2.0 | **1.2368** | ↓ 最优 |
| step-600 | ~3.0 | 1.2492 | ↑ 轻微过拟合 |
| 最终 | 3.0 | 1.2488 | — |

> Loss 在 epoch 2 达到最低，epoch 3 略有回升，整体可控。如需更优结果，可加载 checkpoint-400。

### 1.5 测试集评测

从 3,491 条原始数据中随机抽取 100 条作为独立测试集（seed=42），训练时不可见。

| 指标 | 数值 |
|------|------|
| BLEU-4 | 7.01 |
| ROUGE-1 | 32.84 |
| ROUGE-2 | 17.13 |
| ROUGE-L | 31.46 |
| 推理速度 | 1.85 samples/s |

> 注：此类角色扮演任务的回复高度开放，BLEU/ROUGE 仅供参考，实际效果需结合人工评估。

## 2. 环境配置

### 2.1 硬件

| 组件 | 规格 |
|------|------|
| GPU | NVIDIA RTX 3060 12GB |
| 系统盘 | SSD 218GB |
| 数据盘 | HDD 1TB (`/mnt/hdd/`) |
| NAS | Synology (CIFS 挂载) |

### 2.2 Conda 环境

基于 `vllm-env` 克隆创建独立的 `lora-env` 环境：

```bash
# 一键安装（克隆 vllm-env → lora-env，安装 LLaMA-Factory 依赖）
bash scripts/setup_env.sh

# 手动激活
conda activate lora-env
```

主要依赖：
- LLaMA-Factory (torch + metrics)
- bitsandbytes, peft, trl, datasets
- scipy, tiktoken, tensorboard, nvitop, modelscope

> 所有 `scripts/*.sh` 脚本会自动激活 `lora-env`，无需手动操作。


## 3. 数据集

### 3.1 数据来源

数据集由 [subtitle-sft-dataset](../../1_数据工程/2_subtitle-sft-dataset/) 项目生成。

### 3.2 数据划分

| 集合 | 文件 | 数量 | 说明 |
|------|------|------|------|
| 训练集 | `data/dataset_sharegpt.jsonl` | 3,391 条 | 多轮对话 ShareGPT 格式 |
| 测试集 | `data/test_sharegpt.jsonl` | 100 条 | 独立测试集 (seed=42) |
| 测试 Prompt | `data/test_prompts.jsonl` | 100 条 | 仅首轮 user 输入 + 参考回复 |
| 备用格式 | `data/dataset_alpaca.jsonl` | 24,238 条 | Alpaca 单轮指令格式 |

### 3.3 数据格式 (ShareGPT)

```json
{
  "id": "CAWD-243_0042",
  "system": "你是小悠，一个温柔体贴的角色扮演助手...",
  "conversations": [
    {"from": "human", "value": "用户消息"},
    {"from": "gpt", "value": "模型回复"},
    ...
  ]
}
```

## 4. 项目结构

```
3_lora-finetune-lab/
├── README.md                          # 本文档
├── .gitignore
├── configs/                           # 配置文件
│   ├── qlora_sft.yaml                 # QLoRA 训练配置
│   ├── lora_sft.yaml                  # LoRA 训练配置 (高显存)
│   ├── eval_predict.yaml              # 测试集评测配置
│   ├── inference.yaml                 # 交互式对话配置
│   ├── merge_lora.yaml                # LoRA 合并配置
│   └── api_serve.yaml                 # API 服务配置
├── scripts/                           # 一键脚本
│   ├── setup_env.sh                   # 创建 lora-env conda 环境
│   ├── _activate_env.sh               # 公共：激活 conda 环境
│   ├── train.sh                       # 启动训练
│   ├── eval.sh                        # 测试集评测
│   ├── chat.sh                        # 交互对话
│   ├── merge.sh                       # 合并 LoRA
│   └── serve.sh                       # vLLM 部署
├── data/                              # 数据集
│   ├── dataset_info.json              # LLaMA-Factory 数据注册
│   ├── dataset_sharegpt.jsonl         # 训练集 (3,391 条)
│   ├── test_sharegpt.jsonl            # 测试集 (100 条)
│   ├── test_prompts.jsonl             # 测试 Prompt
│   └── dataset_alpaca.jsonl           # Alpaca 格式备用
└── output/                            # 训练输出 (gitignored)
    ├── qlora-sft/                     # LoRA checkpoint + 适配器
    │   ├── adapter_model.safetensors  # LoRA 权重 (127MB)
    │   ├── checkpoint-400/            # 最优 checkpoint
    │   ├── checkpoint-600/
    │   └── checkpoint-624/
    ├── eval-results/                  # 测试集评测结果
    │   └── generated_predictions.jsonl
    └── merged-model/                  # 合并后完整模型
```

## 5. 使用指南

### 5.1 训练

```bash
# QLoRA 训练 (3060 12GB)
bash scripts/train.sh

# 或指定配置
bash scripts/train.sh configs/lora_sft.yaml

# TensorBoard 监控
tensorboard --logdir output/qlora-sft --host 0.0.0.0 --port 6006
# 访问 http://192.168.31.117:6006
```

### 5.2 测试集评测

```bash
bash scripts/eval.sh
# 结果: output/eval-results/generated_predictions.jsonl
```

### 5.3 交互对话测试

```bash
bash scripts/chat.sh
# 输入对话内容，输入 exit 退出
```

### 5.4 启动 API 服务

```bash
# LLaMA-Factory 内置 OpenAI 兼容 API
llamafactory-cli api configs/api_serve.yaml
# 服务地址: http://192.168.31.117:8000
# API 文档: http://192.168.31.117:8000/docs
```

**调用示例 (curl)**:

```bash
curl http://192.168.31.117:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen3-4B-chat",
    "messages": [
      {"role": "system", "content": "你是小悠，一个温柔体贴的角色扮演助手。"},
      {"role": "user", "content": "今天过得怎么样？"}
    ],
    "temperature": 0.8,
    "max_tokens": 256
  }'
```

**调用示例 (Python)**:

```python
from openai import OpenAI

client = OpenAI(base_url="http://192.168.31.117:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="Qwen3-4B-chat",
    messages=[
        {"role": "system", "content": "你是小悠，一个温柔体贴的角色扮演助手。"},
        {"role": "user", "content": "今天过得怎么样？"}
    ],
    temperature=0.8,
    max_tokens=256
)
print(response.choices[0].message.content)
```

### 5.5 合并 LoRA → 完整模型

```bash
bash scripts/merge.sh
# 输出: output/merged-model/
# 合并后可脱离 LLaMA-Factory，用 transformers/vLLM 独立部署
```

## 6. 训练配置详解

### 6.1 实际使用的 QLoRA 配置

| 参数 | 值 | 说明 |
|------|-----|------|
| model | Qwen3-4B | 从 Qwen3-8B 降级，适配 12GB 显存 |
| quantization_bit | 4 | 4-bit NF4 量化 |
| lora_rank | 16 | 从 64 降低以节省显存 |
| lora_alpha | 32 | rank × 2 |
| lora_target | all | 所有线性层 |
| lora_dropout | 0.05 | — |
| per_device_train_batch_size | 1 | 从 2 降低以避免 OOM |
| gradient_accumulation_steps | 16 | 有效 batch = 16 |
| cutoff_len | 1024 | 从 2048 降低以节省显存 |
| learning_rate | 2e-4 | — |
| num_train_epochs | 3.0 | — |
| lr_scheduler | cosine | 余弦退火 |
| warmup_ratio | 0.1 | — |
| bf16 | true | BFloat16 混合精度 |
| gradient_checkpointing | true | 用时间换显存 |

### 6.2 显存优化策略

RTX 3060 12GB 跑 4B 模型微调需要多重优化：

1. **4-bit 量化 (QLoRA)** — 模型权重从 ~8GB 压缩到 ~2.5GB
2. **梯度检查点** — 不保存中间激活值，反向传播时重新计算
3. **小 batch size** — per_device_train_batch_size=1
4. **短序列** — cutoff_len=1024 (减少注意力矩阵显存)
5. **小 LoRA rank** — rank=16 (可训练参数 33M vs rank=64 的 ~130M)
6. **expandable_segments** — `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` 减少碎片

### 6.3 踩坑记录

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| Qwen3-8B OOM | 8B 模型即使 4-bit 量化也超 12GB | 换 Qwen3-4B |
| batch_size=2 OOM | cross_entropy 需要 batch × seq × vocab 的 logits | batch=1, cutoff=1024 |
| `lora_target: all_linear` 报错 | PEFT 版本不支持 `all_linear` | 改为 `all` |
| 模型加载慢 | 从 NAS (CIFS) 读取大文件瓶颈 | 复制到本地 HDD `/mnt/hdd/models/` |
| V1 模型回复太短 | 训练数据平均仅 ~150 字/条 | V2: vLLM 扩写为 500-800 字剧本 |
| AutoAWQ import 失败 | transformers 新版删除了 `PytorchGELUTanh` | 不影响 vLLM 内置 AWQ 支持 |
| Python 输出不显示 | nohup 重定向时 stdout 默认全缓冲 | `PYTHONUNBUFFERED=1` |

## 7. 存储架构

### 7.1 模型存储

| 内容 | 位置 | 大小 | 说明 |
|------|------|------|------|
| Qwen3-4B 基座 | 3060 HDD `/mnt/hdd/models/Qwen/Qwen3-4B` | ~8GB | 训练用，本地读取快 |
| Qwen3-8B-AWQ | 3060 HDD `/mnt/hdd/ai-models/modelscope/Qwen/Qwen3-8B-AWQ` | ~5GB | V2 扩写用 (vLLM) |
| Qwen3-4B (NAS) | NAS `3_模型部署/models/Qwen/Qwen3-4B` | ~8GB | NAS 备份 |
| Qwen3-8B (NAS) | NAS `3_模型部署/models/Qwen/Qwen3-8B` | ~16GB | NAS 备份 |
| V1 LoRA 适配器 | NAS `output/qlora-sft/` | 127MB | V1 训练结果 |

### 7.3 架构图

```
┌──────────────────────────────────────────────────┐
│                  NAS (Synology)                   │
│  /For-Work/2_项目经验/1_大模型/                    │
│  ├── 1_数据工程/2_subtitle-sft-dataset/           │
│  │   └── datasets/ (训练数据源 + 扩写数据)         │
│  ├── 2_模型微调/3_lora-finetune-lab/              │
│  │   ├── configs/ data/ scripts/ (项目代码)       │
│  │   └── output/ (LoRA checkpoint + 评测结果)     │
│  └── 3_模型部署/models/Qwen/ (模型备份)           │
│  ← CIFS 挂载: /mnt/nas/personal/For-Work/        │
└──────────────────────────────────────────────────┘
                        │
              ┌─────────┴──────────┐
              │  RTX 3060 (12GB)   │
              ├────────────────────┤
              │ SSD 218GB          │
              │  └─ OS + conda     │
              │     ├─ vllm-env    │
              │     └─ lora-env    │
              │ HDD 1TB            │
              │  ├─ models/        │
              │  │  └─ Qwen3-4B    │
              │  └─ ai-models/     │
              │     └─ Qwen3-8B-AWQ│
              └────────────────────┘
```

## 8. 工作流

### 8.1 V1 流程（已完成）

```
数据工程                              模型微调                          部署
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━    ━━━━━━━━━━━━
字幕 → 句对 → 场景 → 改写 → 格式化 → QLoRA 训练 → 评测 → 合并模型 → API 服务
                                      │                                  │
                                      └─ TensorBoard 监控               └─ OpenAI 兼容
                                         :6006                              :8000
```

### 8.2 V2 流程（进行中）

```
V1 数据集 (3,391条, ~150字/条)
  │
  ↓  vLLM (Qwen3-8B-AWQ, conda:vllm-env, :8101)
  │  expand_longform.py — 剧本风格扩写
  ↓
V2 数据集 (3,391条, ~500字/条, 结构化剧本)
  │
  ↓  停止 vLLM → 释放 GPU
  │
QLoRA V2 训练 (cutoff_len=2048)
  │
  ↓  评测对比 V1 vs V2
  │
V2 合并模型 → API 服务 / GGUF 导出 / Ollama
```

### 8.3 环境切换

```
┌───────────────────────────────────────────┐
│          3060 Host (conda 环境)            │
│                                           │
│  vllm-env ──→ vLLM 推理 / 数据扩写        │
│  lora-env ──→ LLaMA-Factory 训练 / 评测    │
│                                           │
│  ※ 两个环境共享 GPU，不可同时使用            │
│  ※ pip/conda 均配置清华镜像                 │
└───────────────────────────────────────────┘
```
