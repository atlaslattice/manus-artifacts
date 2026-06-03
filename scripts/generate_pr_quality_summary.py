#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Generate a markdown quality summary from validator outputs."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('reports', nargs='*')
    a=p.parse_args(); lines=['## PR Quality Summary','']
    for report in a.reports:
        payload=json.loads(Path(report).read_text(encoding='utf-8'))
        lines.append(f"- **{Path(report).name}**: {payload}")
    print('\n'.join(lines)); return 0
if __name__=='__main__': raise SystemExit(main())
