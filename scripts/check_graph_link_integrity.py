#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NODE_INDEX = ROOT / "docs" / "LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md"
ROW_RE = re.compile(r"^\|\s*(N-[^|]+?)\s*\|\s*([^|]+?)\s*\|\s*\[(.*?)\]\((.*?)\)\s*\|\s*(.*?)\s*\|$")


def parse_nodes() -> dict[str, dict[str, object]]:
    nodes: dict[str, dict[str, object]] = {}
    for line in NODE_INDEX.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        node_id, node_type, title, rel_path, links_raw = m.groups()
        links = [part.strip() for part in links_raw.split(",") if part.strip()]
        nodes[node_id] = {
            "type": node_type.strip(),
            "title": title.strip(),
            "path": rel_path.strip(),
            "links": links,
        }
    return nodes


def resolve(path: str) -> Path:
    return (NODE_INDEX.parent / path).resolve()


def main() -> int:
    if not NODE_INDEX.exists():
        print(f"missing node index: {NODE_INDEX}")
        return 1

    nodes = parse_nodes()
    if not nodes:
        print("no nodes parsed from index")
        return 1

    errors: list[str] = []
    for node_id, node in nodes.items():
        target = resolve(str(node["path"]))
        if not target.exists():
            errors.append(f"{node_id}: missing path {node['path']}")
        for linked in node["links"]:
            if linked not in nodes:
                errors.append(f"{node_id}: unknown link target {linked}")

    if errors:
        print("graph link integrity failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    edge_count = sum(len(node["links"]) for node in nodes.values())
    print(f"graph link integrity passed ({len(nodes)} nodes, {edge_count} edges)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
