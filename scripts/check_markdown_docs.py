#!/usr/bin/env python3
"""Repository markdown quality checks for core documentation surfaces."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGETS = (
    REPO_ROOT / "README.md",
    REPO_ROOT / ".github",
    REPO_ROOT / "docs",
    REPO_ROOT / "projects",
    REPO_ROOT / "reference_impl" / "README.md",
    REPO_ROOT / "schemas" / "README.md",
    REPO_ROOT / "scripts" / "README.md",
    REPO_ROOT / "tests" / "README.md",
)

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
INLINE_LINK_RE = re.compile(r"(?<!!)\[[^\]]*]\(([^)]+)\)")
FENCE_RE = re.compile(r"^```(\S*)\s*$")


@dataclass(frozen=True)
class Issue:
    path: Path
    line: int
    message: str


def iter_markdown_files(targets: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for target in targets:
        resolved = target.resolve()
        if not resolved.exists():
            continue
        if resolved.is_dir():
            files.update(path for path in resolved.rglob("*.md") if path.is_file())
        elif resolved.suffix == ".md":
            files.add(resolved)
    return sorted(files)


def slugify(heading: str) -> str:
    normalized = heading.strip().lower()
    normalized = re.sub(r"[^\w\s-]", "", normalized)
    normalized = re.sub(r"[\s_]+", "-", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized)
    return normalized.strip("-")


def build_anchor_index(text: str) -> set[str]:
    anchors: set[str] = set()
    seen: Counter[str] = Counter()
    for raw_line in text.splitlines():
        match = HEADING_RE.match(raw_line)
        if not match:
            continue
        slug = slugify(match.group(2))
        if not slug:
            continue
        suffix = seen[slug]
        seen[slug] += 1
        anchors.add(slug if suffix == 0 else f"{slug}-{suffix}")
    return anchors


def classify_link(link: str) -> tuple[str | None, str]:
    cleaned = link.strip()
    if cleaned.startswith(("http://", "https://", "mailto:", "tel:")):
        return None, ""
    if cleaned.startswith("#"):
        return "", cleaned[1:]
    target, _, anchor = cleaned.partition("#")
    return target, anchor


def resolve_target(source: Path, target: str) -> Path:
    return (source.parent / target).resolve()


def validate_heading_hierarchy(path: Path, text: str) -> list[Issue]:
    issues: list[Issue] = []
    prior_level = 0
    h1_count = 0
    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        match = HEADING_RE.match(raw_line)
        if not match:
            continue
        level = len(match.group(1))
        if level == 1:
            h1_count += 1
        if prior_level and level > prior_level + 1:
            issues.append(
                Issue(
                    path,
                    line_no,
                    f"heading level jumps from H{prior_level} to H{level}",
                )
            )
        prior_level = level
    if h1_count > 1:
        issues.append(Issue(path, 1, f"contains {h1_count} H1 headings"))
    return issues


def validate_code_fences(path: Path, text: str) -> list[Issue]:
    issues: list[Issue] = []
    in_fence = False
    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        match = FENCE_RE.match(raw_line)
        if not match:
            continue
        language = match.group(1)
        if in_fence:
            in_fence = False
            continue
        in_fence = True
        if not language:
            issues.append(Issue(path, line_no, "code fence is missing a language tag"))
    if in_fence:
        issues.append(Issue(path, len(text.splitlines()), "code fence is not closed"))
    return issues


def validate_links(
    path: Path, text: str, anchor_map: dict[Path, set[str]]
) -> list[Issue]:
    issues: list[Issue] = []
    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        for match in INLINE_LINK_RE.finditer(raw_line):
            target, anchor = classify_link(match.group(1))
            if target is None:
                continue
            resolved_path = path if not target else resolve_target(path, target)
            if target and not resolved_path.exists():
                issues.append(
                    Issue(path, line_no, f"broken relative link: {match.group(1)}")
                )
                continue
            if anchor:
                anchors = anchor_map.get(resolved_path)
                if anchors is None:
                    try:
                        anchors = build_anchor_index(
                            resolved_path.read_text(encoding="utf-8")
                        )
                    except OSError:
                        anchors = set()
                if anchor not in anchors:
                    issues.append(
                        Issue(path, line_no, f"broken anchor target: {match.group(1)}")
                    )
    return issues


def validate_files(paths: list[Path]) -> list[Issue]:
    texts = {path: path.read_text(encoding="utf-8") for path in paths}
    anchor_map = {path: build_anchor_index(text) for path, text in texts.items()}

    issues: list[Issue] = []
    for path, text in texts.items():
        issues.extend(validate_heading_hierarchy(path, text))
        issues.extend(validate_code_fences(path, text))
        issues.extend(validate_links(path, text, anchor_map))
    return sorted(
        issues, key=lambda issue: (str(issue.path), issue.line, issue.message)
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate markdown quality for repository documentation surfaces."
    )
    parser.add_argument(
        "targets",
        nargs="*",
        type=Path,
        help="Optional files or directories to scan. Defaults to repository docs surfaces.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    targets = [
        target if target.is_absolute() else REPO_ROOT / target
        for target in args.targets
    ]
    markdown_files = iter_markdown_files(targets or list(DEFAULT_TARGETS))
    issues = validate_files(markdown_files)

    if issues:
        for issue in issues:
            relative_path = issue.path.relative_to(REPO_ROOT)
            print(f"{relative_path}:{issue.line}: {issue.message}")
        print(f"\nMarkdown quality checks failed: {len(issues)} issue(s).")
        return 1

    print(f"Markdown quality checks passed for {len(markdown_files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
