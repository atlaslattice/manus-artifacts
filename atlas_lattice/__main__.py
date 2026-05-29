"""CLI entry point: python -m atlas_lattice <command> [args]"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from .coordinate import (
    Coordinate,
    HOUSE_NAMES,
    SPHERE_NAMES,
    NODE_NAMES,
)


def _cmd_lookup(args: list[str]) -> None:
    if not args:
        print("Usage: python -m atlas_lattice lookup <H##-S##-N##>", file=sys.stderr)
        sys.exit(1)
    try:
        coord = Coordinate.parse(args[0])
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    print(coord)
    print(json.dumps(coord.to_dict(), indent=2))


def _cmd_axes(_args: list[str]) -> None:
    print("=== H-S-N Axes (12×12×12 Atlas Lattice) ===\n")
    print("── Houses (H) ──")
    for i, name in enumerate(HOUSE_NAMES, 1):
        print(f"  H{i:02d}  {name}")
    print("\n── Spheres (S) ──")
    for i, name in enumerate(SPHERE_NAMES, 1):
        print(f"  S{i:02d}  {name}")
    print("\n── Nodes (N) ──")
    for i, name in enumerate(NODE_NAMES, 1):
        print(f"  N{i:02d}  {name}")


def _cmd_explorer(_args: list[str]) -> None:
    explorer = Path(__file__).parent.parent / "docs" / "graph-explorer.html"
    if explorer.exists():
        import webbrowser
        webbrowser.open(explorer.resolve().as_uri())
        print(f"Opened: {explorer}")
    else:
        print(f"Graph explorer not found at: {explorer}", file=sys.stderr)
        sys.exit(1)


COMMANDS = {
    "lookup": _cmd_lookup,
    "axes": _cmd_axes,
    "explorer": _cmd_explorer,
}


def main() -> None:
    argv = sys.argv[1:]
    if not argv or argv[0] in ("-h", "--help"):
        print("atlas-lattice CLI\n")
        print("Commands:")
        print("  lookup <H##-S##-N##>   Look up a coordinate")
        print("  axes                   Print all H-S-N axis labels")
        print("  explorer               Open the graph explorer in a browser")
        return
    cmd, *rest = argv
    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd!r}. Try --help.", file=sys.stderr)
        sys.exit(1)
    COMMANDS[cmd](rest)


if __name__ == "__main__":
    main()
