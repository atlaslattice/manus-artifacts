#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_JSON = ROOT / "docs" / "generated" / "LATTICE_GLOBAL_INDEX.json"


def main() -> int:
    data = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    links = {n["id"]: set(n.get("links", [])) for n in data.get("nodes", [])}

    missing: list[tuple[str, str]] = []
    for src, dests in links.items():
        for dest in dests:
            if dest in links and src not in links[dest]:
                missing.append((src, dest))

    if missing:
        print("bidirectional audit found non-reciprocal edges:")
        for src, dest in missing:
            print(f"- {src} -> {dest} missing reciprocal {dest} -> {src}")
        return 1

    print(f"bidirectional audit passed ({len(links)} nodes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
