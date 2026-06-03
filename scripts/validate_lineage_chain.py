#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate that patches/supersedes links resolve across artifacts."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.lattice_kg_lib import iter_files, load_metadata

def validate(repo_root: Path) -> list[str]:
    metadata={path.relative_to(repo_root).as_posix():load_metadata(path) for path in iter_files(repo_root)}
    known_ids={meta.get('artifact_id') for meta in metadata.values() if meta.get('artifact_id')}
    errors=[]
    for rel, meta in metadata.items():
        for key in ('supersedes','patches'):
            value=meta.get(key) or []
            if isinstance(value, str): value=[value]
            for target in value:
                if target not in known_ids:
                    errors.append(f'{rel}: unresolved {key} target {target}')
    return errors

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); errors=validate(Path(a.repo_root).resolve()); print(json.dumps({'errors':errors}, indent=2)); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
