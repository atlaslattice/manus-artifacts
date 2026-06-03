#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Enforce a minimum inbound link count for markdown artifacts."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.build_lattice_global_index_v2 import build_index

def find_violations(repo_root: Path, minimum: int = 2) -> list[dict]:
    index=build_index(repo_root)
    return [{'path':row['path'],'incoming_links':row['incoming_links']} for row in index['artifacts'] if row['path'].endswith('.md') and row['incoming_links'] < minimum]

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.'); p.add_argument('--minimum',type=int,default=2)
    a=p.parse_args(); rows=find_violations(Path(a.repo_root).resolve(), a.minimum); print(json.dumps({'rows':rows}, indent=2)); return 1 if rows else 0
if __name__=='__main__': raise SystemExit(main())
