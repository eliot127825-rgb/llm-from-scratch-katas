# 04 Neural Network Primitives

## 已发布

1. `001_linear_forward`
2. `002_embedding_lookup`
3. `003_stable_softmax`
4. `004_cross_entropy`
5. `005_layer_norm`
6. `006_rms_norm`

## 待扩展

1. ReLU、GELU、SiLU
2. Dropout
3. BatchNorm
4. MLP
5. Linear 与 MLP backward
6. SGD 与 Momentum
7. Adam 与 AdamW
8. Gradient clipping
9. Warmup 与 cosine schedule

优先用基础 tensor 运算实现，不直接调用对应的 `torch.nn` 组件。
