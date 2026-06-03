#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Ensure ratified artifacts carry ratification receipts."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.lattice_kg_lib import iter_files, load_metadata
REQUIRED=['ratification_event_id','council_signatures','adjudication_date']

def validate_ratification_record(record: dict) -> list[str]:
    if record.get('canon_status')!='ratified': return []
    errors=[]
    for field in REQUIRED:
        if record.get(field) in (None,'',[],{}): errors.append(f'missing {field}')
    return errors

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); rows=[]
    for path in iter_files(Path(a.repo_root).resolve()):
        errors=validate_ratification_record(load_metadata(path))
        if errors: rows.append({'path':path.relative_to(Path(a.repo_root).resolve()).as_posix(),'errors':errors})
    print(json.dumps({'rows':rows}, indent=2)); return 1 if rows else 0
if __name__=='__main__': raise SystemExit(main())
