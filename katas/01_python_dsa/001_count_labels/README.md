# Kata 001: Count Class Labels

## 学习目标

使用 Python 字典统计分类数据中每个标签出现的次数。

```python
def count_labels(labels: list[int]) -> dict[int, int]:
    ...
```

示例：

```python
count_labels([1, 0, 1, 2, 1])
```

返回：

```python
{1: 3, 0: 1, 2: 1}
```

## 为什么机器学习需要它

训练分类模型前，经常需要检查类别是否平衡。如果某个类别远少于其他类别，
准确率可能会产生误导。

## 规则

允许使用字典、循环和条件语句。不要使用 `collections.Counter`、Pandas 或 NumPy。

## 必须满足

- 空列表返回空字典。
- 只接受整数标签；布尔值不视为整数标签。
- 非列表输入或非法标签抛出 `ValueError`。
- 不修改输入列表。
- 字典保留标签第一次出现的顺序。

## 复杂度目标

- 时间：`O(N)`
- 空间：`O(C)`，其中 `C` 是不同类别数

## 运行测试

```powershell
python -m pytest katas/01_python_dsa/001_count_labels -q
```

## 完成后解释

1. 为什么字典适合做频次统计？
2. `labels.count(label)` 写在循环里为什么更慢？
3. 类别分布不均衡会怎样影响准确率？
