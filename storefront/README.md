# Shopify 建站包

一家店,两条线:**A 线(AI agent 诊断服务,现金引擎)** 立即上线;**B 线(匹克球拍隔热套预售)** 商品已备好,通过 TikTok 验证门槛后再发布。

## 内容

| 路径 | 内容 |
|---|---|
| `SETUP.md` | 从零到上线的逐步操作(含 PayPal 收款、CLI 部署) |
| `products/products.csv` | 可直接导入的 3 个商品(2 个服务 SKU + 1 个预售实体 SKU) |
| `theme/sections/` | 3 个自定义 Dawn section(服务 hero、流程步骤、预售合规横幅) |
| `theme/templates/` | 2 个 JSON 模板(服务落地页、预售商品页) |
| `copy/` | 全套英文文案:首页、A 线页面、B 线预售页、政策与 FAQ |

## 设计决策(依据 research/REPORT.md)

- **主题用 Dawn**(非新默认 Horizon):文档与定制生态最成熟,OS 2.0 JSON 模板长期支持(A5)。
- **服务即商品**:`Mini Diagnostic $499` 设为免发货商品可直接下单;`Audit Sprint $4,500` 保持 draft,走"预约诊断电话"(B2B 服务行业惯例,A2),跑通后可改为可下单。
- **预售页合规**:FTC Mail Order Rule 要求醒目标注并兑现发货日期(A3),`preorder-banner` section 强制展示日期,政策文案已含对应条款。
- **收款**:PayPal 中国直收起步(无需海外主体);升级路径见 `playbook/setup-checklist.md`。
