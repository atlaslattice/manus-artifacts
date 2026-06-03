#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate TIDELOCK wake reports against the template sections."""
from __future__ import annotations
import argparse, json
from pathlib import Path
REQUIRED=['One-line wake summary','Convergences','Novel images','Implementation candidates','Contradictions found','Risks / overclaim hazards','Source lineage / receipts','Public-safe translation notes','Human-root decisions requested','Recommended next action']

def validate_report(text: str) -> list[str]:
    return [section for section in REQUIRED if section not in text]

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--root',default='archive/boot/copilotbrain/TIDELOCKBrain')
    a=p.parse_args(); root=Path(a.root); rows=[]
    for path in root.glob('WAKE_REPORT*.md'):
        missing=validate_report(path.read_text(encoding='utf-8'))
        rows.append({'path':path.as_posix(),'missing_sections':missing})
    print(json.dumps({'rows':rows}, indent=2)); return 1 if any(row['missing_sections'] for row in rows) else 0
if __name__=='__main__': raise SystemExit(main())
