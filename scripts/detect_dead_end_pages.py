#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Detect markdown pages with no outbound repository links."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.build_lattice_global_index_v2 import build_index

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); index=build_index(Path(a.repo_root).resolve()); rows=[{'path':row['path']} for row in index['artifacts'] if row['path'].endswith('.md') and not row['outbound_repo_links']]
    print(json.dumps({'rows':rows}, indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
