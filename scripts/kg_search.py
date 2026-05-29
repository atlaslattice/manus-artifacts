from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.build_lattice_global_index import load_graph_data

TOKEN_RE = re.compile(r"[a-z0-9]+")
HOUSE_REGISTRY_PATH = ROOT / "archive/knowledge_graph/HOUSE_SEED_REGISTRY.json"


def _tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def _load_documents() -> list[dict[str, Any]]:
    graph = load_graph_data(ROOT)
    documents = []
    for record_family, records in (("node", graph.nodes), ("edge", graph.edges), ("route", graph.routes)):
        for record in records:
            payload = {"record_family": record_family, **record}
            payload_text = json.dumps(payload, sort_keys=True)
            documents.append({"payload": payload, "text": payload_text})
    if HOUSE_REGISTRY_PATH.exists():
        houses = json.loads(HOUSE_REGISTRY_PATH.read_text(encoding="utf-8")).get("houses", [])
        for house in houses:
            payload = {"record_family": "house_seed", **house}
            documents.append({"payload": payload, "text": json.dumps(payload, sort_keys=True)})
    return documents


def ranked_search(query: str, limit: int = 10) -> list[dict[str, Any]]:
    query_terms = _tokenize(query)
    if not query_terms:
        return []
    docs = _load_documents()
    if not docs:
        return []

    tokenized_docs = [_tokenize(doc["text"]) for doc in docs]
    doc_freq = Counter()
    for terms in tokenized_docs:
        doc_freq.update(set(terms))

    total_docs = len(docs)
    scored: list[tuple[float, dict[str, Any]]] = []
    for doc, terms in zip(docs, tokenized_docs):
        term_counts = Counter(terms)
        if not any(term in term_counts for term in query_terms):
            continue
        score = 0.0
        for term in query_terms:
            tf = term_counts[term]
            if tf == 0:
                continue
            idf = math.log((1 + total_docs) / (1 + doc_freq[term])) + 1.0
            score += tf * idf
        scored.append((score, doc["payload"]))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [{"score": round(score, 6), "result": payload} for score, payload in scored[:limit]]


def main() -> int:
    parser = argparse.ArgumentParser(description="Ranked semantic-ish search over lattice seed graph.")
    parser.add_argument("query", help="Search query text.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum result count.")
    args = parser.parse_args()

    results = ranked_search(args.query, limit=args.limit)
    for item in results:
        print(json.dumps(item, sort_keys=True))
    print(f"results={len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
