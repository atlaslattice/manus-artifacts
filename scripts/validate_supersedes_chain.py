#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate supersedes chains for cycles and missing targets."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.lattice_kg_lib import iter_files, load_metadata

def collect_graph(repo_root: Path):
    graph={}; known={}
    for path in iter_files(repo_root):
        meta=load_metadata(path); aid=meta.get('artifact_id')
        if aid:
            graph[aid]=meta.get('supersedes') or []
            if isinstance(graph[aid], str): graph[aid]=[graph[aid]]
            known[aid]=path.relative_to(repo_root).as_posix()
    return graph, known

def find_cycles(graph: dict[str,list[str]]) -> list[list[str]]:
    cycles=[]
    visiting=set(); visited=set(); stack=[]
    def dfs(node):
        if node in visited: return
        if node in visiting:
            if node in stack: cycles.append(stack[stack.index(node):] + [node])
            return
        visiting.add(node); stack.append(node)
        for nxt in graph.get(node,[]): dfs(nxt)
        stack.pop(); visiting.remove(node); visited.add(node)
    for node in graph: dfs(node)
    return cycles

def validate(repo_root: Path) -> dict:
    graph, known = collect_graph(repo_root)
    missing=[{'artifact_id':src,'missing_target':tgt} for src, tgts in graph.items() for tgt in tgts if tgt not in known]
    return {'missing':missing,'cycles':find_cycles(graph)}

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.')
    a=p.parse_args(); payload=validate(Path(a.repo_root).resolve()); print(json.dumps(payload, indent=2)); return 1 if payload['missing'] or payload['cycles'] else 0
if __name__=='__main__': raise SystemExit(main())
