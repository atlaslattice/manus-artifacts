#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Detect under-linked artifacts with filtering and multiple output formats."""

from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))

import argparse
import json
from pathlib import Path

from scripts.build_lattice_global_index_v2 import build_index
from scripts.lattice_kg_lib import emit_report


def analyze(repo_root: Path, threshold: int, domain: str | None = None, lane: str | None = None) -> list[dict]:
    index = build_index(repo_root)
    rows = []
    for row in index['artifacts']:
        if not row['path'].endswith('.md'):
            continue
        if domain and row['domain'] != domain:
            continue
        if lane and row['lane'] != lane:
            continue
        if row['incoming_links'] < threshold:
            rows.append({
                'path': row['path'],
                'domain': row['domain'],
                'lane': row['lane'],
                'incoming_links': row['incoming_links'],
                'outbound_links': len(row['outbound_repo_links']),
            })
    return rows


def to_markdown(rows: list[dict]) -> str:
    lines = ['# Under-linked Artifacts', '', '| Path | Domain | Lane | Incoming | Outgoing |', '|---|---|---|---:|---:|']
    for row in rows:
        lines.append(f"| {row['path']} | {row['domain']} | {row['lane']} | {row['incoming_links']} | {row['outbound_links']} |")
    return '\n'.join(lines) + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-root', default='.')
    parser.add_argument('--threshold', type=int, default=2)
    parser.add_argument('--domain')
    parser.add_argument('--lane')
    parser.add_argument('--output', choices=['json', 'md', 'csv'], default='md')
    args = parser.parse_args()
    rows = analyze(Path(args.repo_root).resolve(), args.threshold, args.domain, args.lane)
    payload = {'rows': rows, 'threshold': args.threshold}
    if args.output == 'md':
        print(to_markdown(rows), end='')
    else:
        print(emit_report(payload if args.output == 'json' else rows, args.output))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
