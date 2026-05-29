#!/usr/bin/env python3
"""
aetherforge.py
==============
The Atlas Lattice Aetherforge — playable CLI interface for the knowledge graph.

The Aetherforge is the game layer for the lattice. Contributors can:
  - Navigate the 12×12×12 H-S-N hypercube
  - Claim empty cells by submitting artifact proposals
  - View what's at each coordinate
  - Track their score (review-gate completions)
  - Run quests tied to the archive

Usage:
    python aetherforge.py             # interactive mode
    python aetherforge.py explore     # show current position and adjacent cells
    python aetherforge.py move H01 S04 N07   # move to a specific cell
    python aetherforge.py look H01-S04-N07   # inspect a cell
    python aetherforge.py claim H05-S03-N01  # claim an empty cell
    python aetherforge.py score              # show your score
    python aetherforge.py quests             # show available quests
    python aetherforge.py map H01            # show House 01 heatmap
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from textwrap import dedent
from typing import Any

ROOT = Path(__file__).resolve().parent
GRAPH_FILE = ROOT / "docs" / "lattice_graph_nodes.json"
PLAYER_STATE_FILE = ROOT / ".aetherforge_player.json"

HOUSE_LABELS = {
    1: "Elements & Isotopes",
    2: "Frequency & Resonance",
    3: "Color & Harmonic Spectrum",
    4: "Acoustic Resonance",
    5: "States of Matter",
    6: "Spin & Quantum States",
    7: "Neuromorphic Principles",
    8: "Human Knowledge Domains",
    9: "Archive Artifacts",
    10: "IP Lineage",
    11: "Review & Governance States",
    12: "Synthesis & Meta",
}

REVIEW_COLORS = {
    "raw":        "🔴",
    "candidate":  "🟡",
    "reviewed":   "🔵",
    "canon-gate": "🟣",
    "canon":      "🟢",
    "archived":   "⬛",
}

QUESTS = [
    {
        "id": "Q01",
        "title": "Periodic Pilgrim",
        "desc": "Visit all 7 periods of the elements (H01-S01 through H01-S07).",
        "check": lambda visited: all(f"H01-S{s:02d}" in visited for s in range(1, 8)),
        "reward": 70,
    },
    {
        "id": "Q02",
        "title": "Spectrum Surfer",
        "desc": "Visit all 12 Spheres of the Frequency house (H02).",
        "check": lambda visited: all(f"H02-S{s:02d}" in visited for s in range(1, 13)),
        "reward": 120,
    },
    {
        "id": "Q03",
        "title": "Rainbow Rider",
        "desc": "Visit all 7 visible-spectrum Spheres in Color house (H03-S01 through H03-S07).",
        "check": lambda visited: all(f"H03-S{s:02d}" in visited for s in range(1, 8)),
        "reward": 70,
    },
    {
        "id": "Q04",
        "title": "Archive Archivist",
        "desc": "Visit at least 20 Archive Artifacts cells (House 09).",
        "check": lambda visited: sum(1 for v in visited if v.startswith("H09")) >= 20,
        "reward": 200,
    },
    {
        "id": "Q05",
        "title": "Governance Guardian",
        "desc": "Visit all 12 Spheres of the Governance house (H11).",
        "check": lambda visited: all(f"H11-S{s:02d}" in visited for s in range(1, 13)),
        "reward": 120,
    },
    {
        "id": "Q06",
        "title": "Metatron's Path",
        "desc": "Visit at least 1 cell in every House (H01 through H12).",
        "check": lambda visited: all(any(v.startswith(f"H{h:02d}") for v in visited) for h in range(1, 13)),
        "reward": 300,
    },
    {
        "id": "Q07",
        "title": "Chromatic Scale",
        "desc": "Visit all 12 notes (N01-N12) within any single Acoustic octave (H04).",
        "check": lambda visited: any(
            all(f"H04-S{s:02d}-N{n:02d}" in visited for n in range(1, 13))
            for s in range(1, 9)
        ),
        "reward": 144,
    },
]

# Points per action
POINTS = {
    "visit_new_cell": 5,
    "visit_new_house": 20,
    "claim_empty_cell": 50,
    "complete_quest": "variable",
}


# ─── player state ──────────────────────────────────────────────────────────────

def load_state() -> dict[str, Any]:
    if PLAYER_STATE_FILE.exists():
        try:
            return json.loads(PLAYER_STATE_FILE.read_text())
        except Exception:
            pass
    return {
        "player": os.environ.get("USER", "explorer"),
        "position": "H01-S01-N01",
        "score": 0,
        "cells_visited": [],
        "houses_visited": [],
        "cells_claimed": [],
        "quests_completed": [],
    }


def save_state(state: dict[str, Any]) -> None:
    PLAYER_STATE_FILE.write_text(json.dumps(state, indent=2))


def award(state: dict[str, Any], points: int, reason: str) -> None:
    state["score"] += points
    if points > 0:
        print(f"  ✨ +{points} pts — {reason}")


# ─── graph helpers ─────────────────────────────────────────────────────────────

def load_graph_nodes() -> list[dict[str, Any]]:
    if not GRAPH_FILE.exists():
        return []
    try:
        return json.loads(GRAPH_FILE.read_text())
    except Exception:
        return []


def nodes_at(hsn: str, graph: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [n for n in graph if n.get("hsn") == hsn or n.get("hsn_coordinate") == hsn]


def all_occupied_cells(graph: list[dict[str, Any]]) -> set[str]:
    cells = set()
    for n in graph:
        hsn = n.get("hsn") or n.get("hsn_coordinate", "")
        if hsn:
            cells.add(hsn)
    return cells


# ─── commands ──────────────────────────────────────────────────────────────────

def cmd_look(hsn: str, graph: list[dict[str, Any]]) -> None:
    nodes = nodes_at(hsn, graph)
    h = int(hsn[1:3])
    house_label = HOUSE_LABELS.get(h, "Unknown")
    print(f"\n📍 Cell: {hsn}  —  {house_label}\n")
    if not nodes:
        print("  (empty — no artifacts indexed here yet)")
        print(f"  💡 Claim it with: python aetherforge.py claim {hsn}")
    else:
        for nd in nodes:
            icon = REVIEW_COLORS.get(nd.get("review_state", ""), "⚪")
            print(f"  {icon} [{nd.get('type','?')}] {nd.get('id','?')}")
            print(f"     {nd.get('label','')}")
            print(f"     status: {nd.get('status','?')}  review: {nd.get('review_state','?')}")
    print()


def cmd_move(h: int, s: int, n: int, state: dict, graph: list) -> None:
    if not (1 <= h <= 12 and 1 <= s <= 12 and 1 <= n <= 12):
        print("ERROR: H, S, N must all be 1–12")
        return

    hsn = f"H{h:02d}-S{s:02d}-N{n:02d}"
    old = state["position"]
    state["position"] = hsn

    old_house = old[:3]
    new_house = hsn[:3]
    h_num = int(new_house[1:])

    print(f"\n🚀 Moved: {old} → {hsn}  ({HOUSE_LABELS.get(h_num,'?')})")

    if hsn not in state["cells_visited"]:
        state["cells_visited"].append(hsn)
        award(state, POINTS["visit_new_cell"], "new cell discovered")

    h_prefix = hsn[:3]
    if h_prefix not in state["houses_visited"]:
        state["houses_visited"].append(h_prefix)
        award(state, POINTS["visit_new_house"], f"first visit to {HOUSE_LABELS.get(h_num,'')}")

    # Track partial visits for quest checks
    visited_set = set(state["cells_visited"])
    visited_prefixes = set(
        c[:7] for c in state["cells_visited"]  # H##-S## prefix
    )
    _check_quests(state, visited_set, visited_prefixes)

    cmd_look(hsn, graph)


def cmd_explore(state: dict, graph: list) -> None:
    pos = state["position"]
    h, s, n = int(pos[1:3]), int(pos[4:6]), int(pos[7:9])
    h_label = HOUSE_LABELS.get(h, "?")

    print(f"\n🌐 Current position: {pos}  —  {h_label}")
    print(f"   Score: {state['score']} pts | Cells visited: {len(state['cells_visited'])} | Houses: {len(state['houses_visited'])}")

    nodes = nodes_at(pos, graph)
    if nodes:
        print(f"\n   At this cell ({len(nodes)} artifact(s)):")
        for nd in nodes[:3]:
            icon = REVIEW_COLORS.get(nd.get("review_state", ""), "⚪")
            print(f"     {icon} {nd.get('id','?')} — {nd.get('label','')[:50]}")

    print(f"\n   Adjacent cells (same House):")
    for ds in [-1, 0, 1]:
        for dn in [-1, 0, 1]:
            if ds == 0 and dn == 0:
                continue
            ns, nn = s + ds, n + dn
            if 1 <= ns <= 12 and 1 <= nn <= 12:
                adj = f"H{h:02d}-S{ns:02d}-N{nn:02d}"
                count = len(nodes_at(adj, graph))
                mark = "●" if count > 0 else "○"
                print(f"     {mark} {adj} ({count} artifacts)")

    print()


def cmd_claim(hsn: str, state: dict, graph: list) -> None:
    occupied = all_occupied_cells(graph)
    if hsn in occupied:
        nodes = nodes_at(hsn, graph)
        print(f"\n⚠  Cell {hsn} already has {len(nodes)} artifact(s). It is not empty.")
        print("   You can still submit artifacts here — cells are addresses, not exclusive.")
    else:
        print(f"\n🏴 Cell {hsn} is empty! Claiming it…")

    if hsn not in state["cells_claimed"]:
        state["cells_claimed"].append(hsn)
        award(state, POINTS["claim_empty_cell"], f"claimed {hsn}")
        print(f"\n   To submit an artifact here:")
        print(f"   1. Create a Markdown file with hsn_coordinate: {hsn} in its frontmatter")
        print(f"   2. Open a GitHub issue using the Artifact Proposal template")
        print(f"   3. PR it through the review gate\n")
    else:
        print(f"\n   (already claimed by you)")
    print()


def cmd_score(state: dict) -> None:
    print(f"\n🏆 Aetherforge Score Card — {state['player']}")
    print(f"   Score:          {state['score']} pts")
    print(f"   Cells visited:  {len(state['cells_visited'])}")
    print(f"   Houses visited: {len(state['houses_visited'])} / 12")
    print(f"   Cells claimed:  {len(state['cells_claimed'])}")
    print(f"   Quests done:    {len(state['quests_completed'])} / {len(QUESTS)}")
    print()


def cmd_quests(state: dict, graph: list) -> None:
    visited_set = set(state["cells_visited"])
    print(f"\n⚔  Aetherforge Quests\n")
    for q in QUESTS:
        done = q["id"] in state["quests_completed"]
        status = "✅" if done else ("🔒" if not q["check"](visited_set) else "🔓")
        pts = q["reward"]
        print(f"  {status} [{q['id']}] {q['title']} (+{pts} pts)")
        print(f"     {q['desc']}")
    print()


def cmd_map(house: int, graph: list) -> None:
    print(f"\n🗺  House H{house:02d} — {HOUSE_LABELS.get(house, '?')}\n")
    occupied = {}
    for nd in graph:
        hsn = nd.get("hsn") or nd.get("hsn_coordinate", "")
        if hsn and hsn.startswith(f"H{house:02d}"):
            occupied[hsn] = occupied.get(hsn, 0) + 1

    print("    " + "  ".join(f"N{n:02d}" for n in range(1, 13)))
    for s in range(1, 13):
        row = f"S{s:02d} "
        for n in range(1, 13):
            hsn = f"H{house:02d}-S{s:02d}-N{n:02d}"
            count = occupied.get(hsn, 0)
            if count == 0:
                row += "  ·  "
            elif count < 10:
                row += f"  {count}  "
            else:
                row += f" {count:2d}  "
        print(row)
    print()
    total = sum(occupied.values())
    print(f"  Total artifacts in H{house:02d}: {total}")
    print(f"  Occupied cells: {len(occupied)} / 144\n")


def _check_quests(state: dict, visited_set: set, visited_prefixes: set) -> None:
    for q in QUESTS:
        if q["id"] not in state["quests_completed"]:
            if q["check"](visited_set):
                state["quests_completed"].append(q["id"])
                award(state, q["reward"], f"Quest complete: {q['title']}")
                print(f"\n🎉 Quest Complete: {q['title']}!")


def cmd_interactive(state: dict, graph: list) -> None:
    print("\n" + "═" * 60)
    print("  ✨ AETHERFORGE — Atlas Lattice Explorer ✨")
    print("═" * 60)
    print(f"  Welcome, {state['player']}!")
    print("  Navigate the 12×12×12 H-S-N hypercube.")
    print("  Type 'help' for commands, 'quit' to exit.\n")

    commands = {
        "help":    "Show this help",
        "look":    "Look at current cell",
        "explore": "Show position + adjacent cells",
        "move H S N": "Move to H(ouse) S(phere) N(ode)",
        "claim HSN":  "Claim an empty cell (e.g. claim H05-S03-N01)",
        "score":   "Show your score",
        "quests":  "Show available quests",
        "map H":   "Show House heatmap (e.g. map 1)",
        "list-houses": "List all 12 Houses",
        "quit":    "Exit Aetherforge",
    }

    while True:
        pos = state["position"]
        h = int(pos[1:3])
        try:
            raw = input(f"\n[{pos} | {state['score']}pts] > ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not raw:
            continue
        parts = raw.lower().split()
        cmd = parts[0]

        if cmd in ("quit", "exit", "q"):
            break
        elif cmd == "help":
            print("\nCommands:")
            for c, desc in commands.items():
                print(f"  {c:<20} — {desc}")
        elif cmd == "look":
            cmd_look(pos, graph)
        elif cmd == "explore":
            cmd_explore(state, graph)
        elif cmd == "score":
            cmd_score(state)
        elif cmd == "quests":
            cmd_quests(state, graph)
        elif cmd == "list-houses":
            for hk, hl in HOUSE_LABELS.items():
                print(f"  H{hk:02d}  {hl}")
        elif cmd == "move":
            try:
                hv, sv, nv = int(parts[1]), int(parts[2]), int(parts[3])
                cmd_move(hv, sv, nv, state, graph)
            except (IndexError, ValueError):
                print("Usage: move <H> <S> <N>  (e.g. move 1 4 7)")
        elif cmd == "claim":
            hsn = parts[1].upper() if len(parts) > 1 else ""
            if not hsn:
                print("Usage: claim H##-S##-N##")
            else:
                cmd_claim(hsn, state, graph)
        elif cmd == "map":
            try:
                hv = int(parts[1])
                cmd_map(hv, graph)
            except (IndexError, ValueError):
                print("Usage: map <house_number>  (e.g. map 1)")
        else:
            print(f"Unknown command '{cmd}'. Type 'help'.")

    save_state(state)
    print(f"\nScore saved. Goodbye, {state['player']}! 🌟\n")


# ─── main ──────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Aetherforge — Atlas Lattice playable CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=dedent("""\
        Examples:
          python aetherforge.py               # interactive mode
          python aetherforge.py explore
          python aetherforge.py move 1 4 7
          python aetherforge.py look H01-S04-N07
          python aetherforge.py claim H05-S03-N01
          python aetherforge.py map 1
          python aetherforge.py score
          python aetherforge.py quests
        """),
    )
    parser.add_argument("command", nargs="?", default="interactive",
                        choices=["explore", "move", "look", "claim", "score",
                                 "quests", "map", "interactive", "list-houses"],
                        help="Command to run (default: interactive)")
    parser.add_argument("args", nargs="*", help="Command arguments")
    args = parser.parse_args(argv)

    state = load_state()
    graph = load_graph_nodes()

    if not graph:
        print("⚠  Graph not loaded. Run: python scripts/build_lattice_graph.py")
        print("   Continuing in empty-graph mode.\n")

    cmd = args.command
    rest = args.args

    if cmd == "interactive":
        cmd_interactive(state, graph)
    elif cmd == "explore":
        cmd_explore(state, graph)
    elif cmd == "move":
        try:
            hv, sv, nv = int(rest[0]), int(rest[1]), int(rest[2])
        except (IndexError, ValueError):
            print("Usage: python aetherforge.py move <H> <S> <N>")
            return 1
        cmd_move(hv, sv, nv, state, graph)
    elif cmd == "look":
        hsn = rest[0].upper() if rest else state["position"]
        cmd_look(hsn, graph)
    elif cmd == "claim":
        hsn = rest[0].upper() if rest else ""
        if not hsn:
            print("Usage: python aetherforge.py claim H##-S##-N##")
            return 1
        cmd_claim(hsn, state, graph)
    elif cmd == "score":
        cmd_score(state)
    elif cmd == "quests":
        cmd_quests(state, graph)
    elif cmd == "map":
        try:
            hv = int(rest[0])
        except (IndexError, ValueError):
            print("Usage: python aetherforge.py map <house_number>")
            return 1
        cmd_map(hv, graph)
    elif cmd == "list-houses":
        for hk, hl in HOUSE_LABELS.items():
            print(f"  H{hk:02d}  {hl}")

    save_state(state)
    return 0


if __name__ == "__main__":
    sys.exit(main())
