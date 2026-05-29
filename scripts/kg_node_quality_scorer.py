#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_JSON = ROOT / "docs" / "generated" / "LATTICE_GLOBAL_INDEX.json"
OUTPUT = ROOT / "docs" / "generated" / "KG_NODE_QUALITY_SCORES.json"


def score(node: dict[str, object]) -> dict[str, object]:
    checks = {
        "has_id": bool(node.get("id")),
        "has_type": bool(node.get("type")),
        "has_path": bool(node.get("path")),
        "path_exists": bool(node.get("exists")),
        "has_links": bool(node.get("links")),
    }
    passed = sum(1 for ok in checks.values() if ok)
    total = len(checks)
    pct = round((passed / total) * 100, 1)
    return {
        "id": node.get("id"),
        "score": pct,
        "checks": checks,
    }


def main() -> int:
    data = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    scores = [score(node) for node in data.get("nodes", [])]
    avg = round(sum(item["score"] for item in scores) / max(len(scores), 1), 2)
    payload = {
        "status": "Candidate",
        "average_score": avg,
        "node_scores": scores,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
