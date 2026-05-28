from __future__ import annotations

import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
GRAPH_SEED_PATH = ROOT / "archive/knowledge_graph/GRAPH_SEED.jsonl"
ORCS_ROUTE_PATH = ROOT / "archive/knowledge_graph/ORCS_ROUTE_INDEX.seed.jsonl"
GRAPH_INDEX_PATH = ROOT / "archive/knowledge_graph/GRAPH_INDEX.md"


@dataclass(frozen=True)
class GraphData:
    nodes: list[dict]
    edges: list[dict]
    routes: list[dict]


def load_jsonl(path: Path) -> list[dict]:
    records = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL in {path} line {line_no}: {exc}") from exc
    return records


def load_graph_data(root: Path = ROOT) -> GraphData:
    graph_seed = root / "archive/knowledge_graph/GRAPH_SEED.jsonl"
    orcs_route = root / "archive/knowledge_graph/ORCS_ROUTE_INDEX.seed.jsonl"
    records = load_jsonl(graph_seed)
    nodes = [record for record in records if record.get("record_type") == "node"]
    edges = [record for record in records if record.get("record_type") == "edge"]
    routes = load_jsonl(orcs_route)
    return GraphData(nodes=nodes, edges=edges, routes=routes)


def _normalize_path(path_text: str, root: Path) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path
    return root / path


def render_graph_index(graph: GraphData) -> str:
    kind_counts = Counter(node.get("kind", "unknown") for node in graph.nodes)
    relation_counts = Counter(edge.get("relation", "unknown") for edge in graph.edges)
    route_domains: dict[str, list[dict]] = defaultdict(list)
    for route in graph.routes:
        route_domains[route.get("domain", "unknown")].append(route)

    lines = [
        "# Metatron Awakening — Repo Graph Index",
        "",
        "```text",
        "STATUS: GRAPH INDEX — NOT CANON",
        "DATE: 2026-05-28",
        "CANON STATUS: candidate",
        "AUTHORITY: generated navigation and linkage index",
        "PURPOSE: provide a repo-wide node map for governance, specs, code, tests, workflows, and project lanes",
        "SOURCE: scripts/build_lattice_global_index.py",
        "```",
        "",
        "## Graph summary",
        "",
        f"- Nodes: **{len(graph.nodes)}**",
        f"- Edges: **{len(graph.edges)}**",
        f"- ORCS routes: **{len(graph.routes)}**",
        "",
        "## Node kinds",
        "",
    ]
    for kind, count in sorted(kind_counts.items()):
        lines.append(f"- `{kind}` — {count}")

    lines.extend(["", "## Edge relations", ""])
    for relation, count in sorted(relation_counts.items()):
        lines.append(f"- `{relation}` — {count}")

    lines.extend(["", "## Seed nodes", ""])
    for node in sorted(graph.nodes, key=lambda item: item.get("node_id", "")):
        lines.append(
            f"- `{node.get('node_id')}` · **{node.get('label', 'unlabeled')}** "
            f"({node.get('kind', 'unknown')}) → `{node.get('path', '')}`"
        )

    lines.extend(["", "## ORCS route domains", ""])
    for domain, routes in sorted(route_domains.items()):
        lines.append(f"### {domain}")
        lines.append("")
        for route in sorted(routes, key=lambda item: item.get("route_id", "")):
            lines.append(
                f"- `{route.get('route_id')}` · `{route.get('route_class')}` · "
                f"`{route.get('source_path')}` → `{route.get('target_surface')}` · seat `{route.get('seat')}`"
            )
        lines.append("")

    lines.extend(["## Integrity notes", ""])
    lines.append("- Graph seed paths should resolve within the repository root.")
    lines.append("- Edge records should only reference existing `node_id` values.")
    lines.append("- ORCS routes should target concrete repo surfaces and carry a seat assignment.")
    lines.append("")
    return "\n".join(lines)


def build_graph_index(root: Path = ROOT) -> str:
    graph = load_graph_data(root)
    content = render_graph_index(graph)
    output = root / "archive/knowledge_graph/GRAPH_INDEX.md"
    output.write_text(content, encoding="utf-8")
    return content


def main() -> int:
    build_graph_index(ROOT)
    print(f"graph-index-built: {GRAPH_INDEX_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
