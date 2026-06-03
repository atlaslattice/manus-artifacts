#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Reject artifacts claiming canon or authority without ratification."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.lattice_kg_lib import iter_files, load_metadata

def validate_record(record: dict) -> list[str]:
    errors=[]; canon=record.get('canon_status'); authority=str(record.get('authority','NONE')).lower(); rat=record.get('ratification_event_id')
    if canon in {'ratified','approved'} and rat in {None,'','PENDING'}: errors.append('ratified artifact missing ratification_event_id')
    if authority not in {'none','', 'none.'} and rat in {None,'','PENDING'}: errors.append('authority claimed without ratification_event_id')
    return errors

def scan(repo_root: Path) -> list[dict]:
    rows=[]
    for path in iter_files(repo_root):
        meta=load_metadata(path); errors=validate_record(meta)
        if errors: rows.append({'path':path.relative_to(repo_root).as_posix(),'errors':errors})
    return rows

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); rows=scan(Path(a.repo_root).resolve()); print(json.dumps({'rows':rows}, indent=2)); return 1 if rows else 0
if __name__=='__main__': raise SystemExit(main())
