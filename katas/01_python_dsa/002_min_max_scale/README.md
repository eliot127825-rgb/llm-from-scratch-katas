# Kata 002: Min-Max Scaling

## 学习目标

只使用基础 Python，把一列数值缩放到 `[0, 1]`：

```python
def min_max_scale(values: list[float]) -> list[float]:
    ...
```

公式：

```text
scaled_i = (x_i - minimum) / (maximum - minimum)
```

## 为什么机器学习需要它

不同特征的量纲可能相差很大。缩放能避免数值范围较大的特征在距离计算或
梯度更新中占据不合理的优势。

## 规则

允许使用列表、循环、比较和算术。不要使用 NumPy、Pandas、scikit-learn、
`min` 或 `max`。

## 必须满足

- 支持整数和浮点数，并返回浮点数。
- 拒绝空列表、布尔值、非数值和非有限值。
- 所有值相同时抛出 `ValueError`。
- 不修改输入。

## 复杂度目标

- 时间：`O(N)`
- 输出空间：`O(N)`

## 运行测试

```powershell
python -m pytest katas/01_python_dsa/002_min_max_scale -q
```

## 完成后解释

1. 为什么至少需要遍历输入？
2. 为什么常数列不能直接使用这个公式？
3. 测试集应该使用自己的最小值和最大值吗？
