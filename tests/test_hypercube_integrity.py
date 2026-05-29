"""Tests for the 12D hypercube integrity gates and indexing pipeline.

Tests are written against the public functions in:
  - scripts/validate_hypercube_integrity
  - scripts/build_lattice_global_index
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

import pytest

# Make scripts importable
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_hypercube_integrity import (  # noqa: E402
    gate_g01_no_orphans,
    gate_g02_no_duplicates,
    gate_g03_connectivity,
    gate_g04_schema_drift,
    gate_g05_all_dimensions,
    gate_g06_cross_link_targets,
    ALL_DIMENSIONS,
    REQUIRED_NODE_FIELDS,
    run_gates,
)
from build_lattice_global_index import (  # noqa: E402
    parse_frontmatter,
    infer_dimension,
    build_index,
)


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def make_node(artifact_id: str, dimension_id: str = "D01", **extra) -> dict:
    base = {
        "artifact_id": artifact_id,
        "path": f"docs/{artifact_id}.md",
        "dimension_id": dimension_id,
        "canon_status": "not_canon",
        "status": "candidate",
    }
    base.update(extra)
    return base


def make_edge(src: str, dst: str, dim: str = "D01") -> dict:
    return {
        "edge_id": f"links_to.{src}.{dst}",
        "edge_type": "links_to",
        "from_artifact_id": src,
        "to_artifact_id": dst,
        "from_dimension": dim,
        "source_file": f"docs/{src}.md",
    }


def all_dim_nodes() -> list[dict]:
    """Return one node per dimension so G05 is satisfied."""
    return [make_node(f"dim.anchor.{d.lower()}", dimension_id=d) for d in sorted(ALL_DIMENSIONS)]


# ──────────────────────────────────────────────────────────────────────────────
# parse_frontmatter
# ──────────────────────────────────────────────────────────────────────────────

class TestParseFrontmatter:
    def test_basic(self):
        text = "---\nartifact_id: foo.bar.v1\nstatus: candidate\n---\n# Title\n"
        fm = parse_frontmatter(text)
        assert fm["artifact_id"] == "foo.bar.v1"
        assert fm["status"] == "candidate"

    def test_no_frontmatter(self):
        fm = parse_frontmatter("# Just a heading\nNo frontmatter here.")
        assert fm == {}

    def test_missing_closing_delimiter(self):
        fm = parse_frontmatter("---\nkey: value\n# no closing")
        assert fm == {}

    def test_quoted_value(self):
        text = '---\nowner: "@atlaslattice"\n---\n'
        fm = parse_frontmatter(text)
        assert fm["owner"] == "@atlaslattice"


# ──────────────────────────────────────────────────────────────────────────────
# infer_dimension
# ──────────────────────────────────────────────────────────────────────────────

class TestInferDimension:
    def test_known_prefix(self):
        assert infer_dimension("governance.canon.v1") == "D01"
        assert infer_dimension("kg_layer.ontology.v0_5") == "D05"
        assert infer_dimension("cicd.workflow.v1") == "D06"

    def test_fallback_default(self):
        assert infer_dimension("unknown.thing.v1") == "D03"

    def test_empty(self):
        assert infer_dimension("") == "D03"


# ──────────────────────────────────────────────────────────────────────────────
# Gate G01 — no orphan nodes
# ──────────────────────────────────────────────────────────────────────────────

class TestGateG01:
    def test_all_linked(self):
        nodes = [make_node("a.b.v1"), make_node("c.d.v1")]
        edges = [make_edge("a.b.v1", "c.d.v1")]
        assert gate_g01_no_orphans(nodes, edges) == []

    def test_orphan_detected(self):
        nodes = [make_node("a.b.v1"), make_node("orphan.thing.v1")]
        edges = [make_edge("a.b.v1", "a.b.v1")]  # self-loops don't count as linking
        failures = gate_g01_no_orphans(nodes, edges)
        assert any("ORPHAN" in f for f in failures)

    def test_path_fallback_ids_ignored(self):
        """Auto-generated path.* IDs should not be flagged as orphans."""
        nodes = [make_node("path.docs.readme.md")]
        failures = gate_g01_no_orphans(nodes, [])
        assert failures == []


# ──────────────────────────────────────────────────────────────────────────────
# Gate G02 — no duplicate IDs
# ──────────────────────────────────────────────────────────────────────────────

class TestGateG02:
    def test_unique_ids(self):
        nodes = [make_node("a.b.v1"), make_node("c.d.v1")]
        assert gate_g02_no_duplicates(nodes) == []

    def test_duplicate_detected(self):
        nodes = [
            make_node("a.b.v1", path="docs/first.md"),
            make_node("a.b.v1", path="docs/second.md"),
        ]
        failures = gate_g02_no_duplicates(nodes)
        assert any("DUPLICATE" in f for f in failures)

    def test_path_ids_skipped(self):
        nodes = [
            make_node("path.docs.readme.md"),
            make_node("path.docs.readme.md"),
        ]
        assert gate_g02_no_duplicates(nodes) == []


# ──────────────────────────────────────────────────────────────────────────────
# Gate G03 — connectivity
# ──────────────────────────────────────────────────────────────────────────────

class TestGateG03:
    def test_connected(self):
        nodes = [make_node("a.v1"), make_node("b.v1"), make_node("c.v1")]
        edges = [make_edge("a.v1", "b.v1"), make_edge("b.v1", "c.v1")]
        assert gate_g03_connectivity(nodes, edges) == []

    def test_isolated_subgraph(self):
        nodes = [make_node("a.v1"), make_node("b.v1"), make_node("isolated.thing.v1")]
        edges = [make_edge("a.v1", "b.v1")]
        failures = gate_g03_connectivity(nodes, edges)
        assert any("ISOLATED" in f for f in failures)

    def test_single_node_ok(self):
        assert gate_g03_connectivity([make_node("solo.v1")], []) == []


# ──────────────────────────────────────────────────────────────────────────────
# Gate G04 — schema drift
# ──────────────────────────────────────────────────────────────────────────────

class TestGateG04:
    def test_valid_node(self):
        nodes = [make_node("a.b.v1")]
        assert gate_g04_schema_drift(nodes) == []

    def test_missing_field(self):
        node = {"artifact_id": "a.b.v1", "path": "x.md"}  # missing dimension_id etc.
        failures = gate_g04_schema_drift([node])
        assert any("SCHEMA DRIFT" in f for f in failures)


# ──────────────────────────────────────────────────────────────────────────────
# Gate G05 — all dimensions represented
# ──────────────────────────────────────────────────────────────────────────────

class TestGateG05:
    def test_all_present(self):
        nodes = all_dim_nodes()
        assert gate_g05_all_dimensions(nodes) == []

    def test_missing_dimension(self):
        nodes = [make_node("a.v1", dimension_id=d) for d in list(ALL_DIMENSIONS)[:11]]
        failures = gate_g05_all_dimensions(nodes)
        assert any("MISSING DIMENSION" in f for f in failures)


# ──────────────────────────────────────────────────────────────────────────────
# Gate G06 — cross-link targets exist
# ──────────────────────────────────────────────────────────────────────────────

class TestGateG06:
    def test_valid_targets(self):
        nodes = [make_node("a.v1"), make_node("b.v1")]
        edges = [make_edge("a.v1", "b.v1")]
        assert gate_g06_cross_link_targets(nodes, edges) == []

    def test_broken_target(self):
        nodes = [make_node("a.v1")]
        edges = [make_edge("a.v1", "does.not.exist")]
        failures = gate_g06_cross_link_targets(nodes, edges)
        assert any("BROKEN LINK" in f for f in failures)


# ──────────────────────────────────────────────────────────────────────────────
# Integration: build_index + run_gates on temp filesystem
# ──────────────────────────────────────────────────────────────────────────────

class TestIntegration:
    def _write_md(self, root: Path, rel: str, content: str) -> None:
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def test_build_and_validate_minimal(self):
        """Build a minimal well-formed lattice and verify gates pass."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            # One doc per dimension
            dim_ids = {
                "D01": "governance.test.v1",
                "D02": "legal.test.v1",
                "D03": "repo_arch.test.v1",
                "D04": "docs.test.v1",
                "D05": "kg_layer.test.v1",  # 'kg' prefix maps to D05
                "D06": "cicd.test.v1",
                "D07": "security.test.v1",
                "D08": "testing.test.v1",
                "D09": "accessibility.test.v1",
                "D10": "devex.test.v1",
                "D11": "community.test.v1",
                "D12": "operations.test.v1",
            }
            artifact_ids = list(dim_ids.values())

            for dim, aid in dim_ids.items():
                slug = aid.split(".")[0]
                content = (
                    f"---\nartifact_id: {aid}\nstatus: candidate\n"
                    f"canon_status: not_canon\n---\n# {aid}\n"
                )
                self._write_md(root, f"docs/{slug}.md", content)

            # Build the index
            from build_lattice_global_index import build_index, write_jsonl, INDEX_FILE, CROSSLINKS_FILE

            nodes, edges = build_index(root)
            write_jsonl(root / INDEX_FILE, nodes)
            write_jsonl(root / CROSSLINKS_FILE, edges)

            # --- Connectivity: add cross-links so G01 and G03 pass ---
            # We inject edges manually since the temp docs don't have md links
            linked_edges = []
            ids = list(dim_ids.values())
            for i in range(len(ids)):
                linked_edges.append({
                    "edge_id": f"links_to.{ids[i]}.{ids[(i+1) % len(ids)]}",
                    "edge_type": "links_to",
                    "from_artifact_id": ids[i],
                    "to_artifact_id": ids[(i + 1) % len(ids)],
                    "from_dimension": list(dim_ids.keys())[i],
                    "source_file": "test",
                })
            write_jsonl(root / CROSSLINKS_FILE, linked_edges)

            result = run_gates(root)
            assert result == 0, "Integrity gates should pass for a well-formed lattice"

    def test_run_gates_missing_index(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            result = run_gates(root)
            assert result == 1
