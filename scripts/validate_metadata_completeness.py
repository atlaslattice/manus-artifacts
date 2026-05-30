#!/usr/bin/env python3
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / 'docs/knowledge-graph/artifact_registry.v0_1.json'
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--(.*?)-->", re.DOTALL)
KV_RE = re.compile(r"^\s*([A-Za-z0-9_-]+)\s*:\s*(.*?)\s*$")


def load_registry() -> dict:
    try:
        return json.loads(REGISTRY_PATH.read_text(encoding='utf-8'))
    except FileNotFoundError:
        print(f'[FAIL] Registry file missing: {REGISTRY_PATH}')
        sys.exit(1)
    except json.JSONDecodeError as exc:
        print(f'[FAIL] Registry file is invalid JSON: {exc}')
        sys.exit(1)


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


def extract_markdown_metadata(path: Path) -> dict[str, str]:
    text = path.read_text(encoding='utf-8')
    metadata: dict[str, str] = {}

    frontmatter = FRONTMATTER_RE.match(text)
    if frontmatter:
        metadata.update(parse_key_values(frontmatter.group(1)))

    for comment_body in HTML_COMMENT_RE.findall(text):
        if 'metadata' in comment_body.lower() or 'provenance' in comment_body.lower():
            metadata.update(parse_key_values(comment_body))

    stable_id_match = re.search(r"(?im)^\s*>\s*\*\*Stable ID:\*\*\s*(.+?)\s*$", text)
    if stable_id_match and 'stable_id' not in metadata:
        metadata['stable_id'] = stable_id_match.group(1).strip()

    return metadata


def print_check(name: str, ok: bool, details: list[str]) -> None:
    status = 'PASS' if ok else 'FAIL'
    print(f'[{status}] {name}')
    for detail in details:
        print(f'  - {detail}')


def main() -> None:
    registry = load_registry()
    artifacts = registry.get('artifacts', [])
    failures = 0

    ids = [artifact.get('id', '') for artifact in artifacts]
    id_counts = Counter(ids)
    duplicate_ids = [artifact_id for artifact_id, count in sorted(id_counts.items()) if artifact_id and count > 1]
    print_check('Duplicate registry IDs', not duplicate_ids, duplicate_ids or [f'Unique IDs: {len(id_counts)}'])
    failures += 0 if not duplicate_ids else 1

    normalized_title_counts: defaultdict[str, list[str]] = defaultdict(list)
    for artifact in artifacts:
        title = str(artifact.get('title', '')).strip()
        if title:
            normalized_title_counts[title.casefold()].append(title)
    duplicate_titles = []
    for title_group in normalized_title_counts.values():
        if len(title_group) > 1:
            duplicate_titles.append(' / '.join(title_group))
    print_check(
        'Duplicate registry titles (case-insensitive)',
        not duplicate_titles,
        duplicate_titles or [f'Unique titles: {len(normalized_title_counts)}'],
    )
    failures += 0 if not duplicate_titles else 1

    missing_paths = []
    for artifact in artifacts:
        artifact_path = artifact.get('path')
        if artifact_path and not (REPO_ROOT / artifact_path).exists():
            missing_paths.append(f"{artifact.get('id', '<unknown>')} -> {artifact_path}")
    print_check('Registered artifact paths exist', not missing_paths, missing_paths or [f'Existing paths: {len(artifacts) - len(missing_paths)}'])
    failures += 0 if not missing_paths else 1

    registry_paths = {artifact.get('path') for artifact in artifacts if artifact.get('path')}
    orphaned_artifacts = []
    for root_name in ('projects', 'docs'):
        for markdown_path in sorted((REPO_ROOT / root_name).rglob('*.md')):
            rel_path = markdown_path.relative_to(REPO_ROOT).as_posix()
            metadata = extract_markdown_metadata(markdown_path)
            if rel_path not in registry_paths and not metadata.get('stable_id'):
                orphaned_artifacts.append(rel_path)
    print_check(
        'Orphaned markdown artifacts',
        not orphaned_artifacts,
        orphaned_artifacts or ['No unregistered markdown artifacts without stable IDs'],
    )
    failures += 0 if not orphaned_artifacts else 1

    # Check for duplicate stable IDs embedded in markdown files across docs/ and projects/
    markdown_id_paths: defaultdict[str, list[str]] = defaultdict(list)
    for root_name in ('docs', 'projects'):
        for markdown_path in sorted((REPO_ROOT / root_name).rglob('*.md')):
            metadata = extract_markdown_metadata(markdown_path)
            sid = metadata.get('stable_id', '').strip()
            if sid:
                markdown_id_paths[sid].append(markdown_path.relative_to(REPO_ROOT).as_posix())
    duplicate_markdown_ids = [
        f"{sid}: {', '.join(paths)}"
        for sid, paths in sorted(markdown_id_paths.items())
        if len(paths) > 1
    ]
    print_check(
        'Duplicate stable IDs in markdown files',
        not duplicate_markdown_ids,
        duplicate_markdown_ids or [f'Unique stable IDs in markdown: {len(markdown_id_paths)}'],
    )
    failures += 0 if not duplicate_markdown_ids else 1

    registry_ids = {artifact.get('id') for artifact in artifacts if artifact.get('id')}
    missing_targets = []
    for artifact in artifacts:
        for link in artifact.get('links', []):
            target_id = link.get('target_id')
            if target_id not in registry_ids:
                missing_targets.append(f"{artifact.get('id', '<unknown>')} -> {target_id}")
    print_check('Relation target IDs exist', not missing_targets, missing_targets or [f'Validated links across {len(artifacts)} artifacts'])
    failures += 0 if not missing_targets else 1

    declared_count = registry.get('artifact_count')
    count_matches = declared_count == len(artifacts)
    print_check(
        'Declared artifact count matches registry payload',
        count_matches,
        [f'registry artifact_count={declared_count}', f'actual artifacts={len(artifacts)}'],
    )
    failures += 0 if count_matches else 1

    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
