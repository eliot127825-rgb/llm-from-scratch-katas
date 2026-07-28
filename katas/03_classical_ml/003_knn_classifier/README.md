# Kata 003: K-Nearest Neighbors Classifier

## 学习目标

实现 KNN 分类器的预测过程：

```python
def knn_predict(
    train_features: np.ndarray,
    train_labels: np.ndarray,
    query_features: np.ndarray,
    k: int,
) -> np.ndarray:
    ...
```

Shapes：

```text
train_features: (number_of_train_samples, number_of_features)
train_labels:   (number_of_train_samples,)
query_features: (number_of_queries, number_of_features)
output:         (number_of_queries,)
```

对每个查询样本：

1. 计算它与所有训练样本的欧氏距离；
2. 找到距离最小的 `k` 个样本；
3. 统计它们的标签；
4. 返回票数最多的标签；票数相同时选择较小标签。

## 规则

使用 NumPy 和基础 Python。不要使用 scikit-learn、SciPy 或现成 KNN。

## 必须满足

- 特征必须是非空、有限、数值型二维数组。
- 标签必须是非空一维整数数组，且与训练样本数量一致。
- `k` 必须是非布尔整数，并满足 `1 <= k <= number_of_train_samples`。
- 不修改输入。

## 复杂度目标

朴素实现对 `Q` 个查询、`N` 个训练样本和 `D` 个特征：

- 距离计算：`O(QND)`
- 还需要考虑选择最近邻的排序成本

## 运行测试

```powershell
python -m pytest katas/03_classical_ml/003_knn_classifier -q
```

## 完成后解释

1. 为什么特征缩放会影响 KNN？
2. `k` 太小或太大分别有什么风险？
3. KNN 的“训练阶段”为什么几乎不做计算？
