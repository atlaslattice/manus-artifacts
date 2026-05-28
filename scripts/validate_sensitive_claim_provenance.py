#!/usr/bin/env python3
from __future__ import annotations

import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent

TRACKED_PATHS = (
    "docs/",
    "governance/",
    "health/",
    "research/",
)

SENSITIVE_RE = re.compile(
    r"\b("
    r"high-impact|public[- ]risk|critical|unsafe|security|harm|sensitive|institution"
    r")\b",
    re.IGNORECASE,
)
PROVENANCE_RE = re.compile(
    r"(Source:\s|Sources:\s|Citations:\s|Evidence reviewed|https?://)",
    re.IGNORECASE,
)
SKIP_FILES = {
    "governance/README.md",
    "docs/README.md",
}


def git_output(args: list[str]) -> str:
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()


def git_ok(args: list[str]) -> bool:
    try:
        subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError:
        return False


def determine_diff_refs() -> tuple[str | None, str]:
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    base_ref = os.environ.get("GITHUB_BASE_REF", "")
    if event == "pull_request" and base_ref:
        remote_base = f"origin/{base_ref}"
        if not git_ok(["git", "rev-parse", "--verify", remote_base]):
            subprocess.run(["git", "fetch", "origin", base_ref], cwd=ROOT, check=True)
        return remote_base, "HEAD"

    if git_ok(["git", "rev-parse", "--verify", "HEAD^"]):
        return "HEAD^", "HEAD"

    return None, "HEAD"


def changed_markdown_files(before_ref: str | None, after_ref: str) -> list[str]:
    if before_ref is None:
        files = git_output(["git", "ls-files", *TRACKED_PATHS]).splitlines()
    else:
        files = git_output(
            ["git", "diff", "--name-only", before_ref, after_ref, "--", *TRACKED_PATHS]
        ).splitlines()
    return [f for f in files if f.endswith(".md")]


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def main() -> int:
    before_ref, after_ref = determine_diff_refs()
    changed = changed_markdown_files(before_ref, after_ref)
    errors: list[str] = []
    sensitive_files = 0

    for rel_path in changed:
        if rel_path in SKIP_FILES:
            continue
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        body = strip_code_blocks(text)

        sensitive_hits = [line for line in body.splitlines() if SENSITIVE_RE.search(line)]
        if not sensitive_hits:
            continue

        sensitive_files += 1
        if not PROVENANCE_RE.search(body):
            errors.append(
                f"{rel_path}: sensitive claim language detected without provenance markers "
                "(add Source/Citations/Evidence references)"
            )

    if errors:
        print("sensitive claim provenance validation failed:")
        for error_msg in errors:
            print(f"- {error_msg}")
        return 1

    print(
        "sensitive claim provenance validation passed "
        f"({len(changed)} markdown files checked, {sensitive_files} sensitive files with provenance)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
