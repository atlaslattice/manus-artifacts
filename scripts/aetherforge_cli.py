from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.kg_query import run_query

QUESTS = {
    "resonance_hunt": "acoustic resonance",
    "governance_route": "route candidate trust_state",
    "archive_bowl": "artifact provenance review",
}


def play(quest: str, seed: int = 1728) -> dict:
    if quest not in QUESTS:
        raise ValueError(f"unknown quest: {quest}")
    query = QUESTS[quest]
    candidates = run_query(query)
    if not candidates:
        return {"quest": quest, "query": query, "status": "no-artifacts-found"}
    rng = random.Random(seed)
    selected = rng.choice(candidates)
    return {
        "quest": quest,
        "query": query,
        "status": "candidate_selected",
        "selected": selected,
        "score": 100 if selected.get("record_family") == "node" else 80,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Minimal Aetherforge gameplay loop over KG records.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    play_parser = subparsers.add_parser("play", help="Play one quest.")
    play_parser.add_argument("quest", choices=sorted(QUESTS.keys()))
    play_parser.add_argument("--seed", type=int, default=1728)

    quest_parser = subparsers.add_parser("quests", help="List quests.")
    quest_parser.add_argument("--json", action="store_true")

    args = parser.parse_args()
    if args.command == "quests":
        if args.json:
            print(json.dumps(QUESTS, indent=2, sort_keys=True))
        else:
            for quest, query in sorted(QUESTS.items()):
                print(f"{quest}: {query}")
        return 0

    result = play(args.quest, seed=args.seed)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
