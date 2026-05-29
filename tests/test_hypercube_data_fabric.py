"""
test_hypercube_data_fabric.py — Wave 6 Validation Suite
Rainbow Yin Yang Lattice — Hypercube Data Fabric

Tests for T61–T69:
  T61: lattice_node_seeder.py
  T62: lattice_coordinate_mapper.py
  T63: lattice_cross_axis_bridge.py
  T64: LATTICE_NODE_SEED_REGISTRY.yaml
  T65: lattice_riemann_s_calculator.py
  T66: lattice_metatron_geometry.py
  T67: HYPERCUBE_DATA_FABRIC_GUIDE.md
  T68: lattice_graph_export.py / LATTICE_GRAPH_EXPORT.json
  T69: lattice_query_engine.py

Status: Candidate
Date: 2026-05-29
"""

import json
import math
import sys
from pathlib import Path

import pytest
import yaml

# Ensure scripts/ is importable
REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
DATA_DIR = REPO_ROOT / "archive" / "spec" / "lattice-hypercube" / "data"
DOCS_DIR = REPO_ROOT / "docs"

sys.path.insert(0, str(SCRIPTS_DIR))

from lattice_node_seeder import generate_seed_nodes
from lattice_coordinate_mapper import CoordinateMapper, LatticeCoordinate
from lattice_cross_axis_bridge import CrossAxisBridge
from lattice_riemann_s_calculator import RiemannSOperator, riemann_zeta_approx
from lattice_metatron_geometry import MetatronGeometry
from lattice_query_engine import LatticeQueryEngine


# ===========================================================================
# T61 — Node Seeder
# ===========================================================================

class TestNodeSeeder:
    def setup_method(self):
        self.nodes = generate_seed_nodes()

    def test_returns_list(self):
        assert isinstance(self.nodes, list)

    def test_minimum_seed_count(self):
        assert len(self.nodes) >= 40

    def test_apex_node_present(self):
        apex = [n for n in self.nodes if n["node_id"] == "N-APEX"]
        assert len(apex) == 1

    def test_apex_requires_ratification(self):
        apex = next(n for n in self.nodes if n["node_id"] == "N-APEX")
        assert apex.get("requires_ratification") is True

    def test_riemann_spine_count(self):
        spine = [n for n in self.nodes if n.get("seed_class") == "riemann_spine"]
        assert len(spine) == 12

    def test_metatron_center_present(self):
        centre = [n for n in self.nodes if n.get("seed_class") == "metatron_center"]
        assert len(centre) == 1

    def test_metatron_outer_count(self):
        outer = [n for n in self.nodes if n.get("seed_class") == "metatron_outer"]
        assert len(outer) == 12

    def test_all_nodes_have_address(self):
        for n in self.nodes:
            assert "address" in n, f"{n['node_id']} missing address"

    def test_all_nodes_have_status_candidate(self):
        for n in self.nodes:
            assert n.get("status") == "Candidate"

    def test_all_address_values_in_range(self):
        for n in self.nodes:
            addr = n.get("address", {})
            for ax, val in addr.items():
                assert 0 <= val <= 11, f"{n['node_id']} {ax}={val} out of range"


# ===========================================================================
# T62 — Coordinate Mapper
# ===========================================================================

class TestCoordinateMapper:
    def setup_method(self):
        self.mapper = CoordinateMapper()

    def test_map_returns_lattice_coordinate(self):
        coord = self.mapper.map(3, 7, 2)
        assert isinstance(coord, LatticeCoordinate)

    def test_all_values_in_range(self):
        coord = self.mapper.map(0, 0, 0)
        for field, val in coord.to_dict().items():
            assert 0 <= val <= 11, f"{field}={val} out of range"

    def test_origin_maps_consistently(self):
        c1 = self.mapper.map(0, 0, 0)
        c2 = self.mapper.map(0, 0, 0)
        assert c1 == c2

    def test_primary_axes_preserved(self):
        coord = self.mapper.map(3, 7, 9)
        assert coord.ax01_frequency == 3
        assert coord.ax02_matter_state == 7
        assert coord.ax03_element == 9

    def test_freq_color_coupling(self):
        # AX-01 ↔ AX-06: color = frequency
        coord = self.mapper.map(5, 0, 0)
        assert coord.ax06_color == 5

    def test_phase_temporal_coupling(self):
        # AX-02 ↔ AX-10: temporal = matter_state
        coord = self.mapper.map(0, 7, 0)
        assert coord.ax10_temporal == 7

    def test_invalid_coordinate_raises(self):
        with pytest.raises(ValueError):
            self.mapper.map(-1, 0, 0)
        with pytest.raises(ValueError):
            self.mapper.map(0, 12, 0)

    def test_all_corners_8_nodes(self):
        corners = self.mapper.map_all_corners()
        assert len(corners) == 8

    def test_riemann_spine_12_nodes(self):
        spine = self.mapper.riemann_spine()
        assert len(spine) == 12

    def test_riemann_spine_fixed_axes(self):
        spine = self.mapper.riemann_spine()
        for coord in spine:
            assert coord.ax01_frequency == 5
            assert coord.ax02_matter_state == 5

    def test_address_format(self):
        coord = self.mapper.map(3, 7, 2)
        assert coord.as_address() == "[03.07.02]"


# ===========================================================================
# T63 — Cross-Axis Bridge
# ===========================================================================

class TestCrossAxisBridge:
    def setup_method(self):
        self.bridge = CrossAxisBridge()

    def test_self_coupling_is_one(self):
        r = self.bridge.coupling("AX-01", "AX-01")
        assert r.strength == 1.0

    def test_self_coupling_type_self(self):
        r = self.bridge.coupling("AX-05", "AX-05")
        assert r.coupling_type == "self"

    def test_primary_pair_freq_color(self):
        r = self.bridge.coupling("AX-01", "AX-06")
        assert r.is_primary is True
        assert r.strength > 0.7

    def test_riemann_universal_coupling(self):
        for i in range(1, 13):
            other = f"AX-{i:02d}"
            if other == "AX-09":
                continue
            r = self.bridge.coupling("AX-09", other)
            assert r.strength > 0.0

    def test_coupling_strength_in_range(self):
        for i in range(1, 13):
            for j in range(1, 13):
                r = self.bridge.coupling(f"AX-{i:02d}", f"AX-{j:02d}")
                assert 0.0 <= r.strength <= 1.0, \
                    f"AX-{i:02d}↔AX-{j:02d} strength={r.strength}"

    def test_invalid_axis_raises(self):
        with pytest.raises(ValueError):
            self.bridge.coupling("AX-00", "AX-01")

    def test_full_matrix_dimensions(self):
        matrix = self.bridge.full_coupling_matrix()
        assert len(matrix) == 12
        for row in matrix:
            assert len(row) == 12

    def test_matrix_diagonal_is_one(self):
        matrix = self.bridge.full_coupling_matrix()
        for i in range(12):
            assert matrix[i][i] == 1.0

    def test_primary_pairs_all_primary(self):
        for result in self.bridge.primary_pairs_summary():
            assert result.is_primary is True

    def test_spectral_entropy_positive(self):
        h = self.bridge.spectral_entropy("AX-09")
        assert h > 0.0


# ===========================================================================
# T64 — Seed Registry YAML
# ===========================================================================

class TestSeedRegistryYaml:
    def setup_method(self):
        path = DATA_DIR / "LATTICE_NODE_SEED_REGISTRY.yaml"
        self.data = yaml.safe_load(path.read_text(encoding="utf-8"))

    def test_schema_version_present(self):
        assert "schema_version" in self.data

    def test_nodes_present(self):
        assert "nodes" in self.data
        assert isinstance(self.data["nodes"], list)

    def test_total_count_matches(self):
        assert self.data["total_seed_nodes"] == len(self.data["nodes"])

    def test_seed_classes_present(self):
        assert "seed_classes" in self.data
        assert len(self.data["seed_classes"]) > 0

    def test_json_counterpart_exists(self):
        json_path = DATA_DIR / "LATTICE_NODE_SEED_REGISTRY.json"
        assert json_path.exists()
        parsed = json.loads(json_path.read_text(encoding="utf-8"))
        assert parsed["total_seed_nodes"] == self.data["total_seed_nodes"]


# ===========================================================================
# T65 — Riemann S-Calculator
# ===========================================================================

class TestRiemannSCalculator:
    def setup_method(self):
        self.op = RiemannSOperator()

    def test_zeta_approx_at_2_known(self):
        # ζ(2) = π²/6 ≈ 1.6449
        result = riemann_zeta_approx(complex(2, 0), terms=500)
        assert abs(result.real - (math.pi ** 2 / 6)) < 0.01

    def test_compute_samples_returns_12(self):
        samples = self.op.compute_samples()
        assert len(samples) == 12

    def test_samples_indexed_0_to_11(self):
        samples = self.op.compute_samples()
        indices = [s.index for s in samples]
        assert indices == list(range(12))

    def test_all_on_critical_line(self):
        samples = self.op.compute_samples()
        for s in samples:
            assert s.s_real == 0.5

    def test_coupling_weights_in_range(self):
        samples = self.op.compute_samples()
        for s in samples:
            assert 0.0 <= s.coupling_weight <= 1.0

    def test_max_coupling_weight_is_one(self):
        samples = self.op.compute_samples()
        assert max(s.coupling_weight for s in samples) == 1.0

    def test_apply_to_axis_pair_in_range(self):
        for r in range(12):
            val = self.op.apply_to_axis_pair(3, 3, r)
            assert 0.0 <= val <= 1.0

    def test_invalid_riemann_index_raises(self):
        with pytest.raises(ValueError):
            self.op.apply_to_axis_pair(0, 0, 12)


# ===========================================================================
# T66 — Metatron Geometry
# ===========================================================================

class TestMetatronGeometry:
    def setup_method(self):
        self.geo = MetatronGeometry()
        self.nodes = self.geo.generate_nodes()
        self.edges = self.geo.generate_edges(self.nodes)

    def test_exactly_13_nodes(self):
        assert len(self.nodes) == 13

    def test_apex_node_at_origin(self):
        apex = next(n for n in self.nodes if n.id == "APEX")
        assert apex.x == 0.0
        assert apex.y == 0.0

    def test_all_12_axes_represented(self):
        axis_ids = {n.axis_id for n in self.nodes}
        for i in range(1, 13):
            assert f"AX-{i:02d}" in axis_ids

    def test_exactly_78_edges(self):
        # Complete graph on 13 nodes = 13*12/2 = 78
        assert len(self.edges) == 78

    def test_edge_weights_positive(self):
        for e in self.edges:
            assert e.weight > 0.0

    def test_edge_types_valid(self):
        valid = {"spine", "outer", "cross"}
        for e in self.edges:
            assert e.type in valid

    def test_inner_ring_radius(self):
        # Inner ring nodes should be at distance ≈ 1.0 from origin
        inner = [n for n in self.nodes
                 if n.axis_id in {f"AX-0{i}" for i in range(1, 7)}]
        for n in inner:
            dist = math.sqrt(n.x ** 2 + n.y ** 2)
            assert abs(dist - 1.0) < 1e-5, f"{n.id} dist={dist:.6f}"

    def test_json_export_structure(self):
        data = self.geo.export_json()
        assert data["total_nodes"] == 13
        assert data["total_edges"] == 78
        assert "nodes" in data
        assert "edges" in data

    def test_geometry_file_exists(self):
        path = DATA_DIR / "METATRON_CUBE_GEOMETRY.json"
        assert path.exists()


# ===========================================================================
# T67 — Data Fabric Guide
# ===========================================================================

class TestDataFabricGuide:
    def setup_method(self):
        self.path = DOCS_DIR / "HYPERCUBE_DATA_FABRIC_GUIDE.md"

    def test_file_exists(self):
        assert self.path.exists(), "HYPERCUBE_DATA_FABRIC_GUIDE.md not found in docs/"

    def test_minimum_length(self):
        content = self.path.read_text(encoding="utf-8")
        assert len(content) > 500

    def test_contains_wave6_reference(self):
        content = self.path.read_text(encoding="utf-8")
        assert "Wave 6" in content or "wave-6" in content.lower()

    def test_contains_metatron_reference(self):
        content = self.path.read_text(encoding="utf-8")
        assert "Metatron" in content

    def test_contains_riemann_reference(self):
        content = self.path.read_text(encoding="utf-8")
        assert "Riemann" in content


# ===========================================================================
# T68 — Graph Export
# ===========================================================================

class TestGraphExport:
    def setup_method(self):
        path = DATA_DIR / "LATTICE_GRAPH_EXPORT.json"
        self.data = json.loads(path.read_text(encoding="utf-8"))

    def test_file_exists(self):
        assert (DATA_DIR / "LATTICE_GRAPH_EXPORT.json").exists()

    def test_context_present(self):
        assert "@context" in self.data

    def test_graph_present(self):
        assert "@graph" in self.data

    def test_node_count_positive(self):
        assert self.data["total_nodes"] > 0

    def test_edge_count_positive(self):
        assert self.data["total_edges"] > 0

    def test_graph_type(self):
        assert self.data["graph_type"] == "RainbowYinYangLattice"

    def test_schema_version(self):
        assert "schema_version" in self.data

    def test_all_graph_items_have_type(self):
        for item in self.data["@graph"]:
            assert "@type" in item


# ===========================================================================
# T69 — Query Engine
# ===========================================================================

class TestQueryEngine:
    def setup_method(self):
        self.engine = LatticeQueryEngine()

    def test_by_address_returns_result(self):
        result = self.engine.by_address(3, 7, 2)
        assert result is not None
        assert result.node_id == "N-03.07.02"

    def test_by_address_invalid_returns_none(self):
        result = self.engine.by_address(12, 0, 0)
        assert result is None

    def test_neighbors_count(self):
        neighbors = self.engine.neighbors(5, 5, 5, radius=1)
        # Manhattan distance 1 in 3D: 6 face neighbors
        assert len(neighbors) == 6

    def test_neighbors_sorted_by_score(self):
        neighbors = self.engine.neighbors(5, 5, 5, radius=2)
        scores = [n.score for n in neighbors]
        assert scores == sorted(scores, reverse=True)

    def test_riemann_spine_12_nodes(self):
        spine = self.engine.riemann_spine()
        assert len(spine) == 12

    def test_metatron_anchors_13_nodes(self):
        anchors = self.engine.metatron_anchors()
        assert len(anchors) == 13

    def test_path_start_to_end(self):
        path = self.engine.path((0, 0, 0), (3, 3, 3))
        assert path[0].node_id == "N-00.00.00"
        assert path[-1].node_id == "N-03.03.03"

    def test_path_length_manhattan(self):
        path = self.engine.path((0, 0, 0), (3, 0, 0))
        # Manhattan distance = 3, path = 4 nodes
        assert len(path) == 4

    def test_path_all_waypoints_valid(self):
        path = self.engine.path((0, 0, 0), (5, 5, 5))
        for node in path:
            assert node.score == 1.0

    def test_by_axis_value_ax01(self):
        results = self.engine.by_axis_value("AX-01", 3)
        assert len(results) > 0
        for r in results:
            assert r.coordinate.ax01_frequency == 3

    def test_by_coupling_strength_high(self):
        results = self.engine.by_coupling_strength("AX-01", "AX-06", 0.7)
        assert len(results) > 0

    def test_by_coupling_strength_low_returns_empty(self):
        # Force a non-existent high coupling
        results = self.engine.by_coupling_strength("AX-02", "AX-10", 0.99)
        assert results == []
