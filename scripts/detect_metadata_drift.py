#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Detect metadata drift against v1.0 metadata profiles."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json, yaml
from pathlib import Path
from scripts.lattice_kg_lib import infer_artifact_family, iter_files, load_metadata

def detect(repo_root: Path, profiles_path: Path) -> list[dict]:
    profiles=yaml.safe_load(profiles_path.read_text(encoding='utf-8'))['profiles']; rows=[]
    for path in iter_files(repo_root):
        rel=path.relative_to(repo_root).as_posix(); family=infer_artifact_family(rel); profile=profiles.get(family)
        if not profile: continue
        meta=load_metadata(path); missing=[f for f in profile['required'] if meta.get(f) in (None,'',[],{})]
        if missing: rows.append({'path':rel,'family':family,'missing':missing})
    return rows

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.'); p.add_argument('--profiles',default='archive/knowledge_graph/lattice_kg/v1_0/LATTICE_METADATA_PROFILES_v1.0.yaml')
    a=p.parse_args(); rows=detect(Path(a.repo_root).resolve(), Path(a.profiles)); print(json.dumps({'rows':rows}, indent=2)); return 1 if rows else 0
if __name__=='__main__': raise SystemExit(main())
