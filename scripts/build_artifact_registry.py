#!/usr/bin/env python3
"""Build the repository-wide artifact registry, graph, and scorecard.

The knowledge graph is structured as a 12×12×12 hypercube lattice:
  D1 (axis 0-11)  — semantic domain, aligned with the 12-axis campaign
  D2 (row  0-11)  — sub-domain within the axis (hash of 2nd path component)
  D3 (slot 0-11)  — sequential slot within the (D1, D2) cell arm

Each artifact receives a `hypercube_coord` {d1, d2, d3} triple.
`lattice_arm` edges connect D3-adjacent artifacts in the same cell arm.
`lattice_backbone` edges connect the D1-axis spine across rows.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "docs" / "knowledge-graph" / "artifact_registry.v0_1.json"
GRAPH_PATH = ROOT / "graph.json"
SCORECARD_PATH = ROOT / "docs" / "knowledge-graph" / "repo_quality_scorecard.v0_1.json"
RATIFICATION_LOG_PATH = ROOT / "RATIFICATION_LOG.md"
README_PATH = ROOT / "README.md"

ELIGIBLE_SUFFIXES = {".json", ".md", ".py", ".sh", ".toml", ".yaml", ".yml"}
TEXT_SUFFIXES = ELIGIBLE_SUFFIXES
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
TEXT_PATH_RE = re.compile(
    r"(?P<path>(?:\.\.?/)?[A-Za-z0-9_./-]+\.(?:json|md|py|sh|toml|yaml|yml))"
)
HEADING_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)
YAML_NAME_RE = re.compile(r"^\s*name:\s*(.+?)\s*$", re.MULTILINE)
DOCS_WITH_GOVERNANCE_LANGUAGE = (
    ROOT / "README.md",
    ROOT / "docs" / "START_HERE.md",
    ROOT / "docs" / "ARCHIVE_INDEX.md",
)
GENERATED_LINKS = {
    REGISTRY_PATH.relative_to(ROOT).as_posix(): (
        "docs/governance-ratification-process.md",
        "docs/knowledge-graph/repo_quality_scorecard.v0_1.json",
        "graph.json",
        "RATIFICATION_LOG.md",
    ),
    GRAPH_PATH.relative_to(ROOT).as_posix(): (
        "docs/knowledge-graph/artifact_registry.v0_1.json",
        "docs/knowledge-graph/repo_quality_scorecard.v0_1.json",
    ),
    SCORECARD_PATH.relative_to(ROOT).as_posix(): (
        "docs/knowledge-graph/artifact_registry.v0_1.json",
        "graph.json",
        "RATIFICATION_LOG.md",
    ),
}

# ---------------------------------------------------------------------------
# 12×12×12 Hypercube Lattice
# ---------------------------------------------------------------------------
# D1 — 12 semantic domain axes, aligned with the 12-axis Aetherforge campaign
HYPERCUBE_AXES = [
    "Governance Core",            # 0
    "Canon & Adjudication",       # 1
    "Provenance & Receipts",      # 2
    "Information Architecture",   # 3
    "Documentation Excellence",   # 4
    "Security, Trust, Integrity", # 5
    "Testing & Validation",       # 6
    "CI/CD & Automation",         # 7
    "Knowledge Graph",            # 8
    "Public Packaging & Releases",# 9
    "Community & Contributors",   # 10
    "Ops & Living Archive",       # 11
]
HYPERCUBE_DIM = 12  # positions per dimension


def hypercube_d1(rel_path: Path) -> int:
    """Return D1 axis (0-11) based on semantic domain of the artifact."""
    parts = rel_path.parts
    top = parts[0] if parts else ""
    fp = rel_path.as_posix().lower()
    sub = parts[1].lower() if len(parts) > 1 else ""

    # Axis 0 — Governance Core
    if top == ".github" and sub != "workflows":
        return 0
    if top == "docs" and any(x in fp for x in ["governance", "ratif", "adjud", "glossary", "versioning", "start_here", "archive_index"]):
        return 0

    # Axis 1 — Canon & Adjudication
    if rel_path.name.lower() == "ratification_log.md":
        return 1
    if top == "docs":
        return 1

    # Axis 2 — Provenance & Receipts
    if top == "manus-vault":
        return 2
    if top == "archive" and any(x in fp for x in ["spec", "receipt", "manus-vault"]):
        return 2

    # Axis 3 — Information Architecture
    if top == "archive" and any(x in fp for x in ["boot", "chatlog", "fork", "metaphor"]):
        return 3
    if top == "archives":
        return 3

    # Axis 4 — Documentation Excellence
    if top in ("about", "research", "health"):
        return 4

    # Axis 5 — Security, Trust, Integrity
    if top == "schemas":
        return 5

    # Axis 6 — Testing & Validation
    if top in ("tests", "fixtures"):
        return 6

    # Axis 7 — CI/CD & Automation
    if (top == ".github" and sub == "workflows") or top == "scripts":
        return 7

    # Axis 8 — Knowledge Graph
    if rel_path.name == "graph.json" or (top == "docs" and "knowledge" in fp):
        return 8

    # Axis 9 — Public Packaging & Releases
    if top == "projects" or (top == "archive" and "aetherforge" in fp):
        return 9

    # Axis 10 — Community & Contributors
    if top in ("children-of-the-swarm", "council", "council-reviews"):
        return 10

    # Axis 11 — Ops & Living Archive (everything else)
    return 11


def hypercube_d2(rel_path: Path) -> int:
    """Return D2 row (0-11) as a stable hash of the 2nd path component."""
    key = rel_path.parts[1] if len(rel_path.parts) > 1 else rel_path.parts[0]
    return int(hashlib.sha1(key.encode("utf-8")).hexdigest(), 16) % HYPERCUBE_DIM


def assign_hypercube_coords(tracked_paths: list[Path]) -> dict[str, dict[str, int]]:
    """Return {path_posix: {d1, d2, d3}} for every tracked path.

    D3 is assigned sequentially within each (D1, D2) cell, wrapping mod 12
    so that large cells occupy the same arm positions cyclically.
    """
    cell_seq: dict[tuple[int, int], int] = defaultdict(int)
    coords: dict[str, dict[str, int]] = {}
    for rel_path in tracked_paths:
        d1 = hypercube_d1(rel_path)
        d2 = hypercube_d2(rel_path)
        d3 = cell_seq[(d1, d2)] % HYPERCUBE_DIM
        cell_seq[(d1, d2)] += 1
        coords[rel_path.as_posix()] = {"d1": d1, "d2": d2, "d3": d3}
    return coords


def build_lattice_edges(
    artifact_id_by_path: dict[str, str],
    coords: dict[str, dict[str, int]],
) -> list[dict[str, str]]:
    """Return lattice arm + backbone edges for the 12×12×12 hypercube.

    lattice_arm      — D3-sequential neighbors within the same (D1, D2) cell.
    lattice_backbone — D1-axis spine: for each (D2, D3) slice, connect the
                       chain of artifacts ordered by their D1 axis value.
    """
    edges: list[dict[str, str]] = []

    # Group by (d1, d2) cell → ordered list of (d3, path)
    cell_members: dict[tuple[int, int], list[tuple[int, str]]] = defaultdict(list)
    for path, c in coords.items():
        cell_members[(c["d1"], c["d2"])].append((c["d3"], path))

    # lattice_arm: chain within each cell, sorted by d3
    for (_, _), members in cell_members.items():
        members.sort(key=lambda x: x[0])
        for i in range(len(members) - 1):
            src = artifact_id_by_path[members[i][1]]
            tgt = artifact_id_by_path[members[i + 1][1]]
            edges.append({"from": src, "to": tgt, "relation": "lattice_arm"})

    # lattice_backbone: for each (d2, d3) slice, chain artifacts sorted by d1
    slice_members: dict[tuple[int, int], list[tuple[int, str]]] = defaultdict(list)
    for path, c in coords.items():
        slice_members[(c["d2"], c["d3"])].append((c["d1"], path))

    for (_, _), members in slice_members.items():
        members.sort(key=lambda x: x[0])
        for i in range(len(members) - 1):
            src = artifact_id_by_path[members[i][1]]
            tgt = artifact_id_by_path[members[i + 1][1]]
            edges.append({"from": src, "to": tgt, "relation": "lattice_backbone"})

    return edges


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def stable_artifact_id(path: Path) -> str:
    digest = hashlib.sha1(path.as_posix().encode("utf-8")).hexdigest()[:12].upper()
    return f"ART-{digest}"


def git_tracked_files(root: Path) -> list[Path]:
    proc = subprocess.run(
        ["git", "ls-files"],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )
    paths: list[Path] = []
    for raw in proc.stdout.splitlines():
        if not raw:
            continue
        rel = Path(raw)
        if rel.suffix.lower() in ELIGIBLE_SUFFIXES:
            paths.append(rel)
    return sorted(paths)


def parse_markdown_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    if cells and all(set(cell) <= {"-", ":"} for cell in cells):
        return None
    return cells


def parse_ratification_log(path: Path) -> dict[str, dict[str, str | None]]:
    entries: dict[str, dict[str, str | None]] = {}
    for line in load_text(path).splitlines():
        row = parse_markdown_table_row(line)
        if not row or row[0] == "date_utc":
            continue
        if len(row) < 6:
            continue
        date_utc, event_id, artifact_path, decision, adjudicator, notes = row[:6]
        entries[artifact_path] = {
            "date_utc": date_utc or None,
            "ratification_event_id": event_id or None,
            "decision": decision or None,
            "adjudicator": adjudicator or None,
            "notes": notes or None,
        }
    return entries


def decision_to_canon_status(decision: str | None) -> str:
    normalized = (decision or "").strip().lower()
    mapping = {
        "candidate": "candidate",
        "reviewed": "reviewed",
        "ratified": "ratified",
        "superseded": "superseded",
        "deprecated": "deprecated",
        "pending": "candidate",
    }
    return mapping.get(normalized, "candidate")


def infer_title(root: Path, rel_path: Path) -> str:
    if rel_path == README_PATH.relative_to(root):
        return "Manus Artifacts"

    abs_path = root / rel_path
    if rel_path.suffix.lower() == ".md":
        match = HEADING_RE.search(load_text(abs_path))
        if match:
            return match.group(1).strip()
    if rel_path.suffix.lower() in {".yaml", ".yml"}:
        match = YAML_NAME_RE.search(load_text(abs_path))
        if match:
            return match.group(1).strip().strip("'\"")
    return rel_path.stem.replace("-", " ").replace("_", " ").strip() or rel_path.name


def infer_artifact_type(rel_path: Path) -> str:
    posix = rel_path.as_posix()
    suffix = rel_path.suffix.lower()

    if posix == "graph.json":
        return "knowledge_graph"
    if posix.endswith("artifact_registry.v0_1.json"):
        return "artifact_registry"
    if posix.endswith("repo_quality_scorecard.v0_1.json"):
        return "quality_scorecard"
    if rel_path.parts[:2] == (".github", "workflows"):
        return "workflow"
    if rel_path.parts and rel_path.parts[0] == "tests":
        return "test"
    if rel_path.parts and rel_path.parts[0] == "scripts":
        return "script"
    if "schema" in posix or rel_path.parts[:1] == ("schemas",):
        return "schema"
    if rel_path.name == "README.md":
        return "index"
    if suffix == ".md":
        return "document"
    if suffix == ".py":
        return "source_code"
    if suffix in {".yaml", ".yml"}:
        return "configuration"
    if suffix == ".json":
        return "data"
    if suffix == ".toml":
        return "packaging"
    if suffix == ".sh":
        return "shell_script"
    return "artifact"


def infer_owner(rel_path: Path) -> str:
    if not rel_path.parts:
        return "root"
    return "root" if len(rel_path.parts) == 1 else rel_path.parts[0]


def infer_lifecycle_state(canon_status: str) -> str:
    mapping = {
        "candidate": "candidate",
        "reviewed": "active-review",
        "ratified": "ratified-active",
        "superseded": "superseded",
        "deprecated": "deprecated",
    }
    return mapping.get(canon_status, "candidate")


def resolve_repo_path(root: Path, current_rel_path: Path, raw_target: str) -> str | None:
    if raw_target.startswith(("http://", "https://", "mailto:", "#")):
        return None

    path_part = raw_target.split("#", 1)[0].strip()
    if not path_part:
        return None

    if path_part.endswith("/"):
        path_part = f"{path_part}README.md"

    candidate = (current_rel_path.parent / path_part).resolve()
    try:
        rel = candidate.relative_to(root.resolve())
    except ValueError:
        return None

    if candidate.is_dir():
        candidate = candidate / "README.md"
        rel = candidate.relative_to(root.resolve())

    if not candidate.exists():
        return None

    return rel.as_posix()


def extract_links(root: Path, rel_path: Path, known_paths: set[str]) -> set[str]:
    rel_posix = rel_path.as_posix()
    links: set[str] = set()

    # Hardcoded cross-links for known generated files
    if rel_posix in GENERATED_LINKS:
        links.update(target for target in GENERATED_LINKS[rel_posix] if target in known_paths)
    else:
        abs_path = root / rel_path
        if rel_path.suffix.lower() == ".md":
            for match in MARKDOWN_LINK_RE.finditer(load_text(abs_path)):
                resolved = resolve_repo_path(root, rel_path, match.group(1))
                if resolved in known_paths and resolved != rel_posix:
                    links.add(resolved)
        elif rel_path.suffix.lower() in TEXT_SUFFIXES:
            for match in TEXT_PATH_RE.finditer(load_text(abs_path)):
                resolved = resolve_repo_path(root, rel_path, match.group("path"))
                if resolved in known_paths and resolved != rel_posix:
                    links.add(resolved)

    # Walk all ancestor directories and link to every README found so the
    # entire graph forms one connected component ("one octopus, not legos").
    p = rel_path.parent
    while True:
        ancestor_readme = p / "README.md"
        ar_posix = ancestor_readme.as_posix()
        if ar_posix != rel_posix and ar_posix in known_paths:
            links.add(ar_posix)
        if p == Path("."):
            break
        p = p.parent

    return links


def build_registry_bundle(root: Path, generated_utc: str | None = None) -> tuple[dict, dict, dict]:
    generated_utc = generated_utc or now_utc()
    tracked_paths = git_tracked_files(root)
    known_paths = {path.as_posix() for path in tracked_paths}
    artifact_id_by_path = {path.as_posix(): stable_artifact_id(path) for path in tracked_paths}
    ratification_entries = parse_ratification_log(RATIFICATION_LOG_PATH)

    # Assign 12×12×12 hypercube coordinates to every artifact
    coords = assign_hypercube_coords(tracked_paths)

    artifacts: list[dict] = []
    graph_edges: list[dict[str, str]] = []
    linked_count = 0

    for rel_path in tracked_paths:
        rel_posix = rel_path.as_posix()
        governance = ratification_entries.get(rel_posix, {})
        canon_status = decision_to_canon_status(governance.get("decision"))
        links_to_paths = sorted(extract_links(root, rel_path, known_paths))
        links_to_ids = [artifact_id_by_path[target] for target in links_to_paths]
        if links_to_ids:
            linked_count += 1

        for target_path in links_to_paths:
            target_p = Path(target_path)
            try:
                rel_path.relative_to(target_p.parent)
                is_ancestor_readme = target_p.name == "README.md"
            except ValueError:
                is_ancestor_readme = False
            relation = "contained_in" if is_ancestor_readme else "references"
            graph_edges.append(
                {
                    "from": artifact_id_by_path[rel_posix],
                    "to": artifact_id_by_path[target_path],
                    "relation": relation,
                }
            )

        artifacts.append(
            {
                "artifact_id": artifact_id_by_path[rel_posix],
                "title": infer_title(root, rel_path),
                "path": rel_posix,
                "artifact_type": infer_artifact_type(rel_path),
                "owner": infer_owner(rel_path),
                "canon_status": canon_status,
                "lifecycle_state": infer_lifecycle_state(canon_status),
                "ratification_event_id": governance.get("ratification_event_id"),
                "adjudicator": governance.get("adjudicator"),
                "hypercube_coord": coords[rel_posix],
                "provenance": {
                    "source": "github",
                    "tracked_by_git": True,
                    "path": rel_posix,
                },
                "governance": {
                    "decision": governance.get("decision"),
                    "decision_date_utc": governance.get("date_utc"),
                    "notes": governance.get("notes"),
                    "status_authority": "docs/knowledge-graph/artifact_registry.v0_1.json",
                    "event_log": "RATIFICATION_LOG.md",
                },
                "links_to": links_to_ids,
            }
        )

    # Merge lattice edges (arm + backbone) into the graph
    lattice_edges = build_lattice_edges(artifact_id_by_path, coords)
    all_edges = graph_edges + lattice_edges
    all_edges = sorted(
        all_edges,
        key=lambda edge: (edge["from"], edge["to"], edge["relation"]),
    )

    nodes = [artifact["artifact_id"] for artifact in artifacts]
    top_level_dirs = sorted(
        child.name
        for child in root.iterdir()
        if child.is_dir() and (child.name == ".github" or not child.name.startswith("."))
    )
    top_level_with_readmes = sum((root / dirname / "README.md").exists() for dirname in top_level_dirs)
    coverage_pct = round((len(artifacts) / len(tracked_paths) * 100.0), 2) if tracked_paths else 0.0
    linked_pct = round((linked_count / len(artifacts) * 100.0), 2) if artifacts else 0.0
    top_level_readme_pct = round(
        (top_level_with_readmes / len(top_level_dirs) * 100.0), 2
    ) if top_level_dirs else 0.0

    # Hypercube axis distribution for scorecard
    axis_counts = dict(
        sorted(Counter(artifact["hypercube_coord"]["d1"] for artifact in artifacts).items())
    )
    hypercube_cells_used = len(
        {(c["d1"], c["d2"]) for c in coords.values()}
    )

    registry = {
        "schema_version": "0.2",
        "generated_utc": generated_utc,
        "status_authority": "docs/knowledge-graph/artifact_registry.v0_1.json",
        "ratification_event_log": "RATIFICATION_LOG.md",
        "description": "Repository-wide artifact registry for machine-checked governance, provenance, and graph coverage.",
        "hypercube": {
            "dimensions": HYPERCUBE_DIM,
            "axes": HYPERCUBE_AXES,
            "shape": [HYPERCUBE_DIM, HYPERCUBE_DIM, HYPERCUBE_DIM],
            "total_slots": HYPERCUBE_DIM ** 3,
        },
        "eligible_extensions": sorted(ELIGIBLE_SUFFIXES),
        "artifacts": artifacts,
    }
    graph = {
        "version": "0.2",
        "generated_utc": generated_utc,
        "description": (
            "12×12×12 hypercube lattice KG derived from "
            "docs/knowledge-graph/artifact_registry.v0_1.json. "
            "One connected octopus: contained_in + references + lattice_arm + lattice_backbone."
        ),
        "hypercube": {
            "shape": [HYPERCUBE_DIM, HYPERCUBE_DIM, HYPERCUBE_DIM],
            "axes": HYPERCUBE_AXES,
        },
        "nodes": nodes,
        "edges": all_edges,
    }
    scorecard = {
        "schema_version": "0.2",
        "generated_utc": generated_utc,
        "status_authority": "docs/knowledge-graph/artifact_registry.v0_1.json",
        "totals": {
            "tracked_artifact_files": len(tracked_paths),
            "registry_artifacts": len(artifacts),
            "graph_nodes": len(nodes),
            "graph_edges": len(all_edges),
            "graph_coverage_pct": coverage_pct,
            "linked_artifacts_pct": linked_pct,
            "top_level_readme_coverage_pct": top_level_readme_pct,
        },
        "hypercube": {
            "shape": [HYPERCUBE_DIM, HYPERCUBE_DIM, HYPERCUBE_DIM],
            "total_slots": HYPERCUBE_DIM ** 3,
            "cells_used": hypercube_cells_used,
            "artifacts_placed": len(artifacts),
            "axis_distribution": {
                HYPERCUBE_AXES[k]: v for k, v in axis_counts.items()
            },
            "lattice_arm_edges": sum(1 for e in all_edges if e["relation"] == "lattice_arm"),
            "lattice_backbone_edges": sum(1 for e in all_edges if e["relation"] == "lattice_backbone"),
        },
        "status_counts": dict(sorted(Counter(artifact["canon_status"] for artifact in artifacts).items())),
        "artifact_type_counts": dict(sorted(Counter(artifact["artifact_type"] for artifact in artifacts).items())),
        "owner_counts": dict(sorted(Counter(artifact["owner"] for artifact in artifacts).items())),
        "pending_ratification_events": sum(
            1 for artifact in artifacts if artifact["governance"]["decision"] == "pending"
        ),
    }
    return registry, graph, scorecard


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def main() -> int:
    registry, graph, scorecard = build_registry_bundle(ROOT)
    write_json(REGISTRY_PATH, registry)
    write_json(GRAPH_PATH, graph)
    write_json(SCORECARD_PATH, scorecard)
    print(
        "Built artifact registry bundle:"
        f" {scorecard['totals']['registry_artifacts']} artifacts,"
        f" {scorecard['totals']['graph_edges']} edges,"
        f" {scorecard['totals']['graph_coverage_pct']}% coverage"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
