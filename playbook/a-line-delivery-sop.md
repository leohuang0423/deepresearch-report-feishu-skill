# A 线交付 SOP

## Mini Diagnostic($499,5 个工作日,目标人工 ≤4 小时)

| 日 | 动作 |
|---|---|
| D0 | 收到下单 → 自动邮件索要数据(已配在订单确认邮件);收到导出 → 回执确认"5 个工作日倒计时开始" |
| D1 | `ingest.py` → `cluster_failures.py`(500 条 ≈ $20-40 token);扫一遍 failures.json,剔除误报 |
| D2 | `gen_report.py` → 解决所有 `[REVIEW]` 占位:写叙事、root cause、top-3 修复(人工核心价值在这 2-3 小时) |
| D3 | pandoc 转 PDF → 发送 + 一段 Loom 视频(5 分钟走读报告,转化 Sprint 的关键) |
| D3+ | 48h 后跟进邮件:"哪条发现最意外?要不要把 top-3 修了再用前后评测证明?($499 全额抵扣 Sprint)" |

## Audit Sprint($4,500,10 个工作日)

### D1-2 · Kickoff + 摄取
- 30' kickoff:确认成功标准(挑 1-2 个业务指标:escalation 率/解决率/CSAT)、数据交接、staging 访问
- NDA + SOW 签署归档;`ingest.py` 跑全量(≥1,000 条)

### D3-4 · 诊断
- `cluster_failures.py` 全量;人工抽查每个 mode 的 top 例证(误报率 >10% 则收紧该类 prompt 后重跑)
- 产出中期失败图谱,发客户一封"初步发现"邮件(管理预期 + 制造惊喜)

### D5-7 · 修复包
- 按 impact_score 取 top 3-5 个 mode,逐个写修复:prompt diff / 工具定义修改 / 检索配置 / 知识库补丁
- 每个修复必须可直接合并:给完整文件或 PR 格式,不给"建议你考虑"
- 在自己环境复现客户栈跑不了的,写清楚部署步骤让对方 1 小时内能落地

### D8-9 · 前后评测
- 从原始数据留出 20% 对话作 held-out 集(D1 就要切好,不许污染)
- 用 held-out 的用户消息重放:旧配置 vs 新配置,`cluster_failures.py` 各跑一遍
- 产出对比表:每个 mode 的失败率前后变化;有任一 mode 变差必须如实写并解释取舍

### D10 · 交付
- 终版报告(PDF)+ 改进包(repo/zip)+ 回归评测套件(held-out 集 + 运行脚本,客户自留)
- 60' handoff call:走读 + 落地排期;**结尾必推监控订阅**($1,500/月)
- 24h 内:感谢邮件 + case study 授权请求 + referral 请求("你认识的下一个被 agent 折磨的团队是谁?")

### 交付后(内部,30 分钟,不可跳过)
- 新失败模式回写 `automation/audit-pipeline/taxonomy.md`
- 把 1 个发现脱敏成 LinkedIn teardown 素材
- 工时记录:Mini >4h 或 Sprint >5 天人工 → 找出最耗时环节,下一单自动化它
