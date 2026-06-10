# Niche Commerce Venture

目标:通过 Shopify 自动化卖货实现 **$10k/月**(美国/英语市场,单人运营,自动化优先)。

核心方法论:**痛点挖掘 → offer 设计 → 低成本验证 → 自动化交付**。Shopify 只是收银台,可复用的挖掘流水线才是壁垒。

## 目录

| 目录 | 内容 | 状态 |
|---|---|---|
| `research/` | 深度调研报告:方向对比(AI agent 优化服务 vs niche 实体电商)、工具链、单位经济模型、候选 niche | 调研中 |
| `mining-pipeline/` | 通用痛点挖掘流水线(Reddit/X/TikTok 采集 + Claude 聚类打分) | ✅ 可运行 |
| `storefront/` | Shopify 建站包(Dawn 主题定制 + 全套文案 + 可导入商品 CSV) | 待方向确认 |
| `automation/` | 履约自动化(订单→1688 SOP 或 agent 诊断交付流水线) | 待方向确认 |
| `playbook/` | 上线运营手册(注册→收款→上线 checklist、冷启动方案、KPI 模型) | 待方向确认 |

## 工作流

1. 阅读 `research/` 的调研报告与方向推荐
2. 确认方向后,按 `playbook/setup-checklist.md` 开通 Shopify 并部署 `storefront/`
3. 每周跑一次 `mining-pipeline/` 迭代选品/offer
