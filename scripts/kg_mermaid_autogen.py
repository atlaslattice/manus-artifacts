#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_JSON = ROOT / "docs" / "generated" / "LATTICE_GLOBAL_INDEX.json"
OUTPUT_MERMAID = ROOT / "docs" / "generated" / "KG_MERMAID_GRAPH.md"


def label(node_id: str) -> str:
    return node_id.removeprefix("N-")


def node_key(node_id: str) -> str:
    return node_id.replace("-", "_")


def main() -> int:
    if not INDEX_JSON.exists():
        raise SystemExit("missing docs/generated/LATTICE_GLOBAL_INDEX.json; run build_lattice_global_index.py first")

    data = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    nodes = data.get("nodes", [])

    lines = ["```mermaid", "graph TD"]
    for node in nodes:
        node_id = node["id"]
        lines.append(f"    {node_key(node_id)}[{label(node_id)}]")

    for node in nodes:
        node_id = node["id"]
        for linked in node.get("links", []):
            lines.append(f"    {node_key(node_id)} --> {node_key(linked)}")

    lines.append("```")
    OUTPUT_MERMAID.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MERMAID.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT_MERMAID.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
