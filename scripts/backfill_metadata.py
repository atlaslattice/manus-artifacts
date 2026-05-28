#!/usr/bin/env python3
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = [
    'docs',
    'projects',
    'archive/spec',
    'archive/boot/governance',
]
REQUIRED_FIELDS = ['stable_id', 'lifecycle_state', 'provenance', 'owner', 'date']
OUTPUT_PATH = Path('/tmp/metadata_coverage_report.json')

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


def extract_metadata(text: str) -> tuple[dict[str, str], bool]:
    metadata: dict[str, str] = {}
    has_provenance_block = False

    frontmatter = FRONTMATTER_RE.match(text)
    if frontmatter:
        metadata.update(parse_key_values(frontmatter.group(1)))

    for comment_body in HTML_COMMENT_RE.findall(text):
        lowered = comment_body.lower()
        if 'metadata' in lowered or 'provenance' in lowered:
            has_provenance_block = True
            metadata.update(parse_key_values(comment_body))

    stable_id_match = re.search(r"(?im)^\s*>\s*\*\*Stable ID:\*\*\s*(.+?)\s*$", text)
    if stable_id_match and 'stable_id' not in metadata:
        metadata['stable_id'] = stable_id_match.group(1).strip()

    status_match = re.search(r"(?im)^\s*>\s*\*\*Status:\*\*\s*(.+?)\s*$", text)
    if status_match and 'status' not in metadata:
        metadata['status'] = status_match.group(1).strip()

    date_match = re.search(r"(?im)^\s*>\s*\*\*Date:\*\*\s*(.+?)\s*$", text)
    if date_match and 'date' not in metadata:
        metadata['date'] = date_match.group(1).strip()

    return metadata, has_provenance_block


def has_field(metadata: dict[str, str], field: str, has_provenance_block: bool) -> bool:
    if field == 'lifecycle_state':
        return bool(metadata.get('lifecycle_state') or metadata.get('status'))
    if field == 'date':
        return bool(metadata.get('date') or metadata.get('date_created') or metadata.get('created_date'))
    if field == 'provenance':
        return bool(metadata.get('provenance') or has_provenance_block)
    return bool(metadata.get(field))


def main() -> None:
    missing_by_file: dict[str, list[str]] = {}
    missing_counts: Counter[str] = Counter()
    directory_totals: dict[str, dict[str, int]] = {}

    for relative_dir in SCAN_DIRS:
        base_dir = REPO_ROOT / relative_dir
        files = sorted(base_dir.rglob('*.md')) if base_dir.exists() else []
        stats = {'total_files': len(files)}
        for field in REQUIRED_FIELDS:
            stats[f'has_{field}'] = 0

        for file_path in files:
            text = file_path.read_text(encoding='utf-8')
            metadata, has_provenance_block = extract_metadata(text)
            missing_fields = [
                field for field in REQUIRED_FIELDS
                if not has_field(metadata, field, has_provenance_block)
            ]
            for field in REQUIRED_FIELDS:
                if field not in missing_fields:
                    stats[f'has_{field}'] += 1
            if missing_fields:
                rel_path = file_path.relative_to(REPO_ROOT).as_posix()
                missing_by_file[rel_path] = missing_fields
                missing_counts.update(missing_fields)

        directory_totals[relative_dir] = stats

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scan_directories': SCAN_DIRS,
        'required_fields': REQUIRED_FIELDS,
        'summary': {
            'total_files': sum(stats['total_files'] for stats in directory_totals.values()),
            'files_missing_any_field': len(missing_by_file),
            'missing_field_counts': dict(missing_counts),
        },
        'directory_totals': directory_totals,
        'missing_by_file': missing_by_file,
    }

    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')

    print('Metadata coverage summary')
    print(f"- total files scanned: {payload['summary']['total_files']}")
    print(f"- files missing any required field: {payload['summary']['files_missing_any_field']}")
    for field in REQUIRED_FIELDS:
        print(f"- missing {field}: {missing_counts.get(field, 0)}")
    print(f'- report written to: {OUTPUT_PATH}')

    if missing_by_file:
        print('\nFiles missing metadata fields:')
        for rel_path, fields in sorted(missing_by_file.items()):
            print(f"  - {rel_path}: {', '.join(fields)}")


if __name__ == '__main__':
    main()
