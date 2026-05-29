"""
lattice_hypercube.py

Lattice Hypercube 12×12×12 — Periodic Table 2.0
Reference implementation: 1,728-node unified-field knowledge structure.

Structure:
  Axis X (0-11): Knowledge House (domain)
  Axis Y (0-11): Sphere within House (sub-domain)
  Axis Z (0-11): Property Dimension (acoustic, neuromorphic, quantum, ...)

Node address: H{x}.S{y}.P{z}
Total nodes:  12 × 12 × 12 = 1,728

Acoustic base: A4 = 432 Hz (universal fundamental)
Neuromorphic:  STDP / Hebbian weight model
Unified field: 12 orthogonal property axes per (house, sphere) pair

Apache 2.0 — public gift to the world from @atlaslattice.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Iterator


# ---------------------------------------------------------------------------
# Axis Enumerations
# ---------------------------------------------------------------------------

class House(IntEnum):
    """X-axis: 12 Knowledge Houses."""
    NATURAL_SCIENCES = 0
    FORMAL_SCIENCES = 1
    SOCIAL_SCIENCES = 2
    HUMANITIES = 3
    ARTS = 4
    ENGINEERING_TECHNOLOGY = 5
    MEDICINE_HEALTH = 6
    EDUCATION = 7
    BUSINESS_ECONOMICS = 8
    LAW_POLITICS = 9
    RELIGION_PHILOSOPHY = 10
    INTERDISCIPLINARY = 11


HOUSE_LABELS: dict[int, str] = {
    0: "Natural Sciences",
    1: "Formal Sciences",
    2: "Social Sciences",
    3: "Humanities",
    4: "Arts",
    5: "Engineering & Technology",
    6: "Medicine & Health",
    7: "Education",
    8: "Business & Economics",
    9: "Law & Politics",
    10: "Religion & Philosophy",
    11: "Interdisciplinary",
}


class PropertyDim(IntEnum):
    """Z-axis: 12 Unified-Field Property Dimensions."""
    ACOUSTIC = 0        # Vibrational / resonance (base 432 Hz)
    NEUROMORPHIC = 1    # Spike-timing / synaptic plasticity
    QUANTUM = 2         # Superposition / entanglement / decoherence
    ELECTROMAGNETIC = 3 # Frequency band / photon energy
    THERMAL = 4         # Entropy / phase state / temperature
    GRAVITATIONAL = 5   # Mass-energy density / spacetime curvature
    CHEMICAL = 6        # Bond class / periodicity / valence
    BIOLOGICAL = 7      # Metabolic / evolutionary / cellular
    COMPUTATIONAL = 8   # Kolmogorov complexity / algorithmic depth
    SOCIAL = 9          # Diffusion / governance / memetic weight
    TEMPORAL = 10       # Causal chain / phase-transition / decay
    PHENOMENOLOGICAL = 11  # Integrated information Φ / qualia / awareness


PROPERTY_LABELS: dict[int, str] = {
    0: "Acoustic/Vibrational",
    1: "Neuromorphic/Cognitive",
    2: "Quantum/Wave-function",
    3: "Electromagnetic",
    4: "Thermal/Entropic",
    5: "Gravitational/Spacetime",
    6: "Chemical/Molecular",
    7: "Biological/Metabolic",
    8: "Computational/Informational",
    9: "Social/Memetic",
    10: "Temporal/Causal",
    11: "Phenomenological/Conscious",
}

# Electromagnetic band classification by (house × sphere) index
_EM_BANDS = [
    "radio", "microwave", "infrared", "near-infrared",
    "visible-red", "visible-green", "visible-blue", "ultraviolet",
    "soft-x-ray", "hard-x-ray", "gamma", "cosmic",
]

# Thermal phase classes by sphere index
_THERMAL_CLASSES = [
    "absolute-zero", "cryogenic", "solid", "liquid",
    "gas", "plasma", "Bose-Einstein", "Fermi-gas",
    "supercritical", "degenerate", "quark-gluon", "Planck",
]


# ---------------------------------------------------------------------------
# Acoustic Resonance
# ---------------------------------------------------------------------------

ACOUSTIC_BASE_HZ: float = 432.0  # A4 = 432 Hz (universal fundamental)


def acoustic_frequency(house: int, sphere: int) -> float:
    """
    Return the fundamental acoustic frequency (Hz) for a (house, sphere) pair.

    Formula: f = 432 × 2^(house/12) × (sphere+1)/12
    This maps the full 144-sphere lattice across the audible spectrum
    (approximately 36 Hz – 3,456 Hz) using equal-temperament octave
    scaling per house and harmonic step scaling per sphere.
    """
    return ACOUSTIC_BASE_HZ * (2.0 ** (house / 12.0)) * ((sphere + 1) / 12.0)


def harmonic_series(base_hz: float, n: int = 6) -> list[float]:
    """Return the first n harmonics of a fundamental frequency."""
    return [base_hz * k for k in range(1, n + 1)]


def beat_frequency(f1: float, f2: float) -> float:
    """Return the beat frequency between two tones (absolute difference)."""
    return abs(f1 - f2)


def are_resonant(f1: float, f2: float, threshold_hz: float = 1.0) -> bool:
    """True if two frequencies are within threshold_hz of each other (beat coupling)."""
    return beat_frequency(f1, f2) < threshold_hz


# ---------------------------------------------------------------------------
# Neuromorphic Weights
# ---------------------------------------------------------------------------

def neuromorphic_weight(degree: int, max_degree: int, domain_centrality: float) -> float:
    """
    Compute STDP-inspired synaptic weight for a node.

    w = tanh(degree / max_degree) × domain_centrality

    Args:
        degree: number of cross-links from this node
        max_degree: maximum degree across all nodes (for normalisation)
        domain_centrality: PageRank-style centrality [0.0, 1.0]

    Returns:
        Synaptic weight in [0.0, 1.0].
    """
    if max_degree <= 0:
        return 0.0
    raw = math.tanh(degree / max_degree) * domain_centrality
    return max(0.0, min(1.0, raw))


def phi_estimate(house: int, sphere: int, property_dim: int) -> float:
    """
    Integrated Information Theory Φ proxy for a node.

    Uses a geometric mean of normalised axis coordinates to approximate
    the degree to which the node integrates information across dimensions.
    Ranges from 0.0 (edge / isolated) to 1.0 (centre of the hypercube).
    """
    nx = house / 11.0
    ny = sphere / 11.0
    nz = property_dim / 11.0
    # Geometric mean, inverted so that the central node (0.5, 0.5, 0.5) → ~1.0
    centred = (1.0 - abs(nx - 0.5) * 2) * (1.0 - abs(ny - 0.5) * 2) * (1.0 - abs(nz - 0.5) * 2)
    return max(0.0, min(1.0, centred))


# ---------------------------------------------------------------------------
# Node & Hypercube
# ---------------------------------------------------------------------------

@dataclass
class LatticeNode:
    """
    A single node in the 12×12×12 Lattice Hypercube.

    Address: H{house}.S{sphere}.P{property_dim}
    """
    house: int          # 0-11
    sphere: int         # 0-11 (local index within house)
    property_dim: int   # 0-11

    # Derived / computed fields
    label: str = field(default="")
    acoustic_hz: float = field(default=0.0)
    neuromorphic_weight: float = field(default=0.0)
    quantum_coherence: float = field(default=0.5)
    em_band: str = field(default="")
    thermal_class: str = field(default="")
    complexity_bits: int = field(default=0)
    phi: float = field(default=0.0)
    canon_status: str = field(default="CANDIDATE")
    edges: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.label:
            house_label = HOUSE_LABELS.get(self.house, f"H{self.house}")
            prop_label = PROPERTY_LABELS.get(self.property_dim, f"P{self.property_dim}")
            self.label = f"{house_label} / Sphere {self.sphere} / {prop_label}"
        if self.acoustic_hz == 0.0:
            self.acoustic_hz = acoustic_frequency(self.house, self.sphere)
        if self.phi == 0.0:
            self.phi = phi_estimate(self.house, self.sphere, self.property_dim)
        if not self.em_band:
            self.em_band = _EM_BANDS[(self.house * 12 + self.sphere) % 12]
        if not self.thermal_class:
            self.thermal_class = _THERMAL_CLASSES[self.sphere % 12]
        if self.complexity_bits == 0:
            # Heuristic: higher-index dimensions tend toward greater complexity
            self.complexity_bits = 8 + self.house * 3 + self.sphere + self.property_dim * 2

    @property
    def node_id(self) -> str:
        """Canonical node address string: H{x}.S{y}.P{z}"""
        return f"H{self.house}.S{self.sphere}.P{self.property_dim}"

    def harmonics(self, n: int = 6) -> list[float]:
        """Return first n harmonics of this node's acoustic frequency."""
        return harmonic_series(self.acoustic_hz, n)

    def is_resonant_with(self, other: "LatticeNode", threshold_hz: float = 1.0) -> bool:
        """True if this node's acoustic frequency beats with another's."""
        return are_resonant(self.acoustic_hz, other.acoustic_hz, threshold_hz)

    def __repr__(self) -> str:
        return (
            f"LatticeNode({self.node_id}, "
            f"acoustic={self.acoustic_hz:.2f}Hz, "
            f"phi={self.phi:.3f})"
        )


class LatticeHypercube:
    """
    The full 12×12×12 Lattice Hypercube — 1,728 nodes.

    Periodic Table 2.0: every domain of human knowledge mapped against
    every property of matter, energy, and mind.
    """

    SIDE: int = 12
    NODE_COUNT: int = SIDE ** 3  # 1,728

    def __init__(self) -> None:
        self._nodes: dict[str, LatticeNode] = {}
        self._build()
        self._wire_edges()

    # ------------------------------------------------------------------
    # Construction
    # ------------------------------------------------------------------

    def _build(self) -> None:
        """Instantiate all 1,728 nodes."""
        for x in range(self.SIDE):
            for y in range(self.SIDE):
                for z in range(self.SIDE):
                    node = LatticeNode(house=x, sphere=y, property_dim=z)
                    self._nodes[node.node_id] = node

    def _wire_edges(self) -> None:
        """
        Add minimal structural edges:
        - Z-axis edges: every node connects to its Z±1 neighbours (property traversal)
        - Y-axis edges: every node connects to its Y±1 neighbours (sphere traversal)
        - X-axis edges: every node connects to its X±1 neighbours (house traversal)
        This ensures zero orphan nodes and full hypercube connectivity.
        """
        for node in self._nodes.values():
            x, y, z = node.house, node.sphere, node.property_dim
            for dx, dy, dz in [
                (1, 0, 0), (-1, 0, 0),
                (0, 1, 0), (0, -1, 0),
                (0, 0, 1), (0, 0, -1),
            ]:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < self.SIDE and 0 <= ny < self.SIDE and 0 <= nz < self.SIDE:
                    neighbour_id = f"H{nx}.S{ny}.P{nz}"
                    if neighbour_id not in node.edges:
                        node.edges.append(neighbour_id)

        # Update neuromorphic weights now that edges are known
        max_deg = max(len(n.edges) for n in self._nodes.values())
        for node in self._nodes.values():
            # Domain centrality proxy: centre nodes score higher
            centrality = phi_estimate(node.house, node.sphere, node.property_dim)
            node.neuromorphic_weight = neuromorphic_weight(
                len(node.edges), max_deg, max(centrality, 0.01)
            )

    # ------------------------------------------------------------------
    # Access
    # ------------------------------------------------------------------

    def node(self, house: int, sphere: int, property_dim: int) -> LatticeNode:
        """Retrieve a node by (house, sphere, property_dim) coordinates."""
        return self._nodes[f"H{house}.S{sphere}.P{property_dim}"]

    def node_by_id(self, node_id: str) -> LatticeNode:
        """Retrieve a node by its canonical ID string."""
        return self._nodes[node_id]

    def __iter__(self) -> Iterator[LatticeNode]:
        return iter(self._nodes.values())

    def __len__(self) -> int:
        return len(self._nodes)

    # ------------------------------------------------------------------
    # Slices
    # ------------------------------------------------------------------

    def house_slice(self, house: int) -> list[LatticeNode]:
        """All 144 nodes in a given House (X-axis slice)."""
        return [n for n in self if n.house == house]

    def sphere_slice(self, house: int, sphere: int) -> list[LatticeNode]:
        """All 12 property-dimension nodes for a (house, sphere) pair."""
        return [n for n in self if n.house == house and n.sphere == sphere]

    def property_slice(self, property_dim: int) -> list[LatticeNode]:
        """All 144 nodes with a given Property Dimension (Z-axis slice)."""
        return [n for n in self if n.property_dim == property_dim]

    # ------------------------------------------------------------------
    # Acoustic queries
    # ------------------------------------------------------------------

    def acoustic_slice(self) -> list[LatticeNode]:
        """All 144 acoustic-dimension nodes (Z=0)."""
        return self.property_slice(PropertyDim.ACOUSTIC)

    def find_resonant_pairs(
        self, threshold_hz: float = 1.0, property_dim: int = PropertyDim.ACOUSTIC
    ) -> list[tuple[LatticeNode, LatticeNode]]:
        """
        Find all node pairs in a property-dim slice whose acoustic
        frequencies produce a beat frequency below threshold_hz.
        """
        nodes = self.property_slice(property_dim)
        pairs: list[tuple[LatticeNode, LatticeNode]] = []
        for i, a in enumerate(nodes):
            for b in nodes[i + 1 :]:
                if are_resonant(a.acoustic_hz, b.acoustic_hz, threshold_hz):
                    pairs.append((a, b))
        return pairs

    # ------------------------------------------------------------------
    # Neuromorphic queries
    # ------------------------------------------------------------------

    def neuromorphic_slice(self) -> list[LatticeNode]:
        """All 144 neuromorphic-dimension nodes (Z=1)."""
        return self.property_slice(PropertyDim.NEUROMORPHIC)

    def top_neuromorphic_nodes(self, k: int = 12) -> list[LatticeNode]:
        """Return the k nodes with highest neuromorphic weight."""
        return sorted(self, key=lambda n: n.neuromorphic_weight, reverse=True)[:k]

    # ------------------------------------------------------------------
    # Unified-field queries
    # ------------------------------------------------------------------

    def unified_field_vector(self, house: int, sphere: int) -> dict[str, float]:
        """
        Return a 12-dimensional property vector for a (house, sphere) pair.
        Keys are property dimension labels; values are dimension-specific
        scalar readings.
        """
        result: dict[str, float] = {}
        for z in range(self.SIDE):
            node = self.node(house, sphere, z)
            label = PROPERTY_LABELS[z]
            if z == PropertyDim.ACOUSTIC:
                result[label] = node.acoustic_hz
            elif z == PropertyDim.NEUROMORPHIC:
                result[label] = node.neuromorphic_weight
            elif z == PropertyDim.PHENOMENOLOGICAL:
                result[label] = node.phi
            elif z == PropertyDim.COMPUTATIONAL:
                result[label] = float(node.complexity_bits)
            else:
                result[label] = node.phi  # generalised Φ proxy for other dims
        return result

    def phi_centre(self) -> LatticeNode:
        """
        Return the Metatron's Cube Φ-centre node: H6.S6.P6
        (Medicine / Sphere 6 / Computational).
        """
        return self.node(6, 6, 6)

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def stats(self) -> dict:
        """Summary statistics for the full hypercube."""
        freqs = [n.acoustic_hz for n in self.acoustic_slice()]
        weights = [n.neuromorphic_weight for n in self.neuromorphic_slice()]
        phis = [n.phi for n in self]
        return {
            "total_nodes": len(self),
            "acoustic_min_hz": min(freqs),
            "acoustic_max_hz": max(freqs),
            "acoustic_mean_hz": sum(freqs) / len(freqs),
            "neuromorphic_weight_mean": sum(weights) / len(weights),
            "phi_mean": sum(phis) / len(phis),
            "phi_centre": self.phi_centre().phi,
            "total_edges": sum(len(n.edges) for n in self),
            "orphan_nodes": sum(1 for n in self if not n.edges),
        }
