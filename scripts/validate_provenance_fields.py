#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIRS = ['docs', 'projects', 'archive/spec', 'archive/boot/governance']
REQUIRED_FIELDS = ['stable_id', 'lifecycle_state', 'owner', 'date_created']
SUMMARY_PATH = REPO_ROOT / 'docs/provenance-validation-summary.json'
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


def extract_metadata(path: Path) -> dict[str, str]:
    text = path.read_text(encoding='utf-8')
    metadata: dict[str, str] = {}
    frontmatter = FRONTMATTER_RE.match(text)
    if frontmatter:
        metadata.update(parse_key_values(frontmatter.group(1)))
    for comment_body in HTML_COMMENT_RE.findall(text):
        if 'metadata' in comment_body.lower() or 'provenance' in comment_body.lower():
            metadata.update(parse_key_values(comment_body))
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description='Report provenance field coverage for markdown artifacts.')
    parser.add_argument('directories', nargs='*', default=DEFAULT_DIRS, help='Directories to scan relative to repo root.')
    args = parser.parse_args()

    rows = []
    missing_counts: Counter[str] = Counter()
    total_files = 0

    for rel_dir in args.directories:
        base_dir = REPO_ROOT / rel_dir
        if not base_dir.exists():
            continue
        for path in sorted(base_dir.rglob('*.md')):
            total_files += 1
            metadata = extract_metadata(path)
            missing_fields = [field for field in REQUIRED_FIELDS if not metadata.get(field)]
            if missing_fields:
                missing_counts.update(missing_fields)
            rows.append({
                'path': path.relative_to(REPO_ROOT).as_posix(),
                'missing_fields': missing_fields,
            })

    print('| File | Missing fields |')
    print('| --- | --- |')
    for row in rows:
        missing_display = ', '.join(row['missing_fields']) if row['missing_fields'] else 'none'
        print(f"| {row['path']} | {missing_display} |")

    summary = {
        'scan_directories': args.directories,
        'required_fields': REQUIRED_FIELDS,
        'total_files': total_files,
        'files_with_missing_fields': sum(1 for row in rows if row['missing_fields']),
        'missing_field_counts': dict(missing_counts),
        'results': rows,
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')

    print(f'\nSummary written to {SUMMARY_PATH.relative_to(REPO_ROOT).as_posix()}')
    print(f'Files scanned: {total_files}')
    print(f"Files missing one or more fields: {summary['files_with_missing_fields']}")


if __name__ == '__main__':
    main()
