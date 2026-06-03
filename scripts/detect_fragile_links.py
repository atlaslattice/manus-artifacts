#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Detect artifacts that are reached by only one inbound link."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.build_lattice_global_index_v2 import build_index

def detect_fragile(repo_root: Path) -> list[dict]:
    index=build_index(repo_root)
    return [{'path':row['path'],'incoming_links':row['incoming_links']} for row in index['artifacts'] if row['path'].endswith('.md') and row['incoming_links']==1]

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); print(json.dumps({'rows':detect_fragile(Path(a.repo_root).resolve())}, indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
