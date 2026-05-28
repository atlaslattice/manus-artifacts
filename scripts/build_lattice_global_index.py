#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NODE_INDEX = ROOT / "docs" / "LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md"
OUTPUT = ROOT / "docs" / "generated" / "LATTICE_GLOBAL_INDEX.json"
ROW_RE = re.compile(r"^\|\s*(N-[^|]+?)\s*\|\s*([^|]+?)\s*\|\s*\[(.*?)\]\((.*?)\)\s*\|\s*(.*?)\s*\|$")


def parse_nodes() -> list[dict[str, object]]:
    nodes: list[dict[str, object]] = []
    for line in NODE_INDEX.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        node_id, node_type, title, rel_path, links_raw = m.groups()
        links = [part.strip() for part in links_raw.split(",") if part.strip()]
        node_path = (NODE_INDEX.parent / rel_path).resolve()
        nodes.append(
            {
                "id": node_id.strip(),
                "type": node_type.strip(),
                "title": title.strip(),
                "path": rel_path.strip(),
                "exists": node_path.exists(),
                "links": links,
            }
        )
    return nodes


def main() -> int:
    if not NODE_INDEX.exists():
        print(f"missing node index: {NODE_INDEX}")
        return 1

    nodes = parse_nodes()
    node_ids = {node["id"] for node in nodes}
    edge_count = sum(len(node["links"]) for node in nodes)
    orphan_nodes = [node["id"] for node in nodes if not node["links"]]
    unknown_links = sorted(
        {
            link
            for node in nodes
            for link in node["links"]
            if link not in node_ids
        }
    )

    payload = {
        "status": "Candidate",
        "source": str(NODE_INDEX.relative_to(ROOT)),
        "metrics": {
            "node_count": len(nodes),
            "edge_count": edge_count,
            "edge_density": round(edge_count / max(len(nodes), 1), 3),
            "orphan_node_count": len(orphan_nodes),
            "unknown_link_count": len(unknown_links),
        },
        "orphan_nodes": orphan_nodes,
        "unknown_links": unknown_links,
        "nodes": nodes,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
