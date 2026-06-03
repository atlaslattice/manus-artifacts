#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate that delta artifacts reference dream journals."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--root',default='archive/boot/copilotbrain/TIDELOCKBrain')
    a=p.parse_args(); root=Path(a.root); rows=[]
    for path in root.glob('DELTA_EXTRACTION_*.md'):
        text=path.read_text(encoding='utf-8'); rows.append({'path':path.as_posix(),'references_dream':('DREAM_JOURNAL' in text)})
    print(json.dumps({'rows':rows}, indent=2)); return 1 if any(not row['references_dream'] for row in rows) else 0
if __name__=='__main__': raise SystemExit(main())
