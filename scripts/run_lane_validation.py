#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Run validators relevant to a specific lane."""
from __future__ import annotations
import argparse, json, subprocess
LANE_MAP={'archive':['scripts/validate_markdown_links.py'],'docs':['scripts/validate_markdown_links.py'],'scripts':['scripts/validate_supply_chain_workflow.py'],'tests':['scripts/validate_supply_chain_workflow.py'],'specs':['scripts/detect_gptdream_protocol_drift.py']}

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--lane',required=True)
    a=p.parse_args(); commands=LANE_MAP.get(a.lane, ['scripts/validate_markdown_links.py']); rows=[]; rc=0
    for script in commands:
        result=subprocess.run(['python3', script], capture_output=True, text=True, check=False)
        rows.append({'script':script,'returncode':result.returncode})
        rc=max(rc, result.returncode)
    print(json.dumps({'lane':a.lane,'rows':rows}, indent=2)); return rc
if __name__=='__main__': raise SystemExit(main())
