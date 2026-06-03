#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Normalize markdown frontmatter ordering and key names."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.lattice_kg_lib import FRONTMATTER_KEYS, dump_frontmatter, iter_files, load_metadata, read_text, split_frontmatter, utc_now

ALIASES={'STATUS':'status','AUTHORITY':'authority','DEPLOYMENT':'deployment','canonStatus':'canon_status','deploymentStatus':'deployment_status','next-action':'next_safest_action','blocker':'blocker_status'}

def normalize_mapping(meta: dict) -> dict:
    normalized={ALIASES.get(k,k):v for k,v in meta.items()}
    normalized.setdefault('status','CANDIDATE — NOT CANON'); normalized.setdefault('canon_status','candidate'); normalized.setdefault('deployment_status','not_deployable'); normalized.setdefault('authority','NONE')
    normalized.setdefault('generated_at_utc', utc_now()); normalized.setdefault('ratification_event_id','PENDING')
    ordered={}
    for key in FRONTMATTER_KEYS + ['test_receipt','blocker_status','next_safest_action','ratification_event_id']:
        if key in normalized: ordered[key]=normalized[key]
    for key, value in normalized.items():
        if key not in ordered: ordered[key]=value
    return ordered

def detect_unexpected_fields(meta: dict, allowed: set[str]) -> list[str]:
    return sorted(set(meta) - allowed)

def run(repo_root: Path, write: bool) -> list[dict]:
    rows=[]
    for path in iter_files(repo_root, extensions={'.md'}):
        text=read_text(path); meta, body=split_frontmatter(text)
        if not meta: continue
        normalized=normalize_mapping(meta)
        changed=normalized != meta
        rows.append({'path':path.relative_to(repo_root).as_posix(),'changed':changed,'normalized_keys':list(normalized)})
        if write and changed: path.write_text(dump_frontmatter(normalized, body), encoding='utf-8')
    return rows

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.'); p.add_argument('--write',action='store_true')
    a=p.parse_args(); rows=run(Path(a.repo_root).resolve(), a.write); print(json.dumps({'rows':rows,'dry_run':not a.write}, indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
