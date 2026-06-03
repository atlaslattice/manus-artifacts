#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Detect glossary terms that are not linked from other documents."""
from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))
import argparse, json, re
from pathlib import Path
from scripts.lattice_kg_lib import iter_files, read_text
TERM_RE=re.compile(r'^- `([^`]+)`', re.MULTILINE)

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.'); p.add_argument('--glossary',default='archive/knowledge_graph/lattice_kg/v0_5/LATTICE_KG_GLOSSARY_v0.1.md')
    a=p.parse_args(); root=Path(a.repo_root).resolve(); glossary=read_text(root / a.glossary); terms=TERM_RE.findall(glossary); corpus='\n'.join(read_text(path) for path in iter_files(root, extensions={'.md'}) if path.relative_to(root).as_posix()!=a.glossary)
    missing=[term for term in terms if term not in corpus]
    print(json.dumps({'terms_total':len(terms),'unlinked_terms':missing}, indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
