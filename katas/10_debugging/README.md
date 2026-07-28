# 10 Debugging

为每道题准备一个存在真实 bug 的短程序，依次覆盖：

1. Shape mismatch
2. Broadcasting 产生静默错误
3. Causal mask 方向错误
4. Padding token 进入 loss
5. Softmax 数值溢出
6. 梯度为零
7. 梯度爆炸
8. 忘记切换 train/eval
9. 错误使用 detach
10. Optimizer 未清梯度
11. KV Cache sequence axis 错误
12. Mixed-precision overflow
13. 数据重复或泄漏
14. 性能被 Python loop 限制

修复后必须补一个能稳定复现原问题的测试。
