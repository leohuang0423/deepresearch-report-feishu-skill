# Evaluation Rules

重型专题报告任务默认走 10 分制验收，不再使用 0/1/2 简版。

每位专家都按 `contracts/rubric.yaml` 的 10 个维度打分。

通过标准：

- 每位专家总分必须 `> 8.0`
- `task_definition`、`thesis_strength`、`evidence_depth`、`reader_path` 任一 `< 8` 直接 fail
- publish 场景 `delivery_integrity` 必须 `>= 8`
- fail 后只能进入 revise，不能直接 publish

如果任务是轻量或中量，只允许使用降级版检查，不得伪装成高标准专题报告通过。
