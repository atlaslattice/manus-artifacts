from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.build_lattice_global_index import load_graph_data


class ValidationError(RuntimeError):
    pass


def _assert_path_exists(path_text: str, root: Path, label: str) -> None:
    path = Path(path_text)
    resolved = path if path.is_absolute() else root / path
    if not resolved.exists():
        raise ValidationError(f"missing-path:{label}:{path_text}")


def validate_graph(root: Path = ROOT) -> None:
    graph = load_graph_data(root)
    if not graph.nodes:
        raise ValidationError("missing-nodes")
    if not graph.edges:
        raise ValidationError("missing-edges")
    node_ids = {node["node_id"] for node in graph.nodes}

    for node in graph.nodes:
        path_text = node.get("path")
        if not path_text:
            raise ValidationError(f"missing-node-path:{node.get('node_id')}")
        _assert_path_exists(path_text, root, node.get("node_id", "unknown-node"))

    for edge in graph.edges:
        if edge.get("from") not in node_ids:
            raise ValidationError(f"unknown-edge-source:{edge.get('edge_id')}")
        if edge.get("to") not in node_ids:
            raise ValidationError(f"unknown-edge-target:{edge.get('edge_id')}")

    for route in graph.routes:
        if not route.get("seat"):
            raise ValidationError(f"missing-route-seat:{route.get('route_id')}")
        _assert_path_exists(route["source_path"], root, route.get("route_id", "route-source"))
        _assert_path_exists(route["target_surface"], root, route.get("route_id", "route-target"))

    graph_index = root / "archive/knowledge_graph/GRAPH_INDEX.md"
    if not graph_index.exists():
        raise ValidationError("missing-graph-index")
    text = graph_index.read_text(encoding="utf-8")
    if "SOURCE: scripts/build_lattice_global_index.py" not in text:
        raise ValidationError("graph-index-not-generated")


def main() -> int:
    validate_graph(ROOT)
    print("lattice-quality-gates-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
