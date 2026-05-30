#!/usr/bin/env python3
"""Generate a human-readable per-domain metadata coverage report.

Output: docs/domain-metadata-coverage-report.md
Also emits docs/domain-metadata-coverage-report.json (machine-readable).

A file is considered "covered" if it has a stable_id in its metadata block
and is registered in the artifact registry.  Partial coverage means a stable
ID is present in the file but the file is not yet in the registry (or vice
versa).
"""
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / 'docs/knowledge-graph/artifact_registry.v0_1.json'
MD_OUTPUT = REPO_ROOT / 'docs/domain-metadata-coverage-report.md'
JSON_OUTPUT = REPO_ROOT / 'docs/domain-metadata-coverage-report.json'

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--(.*?)-->", re.DOTALL)
KV_RE = re.compile(r"^\s*([A-Za-z0-9_-]+)\s*:\s*(.*?)\s*$")
STABLE_ID_RE = re.compile(r"(?im)^\s*>\s*\*\*Stable ID:\*\*\s*(.+?)\s*$")
ID_DOMAIN_RE = re.compile(r"^AL-([A-Z0-9]+)-\d+$")

SCAN_ROOTS = ('docs', 'projects', 'archive', 'research', 'health', 'scripts', '.github')


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


def extract_stable_id(path: Path) -> str | None:
    try:
        text = path.read_text(encoding='utf-8')
    except (OSError, UnicodeDecodeError):
        return None
    fm = FRONTMATTER_RE.match(text)
    if fm:
        kv = parse_key_values(fm.group(1))
        if kv.get('stable_id'):
            return kv['stable_id']
    for body in HTML_COMMENT_RE.findall(text):
        if 'metadata' in body.lower() or 'provenance' in body.lower():
            kv = parse_key_values(body)
            if kv.get('stable_id'):
                return kv['stable_id']
    m = STABLE_ID_RE.search(text)
    if m:
        return m.group(1).strip()
    return None


def domain_from_id(stable_id: str) -> str:
    m = ID_DOMAIN_RE.match(stable_id)
    return m.group(1) if m else 'OTHER'


def main() -> None:
    try:
        registry = json.loads(REGISTRY_PATH.read_text(encoding='utf-8'))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f'[FAIL] Could not load registry: {exc}')
        sys.exit(1)

    artifacts = registry.get('artifacts', [])
    registry_paths = {a['path'] for a in artifacts if a.get('path')}
    registry_ids = {a['id'] for a in artifacts if a.get('id')}

    # domain → {total, covered, partial, orphaned}
    domain_stats: defaultdict[str, dict[str, int]] = defaultdict(
        lambda: {'total': 0, 'covered': 0, 'partial': 0, 'orphaned': 0}
    )

    # scan all markdown files in relevant scan roots
    orphaned: list[dict] = []
    for root_name in SCAN_ROOTS:
        root = REPO_ROOT / root_name
        if not root.exists():
            continue
        for md_path in sorted(root.rglob('*.md')):
            rel = md_path.relative_to(REPO_ROOT).as_posix()
            sid = extract_stable_id(md_path)
            in_registry = rel in registry_paths
            domain = domain_from_id(sid) if sid else 'UNREGISTERED'

            stats = domain_stats[domain]
            stats['total'] += 1

            if sid and in_registry:
                stats['covered'] += 1
            elif sid and not in_registry:
                stats['partial'] += 1
                orphaned.append({'path': rel, 'stable_id': sid, 'issue': 'id_present_not_registered'})
            elif not sid and in_registry:
                stats['partial'] += 1
                orphaned.append({'path': rel, 'stable_id': None, 'issue': 'registered_no_id_in_file'})
            else:
                stats['orphaned'] += 1
                orphaned.append({'path': rel, 'stable_id': None, 'issue': 'no_id_not_registered'})

    # compute registry-level domain coverage
    registry_domain_stats: defaultdict[str, dict[str, int]] = defaultdict(
        lambda: {'total': 0, 'with_links': 0, 'with_owner': 0}
    )
    for artifact in artifacts:
        sid = artifact.get('id', '')
        domain = domain_from_id(sid) if sid else 'OTHER'
        rs = registry_domain_stats[domain]
        rs['total'] += 1
        if artifact.get('links'):
            rs['with_links'] += 1
        # owner not a registry field directly but check provenance
        rs['with_owner'] += 1  # all registry entries are considered owned

    now = datetime.now(tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # --- JSON output ---
    report_data = {
        'generated_at': now,
        'stable_id': 'AL-HEALTH-003',
        'total_markdown_files_scanned': sum(d['total'] for d in domain_stats.values()),
        'total_registered_artifacts': len(artifacts),
        'domain_coverage': {
            domain: {
                'markdown_total': stats['total'],
                'covered': stats['covered'],
                'partial': stats['partial'],
                'orphaned': stats['orphaned'],
                'coverage_pct': round(100 * stats['covered'] / stats['total'], 1) if stats['total'] else 0,
            }
            for domain, stats in sorted(domain_stats.items())
        },
        'registry_domain_breakdown': {
            domain: rs for domain, rs in sorted(registry_domain_stats.items())
        },
        'orphaned_artifacts': orphaned,
    }
    JSON_OUTPUT.write_text(json.dumps(report_data, indent=2), encoding='utf-8')

    # --- Markdown output ---
    total_md = report_data['total_markdown_files_scanned']
    total_covered = sum(d['covered'] for d in domain_stats.values())
    total_partial = sum(d['partial'] for d in domain_stats.values())
    total_orphaned = sum(d['orphaned'] for d in domain_stats.values())
    overall_pct = round(100 * total_covered / total_md, 1) if total_md else 0

    lines: list[str] = [
        '# Domain Metadata Coverage Report',
        '',
        '<!-- METADATA',
        'stable_id: AL-HEALTH-003',
        'lifecycle_state: CANDIDATE',
        'owner: @atlaslattice',
        f'date_created: {now[:10]}',
        'canon_status: candidate',
        '-->',
        '',
        '> **Status:** CANDIDATE',
        '> **Artifact Type:** report',
        '> **Stable ID:** AL-HEALTH-003',
        f'> **Generated:** {now}',
        '',
        '## Summary',
        '',
        f'| Metric | Value |',
        f'|---|---|',
        f'| Total markdown files scanned | {total_md} |',
        f'| Fully covered (ID + registered) | {total_covered} |',
        f'| Partial coverage (ID only or registered only) | {total_partial} |',
        f'| Orphaned (no ID, not registered) | {total_orphaned} |',
        f'| Overall coverage | **{overall_pct}%** |',
        f'| Registered artifacts | {len(artifacts)} |',
        '',
        '## Per-Domain Coverage',
        '',
        '| Domain | MD Files | Covered | Partial | Orphaned | Coverage % |',
        '|---|---:|---:|---:|---:|---:|',
    ]
    for domain, stats in sorted(domain_stats.items()):
        pct = round(100 * stats['covered'] / stats['total'], 1) if stats['total'] else 0
        lines.append(
            f"| {domain} | {stats['total']} | {stats['covered']} | {stats['partial']} | {stats['orphaned']} | {pct}% |"
        )

    lines += [
        '',
        '## Registry Domain Breakdown',
        '',
        '| Domain | Registered | With Links |',
        '|---|---:|---:|',
    ]
    for domain, rs in sorted(registry_domain_stats.items()):
        lines.append(f"| {domain} | {rs['total']} | {rs['with_links']} |")

    if orphaned:
        lines += [
            '',
            '## Orphaned / Partial Coverage Artifacts',
            '',
            '| Path | Stable ID | Issue |',
            '|---|---|---|',
        ]
        for item in orphaned[:50]:  # cap at 50 rows for readability
            sid_cell = item['stable_id'] or '—'
            lines.append(f"| `{item['path']}` | {sid_cell} | {item['issue']} |")
        if len(orphaned) > 50:
            lines.append(f'| *(+ {len(orphaned) - 50} more — see JSON report)* | — | — |')

    lines += [
        '',
        '---',
        '',
        '*Generated automatically by `scripts/generate_domain_coverage_report.py`.*',
        '*Machine-readable data available at `docs/domain-metadata-coverage-report.json`.*',
        '',
    ]

    MD_OUTPUT.write_text('\n'.join(lines), encoding='utf-8')

    print(f'[OK] Written: {MD_OUTPUT.relative_to(REPO_ROOT)}')
    print(f'[OK] Written: {JSON_OUTPUT.relative_to(REPO_ROOT)}')
    print(f'[INFO] Total markdown scanned: {total_md}')
    print(f'[INFO] Covered: {total_covered} ({overall_pct}%)')
    print(f'[INFO] Orphaned: {total_orphaned}')


if __name__ == '__main__':
    main()
