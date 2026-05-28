#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / 'docs/knowledge-graph/artifact_registry.v0_1.json'
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--(.*?)-->", re.DOTALL)
KV_RE = re.compile(r"^\s*([A-Za-z0-9_-]+)\s*:\s*(.*?)\s*$")


def parse_key_values(block: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#'):
            continue
        match = KV_RE.match(line)
        if match:
            key, value = match.groups()
            data[key.lower()] = value.strip().strip("\"'")
    return data


def extract_file_status(text: str) -> tuple[str | None, bool]:
    metadata: dict[str, str] = {}

    frontmatter = FRONTMATTER_RE.match(text)
    if frontmatter:
        metadata.update(parse_key_values(frontmatter.group(1)))

    for comment_body in HTML_COMMENT_RE.findall(text):
        if 'metadata' in comment_body.lower() or 'provenance' in comment_body.lower():
            metadata.update(parse_key_values(comment_body))

    status_match = re.search(r"(?im)^\s*>\s*\*\*Status:\*\*\s*(.+?)\s*$", text)
    if status_match and 'status' not in metadata:
        metadata['status'] = status_match.group(1).strip()

    file_status = metadata.get('lifecycle_state') or metadata.get('status')
    file_status = file_status.upper() if file_status else None

    canon_violation = False
    if re.search(r"(?im)^\s*(?:lifecycle_state|status|canon_status)\s*:\s*canon\b", text):
        canon_violation = True
    if re.search(r"(?im)^\s*>\s*\*\*Status:\*\*\s*CANON\b", text):
        canon_violation = True

    return file_status, canon_violation


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding='utf-8'))
    mismatches = []
    warnings = []
    skipped = []

    for artifact in registry.get('artifacts', []):
        rel_path = artifact.get('path')
        if not rel_path:
            continue
        file_path = REPO_ROOT / rel_path
        if not file_path.exists():
            warnings.append(f"{artifact.get('id', '<unknown>')} missing file: {rel_path}")
            continue
        if file_path.is_dir():
            skipped.append(f"{artifact.get('id', '<unknown>')} path is a directory, not a file: {rel_path}")
            continue
        text = file_path.read_text(encoding='utf-8')
        file_status, canon_violation = extract_file_status(text)
        registry_status = str(artifact.get('status', '')).upper()

        if file_status is None:
            skipped.append(f"{artifact.get('id', '<unknown>')} has no comparable lifecycle/status field in {rel_path}")
        elif file_status != registry_status:
            mismatches.append(f"{artifact.get('id', '<unknown>')} registry={registry_status} file={file_status} path={rel_path}")

        if registry_status == 'CANDIDATE' and canon_violation:
            warnings.append(f"{artifact.get('id', '<unknown>')} is CANDIDATE in registry but file metadata says canon: {rel_path}")

    print('[PASS] Lifecycle consistency scan completed')
    print(f"  - registry artifacts scanned: {len(registry.get('artifacts', []))}")
    print(f"  - comparable files: {len(registry.get('artifacts', [])) - len(skipped)}")

    print(f'\n[MISMATCHES] {len(mismatches)}')
    for item in mismatches:
        print(f'  - {item}')

    print(f'\n[WARNINGS] {len(warnings)}')
    for item in warnings:
        print(f'  - {item}')

    print(f'\n[SKIPPED] {len(skipped)}')
    for item in skipped:
        print(f'  - {item}')

    sys.exit(1 if mismatches or warnings else 0)


if __name__ == '__main__':
    main()
