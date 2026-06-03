#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Validate quest lifecycle transitions."""
from __future__ import annotations
import argparse, json, yaml
from pathlib import Path
ALLOWED={('open','active'),('active','complete'),('open','blocked'),('blocked','active')}

def validate_transition_sequence(states: list[str]) -> list[str]:
    return [f'invalid transition: {a}->{b}' for a,b in zip(states, states[1:]) if (a,b) not in ALLOWED]

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--input')
    a=p.parse_args();
    if not a.input: print(json.dumps({'errors':[]}, indent=2)); return 0
    payload=yaml.safe_load(Path(a.input).read_text(encoding='utf-8')); errors=validate_transition_sequence(payload.get('states', [])); print(json.dumps({'errors':errors}, indent=2)); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
