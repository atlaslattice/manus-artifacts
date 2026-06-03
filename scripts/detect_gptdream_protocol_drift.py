#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Detect protocol drift between schema versions and manifest/spec expectations."""
from __future__ import annotations
import argparse, json, re, yaml
from pathlib import Path

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--manifest',default='archive/boot/gptbrain/GPTBRAIN_MANIFEST_2026-05-09.md'); p.add_argument('--schema-dir',default='schemas/atlas_orcs/v0_1')
    a=p.parse_args(); manifest=Path(a.manifest).read_text(encoding='utf-8'); expected='0.1'; rows=[]
    for path in Path(a.schema_dir).glob('*.yaml'):
        data=yaml.safe_load(path.read_text(encoding='utf-8')); observed=str(data.get('properties',{}).get('schema_version',{}).get('const',''))
        if observed != expected: rows.append({'path':path.as_posix(),'expected':expected,'observed':observed})
    manifest_refs=len(re.findall(r'SCHEMA', manifest))
    print(json.dumps({'rows':rows,'manifest_schema_mentions':manifest_refs}, indent=2)); return 1 if rows else 0
if __name__=='__main__': raise SystemExit(main())
