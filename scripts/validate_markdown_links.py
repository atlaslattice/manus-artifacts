#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate internal markdown links and flag unsafe external links."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json
from pathlib import Path
from scripts.lattice_kg_lib import classify_external_link, extract_markdown_links, iter_files, read_text, resolve_repo_link

def validate_links(repo_root: Path) -> dict:
    broken=[]; unsafe=[]; valid=[]
    for path in iter_files(repo_root, extensions={'.md'}):
        rel=path.relative_to(repo_root).as_posix(); text=read_text(path)
        for link in extract_markdown_links(text):
            target=link['target']
            if '://' in target:
                issue=classify_external_link(target)
                if issue:
                    unsafe.append({'path':rel,'line':link['line'],'target':target,'issue':issue})
                continue
            resolved=resolve_repo_link(repo_root, rel, target)
            if resolved and (repo_root / resolved).exists():
                valid.append({'path':rel,'line':link['line'],'target':resolved})
            elif target and not target.startswith('#') and not target.startswith('mailto:'):
                broken.append({'path':rel,'line':link['line'],'target':target})
    return {'broken_links':broken,'unsafe_external_links':unsafe,'valid_links':len(valid)}

def validate_links_in_text(repo_root: Path, source_rel: str, text: str) -> dict:
    broken=[]
    for link in extract_markdown_links(text):
        resolved=resolve_repo_link(repo_root, source_rel, link['target'])
        if link['target'].startswith('#'):
            continue
        if resolved and (repo_root / resolved).exists():
            continue
        if '://' in link['target'] or link['target'].startswith('mailto:'):
            continue
        broken.append({'path':source_rel,'line':link['line'],'target':link['target']})
    return {'broken_links':broken}

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo-root',default='.')
    p.add_argument('--output',default='json',choices=['json','md'])
    args=p.parse_args(); payload=validate_links(Path(args.repo_root).resolve())
    if args.output=='md':
        print('# Markdown Link Validation Report')
        print(f"- Broken links: {len(payload['broken_links'])}")
        print(f"- Unsafe external links: {len(payload['unsafe_external_links'])}")
    else:
        print(json.dumps(payload, indent=2))
    return 1 if payload['broken_links'] else 0
if __name__=='__main__': raise SystemExit(main())
