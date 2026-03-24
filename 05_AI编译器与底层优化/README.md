# 05_AI编译器与底层优化

> ⚙️ AI编译器原理、算子开发与硬件感知优化  
> 📅 最后更新：2026 年 3 月  
> 🚧 **本文档正在建设中...**

---

## 📝 当前状态

本专题目前**正在规划中**，预计包含以下内容：

### 计划文档清单

#### 1. AI编译器基础
- [ ] AI编译器概述与发展历程
- [ ] 编译流程详解（Frontend → IR → Optimization → Codegen）
- [ ] 主流编译器对比（TVM vs MLIR vs XLA）

#### 2. TVM深度学习
- [ ] TVM架构与原理解析
- [ ] Relay IR 设计与使用
- [ ] TIR Schedule 与自动调优
- [ ] Ansor 自动调度器
- [ ] MetaSchedule 实战

#### 3. MLIR框架
- [ ] MLIR核心概念（Dialect/Operation/Pattern）
- [ ] 自定义 Dialect 开发
- [ ] Pattern Rewrite 与优化
- [ ] Linalg Dialect 应用
- [ ] GPU Offloading 策略

#### 4. XLA与JAX
- [ ] XLA编译器架构
- [ ] HLO IR 详解
- [ ] JAX编程模型
- [ ] SPMD 分区策略

#### 5. 算子开发实战
- [ ] CUDA编程基础
- [ ] 矩阵乘法优化（从 naive 到 Tensor Core）
- [ ] Convolution 算子优化
- [ ] Attention 算子实现
- [ ] FlashAttention 原理与实现

#### 6. 性能分析与调优
- [ ] Nsight Compute/Systems使用
- [ ] Roofline Model 分析
- [ ] Occupancy 优化
- [ ] Memory Access 优化
- [ ] Instruction Level 优化

---

## 🎯 学习路径（规划）

```
编译原理基础 → TVM入门 → MLIR进阶 → 算子开发 → 性能调优
     ↓           ↓          ↓          ↓          ↓
  编译流程    Relay/TIR   Dialect    CUDA      Nsight
  IR设计      AutoTVM     Pattern    算子实现   Roofline
```

---

## 🔑 核心技术点（预览）

### AI编译器对比
| 编译器 | 优势 | 劣势 | 适用场景 |
|--------|------|------|---------|
| **TVM** | 生态成熟、自动调优强 | 学习曲线陡 | 通用推理 |
| **MLIR** | 模块化、可扩展 | 较新、文档少 | 定制化需求 |
| **XLA** | TensorFlow/JAX原生 | 封闭生态 | Google 生态 |
| **TensorRT** | NVIDIA GPU极致优化 | 仅支持NVIDIA | 生产部署 |

### 算子优化技术栈
- **Memory Hierarchy**: Global → Shared → Register
- **Tiling**: 分块提高缓存命中率
- **Vectorization**: SIMD/SIMT并行
- **Pipeline**: 重叠计算与内存访问
- **Tensor Core**: 混合精度矩阵运算

---

## 💻 前置知识要求

### 必备基础
- ✅ C/C++ 熟练编程
- ✅ Python 脚本编写
- ✅ 线性代数基础
- ✅ 计算机体系结构

### 加分项
- ⭐ CUDA/ROCm编程经验
- ⭐ 编译原理课程
- ⭐ 深度学习框架使用

---

## 📚 推荐学习资源

### 入门课程
- [CMU 15-745: Optimizing Compilers](https://www.cs.cmu.edu/~15745/)
- [Stanford CS149: Parallel Computing](https://cs149.stanford.edu/)

### 官方文档
- [TVM 官方文档](https://tvm.apache.org/docs/)
- [MLIR 官方文档](https://mlir.llvm.org/docs/)
- [XLA 文档](https://www.tensorflow.org/xla)

### 经典论文
- [TVM: An Automated End-to-End Optimizing Compiler for Deep Learning](https://arxiv.org/abs/1802.04799)
- [MLIR: A Compiler Infrastructure for the End of Moore's Law](https://arxiv.org/abs/2002.11054)

### 实践项目
- [TVM GitHub](https://github.com/apache/tvm)
- [MLIR GitHub](https://github.com/llvm/llvm-project/tree/main/mlir)

---

## 🛠️ 开发环境搭建（预告）

### 软件依赖
```bash
# Ubuntu/Debian
sudo apt install cmake llvm clang python3-dev

# macOS
brew install llvm cmake
```

### 源码编译 TVM
```bash
git clone --recursive https://github.com/apache/tvm.git
cd tvm
mkdir build && cd build
cmake ..
make -j$(nproc)
```

---

## 📊 预计内容统计

| 分类 | 计划文档数 | 预计字数 | 代码示例 |
|------|-----------|---------|---------|
| 编译器基础 | 3 篇 | ~30k | 10+ |
| TVM 深度 | 5 篇 | ~50k | 20+ |
| MLIR 框架 | 4 篇 | ~40k | 15+ |
| 算子开发 | 6 篇 | ~60k | 30+ |
| 性能调优 | 3 篇 | ~30k | 10+ |
| **总计** | **21 篇** | **~210k** | **85+** |

---

## 🆕 更新计划

### Phase 1（2026 年 Q2）
- ✅ AI编译器概述
- ✅ TVM 快速入门
- ✅ CUDA 编程基础

### Phase 2（2026 年 Q3）
- [ ] MLIR 核心概念
- [ ] 算子优化实战
- [ ] 性能分析工具

### Phase 3（2026 年 Q4）
- [ ] 高级主题（量化/稀疏化）
- [ ] 国产硬件适配
- [ ] 面试题库

---

## 🤝 贡献指南

如果你对本专题感兴趣，欢迎：
1. 提供你想了解的具体主题
2. 分享你的实战经验
3. 指出文档中的错误
4. 补充更多代码示例

---

## 📬 联系方式

- 📧 Email: (请替换为你的邮箱)
- 💼 简历：[1_简历文件/2026/大模型/](../1_简历文件/2026/大模型/)
- 🌐 GitHub: (请替换为你的 GitHub)

---

> **⚠️ 注意**: 本专题内容正在积极编写中，敬请期待！  
> 
> **维护者**: 陈纬  
> **最后更新**: 2026 年 3 月 13 日  
> **状态**: 🚧 建设中
