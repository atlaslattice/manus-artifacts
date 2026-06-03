#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Map legacy metadata keys to normalized keys and emit a migration diff report."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.lattice_kg_lib import iter_files, read_text, split_frontmatter
from scripts.normalize_metadata import ALIASES

def map_migrations(repo_root: Path) -> list[dict]:
    rows=[]
    for path in iter_files(repo_root, extensions={'.md'}):
        meta,_=split_frontmatter(read_text(path))
        if not meta: continue
        changes={key:ALIASES[key] for key in meta if key in ALIASES}
        if changes: rows.append({'path':path.relative_to(repo_root).as_posix(),'migrations':changes})
    return rows

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); print(json.dumps({'rows':map_migrations(Path(a.repo_root).resolve()),'dry_run':True}, indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
