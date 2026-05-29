#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUS_RE = re.compile(r"^Status:\s*(.+)$", re.MULTILINE)

TRACKED_PATHS = (
    "README.md",
    "docs/",
    "governance/",
    "projects/",
)

ALLOWED_TRANSITIONS = {
    ("draft", "candidate"),
    ("candidate", "canon"),
    ("canon", "archived"),
    ("candidate", "archived"),
    ("canon", "deprecated"),
    ("candidate", "deprecated"),
    ("archived", "deprecated"),
    ("deprecated", "archived"),
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


def read_ref_text(ref: str, rel_path: str) -> str | None:
    if not git_ok(["git", "cat-file", "-e", f"{ref}:{rel_path}"]):
        return None
    return git_output(["git", "show", f"{ref}:{rel_path}"])


def extract_state(text: str | None) -> str | None:
    if text is None:
        return None

    match = STATUS_RE.search(text)
    if not match:
        return None

    value = match.group(1).strip().lower()
    if "not canon" in value:
        return "candidate"

    for state in ("draft", "candidate", "canon", "archived", "deprecated"):
        if re.search(rf"\b{state}\b", value):
            return state
    return None


def main() -> int:
    before_ref, after_ref = determine_diff_refs()
    changed = changed_markdown_files(before_ref, after_ref)
    errors: list[str] = []
    transition_count = 0

    for rel_path in changed:
        after_text = (ROOT / rel_path).read_text(encoding="utf-8") if (ROOT / rel_path).exists() else None
        before_text = read_ref_text(before_ref, rel_path) if before_ref else None

        before_state = extract_state(before_text)
        after_state = extract_state(after_text)

        if before_state == after_state:
            continue

        if before_state is None and after_state is None:
            continue

        transition_count += 1
        if before_state is None:
            if after_state in {"draft", "candidate"}:
                continue
            errors.append(
                f"{rel_path}: unable to classify state transition "
                f"({before_state or 'missing/unknown'} -> {after_state or 'missing/unknown'})"
            )
            continue
        if after_state is None:
            errors.append(
                f"{rel_path}: unable to classify state transition "
                f"({before_state or 'missing/unknown'} -> {after_state or 'missing/unknown'})"
            )
            continue

        if (before_state, after_state) not in ALLOWED_TRANSITIONS:
            errors.append(
                f"{rel_path}: invalid canon lifecycle transition "
                f"({before_state} -> {after_state})"
            )

    if errors:
        print("canon transition validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "canon transition validation passed "
        f"({len(changed)} markdown files checked, {transition_count} transitions detected)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
