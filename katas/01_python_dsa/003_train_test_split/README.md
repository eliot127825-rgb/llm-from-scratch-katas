# Kata 003: Train-Test Split

## 学习目标

实现一个可复现的训练集/测试集划分：

```python
def train_test_split(
    features: list[list[float]],
    labels: list[int],
    test_ratio: float,
    seed: int,
) -> tuple[
    list[list[float]],
    list[list[float]],
    list[int],
    list[int],
]:
    ...
```

返回顺序：

```text
train_features, test_features, train_labels, test_labels
```

使用 `random.Random(seed)` 创建局部随机数生成器，打乱样本索引。测试集大小为：

```text
int(number_of_samples * test_ratio)
```

## 为什么机器学习需要它

模型必须在未参与训练的数据上评估。特征和标签必须始终保持一一对应，
固定随机种子才能复现实验。

## 规则

允许使用 Python 列表、索引和 `random.Random`。不要使用 scikit-learn、
NumPy 或全局 `random.seed`。

## 必须满足

- 特征数和标签数相同，且至少有两个样本。
- 特征矩阵必须非空且每行等长。
- 标签必须是非布尔整数。
- `0 < test_ratio < 1`，划分后训练集和测试集都不能为空。
- `seed` 必须是非布尔整数。
- 不修改输入，返回的新行不能与输入行共享引用。

## 运行测试

```powershell
python -m pytest katas/01_python_dsa/003_train_test_split -q
```

## 完成后解释

1. 为什么不能分别打乱特征和标签？
2. 为什么使用局部随机数生成器？
3. 测试集参与特征缩放参数计算会造成什么问题？
