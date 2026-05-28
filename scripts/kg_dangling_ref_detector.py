#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_JSON = ROOT / "docs" / "generated" / "LATTICE_GLOBAL_INDEX.json"


def main() -> int:
    data = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    missing = [node for node in data.get("nodes", []) if not node.get("exists")]
    if missing:
        print("dangling references detected:")
        for node in missing:
            print(f"- {node['id']} -> {node['path']}")
        return 1

    print(f"dangling ref detector passed ({len(data.get('nodes', []))} nodes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
