# 07 Training

建议题目顺序：

1. Next-token data construction
2. Padding 与 loss mask
3. Sequence packing
4. Minimal training loop
5. Gradient accumulation
6. Gradient clipping
7. Learning-rate schedule
8. Mixed precision
9. Checkpoint save/load
10. Activation checkpointing
11. 简化版 DDP
12. 训练指标与验证循环

训练题应在小数据上验证 loss 能够下降，并检查是否存在数据泄漏。
