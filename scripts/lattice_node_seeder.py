"""
lattice_node_seeder.py — T61: Lattice Node Seed Instance Generator
Rainbow Yin Yang Lattice — 12×12×12 Hypercube Data Fabric

Reads Wave 5 ontology YAMLs and generates seed node instances for
representative positions across the 1728-node hypercube.

Status: Candidate
Date: 2026-05-29
Author: TIDELOCKBrain / @atlaslattice
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

ONTOLOGY_DIR = (
    Path(__file__).resolve().parent.parent
    / "archive" / "spec" / "lattice-hypercube" / "ontology"
)
DATA_DIR = (
    Path(__file__).resolve().parent.parent
    / "archive" / "spec" / "lattice-hypercube" / "data"
)


def _load(filename: str) -> dict:
    return yaml.safe_load((ONTOLOGY_DIR / filename).read_text(encoding="utf-8"))


def _axis_index_label(axis_id: str, index: int, axes: list[dict]) -> str:
    """Return a human-readable label for an axis index."""
    ax = next((a for a in axes if a["id"] == axis_id), None)
    if ax is None:
        return str(index)
    return f"{ax['name']}[{index}]"


def generate_seed_nodes() -> list[dict[str, Any]]:
    """
    Generate representative seed nodes covering:
    - All 12 corners of the primary AX-01/AX-02/AX-03 cube face
    - The 12 Riemann operator spine nodes (AX-09 = 0..11)
    - The apex (unified field) node
    - 12 Metatron's Cube geometry anchor nodes

    Returns a list of node dicts.
    """
    axes_data = _load("AXES_12_FORMAL_DEFINITIONS.yaml")
    node_types = _load("NODE_TYPE_TAXONOMY.yaml")
    axes = axes_data["axes"]

    nodes: list[dict[str, Any]] = []

    # --- Seed set 1: primary axis corners (AX-01 × AX-02 × AX-03, edges) ---
    for i in [0, 5, 11]:
        for j in [0, 5, 11]:
            for k in [0, 5, 11]:
                node = {
                    "node_id": f"N-{i:02d}.{j:02d}.{k:02d}",
                    "address": {"AX-01": i, "AX-02": j, "AX-03": k},
                    "properties": {
                        "AX-04": (i + j) % 12,       # Spin (derived)
                        "AX-05": (j + k) % 12,       # Acoustic (derived)
                        "AX-06": (i * 11) // 11,     # Color harmonic (freq-mapped)
                        "AX-07": k % 12,              # Neuromorphic
                        "AX-08": 5 if (i + j + k) % 2 == 0 else 6,  # Yin-Yang balance
                        "AX-09": (i + j + k) % 12,  # Riemann index
                        "AX-10": i % 12,              # Temporal
                        "AX-11": j % 12,              # Spatial topology
                        "AX-12": k % 12,              # Information
                    },
                    "node_type": "FrequencyNode" if i == 0 else (
                        "RiemannOperatorNode" if i == 11 else "MatterPhaseNode"
                    ),
                    "yin_yang": "balanced" if (i + j + k) % 2 == 0 else "yang_dominant",
                    "status": "Candidate",
                    "seed_class": "primary_corner",
                }
                nodes.append(node)

    # --- Seed set 2: Riemann spine nodes (AX-09 = 0..11, all at AX-01=5, AX-02=5) ---
    for r in range(12):
        node = {
            "node_id": f"N-RIEMANN-{r:02d}",
            "address": {"AX-01": 5, "AX-02": 5, "AX-03": r},
            "properties": {
                "AX-04": r % 12,
                "AX-05": r % 12,
                "AX-06": r % 12,
                "AX-07": r % 12,
                "AX-08": 5,          # balanced
                "AX-09": r,          # Riemann spine
                "AX-10": r % 12,
                "AX-11": r % 12,
                "AX-12": r % 12,
            },
            "node_type": "RiemannOperatorNode",
            "yin_yang": "meta",
            "status": "Candidate",
            "seed_class": "riemann_spine",
        }
        nodes.append(node)

    # --- Seed set 3: Apex / Unified Field node ---
    nodes.append({
        "node_id": "N-APEX",
        "address": {"AX-01": 11, "AX-02": 11, "AX-03": 11},
        "properties": {axis["id"]: 11 for axis in axes},
        "node_type": "UnifiedFieldApex",
        "yin_yang": "perfect_balance",
        "status": "Candidate",
        "seed_class": "apex",
        "requires_ratification": True,
    })

    # --- Seed set 4: Metatron's Cube geometry anchors (13 nodes: 1 centre + 12 outer) ---
    # Centre
    nodes.append({
        "node_id": "N-METATRON-CENTER",
        "address": {"AX-01": 5, "AX-02": 5, "AX-03": 5},
        "properties": {axis["id"]: 5 for axis in axes},
        "node_type": "YinYangBalanceNode",
        "yin_yang": "perfect_balance",
        "status": "Candidate",
        "seed_class": "metatron_center",
    })
    # 12 outer nodes of Metatron's Cube — equally spaced by axis index cycle
    metatron_offsets = [
        (0, 5, 5), (11, 5, 5), (5, 0, 5), (5, 11, 5),
        (5, 5, 0), (5, 5, 11), (0, 0, 5), (11, 11, 5),
        (0, 11, 5), (11, 0, 5), (5, 0, 11), (5, 11, 0),
    ]
    for idx, (i, j, k) in enumerate(metatron_offsets):
        nodes.append({
            "node_id": f"N-METATRON-{idx + 1:02d}",
            "address": {"AX-01": i, "AX-02": j, "AX-03": k},
            "properties": {
                "AX-04": idx % 12,
                "AX-05": idx % 12,
                "AX-06": (idx * 11) // 11,
                "AX-07": idx % 12,
                "AX-08": 5,
                "AX-09": idx % 12,
                "AX-10": idx % 12,
                "AX-11": idx % 12,
                "AX-12": idx % 12,
            },
            "node_type": "YinYangBalanceNode",
            "yin_yang": "balanced",
            "status": "Candidate",
            "seed_class": "metatron_outer",
        })

    return nodes


def write_seed_registry(nodes: list[dict[str, Any]], output_path: Path) -> None:
    """Write seed nodes to YAML and JSON."""
    registry = {
        "schema_version": "0.1",
        "status": "Candidate",
        "date": "2026-05-29",
        "author": "TIDELOCKBrain / @atlaslattice",
        "total_seed_nodes": len(nodes),
        "seed_classes": sorted(set(n["seed_class"] for n in nodes)),
        "nodes": nodes,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    yaml_path = output_path.with_suffix(".yaml")
    json_path = output_path.with_suffix(".json")
    yaml_path.write_text(
        yaml.dump(registry, allow_unicode=True, sort_keys=False, default_flow_style=False),
        encoding="utf-8",
    )
    json_path.write_text(
        json.dumps(registry, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"✅  Written {len(nodes)} seed nodes → {yaml_path.name} + {json_path.name}")


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    nodes = generate_seed_nodes()
    write_seed_registry(nodes, DATA_DIR / "LATTICE_NODE_SEED_REGISTRY")
    print(f"🌐  Total seed nodes: {len(nodes)}")
    class_counts = {}
    for n in nodes:
        class_counts[n["seed_class"]] = class_counts.get(n["seed_class"], 0) + 1
    for cls, cnt in sorted(class_counts.items()):
        print(f"   {cls}: {cnt}")


if __name__ == "__main__":
    main()
