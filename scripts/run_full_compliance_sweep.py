#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Run a full compliance sweep and aggregate a 0-144 score."""
from __future__ import annotations
import argparse, json, subprocess
VALIDATORS=[
    'scripts/validate_markdown_links.py',
    'scripts/validate_edge_directions.py',
    'scripts/validate_supersedes_chain.py',
    'scripts/validate_contradiction_pairs.py',
    'scripts/validate_no_self_promotion.py',
    'scripts/validate_trust_state.py',
    'scripts/validate_deployment_state.py',
    'scripts/validate_supply_chain_workflow.py',
]

def is_success(result): return result.returncode == 0

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--score-max',type=int,default=144)
    a=p.parse_args(); rows=[]; passed=0
    for script in VALIDATORS:
        result=subprocess.run(['python3', script], capture_output=True, text=True, check=False)
        ok=is_success(result); passed += 1 if ok else 0; rows.append({'script':script,'passed':ok,'returncode':result.returncode})
    score=round(a.score_max * passed / len(VALIDATORS))
    print(json.dumps({'score':score,'score_max':a.score_max,'rows':rows}, indent=2)); return 0 if passed==len(VALIDATORS) else 1
if __name__=='__main__': raise SystemExit(main())
