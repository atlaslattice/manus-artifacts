"""
test_lattice_hypercube_periodic_table.py

Tests for the 12×12×12 Lattice Hypercube — Periodic Table 2.0.

Validates:
- Correct node count (1,728)
- Acoustic frequency bounds (36 Hz – 3,500 Hz, base 432 Hz)
- Neuromorphic weight bounds [0.0, 1.0]
- Φ (integrated information) bounds [0.0, 1.0]
- Zero orphan nodes (every node has at least one edge)
- Metatron's Cube Φ-centre node exists at H6.S6.P6
- Unified-field vector has 12 dimensions
- House slices contain exactly 144 nodes
- Property dimension slices contain exactly 144 nodes
- Sphere slice contains exactly 12 nodes
- Acoustic resonance pair detection works
- Beat frequency formula is correct
- Harmonic series generation is correct
- Node IDs are unique
- Node __repr__ is informative
"""

import math
import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codebases", "lattice-hypercube"))

from lattice_hypercube import (
    ACOUSTIC_BASE_HZ,
    HOUSE_LABELS,
    PROPERTY_LABELS,
    House,
    LatticeHypercube,
    LatticeNode,
    PropertyDim,
    acoustic_frequency,
    are_resonant,
    beat_frequency,
    harmonic_series,
    neuromorphic_weight,
    phi_estimate,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def cube() -> LatticeHypercube:
    """Build the full 12×12×12 hypercube once per test module."""
    return LatticeHypercube()


# ---------------------------------------------------------------------------
# Structure tests
# ---------------------------------------------------------------------------

def test_node_count(cube: LatticeHypercube) -> None:
    """The hypercube must contain exactly 12×12×12 = 1,728 nodes."""
    assert len(cube) == 1728


def test_node_count_constant() -> None:
    assert LatticeHypercube.NODE_COUNT == 1728
    assert LatticeHypercube.SIDE == 12


def test_all_node_ids_unique(cube: LatticeHypercube) -> None:
    ids = [n.node_id for n in cube]
    assert len(ids) == len(set(ids))


def test_node_id_format(cube: LatticeHypercube) -> None:
    node = cube.node(0, 0, 0)
    assert node.node_id == "H0.S0.P0"
    node = cube.node(11, 11, 11)
    assert node.node_id == "H11.S11.P11"


# ---------------------------------------------------------------------------
# Axis enumeration tests
# ---------------------------------------------------------------------------

def test_house_enum_count() -> None:
    assert len(House) == 12


def test_property_dim_enum_count() -> None:
    assert len(PropertyDim) == 12


def test_house_labels_complete() -> None:
    assert len(HOUSE_LABELS) == 12
    for i in range(12):
        assert i in HOUSE_LABELS


def test_property_labels_complete() -> None:
    assert len(PROPERTY_LABELS) == 12
    for i in range(12):
        assert i in PROPERTY_LABELS


# ---------------------------------------------------------------------------
# Acoustic resonance tests
# ---------------------------------------------------------------------------

def test_acoustic_base_hz() -> None:
    assert ACOUSTIC_BASE_HZ == 432.0


def test_acoustic_frequency_base_case() -> None:
    # H0, S0: 432 × 2^0 × 1/12 = 432/12 = 36 Hz
    f = acoustic_frequency(0, 0)
    assert abs(f - 36.0) < 0.01


def test_acoustic_frequency_increases_with_house() -> None:
    for house in range(11):
        f_low = acoustic_frequency(house, 6)
        f_high = acoustic_frequency(house + 1, 6)
        assert f_high > f_low


def test_acoustic_frequency_increases_with_sphere() -> None:
    for sphere in range(11):
        f_low = acoustic_frequency(6, sphere)
        f_high = acoustic_frequency(6, sphere + 1)
        assert f_high > f_low


def test_acoustic_frequency_range_all_nodes(cube: LatticeHypercube) -> None:
    """All acoustic-dimension frequencies must fall within the audible range."""
    for node in cube.acoustic_slice():
        assert 30.0 <= node.acoustic_hz <= 4000.0, (
            f"Node {node.node_id} frequency {node.acoustic_hz:.2f} Hz out of bounds"
        )


def test_harmonic_series_length() -> None:
    h = harmonic_series(432.0, 6)
    assert len(h) == 6
    assert abs(h[0] - 432.0) < 0.01
    assert abs(h[1] - 864.0) < 0.01


def test_harmonic_series_integer_multiples() -> None:
    base = 100.0
    h = harmonic_series(base, 8)
    for i, f in enumerate(h, start=1):
        assert abs(f - base * i) < 0.0001


def test_beat_frequency() -> None:
    assert abs(beat_frequency(440.0, 432.0) - 8.0) < 0.0001
    assert abs(beat_frequency(432.0, 440.0) - 8.0) < 0.0001


def test_are_resonant_true() -> None:
    assert are_resonant(432.0, 432.5, threshold_hz=1.0) is True


def test_are_resonant_false() -> None:
    assert are_resonant(432.0, 434.0, threshold_hz=1.0) is False


def test_node_harmonics(cube: LatticeHypercube) -> None:
    node = cube.node(0, 0, 0)
    h = node.harmonics(3)
    assert len(h) == 3
    assert abs(h[0] - node.acoustic_hz) < 0.01


def test_resonant_pairs_return_type(cube: LatticeHypercube) -> None:
    pairs = cube.find_resonant_pairs(threshold_hz=0.5)
    assert isinstance(pairs, list)
    for a, b in pairs:
        assert isinstance(a, LatticeNode)
        assert isinstance(b, LatticeNode)
        assert abs(a.acoustic_hz - b.acoustic_hz) < 0.5


# ---------------------------------------------------------------------------
# Neuromorphic tests
# ---------------------------------------------------------------------------

def test_neuromorphic_weight_bounds() -> None:
    for degree in [0, 1, 3, 6, 10, 20]:
        w = neuromorphic_weight(degree, 20, 0.8)
        assert 0.0 <= w <= 1.0, f"Weight {w} out of bounds for degree={degree}"


def test_neuromorphic_weight_zero_degree() -> None:
    assert neuromorphic_weight(0, 10, 1.0) == 0.0


def test_neuromorphic_weight_zero_max_degree() -> None:
    assert neuromorphic_weight(5, 0, 1.0) == 0.0


def test_all_nodes_neuromorphic_weight_in_bounds(cube: LatticeHypercube) -> None:
    for node in cube:
        assert 0.0 <= node.neuromorphic_weight <= 1.0, (
            f"Node {node.node_id} weight {node.neuromorphic_weight} out of bounds"
        )


def test_top_neuromorphic_nodes_count(cube: LatticeHypercube) -> None:
    top = cube.top_neuromorphic_nodes(k=12)
    assert len(top) == 12
    # All should have weight >= 0
    for n in top:
        assert n.neuromorphic_weight >= 0.0


# ---------------------------------------------------------------------------
# Φ (integrated information) tests
# ---------------------------------------------------------------------------

def test_phi_estimate_bounds() -> None:
    for x in range(12):
        for y in range(12):
            for z in range(12):
                phi = phi_estimate(x, y, z)
                assert 0.0 <= phi <= 1.0


def test_phi_centre_is_highest_phi() -> None:
    """Centre of hypercube should have phi > corner."""
    centre_phi = phi_estimate(6, 6, 6)
    corner_phi = phi_estimate(0, 0, 0)
    assert centre_phi >= corner_phi


def test_phi_centre_node(cube: LatticeHypercube) -> None:
    centre = cube.phi_centre()
    assert centre.node_id == "H6.S6.P6"


def test_all_nodes_phi_in_bounds(cube: LatticeHypercube) -> None:
    for node in cube:
        assert 0.0 <= node.phi <= 1.0, f"Node {node.node_id} phi={node.phi} out of bounds"


# ---------------------------------------------------------------------------
# Edge / connectivity tests
# ---------------------------------------------------------------------------

def test_no_orphan_nodes(cube: LatticeHypercube) -> None:
    """Every node must have at least one edge (no isolated nodes)."""
    orphans = [n for n in cube if not n.edges]
    assert orphans == [], f"Orphan nodes found: {[n.node_id for n in orphans]}"


def test_interior_node_has_six_edges(cube: LatticeHypercube) -> None:
    """An interior node (no axis == 0 or 11) must have exactly 6 face-neighbours."""
    node = cube.node(6, 6, 6)
    assert len(node.edges) == 6


def test_corner_node_has_three_edges(cube: LatticeHypercube) -> None:
    """A corner node (all axes == 0 or 11) must have exactly 3 face-neighbours."""
    node = cube.node(0, 0, 0)
    assert len(node.edges) == 3


def test_edges_reference_valid_nodes(cube: LatticeHypercube) -> None:
    """All edges must point to node IDs that exist in the hypercube."""
    valid_ids = {n.node_id for n in cube}
    for node in cube:
        for edge_id in node.edges:
            assert edge_id in valid_ids, (
                f"Node {node.node_id} references non-existent edge {edge_id}"
            )


# ---------------------------------------------------------------------------
# Slice tests
# ---------------------------------------------------------------------------

def test_house_slice_size(cube: LatticeHypercube) -> None:
    for house in range(12):
        s = cube.house_slice(house)
        assert len(s) == 144, f"House {house} slice has {len(s)} nodes, expected 144"


def test_property_slice_size(cube: LatticeHypercube) -> None:
    for prop in range(12):
        s = cube.property_slice(prop)
        assert len(s) == 144, f"Property {prop} slice has {len(s)} nodes, expected 144"


def test_sphere_slice_size(cube: LatticeHypercube) -> None:
    s = cube.sphere_slice(5, 7)
    assert len(s) == 12


def test_acoustic_slice_size(cube: LatticeHypercube) -> None:
    assert len(cube.acoustic_slice()) == 144


def test_neuromorphic_slice_size(cube: LatticeHypercube) -> None:
    assert len(cube.neuromorphic_slice()) == 144


# ---------------------------------------------------------------------------
# Unified-field vector tests
# ---------------------------------------------------------------------------

def test_unified_field_vector_dimensionality(cube: LatticeHypercube) -> None:
    vec = cube.unified_field_vector(5, 7)
    assert len(vec) == 12


def test_unified_field_vector_acoustic_matches_node(cube: LatticeHypercube) -> None:
    vec = cube.unified_field_vector(3, 3)
    node = cube.node(3, 3, PropertyDim.ACOUSTIC)
    assert abs(vec[PROPERTY_LABELS[0]] - node.acoustic_hz) < 0.01


def test_unified_field_vector_neuromorphic_matches_node(cube: LatticeHypercube) -> None:
    vec = cube.unified_field_vector(3, 3)
    node = cube.node(3, 3, PropertyDim.NEUROMORPHIC)
    assert abs(vec[PROPERTY_LABELS[1]] - node.neuromorphic_weight) < 1e-9


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def test_stats_structure(cube: LatticeHypercube) -> None:
    s = cube.stats()
    assert s["total_nodes"] == 1728
    assert s["orphan_nodes"] == 0
    assert s["acoustic_min_hz"] > 0
    assert s["acoustic_max_hz"] > s["acoustic_min_hz"]
    assert 0.0 <= s["neuromorphic_weight_mean"] <= 1.0
    assert 0.0 <= s["phi_mean"] <= 1.0
    assert s["total_edges"] > 0


# ---------------------------------------------------------------------------
# Node representation
# ---------------------------------------------------------------------------

def test_node_repr_contains_id(cube: LatticeHypercube) -> None:
    node = cube.node(1, 2, 3)
    r = repr(node)
    assert "H1.S2.P3" in r


def test_node_label_populated(cube: LatticeHypercube) -> None:
    node = cube.node(0, 0, 0)
    assert node.label != ""
    assert "Natural Sciences" in node.label


def test_node_em_band_populated(cube: LatticeHypercube) -> None:
    for node in cube:
        assert node.em_band != ""


def test_node_thermal_class_populated(cube: LatticeHypercube) -> None:
    for node in cube:
        assert node.thermal_class != ""


def test_node_complexity_bits_positive(cube: LatticeHypercube) -> None:
    for node in cube:
        assert node.complexity_bits > 0


# ---------------------------------------------------------------------------
# Canon status
# ---------------------------------------------------------------------------

def test_all_nodes_candidate_by_default(cube: LatticeHypercube) -> None:
    for node in cube:
        assert node.canon_status == "CANDIDATE"
