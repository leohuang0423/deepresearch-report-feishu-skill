# Deep Research Report Feishu Skill

[中文](#中文说明) | [English](#english)

## English

Production-grade deep research report skill for `Codex`, `Claude Code`, and `OpenClaw`.

This repository publishes the stable skill slug `research-feishu-report-cocreate` as a clean public release:

- creator-first deep research
- non-consensus synthesis
- report-first structure
- figure planning and Feishu-ready delivery
- self-contained platform skill folders

### What This Repo Is For

- high-standard topic research with explicit audience and decision value
- creator-first evidence gathering and case packets
- report packages that need charts/figures and Feishu delivery discipline
- shareable installable skill distribution from GitHub

### What This Repo Is Not For

- generic writing
- lightweight browsing answers
- automatic product judgment replacement
- one-off prompt snippets without a skill contract

### Platform Support

| Platform | Public Path | Install Model |
| --- | --- | --- |
| Codex | `skills/codex/research-feishu-report-cocreate` | GitHub path install |
| Claude Code | `skills/claude/research-feishu-report-cocreate` | Claude marketplace/plugin |
| OpenClaw | `skills/openclaw/research-feishu-report-cocreate` | repo skill or plugin-style load |

### Quick Install

Codex:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo leohuang0423/deepresearch-report-feishu-skill \
  --path skills/codex/research-feishu-report-cocreate
```

Claude Code:

```text
/plugin marketplace add leohuang0423/deepresearch-report-feishu-skill
/plugin install deepresearch-report-feishu-skill@deepresearch-report-feishu-skill-marketplace
```

OpenClaw:

```bash
git clone https://github.com/leohuang0423/deepresearch-report-feishu-skill.git
mkdir -p "${HOME}/.openclaw/skills"
cp -R deepresearch-report-feishu-skill/skills/openclaw/research-feishu-report-cocreate "${HOME}/.openclaw/skills/"
openclaw skills list | rg research-feishu-report-cocreate
```

### Verification

```bash
python3 scripts/validate_public_repo.py --repo-root .
```

### Repo Semantics

- human-facing repo/release name: `deepresearch-report-feishu-skill`
- stable skill slug: `research-feishu-report-cocreate`
- current public release version: `0.4.0`

### Agent Acceptance Standard

One required acceptance case for this repository is:

- give the GitHub URL to `Claude Code` or `OpenClaw`
- the agent can infer the repo structure on its own
- the agent can complete install + minimum validation
- the agent can report the test result back to its user

## 中文说明

这是一个面向 `Codex`、`Claude Code`、`OpenClaw` 的生产级深度研究报告 skill 仓库。

这个仓库发布的是稳定 skill slug `research-feishu-report-cocreate`，但对开发者暴露的是更容易理解的公开名字 `deepresearch-report-feishu-skill`。

它适合：

- 高标准专题研究
- creator-first 证据采集与 case packet
- 非共识判断与读者友好主报告
- 需要重点图表与飞书交付纪律的报告任务
- 从 GitHub 直接发现、安装、验证这个 skill

它不适合：

- 通用写作
- 轻量问答
- 替用户做产品判断
- 没有 skill contract 的一次性 prompt

### 平台支持

| 平台 | 公开路径 | 安装方式 |
| --- | --- | --- |
| Codex | `skills/codex/research-feishu-report-cocreate` | GitHub 路径安装 |
| Claude Code | `skills/claude/research-feishu-report-cocreate` | marketplace/plugin 安装 |
| OpenClaw | `skills/openclaw/research-feishu-report-cocreate` | repo skill / plugin 风格加载 |

### 快速安装

Codex：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo leohuang0423/deepresearch-report-feishu-skill \
  --path skills/codex/research-feishu-report-cocreate
```

Claude Code：

```text
/plugin marketplace add leohuang0423/deepresearch-report-feishu-skill
/plugin install deepresearch-report-feishu-skill@deepresearch-report-feishu-skill-marketplace
```

OpenClaw：

```bash
git clone https://github.com/leohuang0423/deepresearch-report-feishu-skill.git
mkdir -p "${HOME}/.openclaw/skills"
cp -R deepresearch-report-feishu-skill/skills/openclaw/research-feishu-report-cocreate "${HOME}/.openclaw/skills/"
openclaw skills list | rg research-feishu-report-cocreate
```

### 最小验证

```bash
python3 scripts/validate_public_repo.py --repo-root .
```

### 版本语义

- 人类可读的仓库 / release 名：`deepresearch-report-feishu-skill`
- 稳定 skill slug：`research-feishu-report-cocreate`
- 当前公开版本：`0.4.0`

### Agent 验收标准

这个仓库有一条明确验收标准：

- 把 GitHub 链接直接丢给 `Claude Code` 或 `OpenClaw`
- agent 能自主理解仓库结构
- agent 能完成安装和最小验证
- agent 能把测试报告回给用户

More detailed installation and release notes live in [INSTALL.md](./INSTALL.md).

