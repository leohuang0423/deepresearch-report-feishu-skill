# 开通与收款 Checklist(大陆主体,PayPal 起步路径)

依据 research/raw/A5;升级触发条件在文末。

## 1. 收款(最先做,有审核周期)

- [ ] 注册 **PayPal 企业账户**(paypal.com 中国站,营业执照或个体户;无主体可先用个人升级企业,但限额低)
- [ ] 完成实名 + 绑定对公/个人银行卡,开通美元收款
- [ ] 知悉费率:跨境收款 ~4.4% + 固定费 + 提现/结汇环节费用;计入定价
- [ ] 备选并行申请:万里汇(WorldFirst)/ Wise 账户,用于 1688 采购付款与未来 B2B 收款

## 2. Shopify

- [ ] 注册试用 → 验证跑通后转 **Basic 年付**($29/月)
- [ ] Settings → Payments → 激活 PayPal Express Checkout(授权企业账号)
- [ ] 确认知悉:未用 Shopify Payments,Basic 档每单加收 2% 附加费 → 综合支付成本 ~6.4%,定价时已含
- [ ] 域名:Shopify 内购或 Cloudflare(~$12/年),品牌中性词(两条线共用,如 `<brand>.com`,避免纯 AI 或纯运动品类词)
- [ ] 其余按 `storefront/SETUP.md` 执行

## 3. 交付与获客工具(A 线)

- [ ] Calendly 免费版(30 分钟"diagnostic call"事件)→ 链接填进 audit 页 hero
- [ ] ANTHROPIC_API_KEY(API 余额 $50 起步)
- [ ] 一个干净的发件域名邮箱(Google Workspace $7/月或 Zoho 免费),冷邮件**不要**用主域名——买 `<brand>-hq.com` 类副域名预热 2 周(每天手动 5-10 封)再上量
- [ ] NDA 模板:用通用 mutual NDA 模板改抬头即可,放 `automation/audit-pipeline/` 同级备用

## 4. B 线补充(过验证门槛后再做)

- [ ] CJdropshipping 账号 + Shopify 应用安装
- [ ] TikTok 个人创作者账号(美区内容方向),主页链接挂 Shopify 预售页
- [ ] 1688 账号 + 万里汇绑定(采购付款)

## 升级触发条件(写给 3 个月后的你)

| 触发 | 动作 |
|---|---|
| A 线连续 2 个月 ≥$8k 或单一客户要求刷卡/发票主体 | 设美国 LLC(Stripe Atlas $500)→ 开 Stripe/Shopify Payments → 支付成本从 ~6.4% 降到 ~3%;记住每年 Form 5472(漏报罚 $2.5 万) |
| B 线单批 >50 单 | 切换批量进口 + CJ 美仓/3PL(`cj-presale-sop.md` 路径 B) |
| 月营收 >$15k | 找跨境税务师做架构(LLC vs 香港公司),别自己猜 |
