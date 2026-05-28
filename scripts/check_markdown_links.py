#!/usr/bin/env python3
"""Validate relative markdown links in repository files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

LINK_PATTERN = re.compile(r"\[[^\]]*]\(([^)]+)\)")
SKIP_DIRS = {".git"}


def is_external(link: str) -> bool:
    return link.startswith(("http://", "https://", "mailto:", "tel:"))


def should_skip_link(link: str) -> bool:
    return link.startswith("#") or link.startswith("data:") or "{{" in link or "}}" in link


def check_file(path: Path, repo_root: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    errors: list[str] = []
    for match in LINK_PATTERN.finditer(text):
        raw_link = match.group(1).strip()
        if not raw_link or is_external(raw_link) or should_skip_link(raw_link):
            continue
        target_link = raw_link.split("#", 1)[0].strip()
        if not target_link:
            continue
        resolved = (path.parent / target_link).resolve()
        if not resolved.exists():
            errors.append(
                f"{path.relative_to(repo_root)} -> {raw_link} "
                f"(resolved: {resolved.relative_to(repo_root) if resolved.is_relative_to(repo_root) else resolved})"
            )
    return errors


def iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        files.append(path)
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    root = args.root.resolve()
    markdown_files = iter_markdown_files(root)
    failures: list[str] = []

    for file_path in markdown_files:
        failures.extend(check_file(file_path, root))

    if failures:
        print("Broken markdown links found:")
        for failure in failures:
            print(f"- {failure}")
        print(f"Total broken links: {len(failures)}")
        return 1

    print(f"Link check passed across {len(markdown_files)} markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
