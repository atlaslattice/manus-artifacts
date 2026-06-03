#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Detect multiple canon claims for the same concept without a supersedes chain."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from collections import defaultdict
from pathlib import Path
from scripts.lattice_kg_lib import iter_files, load_metadata

def detect_conflicting_claims(records: list[dict]) -> list[dict]:
    groups=defaultdict(list)
    for record in records:
        concept=record.get('concept_id') or record.get('artifact_family') or record.get('artifact_id')
        if record.get('canon_status') in {'approved','ratified'}:
            groups[concept].append(record)
    rows=[]
    for concept, items in groups.items():
        if len(items) < 2: continue
        ids={item.get('artifact_id') for item in items}
        linked=False
        for item in items:
            supersedes=item.get('supersedes') or []
            if isinstance(supersedes, str): supersedes=[supersedes]
            if ids & set(supersedes): linked=True
        if not linked: rows.append({'concept':concept,'artifact_ids':sorted(ids)})
    return rows

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); root=Path(a.repo_root).resolve(); rows=detect_conflicting_claims([load_metadata(path) for path in iter_files(root)]); print(json.dumps({'rows':rows}, indent=2)); return 1 if rows else 0
if __name__=='__main__': raise SystemExit(main())
