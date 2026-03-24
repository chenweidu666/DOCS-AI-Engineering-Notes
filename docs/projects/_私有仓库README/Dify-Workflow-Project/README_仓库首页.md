<!-- README 同步自私有仓库 Dify-Workflow-Project（仅首页说明，代码未包含） -->

# Dify Project 目录结构说明

## 📁 目录结构

```
dify_project/
├── workflows/           # 工作流文件
│   ├── btc/            # BTC 分析工作流
│   │   ├── btc.yaml                    # 主工作流文件（已优化，可直接导入）
│   │   ├── btc.yaml.fixed              # 简化版（无搜索功能）
│   │   ├── btc.yaml完整版（含搜索）    # 完整版（含搜索功能）
│   │   ├── btc.yaml配置指南.md         # 详细配置说明
│   │   └── btc.yaml配置清单.md         # 配置检查清单
│   └── tests/          # 测试工作流
│       ├── test_qwen_api.yaml          # 简单 API 测试
│       ├── test_qwen_api_完整版.yaml   # 完整 API 测试
│       ├── 测试说明.md                 # 测试详细说明
│       └── 快速测试指南.md             # 快速测试指南
├── docs/               # 文档文件
│   ├── 自动导入DSL配置指南.md          # 自动导入 DSL 配置与使用（推荐）
│   ├── 配置通义千问API.md              # API 配置指南
│   ├── 手动配置指南.md                 # 手动配置步骤
│   └── 配置检查清单.md                 # 配置检查清单
├── scripts/            # 脚本文件
│   ├── 智能导入工作流.py               # 自动导入 DSL（推荐）
│   ├── 自动导入工作流.py               # 基础自动导入
│   └── 自动配置通义千问.py             # 自动配置脚本
├── configs/            # 配置文件目录
│   ├── qwen.yaml                       # 通义千问 API Key 配置
│   └── README.md                       # 配置目录说明
└── README.md           # 本文件

```

## 🚀 快速开始

### 1. 配置通义千问 API

**API Key**: 见 `configs/qwen.yaml`（已移动到项目内）

**配置步骤**:
1. 访问: http://localhost
2. 设置 → 模型供应商 → 通义千问
3. 添加 API Key: `sk-f62a8c8f318240e4874ef0095e7173b4`
4. 保存

详细说明见: `docs/配置通义千问API.md`

### 2. 测试 API（推荐先测试）

**测试文件**: `workflows/qwen_tests/test_qwen_api.yaml`

**步骤**:
1. Dify Web → 创建应用 → 从 DSL 导入
2. 选择测试文件
3. 运行测试

详细说明见: `workflows/qwen_tests/快速测试指南.md`

### 3. 导入工作流（手动或自动）

**手动导入**: Dify Web → 创建应用 → 从 DSL 导入 → 选择 YAML 文件

**自动导入**（一条命令，适合本地 Dify）:
1. 配置认证：见 `docs/自动导入DSL配置指南.md`
2. 执行：`python3 scripts/智能导入工作流.py workflows/us_stock_analysis/us_stock.yaml`

详细说明见: `docs/自动导入DSL配置指南.md`

## 📋 文件说明

### 工作流文件

#### BTC 工作流 (`workflows/btc/`)
- **btc.yaml** - 主工作流（推荐使用）
  - 已优化，可直接导入
  - 移除了搜索工具依赖
  - 使用通义千问模型

- **btc.yaml.fixed** - 简化版
  - 无搜索功能
  - 更简单，适合快速测试

- **btc.yaml完整版（含搜索）** - 完整版
  - 包含新闻搜索功能
  - 需要先安装搜索工具

#### 测试工作流 (`workflows/qwen_tests/`)
- **test_qwen_api.yaml** - 简单测试
  - 快速验证 API 是否可用
  - 只测试基础对话

- **test_qwen_api_完整版.yaml** - 完整测试
  - 测试多个场景
  - 更详细的测试结果

### 文档文件 (`docs/`)
- **配置通义千问API.md** - API 配置详细指南
- **手动配置指南.md** - 手动配置步骤
- **配置检查清单.md** - 配置检查清单

### 脚本文件 (`scripts/`)
- **自动配置通义千问.py** - 自动配置脚本（需要 Dify API Key）

## 🔧 使用建议

1. **首次使用**:
   - 先配置通义千问 API（见 `docs/`）
   - 运行测试工作流验证配置（见 `workflows/qwen_tests/`）
   - 导入 BTC 工作流使用（见 `workflows/btc/`）

2. **选择工作流版本**:
   - 新手/快速测试: 使用 `btc.yaml.fixed`
   - 正常使用: 使用 `btc.yaml`
   - 需要新闻功能: 使用 `btc.yaml完整版（含搜索）`

3. **遇到问题**:
   - 查看对应的配置指南文档
   - 检查配置检查清单
   - 运行测试工作流定位问题

## 📝 相关文件

- **API Key 配置**: `configs/qwen.yaml`
- **Dify 安装目录**: `/home/cw/桌面/AI/dify/`

## 🎯 目录组织原则

- **workflows/** - 所有工作流 DSL 文件
  - **btc/** - BTC 相关工作流及文档
  - **tests/** - 测试工作流及文档
- **docs/** - 通用文档和指南
- **scripts/** - 自动化脚本

---

**最后更新**: 2026-01-30
