# Install Guide

## English

### Codex

Install directly from GitHub:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo leohuang0423/deepresearch-report-feishu-skill \
  --path skills/codex/research-feishu-report-cocreate
```

Validate:

```bash
test -f "${CODEX_HOME:-$HOME/.codex}/skills/research-feishu-report-cocreate/SKILL.md"
```

### Claude Code

Add the marketplace repo:

```text
/plugin marketplace add leohuang0423/deepresearch-report-feishu-skill
```

Install the plugin package:

```text
/plugin install deepresearch-report-feishu-skill@deepresearch-report-feishu-skill-marketplace
```

### OpenClaw

Clone and install the skill folder:

```bash
git clone https://github.com/leohuang0423/deepresearch-report-feishu-skill.git
mkdir -p "${HOME}/.openclaw/skills"
cp -R deepresearch-report-feishu-skill/skills/openclaw/research-feishu-report-cocreate "${HOME}/.openclaw/skills/"
openclaw skills list | rg research-feishu-report-cocreate
```

## 中文

### Codex

直接从 GitHub 安装：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo leohuang0423/deepresearch-report-feishu-skill \
  --path skills/codex/research-feishu-report-cocreate
```

验证：

```bash
test -f "${CODEX_HOME:-$HOME/.codex}/skills/research-feishu-report-cocreate/SKILL.md"
```

### Claude Code

先把这个 GitHub 仓库加成 marketplace：

```text
/plugin marketplace add leohuang0423/deepresearch-report-feishu-skill
```

再安装 plugin：

```text
/plugin install deepresearch-report-feishu-skill@deepresearch-report-feishu-skill-marketplace
```

### OpenClaw

手工 clone 后把公开 skill 目录复制到本地：

```bash
git clone https://github.com/leohuang0423/deepresearch-report-feishu-skill.git
mkdir -p "${HOME}/.openclaw/skills"
cp -R deepresearch-report-feishu-skill/skills/openclaw/research-feishu-report-cocreate "${HOME}/.openclaw/skills/"
openclaw skills list | rg research-feishu-report-cocreate
```

