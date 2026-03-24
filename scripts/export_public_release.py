#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path


SKILL_SLUG = "research-feishu-report-cocreate"
PLATFORMS = ("codex", "claude", "openclaw")
HASH_DUPLICATE_RE = re.compile(r".+-[0-9a-f]{8}(?:\.[A-Za-z0-9._-]+)?$")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt"}
FORBIDDEN_NAMES = {".DS_Store"}
FIXTURE_MAP = {
    "tests/sample_main_doc.md": "tests/fixtures/sample_main_doc.md",
    "tests/sample_doc_tree.yaml": "tests/fixtures/sample_doc_tree.yaml",
    "runtime/assets/figure_manifest_template.yaml": "tests/fixtures/figure_manifest_template.yaml",
}


def is_hash_duplicate(name: str) -> bool:
    return bool(HASH_DUPLICATE_RE.fullmatch(name))


def should_skip(path: Path) -> bool:
    return (
        path.name in FORBIDDEN_NAMES
        or path.name.endswith(".lock")
        or path.name == "__pycache__"
        or is_hash_duplicate(path.name)
    )


def sanitize_skill_text(text: str, source_root: Path) -> str:
    lines = text.splitlines()
    cleaned: list[str] = []
    skip_bundle_script_block = False

    for line in lines:
        if "If deterministic publish or QA is needed, use bundle scripts at:" in line:
            skip_bundle_script_block = True
            continue
        if skip_bundle_script_block:
            if line.startswith("## "):
                skip_bundle_script_block = False
                cleaned.append(line)
            elif line.startswith("# "):
                skip_bundle_script_block = False
                cleaned.append(line)
            else:
                continue
            continue
        cleaned.append(line)

    sanitized = "\n".join(cleaned).replace(str(source_root), ".")
    if "/Users/" in sanitized:
        raise ValueError("sanitized text still contains local absolute paths")
    return sanitized + "\n"


def copy_text_file(src: Path, dst: Path, source_root: Path) -> None:
    content = src.read_text(encoding="utf-8")
    if src.name == "SKILL.md":
        content = sanitize_skill_text(content, source_root)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(content, encoding="utf-8")


def copy_binary_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def copy_tree(src_root: Path, dst_root: Path, source_root: Path) -> None:
    if dst_root.exists():
        shutil.rmtree(dst_root)
    dst_root.mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(src_root):
        root_path = Path(root)
        dirs[:] = [name for name in dirs if not should_skip(root_path / name)]
        for file_name in files:
            src_file = root_path / file_name
            if should_skip(src_file):
                continue
            rel_path = src_file.relative_to(src_root)
            dst_file = dst_root / rel_path
            if src_file.suffix in TEXT_SUFFIXES:
                copy_text_file(src_file, dst_file, source_root)
            else:
                copy_binary_file(src_file, dst_file)


def copy_fixture(src_root: Path, repo_root: Path, rel_src: str, rel_dst: str) -> None:
    src = src_root / rel_src
    if not src.exists():
        return
    dst = repo_root / rel_dst
    if src.suffix in TEXT_SUFFIXES:
        copy_text_file(src, dst, src_root)
    else:
        copy_binary_file(src, dst)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export a sanitized public release from the internal bundle")
    parser.add_argument("--source-bundle", required=True, help="Path to the internal canonical bundle")
    parser.add_argument("--repo-root", default=".", help="Path to the public repo root")
    args = parser.parse_args()

    source_root = Path(args.source_bundle).resolve()
    repo_root = Path(args.repo_root).resolve()

    for platform in PLATFORMS:
        src = source_root / "adapters" / platform / SKILL_SLUG
        if not src.exists():
            raise FileNotFoundError(f"missing source adapter: {src}")
        dst = repo_root / "skills" / platform / SKILL_SLUG
        copy_tree(src, dst, source_root)

    for rel_src, rel_dst in FIXTURE_MAP.items():
        copy_fixture(source_root, repo_root, rel_src, rel_dst)

    print(repo_root)


if __name__ == "__main__":
    main()

