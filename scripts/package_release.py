#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import tarfile
import tempfile
from pathlib import Path

import yaml


EXCLUDE_NAMES = {".git", ".DS_Store", "__pycache__", "dist"}


def load_manifest(repo_root: Path) -> dict:
    return yaml.safe_load((repo_root / "release-manifest.yaml").read_text(encoding="utf-8"))


def should_skip(path: Path) -> bool:
    return (
        path.name in EXCLUDE_NAMES
        or path.name.endswith(".lock")
        or path.name.endswith(".pyc")
        or (path.name.startswith(".") and path.name not in {".claude-plugin", ".github", ".gitignore"})
    )


def copy_repo(src_root: Path, dst_root: Path) -> None:
    for item in src_root.iterdir():
        if should_skip(item):
            continue
        dst = dst_root / item.name
        if item.is_dir():
            shutil.copytree(item, dst, ignore=shutil.ignore_patterns(".DS_Store", "*.lock", "__pycache__", "*.pyc"))
        else:
            shutil.copy2(item, dst)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a GitHub release archive for the public skill repo")
    parser.add_argument("--repo-root", default=".", help="Path to the repo root")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    manifest = load_manifest(repo_root)
    release_name = f"{manifest['release_slug']}-v{manifest['version']}"
    dist_dir = repo_root / "dist"
    dist_dir.mkdir(exist_ok=True)
    archive_path = dist_dir / f"{release_name}.tgz"

    with tempfile.TemporaryDirectory(prefix="public-release-") as tmp:
        staging_root = Path(tmp) / release_name
        staging_root.mkdir(parents=True, exist_ok=True)
        copy_repo(repo_root, staging_root)
        with tarfile.open(archive_path, "w:gz") as tar:
            tar.add(staging_root, arcname=release_name)

    print(archive_path)


if __name__ == "__main__":
    main()

