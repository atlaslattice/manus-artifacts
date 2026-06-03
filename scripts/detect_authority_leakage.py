#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Detect authority leakage outside ratified state."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.lattice_kg_lib import iter_files, load_metadata

def find_authority_leakage(records: list[dict]) -> list[dict]:
    rows=[]
    for record in records:
        authority=str(record.get('authority','NONE')).lower()
        if authority not in {'none',''} and record.get('canon_status') != 'ratified':
            rows.append({'artifact_id':record.get('artifact_id'),'authority':record.get('authority')})
    return rows

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); root=Path(a.repo_root).resolve(); rows=find_authority_leakage([load_metadata(path) for path in iter_files(root)]); print(json.dumps({'rows':rows}, indent=2)); return 1 if rows else 0
if __name__=='__main__': raise SystemExit(main())
