#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate deployment status consistency against candidate/ratified state."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.lattice_kg_lib import iter_files, load_metadata

def deployment_state_error(record: dict) -> str | None:
    deployment=record.get('deployment_status') or record.get('deployment')
    canon=record.get('canon_status')
    rat=record.get('ratification_event_id')
    if canon != 'ratified' and deployment not in {'not_deployable','NONE',None}: return f'invalid candidate deployment_status: {deployment}'
    if canon == 'ratified' and deployment == 'deployable' and rat in {None,'','PENDING'}: return 'deployable requires ratification receipt'
    return None

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); rows=[]; root=Path(a.repo_root).resolve()
    for path in iter_files(root):
        error=deployment_state_error(load_metadata(path))
        if error: rows.append({'path':path.relative_to(root).as_posix(),'error':error})
    print(json.dumps({'rows':rows}, indent=2)); return 1 if rows else 0
if __name__=='__main__': raise SystemExit(main())
