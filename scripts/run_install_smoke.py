#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml


SKILL_SLUG = "research-feishu-report-cocreate"
CODEX_INSTALLER_RELATIVE = Path("skills/.system/skill-installer/scripts/install-skill-from-github.py")


def run(cmd: list[str], env: dict[str, str] | None = None) -> None:
    subprocess.run(cmd, check=True, text=True, env=env)


def find_codex_installer() -> Path | None:
    codex_home = os.environ.get("CODEX_HOME")
    candidates = []
    if codex_home:
        candidates.append(Path(codex_home) / CODEX_INSTALLER_RELATIVE)
    candidates.append(Path.home() / ".codex" / CODEX_INSTALLER_RELATIVE)
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def assert_self_contained_skill(skill_root: Path) -> None:
    required = ["SKILL.md", "assets", "references", "contracts"]
    for name in required:
        if not (skill_root / name).exists():
            raise AssertionError(f"Missing required skill artifact: {name}")


def codex_install_smoke(repo_root: Path) -> dict[str, str]:
    installer = find_codex_installer()
    source_skill = repo_root / "skills" / "codex" / SKILL_SLUG
    with tempfile.TemporaryDirectory(prefix="codex-public-smoke-") as tmp:
        dest = Path(tmp) / "skills"
        if installer:
            run(
                [
                    "python3",
                    str(installer),
                    "--repo",
                    "leohuang0423/deepresearch-report-feishu-skill",
                    "--path",
                    "skills/codex/research-feishu-report-cocreate",
                    "--dest",
                    str(dest),
                ]
            )
            installed_skill = dest / SKILL_SLUG
            assert_self_contained_skill(installed_skill)
            return {"status": "passed", "mode": "github_path_install"}

        shutil.copytree(source_skill, dest / SKILL_SLUG)
        installed_skill = dest / SKILL_SLUG
        assert_self_contained_skill(installed_skill)
        return {"status": "passed", "mode": "self_contained_fallback"}


def claude_manifest_smoke(repo_root: Path) -> dict[str, str]:
    marketplace = json.loads((repo_root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    plugin = json.loads((repo_root / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    skill_root = repo_root / "skills" / "claude" / SKILL_SLUG
    if not (skill_root / "CLAUDE.md.fragment").exists():
        raise AssertionError("Claude fragment missing")
    if marketplace["plugins"][0]["name"] != plugin["name"]:
        raise AssertionError("Claude marketplace and plugin names do not match")
    assert_self_contained_skill(skill_root)
    return {"status": "passed", "mode": "manifest_and_structure"}


def openclaw_manifest_smoke(repo_root: Path) -> dict[str, str]:
    manifest = json.loads((repo_root / "openclaw.plugin.json").read_text(encoding="utf-8"))
    skill_dir = repo_root / "skills" / "openclaw" / SKILL_SLUG
    if manifest["skills"] != ["skills/openclaw"]:
        raise AssertionError("Unexpected OpenClaw skills entry")
    assert_self_contained_skill(skill_dir)
    return {"status": "passed", "mode": "plugin_manifest_and_structure"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run install smoke checks for the public skill repo")
    parser.add_argument("--repo-root", default=".", help="Path to the repo root")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    result = {
        "codex": codex_install_smoke(repo_root),
        "claude": claude_manifest_smoke(repo_root),
        "openclaw": openclaw_manifest_smoke(repo_root),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
