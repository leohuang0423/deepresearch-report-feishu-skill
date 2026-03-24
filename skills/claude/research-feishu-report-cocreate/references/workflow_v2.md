# Workflow v2 Runtime Reference

运行时只使用四阶段骨架：

1. 定义任务
2. 组织证据
3. 形成内容
4. 交付与验收

当任务同时满足以下条件中的至少 3 条时，判定为 `heavy_topic_report`：

- 主题仍需收敛
- 证据来源多于 1 类
- 目标读者明确且标准高
- 需要多轮改稿
- 最终要交付到飞书
- 返工成本高

在 `heavy_topic_report` 下，默认路径是：

1. `brief`
2. `ideal_state_panel`
3. `research_question`
4. `evidence_map`
5. `evidence_panel`
6. `outline_freeze`
7. `pre_draft_gate`
8. `draft`
9. `review_panel`
10. `revise_until_pass`
11. `publish`
12. `qa_panel`

只在高歧义、高杠杆、高返工成本节点触发正式发散/收敛。

不是普适原则：

- 母子文档
- case-first
- 发散/收敛

普适原则是：

- 先定信息层级与阅读路径
- 先锁研究问题，再建证据结构
- 先把证据讲清，再抽方法、insight、foresight
- 高标准专题报告必须先过 gate，再写 full draft
