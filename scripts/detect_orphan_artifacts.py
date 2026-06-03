#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Detect orphan markdown artifacts with zero incoming links."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.build_lattice_global_index_v2 import build_index

def find_orphans(repo_root: Path, lane: str | None = None) -> list[dict]:
    index=build_index(repo_root)
    rows=[]
    for row in index['artifacts']:
        if not row['path'].endswith('.md'):
            continue
        if lane and row['lane'] != lane:
            continue
        if row['incoming_links']==0:
            rows.append({'path':row['path'],'lane':row['lane'],'domain':row['domain']})
    return rows

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.'); p.add_argument('--lane')
    a=p.parse_args(); rows=find_orphans(Path(a.repo_root).resolve(), a.lane); print(json.dumps({'rows':rows}, indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
