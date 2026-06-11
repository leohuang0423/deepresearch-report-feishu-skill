# 运营手册:90 天路线图与 KPI 模型

目标:**$10k/月净利**。策略:A 线(agent 诊断服务)做现金引擎,B 线(niche 实体)轻验证,谁先跑通加倍谁。依据见 `research/REPORT.md`。

## 90 天路线图

### 第 1-2 周 · 地基
- [ ] `setup-checklist.md` 全过一遍:PayPal 企业号 → Shopify 开店 → 按 `storefront/SETUP.md` 部署上线
- [ ] 提交 Reddit API 应用审批(排队 2-4 周,现在就交)
- [ ] LinkedIn 个人资料改版:headline = "I find where AI agents fail — using your real conversations"
- [ ] 写第 1 篇公开 teardown(拿任意公开聊天机器人做诊断演示,跑 `automation/audit-pipeline`)
- [ ] 1688 询样匹克球拍隔热套(`automation/fulfillment/cj-presale-sop.md` 阶段 0)

### 第 3-6 周 · A 线冷启动(主力)+ B 线备料
- [ ] 执行 `a-line-gtm.md`:暖网络 20 人 + 每周 20 封触发式冷邮件 + 每周 2 篇 LinkedIn teardown
- [ ] 目标:**第 6 周末 ≥1 个付费客户**(Mini 或 Sprint)
- [ ] B 线:样品到手 → 拍红外测温素材 → TikTok 账号开播(`b-line-launch.md`)
- [ ] 每周日跑一次 `mining-pipeline/`,机会榜进 `research/`

### 第 7-12 周 · 验证与加倍
- [ ] A 线:第 1 单交付即要 case study 授权(可半价换);沉淀 taxonomy
- [ ] B 线:TikTok 素材累计 ≥30 条后看门槛(见下);过门槛 → 发布预售页;不过 → 换 A4 榜单下一个候选
- [ ] 第 12 周复盘:对照决策门,砍掉不达标的线

## 决策门(Go / No-Go)

| 检查点 | 指标 | Go | No-Go 动作 |
|---|---|---|---|
| 第 6 周 | A 线付费客户 | ≥1 | 价格降到 $2.5k 再试 4 周;两轮皆空 → 重新定位 ICP |
| 第 8 周 | B 线 TikTok | 任意一条 ≥10k 播放 或 累计 500 访问且邮件名单 ≥100 | 换下一个 niche 候选 |
| 预售截单 | 预售单量 | ≥15 单 | 全额退款,记录教训,换候选 |
| 第 12 周 | 月营收 run-rate | ≥$5k | 聚焦单线,停掉另一条 |

## KPI 模型(到 $10k/月的两条算术)

**A 线(主路径)**
```
漏斗假设(待实测校准):50 触达 → 10% 回复 → 5 通电话 → 30% 成交 → 1.5 单
$10k/月 = 2 × Sprint $4,500 + 2 × Mini $499 ≈ $10k 毛收入
成本:token ~$700 + 工具 $200 → 净 ~$9.1k;你的时间 ~8 天/月
北极星:每周预约电话数(≥2 通/周 = 在轨)
```

**B 线(副线,验证期不背营收指标)**
```
单件贡献:售价 $27.99 − COGS $4.5 − 履约+税 ~$7 ≈ $16(2-Pack 贡献 ~$30)
预售批 30 单 ≈ $500-700 毛利——目的是验证,不是赚钱
规模化后看:自然流转化率 ≥2%、纠纷率 <0.9%、复购/扩 SKU 路径
```

## 周节奏(单人,~25 小时/周)

| 时段 | 事项 |
|---|---|
| 周一 | LinkedIn teardown #1;冷邮件 10 封 |
| 周二-周四 | 交付(有单)/ 公开 teardown 打磨(无单);TikTok 拍摄 2-3 条 |
| 周五 | LinkedIn teardown #2;冷邮件 10 封;跟进本周所有回复 |
| 周日晚 | mining-pipeline 周跑;KPI 表更新;下周计划 |
