# Kata 001: Mean Squared Error

## 学习目标

实现回归任务中最常见的均方误差：

```python
def mean_squared_error(
    y_true: np.ndarray,
    y_pred: np.ndarray,
) -> float:
    ...
```

公式：

```text
MSE = (1 / N) * sum((y_true_i - y_pred_i)^2)
```

## 直觉

误差先平方，所以正误差和负误差不会相互抵消；较大的错误会受到更重惩罚。

## 规则

使用 NumPy 的基础数组运算和归约。不要使用 scikit-learn 或任何现成
loss 函数。

## 必须满足

- 两个输入都是形状相同的非空一维 NumPy 数组。
- 接受整数或浮点 dtype。
- 拒绝布尔、非数值和非有限值。
- 返回 Python `float`。
- 不修改输入。

## 复杂度目标

- 时间：`O(N)`
- 额外空间：取决于是否分配中间误差数组

## 运行测试

```powershell
python -m pytest katas/03_classical_ml/001_mean_squared_error -q
```

## 完成后解释

1. 为什么误差需要平方？
2. MSE 为什么容易受离群值影响？
3. MAE 与 MSE 的优化行为有什么不同？
