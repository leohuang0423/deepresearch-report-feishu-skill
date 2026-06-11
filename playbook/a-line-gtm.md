# A 线获客手册(GTM)

定位一句话:**"We find where your AI agent fails — using your real conversations — and ship the fixes in 10 days, fixed price."**

## ICP(按优先级)

1. **已上线客服/支持 agent 的 B2B SaaS(20-200 人)**——有真实流量、有预算、质量问题直接烧客户。信号:用 Intercom Fin / Voiceflow / Ada / 自建,且在招或刚撤了 "AI engineer" 岗。
2. **agent 产品本身就是卖点的初创**(AI SDR、AI 客服、voice agent)——demo 好看上线拉胯,正处在 churn 恐慌中。
3. **内部 copilot 团队**(中型企业)——预算最稳但周期长,放第三优先。

反 ICP:还没上线 agent 的(卖给他们的是咨询不是审计)、五人以下没付费用户的。

## 渠道与节奏

### 1. 暖网络(第 1 周,一次性)
给 20 个认识的人发一对一消息(不是群发):
> 我最近在做一件事:拿企业 AI agent 的真实对话日志,跑失败模式分析,10 天内交付修复包。你认识谁家的 AI 客服/copilot 上线后效果拉胯的吗?引荐成单我付 10% referral fee。

### 2. LinkedIn 内容(每周 2 篇,永续)
内容只有一种格式——**真实 teardown**:
- 拿一个公开聊天机器人(银行/航司/电商官网都有),跑 `automation/audit-pipeline`,发"我给 X 的客服 bot 做了次体检:发现了这 3 类失败"
- 结构:截图证据 → 失败模式命名 → 根因推断 → 一个具体修复建议
- 关键:每篇都展示方法论(taxonomy + 引用证据),这就是销售演示
- CTA 永远同一句:"Want this run on your agent's real logs? $499, 5 days." 链到 Mini Diagnostic

### 3. 触发式冷邮件(每周 20 封,周一/周五各 10)

**触发源(每周日晚收集,30 分钟):**
- LinkedIn/Indeed 上挂出 ≥60 天的 "AI engineer / prompt engineer" 岗位(说明内部修不动)
- 新发布 AI agent 功能的 SaaS(Product Hunt、changelog、新闻稿,上线 1-3 个月正是发现拉胯的时候)
- 公开吐槽自家 bot 的(G2/Twitter 上客户骂某产品的 AI 客服)

**模板(<90 词,纯文本):**
> Subject: {Company}'s agent — 3 conversations
>
> Hi {Name} — I ran 3 public conversations with {Company}'s {agent name} through my failure-mode pipeline. Found {one specific finding, e.g. "it loses user context after the 4th turn and re-asks for the order number"}.
>
> I do this on real logs: 500 conversations in, ranked failure map + top-3 fixes out, 5 business days, $499 flat.
>
> Worth a 20-min look at the full finding? Either way, happy to send the 3-conversation mini-report — it's yours.
>
> {Name}

要点:邮件里必须有**一条真发现**(发前花 10 分钟跟对方 bot 真聊);白送 mini-report 是钩子;不吹"AI 革命",只谈他家 bot 的具体病。

### 4. 不做的渠道(前 90 天)
付费广告(B2B 服务 CAC 打不平)、SEO(too slow)、外包 agency 名录(竞底价)。

## 电话脚本骨架(30 分钟 diagnostic call)

1. (5')他们的 agent 现状:栈、流量、最痛的投诉
2. (15')**现场演示**:屏幕共享跑一条他们的公开对话过 pipeline——卖的就是这个瞬间
3. (5')报价:Sprint $4,500 固定价固定期;犹豫 → 降级推 Mini $499 抵扣
4. (5')敲定数据交接与 NDA;24h 内发跟进邮件附 SOW 一页纸

## 异议处理

| 异议 | 回应 |
|---|---|
| "我们有 LangSmith/Langfuse" | 那是仪表盘,告诉你指标掉了;我交付的是**为什么掉 + 改好的 prompt/配置 + 前后对比证明**。工具是望远镜,我是医生。 |
| "太贵" | 时薪换算 $150-300/小时市场价,10 天人肉审计远超 $4.5k;且 Mini $499 可以先验货。 |
| "数据敏感" | NDA 先行、只读权限、30 天删除(隐私政策白纸黑字);可只给脱敏导出。 |
| "我们工程师自己能修" | 能修早修了——这岗位你们挂了 3 个月(如果命中触发源,直说)。 |

## 定价纪律

- 前 2 单可半价($2,250)换 case study 书面授权,**绝不白送**
- 第 5 单起涨到 $6,000;出现排队 → $8,000
- 交付完必推 **$1,500/月持续监控订阅**(每月自动跑 pipeline + 回归报告)——这是真正的自动化收入,目标 90 天后 ≥2 个订阅
