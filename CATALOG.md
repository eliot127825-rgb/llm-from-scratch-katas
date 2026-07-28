# Trial Edition Kata Catalog

题目按依赖顺序排列。`Published` 表示题面、实现桩、测试和复盘模板均已具备，
不代表学习者已经完成实现。

本目录只列出当前试用版实际提供的 19 道题。下一版本正在开发，尚未发布的内容
不会存放在本公开仓库中；版本状态见 [EDITIONS.md](EDITIONS.md)。

## 01 Python and Data Handling

| ID | Kata | Difficulty | Prerequisites | Status |
|---|---|---|---|---|
| 001 | [Count Labels](katas/01_python_dsa/001_count_labels/README.md) | Beginner | Lists, loops, dictionaries | Published |
| 002 | [Min-Max Scale](katas/01_python_dsa/002_min_max_scale/README.md) | Beginner | Loops, arithmetic | Published |
| 003 | [Train-Test Split](katas/01_python_dsa/003_train_test_split/README.md) | Beginner | Lists, indices, random seed | Published |

## 02 Tensor Operations

| ID | Kata | Difficulty | Prerequisites | Status |
|---|---|---|---|---|
| 001 | [Matrix Multiplication](katas/02_tensor_ops/001_matrix_multiplication/README.md) | Easy | Python loops, lists | Published |
| 002 | [Transpose 2D](katas/02_tensor_ops/002_transpose_2d/README.md) | Easy | Python lists, shape reasoning | Published |
| 003 | [Batched Matrix Multiplication](katas/02_tensor_ops/003_batched_matrix_multiplication/README.md) | Medium | Matrix multiplication, NumPy | Published |
| 004 | [Causal Mask](katas/02_tensor_ops/004_causal_mask/README.md) | Easy | Boolean masks, broadcasting | Published |
| 005 | [Stable LogSumExp](katas/02_tensor_ops/005_stable_logsumexp/README.md) | Medium | NumPy reductions, numerical stability | Published |

## 03 Classical Machine Learning

| ID | Kata | Difficulty | Prerequisites | Status |
|---|---|---|---|---|
| 001 | [Mean Squared Error](katas/03_classical_ml/001_mean_squared_error/README.md) | Beginner | NumPy arrays, averages | Published |
| 002 | [Linear Regression Predict](katas/03_classical_ml/002_linear_regression_predict/README.md) | Beginner | Dot product, shapes | Published |
| 003 | [KNN Classifier](katas/03_classical_ml/003_knn_classifier/README.md) | Easy | Distance, sorting, voting | Published |

## 04 Neural Network Primitives

| ID | Kata | Difficulty | Prerequisites | Status |
|---|---|---|---|---|
| 001 | [Linear Forward](katas/04_nn_primitives/001_linear_forward/README.md) | Easy | Matrix multiplication, broadcasting | Published |
| 002 | [Embedding Lookup](katas/04_nn_primitives/002_embedding_lookup/README.md) | Easy | NumPy indexing | Published |
| 003 | [Stable Softmax](katas/04_nn_primitives/003_stable_softmax/README.md) | Medium | Stable LogSumExp | Published |
| 004 | [Cross Entropy](katas/04_nn_primitives/004_cross_entropy/README.md) | Medium | Stable LogSumExp, indexing | Published |
| 005 | [LayerNorm](katas/04_nn_primitives/005_layer_norm/README.md) | Medium | Reduction axes, broadcasting | Published |
| 006 | [RMSNorm](katas/04_nn_primitives/006_rms_norm/README.md) | Medium | Reduction axes, broadcasting | Published |

## 05 Transformer

| ID | Kata | Difficulty | Prerequisites | Status |
|---|---|---|---|---|
| 001 | [Scaled Dot-Product Attention](katas/05_transformer/001_scaled_dot_product_attention/README.md) | Medium | Matmul, masks, stable softmax | Published |

## 06 Generation

| ID | Kata | Difficulty | Prerequisites | Status |
|---|---|---|---|---|
| 001 | [Greedy Decoding](katas/06_generation/001_greedy_decoding/README.md) | Easy | Python control flow, logits | Published |

## Recommended first path

```text
01/001 -> 01/002 -> 01/003
       -> 02/002 -> 02/001 -> 02/003 -> 02/004 -> 02/005
       -> 03/001 -> 03/002 -> 03/003
       -> 04/001 -> 04/002 -> 04/003 -> 04/004
       -> 04/005 -> 04/006 -> 05/001 -> 06/001
```
