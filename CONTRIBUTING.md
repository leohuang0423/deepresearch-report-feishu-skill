# Contributing

## English

This repository is a public release projection of an internal canonical bundle.

Contribute here if you are improving:

- public installability
- public docs
- GitHub discovery
- release engineering
- platform metadata for Codex, Claude Code, or OpenClaw

Do not open PRs that reintroduce:

- local absolute paths
- clicklink duplicate files
- `.DS_Store` or lockfiles
- internal experiment logs or local runner traces

Before submitting:

```bash
python3 scripts/validate_public_repo.py --repo-root .
python3 scripts/run_install_smoke.py --repo-root .
```

## 中文

这个仓库是内部 canonical bundle 的公开发行版投影。

欢迎贡献的方向：

- 公开安装体验
- 对外文档
- GitHub 发现性
- release 工程
- Codex / Claude Code / OpenClaw 的平台元数据

不要提交会重新引入以下问题的改动：

- 本机绝对路径
- clicklink 重复文件
- `.DS_Store` 或 lock 文件
- 内部实验日志、盲评运行痕迹、本地 runner trace

提交前至少运行：

```bash
python3 scripts/validate_public_repo.py --repo-root .
python3 scripts/run_install_smoke.py --repo-root .
```

