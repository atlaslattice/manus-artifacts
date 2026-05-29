#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NODE_INDEX = ROOT / "docs" / "LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md"
ROW_RE = re.compile(r"^\|\s*(N-[^|]+?)\s*\|")


def parse_front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}

    meta: dict[str, str] = {}
    i = 1
    while i < len(lines):
        line = lines[i].strip()
        if line == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
        i += 1
    return meta


def infer_node_id(path: Path) -> str:
    stem = re.sub(r"[^A-Za-z0-9]+", "-", path.stem).strip("-").upper()
    return f"N-{stem}"


def infer_links(raw: str) -> list[str]:
    if not raw:
        return []
    return [part.strip() for part in raw.split(",") if part.strip()]


def existing_node_ids(text: str) -> set[str]:
    ids: set[str] = set()
    for line in text.splitlines():
        m = ROW_RE.match(line.strip())
        if m:
            ids.add(m.group(1))
    return ids


def main() -> int:
    parser = argparse.ArgumentParser(description="Import markdown files into KG node index")
    parser.add_argument("markdown_paths", nargs="+", help="Markdown files relative to repo root")
    args = parser.parse_args()

    idx_text = NODE_INDEX.read_text(encoding="utf-8")
    ids = existing_node_ids(idx_text)
    additions: list[str] = []

    for rel in args.markdown_paths:
        p = (ROOT / rel).resolve()
        if not p.exists() or p.suffix.lower() != ".md":
            continue
        rel_from_docs = Path("..") / p.relative_to(ROOT)
        text = p.read_text(encoding="utf-8")
        meta = parse_front_matter(text)

        node_id = meta.get("kg_node_id") or infer_node_id(p)
        if node_id in ids:
            continue

        node_type = meta.get("kg_type", "Program")
        links = infer_links(meta.get("kg_links", ""))
        links_str = ", ".join(links) if links else "N-README"

        additions.append(
            f"| {node_id} | {node_type} | [{rel_from_docs.as_posix()}]({rel_from_docs.as_posix()}) | {links_str} |"
        )
        ids.add(node_id)

    if not additions:
        print("no new nodes to import")
        return 0

    marker = "## Operational rule"
    if marker not in idx_text:
        print(f"missing marker in {NODE_INDEX}")
        return 1

    insertion = "\n" + "\n".join(additions) + "\n"
    updated = idx_text.replace(marker, insertion + marker)
    NODE_INDEX.write_text(updated, encoding="utf-8")
    print(f"imported {len(additions)} nodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
