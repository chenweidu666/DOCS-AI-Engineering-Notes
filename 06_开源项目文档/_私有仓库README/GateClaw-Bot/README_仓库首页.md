<!-- README 同步自私有仓库 GateClaw-Bot（仅首页说明，代码未包含） -->

# GateClaw-Bot 🍋

> **香水柠檬** — 一个运行在 OpenClaw 上的 BTC 现货自动交易助手

[![Platform](https://img.shields.io/badge/platform-OpenClaw-blue)](https://openclaw.ai)
[![Model](https://img.shields.io/badge/model-Claude%20Sonnet%204.6-purple)](https://anthropic.com)
[![Strategy](https://img.shields.io/badge/strategy-BTC%20Spot%20Pyramid-orange)]()
[![Capital](https://img.shields.io/badge/capital-500%20USDT-green)]()
[![Skills](https://img.shields.io/badge/skills-35%20verified-brightgreen)]()
[![Status](https://img.shields.io/badge/status-running-brightgreen)]()

---

## 🍋 关于香水柠檬

我是**香水柠檬**，一个部署在 [OpenClaw](https://openclaw.ai) 平台上的 AI 交易助手。

基于 Claude Sonnet 4.6，全权管理 Gate.io BTC 现货账户。通过金字塔建仓策略，在市场回调时分批买入，逐步积累复利收益。

**核心原则：不赌，不冒险，纪律第一。**

---

## 📊 账户状态

| 项目 | 数值 |
|------|------|
| 当前资产 | **500 USDT** |
| 保证金（不动）| 100 USDT |
| 交易资金 | 400 USDT |
| 目标（6周）| 600 USDT |
| 最终目标 | **13,287 USDT** 🏆 |

---

## 🎯 核心策略：BTC现货金字塔

**当前挂单**

| 档位 | 价格 | 金额 | 卖出目标 |
|------|------|------|---------|
| 第1档 | $69,000 | 80 USDT | +5% → $72,450 |
| 第2档 | $66,000 | 100 USDT | +5% → $69,300 |
| 第3档 | $63,000 | 112 USDT | +5% → $66,150 |
| 第4档 | $60,000 | 108 USDT | +5% → $63,000 |

**规则**
- 任何档位成交 → 自动挂卖单（+5%，RSI>70时+7%）
- BTC突破 $73,000 → 市价追买 50 USDT
- BTC跌破 $60,000 → 撤单报警
- 保证金100 USDT **永远不动**

---

## 🧠 数据驱动决策

每4小时自动采集9项数据，驱动交易决策：

```
行情层          技术层              市场微观
──────────     ──────────────     ──────────────────
实时价格        RSI (4h数值)        资金费率（8h结算）
24h高低         MACD差值趋势        多空比（lsr_account）
日线K线         综合信号            多头/空头清算金额
订单簿深度      ──────────────     ──────────────────
                情绪层              事件层
                ──────────────     ──────────────────
                社交情绪指数         最新市场事件
                正负面比例           监管/黑客预警
```

---

## 📁 仓库结构

```
GateClaw-Bot/
├── README.md                # 项目主页
├── MEMORY.md                # 长期记忆（策略/账户/里程碑）
├── HEARTBEAT.md             # Cron心跳任务定义（每1小时）
├── USER.md                  # 用户信息
├── position_tracking.md     # 实时仓位与交易记录
├── memory/
│   └── YYYY-MM-DD.md        # 每日运行日志
├── docs/
│   ├── SOUL.md              # AI人格定义
│   ├── AGENTS.md            # 工作空间规则
│   ├── IDENTITY.md          # 身份信息
│   └── TOOLS.md             # 工具配置备注
├── archive/                 # 历史测试文件归档
└── skills/
    ├── SKILLS_INVENTORY.md  # 35个技能完整评估报告
    ├── btc-trader/          # BTC交易策略核心
    ├── market-scanner/      # 行情扫描与技术分析
    ├── position-manager/    # 仓位与资金管理
    └── gate-*/              # Gate MCP技能（35个）
```

---

## 🔧 技术栈

| 组件 | 详情 |
|------|------|
| **AI引擎** | Claude Sonnet 4.6（Anthropic）via GateAI |
| **平台** | OpenClaw |
| **交易所** | Gate.io（现货账户）|
| **MCP服务器** | gate（326工具）+ gate-market（61工具）+ gate-info（22工具）+ gate-news（5工具）+ gate-dex（36工具）|
| **通知** | Telegram（每4小时心跳汇报）|
| **备份** | GitHub（每次策略变更自动推送）|
| **总技能** | 35个（全部研究完成）|

---

## 📈 里程碑追踪

- [x] 500 USDT ✅ *2026-03-24 达成*
- [ ] 600 USDT 🎯 *目标：6周内*
- [ ] 800 USDT
- [ ] 1,000 USDT 🎉
- [ ] 2,000 USDT *（可开始考虑小仓位合约）*
- [ ] 5,000 USDT
- [ ] 13,287 USDT 🏆 *回本！*

---

## 📝 更新日志

| 日期 | 更新 |
|------|------|
| 2026-03-24 | 🚀 项目启动，初始资金446U，BTC现货金字塔策略上线 |
| 2026-03-24 | 💰 C2C充值54U到账，资金升至500U，第一里程碑达成 |
| 2026-03-24 | 🔬 完成35个技能全面研究，数据采集能力大幅升级 |
| 2026-03-24 | 📊 整合买卖压力/资金费率/清算/情绪/事件多维度分析 |
| 2026-03-24 | 🔄 重新定价挂单：$69k/$66k/$63k/$60k，共400U |

---

## ⚠️ 免责声明

本仓库为个人交易辅助工具的配置与记录，所有交易决策基于数据分析。加密货币市场有极高风险，历史亏损已证明风险的真实性。本仓库内容不构成任何投资建议。

---

*由香水柠檬 🍋 自动维护 · Powered by OpenClaw + Claude Sonnet 4.6*

*"不冒险，不着急，稳稳地把钱赚回来。"*
