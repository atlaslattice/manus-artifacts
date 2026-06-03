#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Run validators scoped to changed files."""
from __future__ import annotations
import argparse, json, subprocess

def pick_validators(changed: list[str]) -> list[str]:
    validators={'scripts/validate_markdown_links.py'}
    if any(path.startswith('.github/workflows/') for path in changed): validators.add('scripts/validate_supply_chain_workflow.py')
    if any('gptdream' in path or 'atlas_orcs' in path for path in changed): validators.add('scripts/detect_gptdream_protocol_drift.py')
    return sorted(validators)

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('changed_files', nargs='*')
    a=p.parse_args(); validators=pick_validators(a.changed_files); rows=[]; rc=0
    for script in validators:
        result=subprocess.run(['python3', script], capture_output=True, text=True, check=False)
        rows.append({'script':script,'returncode':result.returncode}); rc=max(rc, result.returncode)
    print(json.dumps({'validators':validators,'rows':rows}, indent=2)); return rc
if __name__=='__main__': raise SystemExit(main())
