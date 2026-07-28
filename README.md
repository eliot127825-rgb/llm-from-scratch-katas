# Machine Learning Foundations: From-Scratch Katas — Trial Edition

一个面向**代码基础薄弱学习者**的渐进式机器学习代码训练项目。

> 当前公开仓库是 **Trial Edition（试用版）**，包含 19 道练习和基础 Codex
> 教练 Skill。付费 **Complete Edition（完整版）** 将在独立私有仓库中维护，
> 不会通过本仓库的分支发布。

目标不是背诵库函数，而是沿着一条平缓的路径建立真正可迁移的能力：

1. 用 Python 表达数据处理步骤。
2. 理解 NumPy shape、向量化和数值稳定性。
3. 把机器学习公式翻译成可运行代码。
4. 用测试定位边界条件和实现错误。
5. 在掌握经典算法后继续学习神经网络与 LLM。

每道练习只聚焦一个概念，通常可在 20–60 分钟内完成。

## 两个版本

- **Trial Edition**：当前公开仓库，帮助学习者免费体验训练方式。
- **Complete Edition**：计划中的付费完整版，提供扩展题库、参考实现、系统讲解、
  综合项目和增强版教练 Skill。

详细边界和当前发布状态见 [EDITIONS.md](EDITIONS.md)。根目录的
[`EDITION.json`](EDITION.json) 用于让工具和 Skill 识别当前版本。

## 学习路径

```text
Python 基础
  -> NumPy 与矩阵运算
  -> 经典机器学习
  -> 神经网络原语
  -> Transformer 与生成
  -> 训练、效率、调试与面试
```

## 项目结构

```text
llm-from-scratch-katas/
├── README.md
├── EDITION.json
├── EDITIONS.md
├── CATALOG.md
├── ROADMAP.md
├── PROGRESS.md
├── requirements.txt
├── katas/
│   ├── 01_python_dsa/
│   ├── 02_tensor_ops/
│   ├── 03_classical_ml/
│   ├── 04_nn_primitives/
│   ├── 05_transformer/
│   ├── 06_generation/
│   ├── 07_training/
│   ├── 08_post_training/
│   ├── 09_efficiency/
│   ├── 10_debugging/
│   └── 11_mock_interviews/
├── templates/
│   └── kata/
├── scripts/
│   └── validate_repository.py
└── tests/
```

## 试用版已发布题目

Trial Edition 当前包含 **19 道带自动测试的 kata**：

- Python 与数据处理：3 道
- Tensor Operations：5 道
- Classical Machine Learning：3 道
- Neural Network Primitives：6 道
- Transformer：1 道
- Generation：1 道

完整题目、难度和前置依赖见 [CATALOG.md](CATALOG.md)。

## 每道练习的标准结构

```text
001_softmax/
├── README.md          # 题目、公式、shape、限制条件
├── implementation.py  # 自己从零实现
├── test_implementation.py
├── mistakes.md        # 只记录自己真实遇到的问题
└── benchmark.py       # 可选
```

`implementation.py` 默认只提供接口，不提供答案。测试负责告诉你“哪里还不符合
要求”，而不是替你写实现。

## 第一次练习

从最简单的标签计数开始：

```powershell
python -m pytest katas/01_python_dsa/001_count_labels -q
```

打开对应的 `implementation.py`，一次只修复一个失败测试。完成后在
`mistakes.md` 记录真正遇到的问题。

## 一次练习的流程

1. 阅读目标、示例、接口和限制。
2. 先写出输入、输出和最小步骤。
3. 从空实现开始编码。
4. 运行当前目录的测试，一次修复一个失败。
5. 回答题目末尾的解释问题。
6. 在 `mistakes.md` 记录错误及其原因。
7. 隔一天和一周后分别闭卷重写。

卡住时先缩小问题：打印中间变量、手算一个最小例子、检查 shape。不要立即复制
完整答案。

## Codex Skill

试用版内置 `practice-ml-katas-trial` 教练 Skill：

```text
skills/practice-ml-katas-trial/
```

它可以初始化或发现本地题库、选择下一题、提供分级提示、运行当前题测试、
引导复盘并维护学习进度。

推荐直接让 Codex 从 GitHub 子目录安装：

```text
Install the skill from:
https://github.com/eliot127825-rgb/llm-from-scratch-katas_V1/tree/main/skills/practice-ml-katas-trial
```

已经克隆仓库时，也可以手动复制到个人 Codex skills 目录：

```powershell
Copy-Item -Recurse `
  .\skills\practice-ml-katas-trial `
  "$env:USERPROFILE\.codex\skills\practice-ml-katas-trial"
```

使用示例：

```text
Use $practice-ml-katas-trial to start my next beginner-friendly ML exercise.
```

如果只安装了 Skill、尚未克隆题库，首次调用会先请你确认存放目录和网络访问，
然后使用内置 `bootstrap_course.py` 安全初始化公开试用题库。它不会覆盖非空目录。

### 初学者只需要三步

1. 安装 Skill。
2. 输入：

   ```text
   Use $practice-ml-katas-trial to start my first exercise.
   ```

3. 按教练提示只打开一个 `implementation.py` 文件并完成一个小步骤。

Skill 会负责检查环境、寻找题库、选择题目和运行单题测试。你不需要先理解
虚拟环境、pytest 或完整目录结构。测试失败是练习反馈，不代表操作失败。

## 环境

完整环境说明见 [ENVIRONMENT.md](ENVIRONMENT.md)。推荐使用项目内虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

如果已经使用 Conda，也可以创建或激活自己的 Python 3.10+ 环境：

```powershell
conda create -n ml-katas python=3.11
conda activate ml-katas
```

建议使用 Python 3.10 或更高版本。基础阶段只需要 NumPy 和 pytest：

```powershell
python -m pip install -r requirements.txt
```

运行当前练习的测试：

```powershell
python -m pytest katas/01_python_dsa/001_count_labels -q
```

练习仓库中的未完成实现会故意抛出 `NotImplementedError`，因此不把“全部题目
通过”作为仓库健康标准。检查所有 kata 的必需文件、目录编号和 Python 语法：

```powershell
python scripts/validate_repository.py
```

## 当前阶段

推荐从 `katas/01_python_dsa/001_count_labels` 开始，沿
[CATALOG.md](CATALOG.md) 中的依赖路径练习。总体路线见
[ROADMAP.md](ROADMAP.md)，个人完成情况记录在 [PROGRESS.md](PROGRESS.md)。
