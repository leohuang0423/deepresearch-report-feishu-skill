# Main-Doc Review Rules

这个模块不是通用改稿器，而是 heavy 模式里的高杠杆 reducer。

只在满足以下 gating 条件时触发：

- 主文已有可读初稿
- 目标读者明确
- 当前问题是结构、可读性、sharp 判断边界或阅读流
- 当前节点高歧义、高杠杆、高返工成本

典型触发点：

- `pre_draft_gate` 之前：比较 outline / thesis / reader path
- `post_draft_gate` 阶段：收敛首稿的关键问题
- `acceptance_panel` 之后：把失败原因收成下一轮修订项

输出只能是 reducer 结果：

- 共识
- 冲突
- Top N 改动项
- 优先级
- 验收口径

不做：

- 语法润色
- 轻量博客改写
- 主题未成型稿件的早期发散
- 代替用户决定最终行业观点
