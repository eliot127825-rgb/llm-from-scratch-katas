# Kata 002: Linear Regression Prediction

## 学习目标

实现多特征线性回归的预测函数：

```python
def linear_regression_predict(
    features: np.ndarray,
    weights: np.ndarray,
    bias: float,
) -> np.ndarray:
    ...
```

Shapes：

```text
features: (number_of_samples, number_of_features)
weights:  (number_of_features,)
output:   (number_of_samples,)
```

公式：

```text
y_hat = Xw + b
```

## 直觉

每个特征乘以自己的权重，再把结果相加。偏置表示所有特征都为零时的基础预测。

## 规则

使用 NumPy。不要使用 scikit-learn、PyTorch 或现成的线性模型。

## 必须满足

- 验证输入 rank 和特征维度。
- 拒绝空维度、布尔数组、非数值数组和非有限值。
- `bias` 必须是有限实数，布尔值非法。
- 不修改输入。

## 复杂度目标

- 时间：`O(ND)`
- 输出空间：`O(N)`

## 运行测试

```powershell
python -m pytest katas/03_classical_ml/002_linear_regression_predict -q
```

## 完成后解释

1. 每一行样本如何变成一个预测值？
2. 权重的正负分别表示什么？
3. 预测函数与训练函数有什么区别？
