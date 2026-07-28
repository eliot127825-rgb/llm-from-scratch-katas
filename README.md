# ML From-Scratch Katas

> 面向代码基础薄弱学习者的机器学习算法训练营：用小题、自动测试和自适应 AI
> 教练，把“看懂公式”一步步变成“能够独立写出代码”。

[![Validate and package](https://github.com/eliot127825-rgb/llm-from-scratch-katas_V1/actions/workflows/validate-plugin.yml/badge.svg)](https://github.com/eliot127825-rgb/llm-from-scratch-katas_V1/actions/workflows/validate-plugin.yml)
[![Trial Edition](https://img.shields.io/badge/edition-Trial-blue)](EDITIONS.md)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776AB)](ENVIRONMENT.md)
[![Katas 19](https://img.shields.io/badge/katas-19-2EA44F)](CATALOG.md)

[为什么做](#为什么要做这个项目) ·
[适用人群](#适合谁) ·
[学习内容](#你会练到什么) ·
[核心功能](#核心功能) ·
[安装使用](#最推荐的使用方式codex-自适应教练) ·
[版本规划](#版本规划) ·
[常见问题](#常见问题)

当前仓库是公开免费的 **Trial Edition（试用版）**，包含：

- 19 道从 Python 基础逐步延伸到 Attention 和生成算法的编程练习；
- 每道题独立的题面、实现接口、自动测试和错题复盘文件；
- 一个可以直接安装到 Codex 的自适应学习教练 Skill；
- 5 题能力诊断，以及 Starter、Foundation、Guided、Independent 四级教学方式；
- 环境检查、题目推荐、渐进提示、单题测试、错误解释和学习复盘。

这里的 **kata** 指“一次只训练一个能力点的小型编程练习”。每道题通常需要
20–60 分钟，不要求你一次搭建完整机器学习项目。

## 为什么要做这个项目

很多机器学习入门资料解决了“知识看过没有”，却没有解决“能不能自己写出来”：

- 视频听懂了，关闭视频后不会从空文件开始；
- 公式认识，但不知道怎样拆成变量、循环和数组操作；
- 会调用现成库，却说不清 shape、边界条件和数值稳定性；
- 测试一失败就不知道先看哪里，最后只能复制完整答案；
- 题目太散，不知道当前水平适合练什么、下一题应该做什么。

这个项目的写作目的，是为代码能力较弱的学习者提供一条足够平缓、能够执行、
能够获得反馈的机器学习基础算法入门路径。

它不是另一本只供阅读的教程，也不是答案合集。你需要亲手补全
`implementation.py`，自动测试负责提供反馈，AI 教练负责根据你的能力调整题目
和讲解方式。

| 常见学习方式 | 本项目的训练方式 |
|---|---|
| 一次听完一大章 | 一次只练一个能力点 |
| 所有人从同一难度开始 | 先诊断，再匹配题目和讲解 |
| 看答案后觉得自己会了 | 从空实现开始，用测试验证 |
| 测试失败后面对整屏报错 | 先解释第一个有用的失败 |
| 零散刷题，不清楚下一步 | 按前置依赖推荐学习路径 |
| 只记录“做过” | 记录真实错误并安排重写 |

## 适合谁

### 推荐使用

- Python 只学过变量、循环、函数，希望进入机器学习的初学者；
- 看过机器学习课程，但很难把公式翻译成代码的学习者；
- 经常被 NumPy shape、broadcast、索引和矩阵运算卡住的人；
- 想在学习深度学习和 LLM 前补齐算法实现基础的人；
- 需要明确练习顺序、即时反馈和复盘机制的自学者；
- 想从“会调用 API”进步到“理解算法内部发生了什么”的开发者。

### 暂时不适合

- 只想复制完整答案、快速完成作业的人；
- 只寻找 scikit-learn、PyTorch 或大模型框架 API 教程的人；
- 已经能熟练从零实现 Transformer，主要需要论文复现或分布式训练的人；
- 希望当前免费版直接提供完整参考答案和大型综合项目的人。

## 你会练到什么

试用版当前提供 6 个已发布模块、19 道带自动测试的练习。

| 阶段 | 题量 | 代表内容 | 学习结果 |
|---|---:|---|---|
| Python 与数据处理 | 3 | 标签计数、Min-Max 归一化、训练集划分 | 用 Python 表达基本数据处理步骤 |
| Tensor Operations | 5 | 矩阵乘法、转置、因果掩码、LogSumExp | 理解 shape、broadcast 与数值稳定性 |
| 经典机器学习 | 3 | MSE、线性回归预测、KNN | 把损失、预测和距离投票写成代码 |
| 神经网络原语 | 6 | Linear、Embedding、Softmax、Cross Entropy、LayerNorm、RMSNorm | 理解常见网络组件内部计算 |
| Transformer | 1 | Scaled Dot-Product Attention | 串联矩阵乘法、mask 与 Softmax |
| Generation | 1 | Greedy Decoding | 理解 logits 到 token 的最小生成流程 |

题目清单、难度和前置依赖见 [CATALOG.md](CATALOG.md)，长期能力路线见
[ROADMAP.md](ROADMAP.md)。

推荐路径：

```text
Python 数据处理
  -> NumPy 与 Tensor
  -> 经典机器学习
  -> 神经网络原语
  -> Attention
  -> 文本生成
```

## 核心功能

### 1. 小步练习，而不是一次实现整个模型

每道 kata 只聚焦一个概念。标准结构如下：

```text
001_softmax/
├── README.md               # 目标、公式、示例、shape 和限制条件
├── implementation.py       # 学习者需要补全的接口
├── test_implementation.py  # 自动测试
└── mistakes.md             # 记录自己真实遇到的错误
```

公开试用版默认不在 `implementation.py` 中提供答案。你会从可运行的接口开始，
通过测试逐步发现遗漏的情况。

### 2. 五题能力诊断

首次使用教练 Skill 时，可以进行一个约 5 分钟、可跳过的能力诊断。它依次检查：

1. Python 循环和字典；
2. 基础调试；
3. 矩阵 shape；
4. 训练集与测试集概念；
5. 把问题拆成算法步骤的能力。

这不是排名考试。它的作用是避免所有初学者收到同一种题目和同一种解释。

### 3. 四级自适应教学

| 支持等级 | 建议题目 | 教练方式 |
|---|---|---|
| Starter | Beginner | 解释必要术语，使用具体数字，一次只给一个动作 |
| Foundation | Beginner / Easy | 跟踪循环和中间值，简要解释语法 |
| Guided | Easy / Medium | 先让学习者写伪代码、判断 shape 和边界情况 |
| Independent | Medium | 提供简洁挑战，延后提示，复盘复杂度与取舍 |

学习者始终可以要求更简单或更困难的题目。一次困难不会导致自动降级；完成一定
数量的练习后，可以重新诊断。

### 4. 渐进提示，不立即泄露答案

教练按以下顺序提供帮助：

1. 提一个定位问题；
2. 手算一个最小例子或追踪 shape；
3. 给出伪代码或指出错误区域；
4. 只有在学习者尝试后明确索要答案时，才提供完整实现。

这样既不会让初学者长时间无助，也尽量保留真正动手思考的过程。

### 5. 聚焦单题的测试与错误解释

Skill 使用安全的单题测试运行器，不会因为不同 kata 中存在同名测试文件而混淆
结果。测试失败时，它会优先解释第一个真正有帮助的错误，并区分：

- 语法错误；
- 类型错误；
- shape 错误；
- 数值稳定性错误；
- 算法逻辑错误；
- 输入验证和边界条件错误。

测试失败是练习反馈，不代表学习者“学不会”或操作失败。

### 6. 新手环境检查与安全初始化

教练可以：

- 检查 Python、NumPy、pytest、Git 和项目路径；
- 发现已经克隆的 Trial Edition；
- 在用户确认目录和网络访问后初始化公开题库；
- 拒绝覆盖一个已有内容的非题库目录；
- 使用清华 PyPI 镜像安装基础依赖。

### 7. 本地学习档案与隐私

诊断只保存维度分数、支持等级和教学偏好，不保存五道题的原始回答。学习档案位于：

```text
.local/learner_profile.json
```

`.local/` 已被 Git 忽略，不会进入代码提交或插件 ZIP。

## 最推荐的使用方式：Codex 自适应教练

这种方式适合不知道从哪一题开始、希望有人解释报错的学习者。

### 第一步：安装 Skill

在 Codex 中发送：

```text
Use $skill-installer to install the skill from:
https://github.com/eliot127825-rgb/llm-from-scratch-katas_V1/tree/main/skills/practice-ml-katas-trial
```

安装完成后，新建一个对话。如果 Codex 没有发现新 Skill，请重启 Codex 后再新建
对话。

### 第二步：开始诊断和第一题

在新对话中发送：

```text
Use $practice-ml-katas-trial to assess my level and start my first exercise.
```

如果你不想诊断，可以直接发送：

```text
Use $practice-ml-katas-trial to skip the assessment, start me at Starter level,
and guide me through my first exercise.
```

### 第三步：只完成教练给出的一个小动作

教练会检查环境、找到或初始化题库、推荐难度、告诉你需要打开的确切文件，并且
一次只引导一个小步骤。你不需要提前理解虚拟环境、pytest 或整个仓库结构。

## 不使用 AI 教练：直接练题

如果你已经熟悉 Git、Python 和终端，可以直接使用题库。

### 1. 克隆公开试用版

```powershell
git clone https://github.com/eliot127825-rgb/llm-from-scratch-katas_V1.git
cd llm-from-scratch-katas_V1
```

### 2. 创建环境并使用清华源安装依赖

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt `
  -i https://pypi.tuna.tsinghua.edu.cn/simple
```

项目要求 Python 3.10 或更高版本，基础依赖只有 NumPy 和 pytest。Conda、
macOS 和 Linux 的操作见 [ENVIRONMENT.md](ENVIRONMENT.md)。

### 3. 运行第一题

```powershell
python -m pytest katas/01_python_dsa/001_count_labels -q
```

然后打开：

```text
katas/01_python_dsa/001_count_labels/implementation.py
```

看到 `NotImplementedError` 是正常的：它表示练习尚未完成，不表示仓库损坏。

## 一次完整练习应该怎样进行

1. 阅读当前 kata 的目标、输入、输出、示例和限制；
2. 先写出最小步骤，必要时手算一个例子；
3. 只修改当前题的 `implementation.py`；
4. 运行当前题测试；
5. 一次理解和修复一个失败；
6. 测试通过后解释正确性、shape、复杂度和机器学习意义；
7. 在 `mistakes.md` 中记录自己真实犯过的错误；
8. 第二天和一周后分别进行一次闭卷重写。

不要把“看完题解”当成完成。能够在没有答案的情况下重新写出来，才说明这个能力
开始变得可迁移。

## 常用教练指令

### 不知道从哪开始

```text
Use $practice-ml-katas-trial to assess me and recommend one suitable exercise.
```

### 继续上次练习

```text
Use $practice-ml-katas-trial to continue my current kata.
```

### 测试当前代码

```text
Use $practice-ml-katas-trial to test my current kata and explain only the first
useful failure.
```

### 我完全看不懂报错

```text
Use $practice-ml-katas-trial to explain this error as if I only know basic
Python. Give me one next action, not the full answer.
```

### 我觉得题目太难或太简单

```text
Use $practice-ml-katas-trial to choose an easier exercise.
```

```text
Use $practice-ml-katas-trial to give me a harder exercise with fewer hints.
```

### 重新评估能力

```text
Use $practice-ml-katas-trial to reassess my level.
```

## 版本规划

| 版本 | 当前状态 | 说明 |
|---|---|---|
| V1 Trial Edition | 已公开，可直接使用 | 当前仓库，包含 19 道 kata 和自适应 Codex 教练 |
| 下一版本 | 正在开发 | 具体内容、题量和发布时间将在准备完成后公布 |

两个版本分别维护，当前仓库只承诺 [CATALOG.md](CATALOG.md) 中已经发布的内容。
下一版本仍在开发，不在 README 中提前承诺尚未完成的功能。版本状态见
[EDITIONS.md](EDITIONS.md)。

## 项目结构

```text
llm-from-scratch-katas/
├── .codex-plugin/
│   └── plugin.json              # Codex Plugin 清单
├── katas/                       # 19 道公开练习
│   ├── 01_python_dsa/
│   ├── 02_tensor_ops/
│   ├── 03_classical_ml/
│   ├── 04_nn_primitives/
│   ├── 05_transformer/
│   └── 06_generation/
├── skills/
│   └── practice-ml-katas-trial/ # 自适应 Codex 教练
├── scripts/
│   ├── build_plugin.py          # 构建干净的 Plugin ZIP
│   └── validate_repository.py   # 检查目录、题目和 Python 语法
├── CATALOG.md                   # 当前题目、难度和依赖
├── ROADMAP.md                   # 长期能力路线
├── EDITIONS.md                  # V1/V2 版本边界
├── ENVIRONMENT.md               # 环境配置
└── PROGRESS.md                  # 学习进度模板
```

这个仓库本身已经按照 **skills-only Codex Plugin** 结构包装。插件安装、手动
安装 Skill、构建 ZIP 和发布前检查见 [PLUGIN.md](PLUGIN.md)。

## 常见问题

### Kata 是什么意思？

Kata 原本表示反复练习一个动作。在这个项目里，一道 kata 就是一个只训练单个
算法或代码能力的小题，例如“稳定 Softmax”或“训练集划分”。

### 为什么项目名里有 LLM，却从 Python 和机器学习开始？

LLM 不是孤立的 API。Attention、归一化、损失函数和生成算法都建立在 Python、
矩阵运算、数值稳定性和神经网络原语之上。本项目把 LLM 作为长期方向，但刻意从
真正的前置能力开始。

### 完全不会机器学习，可以开始吗？

可以。建议先做能力诊断，并从 Starter 等级和第一道标签计数开始。但你至少需要
愿意学习最基本的 Python 变量、循环和函数。

### 数学不好怎么办？

前几题主要使用四则运算、平均值、距离和矩阵 shape。教练会先用具体数字解释，
再连接公式。后续题目仍需要逐步补充线性代数和概率基础。

### 为什么不直接提供答案？

试用版的目标是验证“练习—测试—调试—复盘”的学习方式。过早看到完整答案很容易
产生“看懂了就是会了”的错觉。下一版本正在开发，具体会增加哪些学习材料将在
准备完成后统一公布。

### 为什么不能在仓库根目录直接运行全部 pytest？

不同 kata 为了保持独立和易读，可能包含同名测试模块；同时未完成的实现本来就会
失败。请运行单题目录，或让 Skill 使用内置的安全单题运行器。

### 如何判断仓库本身是否完整？

运行：

```powershell
python scripts/validate_repository.py
```

这个命令检查 19 道题的必需文件、目录编号、版本信息和 Python 语法，不要求所有
未完成练习的测试通过。

### 如何反馈问题？

请在 [GitHub Issues](https://github.com/eliot127825-rgb/llm-from-scratch-katas_V1/issues)
中说明操作系统、Python 版本、kata 路径、执行命令和完整错误信息。请不要在 Issue
中提交未发布版本内容、密钥或个人学习档案。

## 当前状态

- Trial Edition：公开可用，当前 19 道练习；
- Codex Skill：已包装，可从 GitHub 安装；
- Plugin ZIP：可通过 `python scripts/build_plugin.py` 构建；
- 下一版本：正在开发，具体信息将在准备完成后公布。

如果你第一次来到这里，最简单的开始方式只有一句话：

```text
Use $practice-ml-katas-trial to assess my level and start my first exercise.
```
