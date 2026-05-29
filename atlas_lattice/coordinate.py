"""H-S-N coordinate system for the Atlas Lattice 12×12×12 hypercube."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional

# 12 House labels (A-axis: major knowledge domain)
HOUSE_NAMES = [
    "Governance Core",           # H01
    "Canon & Adjudication",      # H02
    "Provenance & Receipts",     # H03
    "Information Architecture",  # H04
    "Documentation Excellence",  # H05
    "Security, Trust, Integrity",# H06
    "Testing & Validation",      # H07
    "CI/CD & Automation",        # H08
    "Knowledge Graph",           # H09
    "Public Packaging & Releases",# H10
    "Community & Contributors",  # H11
    "Ops & Living Archive",      # H12
]

# 12 Sphere labels (B-axis: operator / layer)
SPHERE_NAMES = [
    "Foundation",       # S01
    "Structure",        # S02
    "Process",          # S03
    "Interface",        # S04
    "Evidence",         # S05
    "Review",           # S06
    "Validation",       # S07
    "Publication",      # S08
    "Knowledge Graph",  # S09
    "Integration",      # S10
    "Archive",          # S11
    "Promotion",        # S12
]

# 12 Node labels (C-axis: local state / primitive)
NODE_NAMES = [
    "Seed",         # N01
    "Artifact",     # N02
    "Schema",       # N03
    "Receipt",      # N04
    "Claim",        # N05
    "Evidence",     # N06
    "Review",       # N07
    "Ratified",     # N08
    "Canon",        # N09
    "Quarantine",   # N10
    "Missing",      # N11
    "Superseded",   # N12
]

_COORD_RE = re.compile(r"^H(\d{1,2})-S(\d{1,2})-N(\d{1,2})$", re.IGNORECASE)


@dataclass(frozen=True)
class HSNAxis:
    """One axis value (1-based index + label)."""
    index: int
    label: str

    def __str__(self) -> str:
        return self.label


@dataclass(frozen=True)
class Coordinate:
    """An H-S-N lattice coordinate in the 12×12×12 Atlas Lattice.

    All indices are 1-based (1..12).
    """

    house: int
    sphere: int
    node: int

    # ------------------------------------------------------------------ #
    # Constructors                                                         #
    # ------------------------------------------------------------------ #

    @classmethod
    def parse(cls, text: str) -> "Coordinate":
        """Parse a coordinate string such as ``H04-S09-N02``.

        Raises:
            ValueError: if the string is not a valid H-S-N coordinate.
        """
        m = _COORD_RE.match(text.strip())
        if not m:
            raise ValueError(
                f"Invalid H-S-N coordinate: {text!r}. "
                "Expected format: H##-S##-N## (e.g. H04-S09-N02)"
            )
        h, s, n = int(m.group(1)), int(m.group(2)), int(m.group(3))
        for name, val in (("H", h), ("S", s), ("N", n)):
            if not 1 <= val <= 12:
                raise ValueError(f"{name} index must be 1–12, got {val}")
        return cls(house=h, sphere=s, node=n)

    @classmethod
    def from_indices(cls, house: int, sphere: int, node: int) -> "Coordinate":
        """Create a coordinate from 1-based integer indices."""
        return cls.parse(f"H{house:02d}-S{sphere:02d}-N{node:02d}")

    # ------------------------------------------------------------------ #
    # Properties                                                           #
    # ------------------------------------------------------------------ #

    @property
    def address(self) -> str:
        """Canonical string address, e.g. ``H04-S09-N02``."""
        return f"H{self.house:02d}-S{self.sphere:02d}-N{self.node:02d}"

    @property
    def house_label(self) -> str:
        return HOUSE_NAMES[self.house - 1]

    @property
    def sphere_label(self) -> str:
        return SPHERE_NAMES[self.sphere - 1]

    @property
    def node_label(self) -> str:
        return NODE_NAMES[self.node - 1]

    @property
    def cell_index(self) -> int:
        """0-based linear index in the 1728-cell hypercube."""
        return (self.house - 1) * 144 + (self.sphere - 1) * 12 + (self.node - 1)

    # ------------------------------------------------------------------ #
    # Representation                                                       #
    # ------------------------------------------------------------------ #

    def __str__(self) -> str:
        return (
            f"{self.address} — "
            f"{self.house_label} · {self.sphere_label} · {self.node_label}"
        )

    def __repr__(self) -> str:
        return f"Coordinate(house={self.house}, sphere={self.sphere}, node={self.node})"

    # ------------------------------------------------------------------ #
    # Utility                                                              #
    # ------------------------------------------------------------------ #

    def to_dict(self) -> dict:
        """Serialize to a plain dict."""
        return {
            "address": self.address,
            "house": {"index": self.house, "label": self.house_label},
            "sphere": {"index": self.sphere, "label": self.sphere_label},
            "node": {"index": self.node, "label": self.node_label},
            "cell_index": self.cell_index,
        }
