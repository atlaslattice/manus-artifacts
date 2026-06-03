#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Suggest backlinks for under-linked artifacts using token overlap."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.build_lattice_global_index_v2 import build_index
from scripts.lattice_kg_lib import path_tokens

def suggest(repo_root: Path, top_n: int = 3) -> list[dict]:
    index=build_index(repo_root)
    rows=index['artifacts']
    token_map={row['path']:set(path_tokens(row['path'])) for row in rows if row['path'].endswith('.md')}
    suggestions=[]
    for row in rows:
        if not row['path'].endswith('.md') or row['incoming_links'] >= 2:
            continue
        scored=[]
        target_tokens=token_map[row['path']]
        for other, tokens in token_map.items():
            if other==row['path'] or other in row['outbound_repo_links']:
                continue
            score=len(target_tokens & tokens) + (1 if row['domain'] in other else 0)
            if score>0:
                scored.append((score, other))
        scored.sort(key=lambda item:(-item[0], item[1]))
        suggestions.append({'path':row['path'],'suggested_sources':[candidate for _,candidate in scored[:top_n]]})
    return suggestions

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.'); p.add_argument('--top',type=int,default=3)
    a=p.parse_args(); print(json.dumps({'rows':suggest(Path(a.repo_root).resolve(), a.top)}, indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
