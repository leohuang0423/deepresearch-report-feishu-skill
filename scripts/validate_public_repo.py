#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


SKILL_SLUG = "research-feishu-report-cocreate"
PLATFORMS = ("codex", "claude", "openclaw")
HASH_DUPLICATE_RE = re.compile(r".+-[0-9a-f]{8}(?:\.[A-Za-z0-9._-]+)?$")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt"}
REQUIRED_ROOT_FILES = (
    "README.md",
    "INSTALL.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "LICENSE",
    "release-manifest.yaml",
    ".claude-plugin/marketplace.json",
    ".claude-plugin/plugin.json",
    ".github/workflows/validate.yml",
    ".github/workflows/release.yml",
    "docs/RELEASE_ENGINEERING.md",
    "openclaw.plugin.json",
    "scripts/export_public_release.py",
    "scripts/package_release.py",
    "scripts/run_install_smoke.py",
    "scripts/validate_public_repo.py",
    "tests/public_validation_cases.yaml",
)


def assert_exists(path: Path, message: str) -> None:
    if not path.exists():
        raise AssertionError(message)


def validate_root(repo_root: Path) -> dict[str, object]:
    for rel in REQUIRED_ROOT_FILES:
        assert_exists(repo_root / rel, f"missing required file: {rel}")
    manifest = yaml.safe_load((repo_root / "release-manifest.yaml").read_text(encoding="utf-8"))
    if manifest["skill_slug"] != SKILL_SLUG:
        raise AssertionError("unexpected skill slug")
    return manifest


def validate_skill_dirs(repo_root: Path) -> list[str]:
    checked: list[str] = []
    for platform in PLATFORMS:
        skill_dir = repo_root / "skills" / platform / SKILL_SLUG
        assert_exists(skill_dir / "SKILL.md", f"{platform} missing SKILL.md")
        assert_exists(skill_dir / "assets", f"{platform} missing assets")
        assert_exists(skill_dir / "references", f"{platform} missing references")
        assert_exists(skill_dir / "contracts", f"{platform} missing contracts")
        if platform == "codex":
            assert_exists(skill_dir / "agents" / "openai.yaml", "codex missing openai.yaml")
        if platform == "claude":
            assert_exists(skill_dir / "CLAUDE.md.fragment", "claude missing CLAUDE.md.fragment")
        checked.append(str(skill_dir.relative_to(repo_root)))
    return checked


def validate_forbidden_patterns(repo_root: Path) -> dict[str, int]:
    text_files = 0
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        if path.name == ".DS_Store" or path.name.endswith(".lock"):
            raise AssertionError(f"forbidden file present: {path}")
        if HASH_DUPLICATE_RE.fullmatch(path.name):
            raise AssertionError(f"clicklink duplicate present: {path}")
        if path.suffix in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8")
            if "/Users/" in text:
                raise AssertionError(f"local absolute path found in {path}")
            if "Context Engineering研究" in text:
                raise AssertionError(f"internal local path marker found in {path}")
            if "v15_market_proof_converged" in text:
                raise AssertionError(f"legacy internal name found in {path}")
            text_files += 1
    return {"text_files_checked": text_files}


def validate_agent_acceptance_case(repo_root: Path) -> dict[str, object]:
    cases = yaml.safe_load((repo_root / "tests" / "public_validation_cases.yaml").read_text(encoding="utf-8"))
    case_ids = {case["id"] for case in cases["cases"]}
    required = {"repo_url_autoinstall_claude", "repo_url_autoinstall_openclaw"}
    if not required.issubset(case_ids):
        raise AssertionError("missing autonomous install acceptance cases")
    return {"cases": sorted(case_ids)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the public skill repo")
    parser.add_argument("--repo-root", default=".", help="Path to the repo root")
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()

    manifest = validate_root(repo_root)
    skills = validate_skill_dirs(repo_root)
    forbidden = validate_forbidden_patterns(repo_root)
    cases = validate_agent_acceptance_case(repo_root)

    print(
        json.dumps(
            {
                "status": "passed",
                "release": manifest["release_slug"],
                "version": manifest["version"],
                "skills": skills,
                "forbidden_scan": forbidden,
                "acceptance_cases": cases,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
