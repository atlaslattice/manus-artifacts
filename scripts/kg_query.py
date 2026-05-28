from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.build_lattice_global_index import load_graph_data


def _matches_query(payload: dict, query: str) -> bool:
    haystack = json.dumps(payload, sort_keys=True).lower()
    return all(term in haystack for term in query.lower().split())


def run_query(query: str, seat: str | None = None, domain: str | None = None, root: Path = ROOT) -> list[dict]:
    graph = load_graph_data(root)
    results: list[dict] = []
    for node in graph.nodes:
        payload = {"record_family": "node", **node}
        if _matches_query(payload, query):
            results.append(payload)
    for edge in graph.edges:
        payload = {"record_family": "edge", **edge}
        if _matches_query(payload, query):
            results.append(payload)
    for route in graph.routes:
        payload = {"record_family": "route", **route}
        if seat and route.get("seat") != seat:
            continue
        if domain and route.get("domain") != domain:
            continue
        if _matches_query(payload, query):
            results.append(payload)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Query the lattice knowledge graph seed data.")
    parser.add_argument("query", help="Search text for nodes, edges, and routes.")
    parser.add_argument("--seat", help="Filter ORCS routes by seat.")
    parser.add_argument("--domain", help="Filter ORCS routes by domain.")
    args = parser.parse_args()

    results = run_query(args.query, seat=args.seat, domain=args.domain, root=ROOT)
    for result in results:
        print(json.dumps(result, sort_keys=True))
    print(f"results={len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
