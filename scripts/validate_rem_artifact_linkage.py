#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate dream journal, wake report, and delta extraction triplets."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
LABEL_RE=re.compile(r'(100Y_[A-Z0-9_]+_\d{4}-\d{2}-\d{2}|100Y_[A-Z0-9_]+)')

def extract_key(name: str) -> str:
    stem=Path(name).stem.replace('WAKE_REPORT_','').replace('DREAM_JOURNAL_','').replace('DELTA_EXTRACTION_','')
    return stem

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--root',default='archive/boot/copilotbrain/TIDELOCKBrain')
    a=p.parse_args(); root=Path(a.root); groups={}
    for prefix in ['WAKE_REPORT','DREAM_JOURNAL','DELTA_EXTRACTION']:
        for path in root.glob(f'{prefix}_*.md'):
            groups.setdefault(extract_key(path.name), set()).add(prefix)
    rows=[{'cycle':key,'missing':sorted({'WAKE_REPORT','DREAM_JOURNAL','DELTA_EXTRACTION'} - value)} for key,value in sorted(groups.items())]
    print(json.dumps({'rows':rows}, indent=2)); return 1 if any(row['missing'] for row in rows) else 0
if __name__=='__main__': raise SystemExit(main())
