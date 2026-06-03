#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Run validators repeatedly and flag unstable outputs."""
from __future__ import annotations
import argparse, hashlib, json, subprocess

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('scripts', nargs='+')
    a=p.parse_args(); rows=[]
    for script in a.scripts:
        digests=[]
        for _ in range(3):
            result=subprocess.run(['python3', script], capture_output=True, text=True, check=False)
            digests.append(hashlib.sha256((result.stdout+result.stderr).encode()).hexdigest())
        rows.append({'script':script,'stable':len(set(digests))==1})
    print(json.dumps({'rows':rows}, indent=2)); return 1 if any(not row['stable'] for row in rows) else 0
if __name__=='__main__': raise SystemExit(main())
