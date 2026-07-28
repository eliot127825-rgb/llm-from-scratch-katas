# Roadmap

路线按照依赖关系排列，但不要求完成一个阶段的全部题目后才能进入下一阶段。

当前已发布的题目与前置依赖见 [CATALOG.md](CATALOG.md)。当前题库包含
19 道题，从 Python 数据处理逐步延伸到经典机器学习、神经网络和 LLM。

## Phase 1：Python 与数据处理

对应目录：`katas/01_python_dsa`

退出标准：

- 能使用列表、字典、循环和函数处理小型数据集。
- 能保持特征与标签对齐。
- 能解释随机种子和训练集/测试集划分。
- 能写出基本的输入验证和边界测试。

## Phase 2：NumPy 与 Tensor

对应目录：`katas/02_tensor_ops`

退出标准：

- 能准确推导 reshape、transpose、broadcast 和 matmul 后的 shape。
- 能用向量化代码替代明显的 Python 多重循环。
- 能识别常见的数值溢出问题。

## Phase 3：经典机器学习

对应目录：`katas/03_classical_ml`

退出标准：

- 能实现回归损失和线性模型预测。
- 能实现基于距离与投票的分类器。
- 能解释训练、预测、评估和数据泄漏的区别。
- 能进一步实现梯度下降、逻辑回归、K-Means 和 PCA。

## Phase 4：神经网络原子组件

对应目录：`katas/04_nn_primitives`

退出标准：

- 能手写稳定的 Softmax、Cross Entropy、LayerNorm 和 RMSNorm。
- 能实现 Linear、Embedding、MLP 以及简单反向传播。
- 能解释 SGD、Momentum、Adam 和 AdamW 的差异。

## Phase 5：Transformer 与生成

对应目录：

- `katas/05_transformer`
- `katas/06_generation`

退出标准：

- 能从空文件实现 causal self-attention 和 multi-head attention。
- 能实现 RoPE、SwiGLU、Decoder Block 和一个最小 GPT。
- 能实现 temperature、top-k、top-p 和 KV Cache 推理。

## Phase 6：训练与后训练

对应目录：

- `katas/07_training`
- `katas/08_post_training`

退出标准：

- 能写出 next-token training loop、loss mask、梯度累积与裁剪。
- 能解释并实现 SFT、reward-model loss 和 DPO 的最小版本。
- 能在 toy problem 上验证 PPO 或 GRPO 的核心公式。

## Phase 7：效率、调试与模拟面试

对应目录：

- `katas/09_efficiency`
- `katas/10_debugging`
- `katas/11_mock_interviews`

退出标准：

- 能实现 online softmax、分块 attention、LoRA 和简单量化。
- 能系统排查 shape、mask、梯度、数值稳定性和性能问题。
- 能在 45–60 分钟内边解释边完成一个综合组件。

## 推荐节奏

- 初学阶段：一道 20–40 分钟的小题。
- 进阶阶段：一道 30–60 分钟的组件题。
- 周末：重写本周最容易出错的一题。
- 每完成 8–10 道：做一次限时综合练习。
- 学完经典机器学习后：完成一个不依赖 scikit-learn 的小项目。
- 进入 LLM 阶段后：定期从空文件重写 mini GPT。
