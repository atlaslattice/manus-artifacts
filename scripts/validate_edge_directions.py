#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate edge source/target presence and self-loop prevention."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.build_lattice_global_index_v2 import build_index

def validate(repo_root: Path) -> list[str]:
    index=build_index(repo_root); known={row['artifact_id'] for row in index['artifacts']}; errors=[]
    for edge in index['edges']:
        if edge['from_id'] not in known or edge['to_id'] not in known: errors.append(f"missing endpoint in {edge['edge_id']}")
        if edge['from_id']==edge['to_id']: errors.append(f"self-loop in {edge['edge_id']}")
    return errors

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); errors=validate(Path(a.repo_root).resolve()); print(json.dumps({'errors':errors}, indent=2)); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
