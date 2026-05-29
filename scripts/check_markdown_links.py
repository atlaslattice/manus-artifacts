from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")



def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[`*_]", "", value)
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-")



def anchors_for_file(path: Path) -> set[str]:
    anchors: set[str] = set()
    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            anchor = slugify(match.group(2))
            if anchor:
                anchors.add(anchor)
    return anchors



def iter_markdown_files() -> list[Path]:
    files: set[Path] = set()
    readme = ROOT / "README.md"
    if readme.exists():
        files.add(readme)

    for path in (ROOT / "docs").rglob("*.md"):
        files.add(path)
    for path in (ROOT / ".github").glob("*.md"):
        files.add(path)

    return sorted(files)



def is_external(link: str) -> bool:
    return link.startswith(("http://", "https://", "mailto:", "{{"))



def check_links() -> int:
    markdown_files = iter_markdown_files()
    anchor_index = {path: anchors_for_file(path) for path in markdown_files}
    failures: list[str] = []

    for file_path in markdown_files:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        for raw_link in LINK_RE.findall(text):
            link = raw_link.strip()
            if not link or is_external(link):
                continue

            target_path = link
            anchor = None
            if "#" in link:
                target_path, anchor = link.split("#", 1)
                anchor = slugify(anchor)

            if target_path.startswith("/"):
                resolved = ROOT / target_path.lstrip("/")
            elif target_path:
                resolved = (file_path.parent / target_path).resolve()
            else:
                resolved = file_path

            if not resolved.exists():
                failures.append(f"{file_path.relative_to(ROOT)}: broken link '{link}'")
                continue

            if resolved.is_dir():
                continue

            if anchor and resolved.suffix.lower() in {".md", ""}:
                target_anchors = anchor_index.get(resolved)
                if target_anchors is None:
                    target_anchors = anchors_for_file(resolved)
                    anchor_index[resolved] = target_anchors
                if anchor not in target_anchors:
                    failures.append(
                        f"{file_path.relative_to(ROOT)}: missing anchor '{anchor}' in '{resolved.relative_to(ROOT)}'"
                    )

    if failures:
        print("docs link integrity: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("docs link integrity: PASS")
    return 0



if __name__ == "__main__":
    sys.exit(check_links())
