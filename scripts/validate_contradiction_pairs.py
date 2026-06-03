#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate contradiction edges for existence and evidence refs."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.lattice_kg_lib import iter_files, load_metadata

def validate_contradiction_edge(edge: dict, known_ids: set[str]) -> list[str]:
    errors=[]
    if edge.get('from_id') not in known_ids: errors.append('missing from_id')
    if edge.get('to_id') not in known_ids: errors.append('missing to_id')
    if not edge.get('evidence_refs'): errors.append('missing evidence_refs')
    return errors

def validate(repo_root: Path) -> list[dict]:
    metadata=[load_metadata(path) for path in iter_files(repo_root)]
    known_ids={meta.get('artifact_id') for meta in metadata if meta.get('artifact_id')}
    rows=[]
    for meta in metadata:
        contradictions=meta.get('contradictions') or []
        if isinstance(contradictions, dict): contradictions=[contradictions]
        for edge in contradictions:
            errors=validate_contradiction_edge(edge, known_ids)
            if errors: rows.append({'edge':edge,'errors':errors})
    return rows

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); rows=validate(Path(a.repo_root).resolve()); print(json.dumps({'rows':rows}, indent=2)); return 1 if rows else 0
if __name__=='__main__': raise SystemExit(main())
