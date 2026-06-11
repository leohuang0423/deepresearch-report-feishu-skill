# Niche Commerce Venture

目标:通过 Shopify 自动化卖货实现 **$10k/月**(美国/英语市场,单人运营,自动化优先)。

核心方法论:**痛点挖掘 → offer 设计 → 低成本验证 → 自动化交付**。Shopify 只是收银台,可复用的挖掘流水线才是壁垒。

## 目录

| 目录 | 内容 | 状态 |
|---|---|---|
| `research/` | 深度调研:总报告 `REPORT.md`(方向对比 + 推荐)+ 5 个带引用的原始模块 | ✅ 完成 |
| `mining-pipeline/` | 通用痛点挖掘流水线(Reddit/X/TikTok 采集 + Claude 聚类打分) | ✅ 可运行 |
| `storefront/` | Shopify 建站包:Dawn 自定义 sections/templates + 商品 CSV + 全套英文文案 + `SETUP.md` | ✅ 完成 |
| `automation/` | `audit-pipeline/`(A 线诊断交付半自动化)+ `fulfillment/`(B 线预售批量履约 SOP) | ✅ 完成 |
| `playbook/` | 90 天路线图 + 决策门 + 开通/收款 checklist + A 线 GTM/交付 SOP + B 线启动手册 | ✅ 完成 |

## 已确认的方向(2026-06)

**分阶段混合**:A 线(AI agent 诊断优化服务,$499 Mini / $4,500 Sprint)做现金引擎;B 线选定**匹克球拍隔热套**做预售轻验证;收款 **PayPal 中国直收**起步(升级路径见 `playbook/setup-checklist.md`)。完整论证见 `research/REPORT.md`。

## 工作流

1. 读 `research/REPORT.md` → 按 `playbook/setup-checklist.md` 开通账号收款
2. 按 `storefront/SETUP.md` 一天内建店上线 → 按 `playbook/a-line-gtm.md` 开始获客
3. 接单后用 `automation/audit-pipeline/` 交付(SOP:`playbook/a-line-delivery-sop.md`)
4. B 线按 `playbook/b-line-launch.md` 推进,过验证门槛才发预售页
5. 每周日跑一次 `mining-pipeline/` 迭代选品/offer
