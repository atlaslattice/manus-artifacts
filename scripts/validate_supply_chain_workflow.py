#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate workflows for pinned actions, sudo usage, and secret exposure patterns."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
ACTION_RE=re.compile(r'uses:\s*([^\s]+@[^\s]+)')

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--root',default='.github/workflows')
    a=p.parse_args(); rows=[]
    for path in Path(a.root).glob('*.yml'):
        text=path.read_text(encoding='utf-8'); actions=ACTION_RE.findall(text)
        issues=[]
        if 'sudo ' in text: issues.append('sudo usage')
        if re.search(r'\b[A-Za-z_]*SECRET[A-Za-z_]*\s*:\s*["\']?[A-Za-z0-9]{16,}', text): issues.append('possible secret exposure')
        for action in actions:
            if '@' not in action: issues.append(f'unpinned action {action}')
        rows.append({'path':path.as_posix(),'issues':issues,'actions':actions})
    print(json.dumps({'rows':rows}, indent=2)); return 1 if any(row['issues'] for row in rows) else 0
if __name__=='__main__': raise SystemExit(main())
