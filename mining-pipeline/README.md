# 痛点挖掘流水线 (Pain-Point Mining Pipeline)

可复用的「垂直人群痛点挖掘」流水线:从社区讨论中采集真实抱怨 → Claude 提取并聚类痛点 → 按机会分排序输出报告。这是整个生意的核心资产,选品和服务方向都靠它驱动。

## 流程

```
collectors/  采集 (Reddit 免费 / X 付费API / TikTok via Apify)
    │  posts.jsonl
analyze/pain_extract.py  Claude 两段式分析:提取痛点提及 → 聚类打分
    │  pain_clusters.json
analyze/report.py  输出 opportunity_report.md(按 1-10 机会分排序)
```

## 快速开始

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...

# 只用 Reddit(免费,无需其他 key)
python pipeline.py --subreddits dogtraining BuyItForLife --out-dir data/run1

# 查看结果
cat data/run1/opportunity_report.md
```

## 所需 API Key

| Key | 必需? | 用途 | 成本 |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | ✅ | 痛点提取与聚类 | 按量,一次完整运行约 $1-5 |
| `X_BEARER_TOKEN` | 可选 | X 搜索(`--x-query`) | X API Basic 档付费,启用前先看调研报告 A1 |
| `APIFY_TOKEN` | 可选 | TikTok 评论(`--tiktok-urls`) | 按结果数计费 |

## 合规说明

- Reddit:使用公开 JSON 端点,低频只读;上量请注册官方 OAuth 应用
- X:仅官方 API
- TikTok:经 Apify 托管采集公开评论,属 ToS 灰色地带——仅作研究、控制量级
- 不采集任何登录墙后内容,不存储个人身份信息用于其他目的

## 怎么选 subreddit

找「热情/绝望人群」聚集地:具体爱好(r/houseplants)、具体困扰(r/backpain)、具体身份(r/NewParents)、具体职业。越垂直越好,泛论坛信噪比低。
