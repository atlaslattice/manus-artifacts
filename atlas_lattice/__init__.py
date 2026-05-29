"""
atlas-lattice: H-S-N coordinate system for the 12×12×12 Atlas Lattice knowledge graph.

Quick start::

    from atlas_lattice import Coordinate
    coord = Coordinate.parse("H04-S09-N02")
    print(coord)

CLI::

    python -m atlas_lattice lookup H04-S09-N02
    python -m atlas_lattice axes
"""

from .coordinate import Coordinate, HSNAxis, HOUSE_NAMES, SPHERE_NAMES, NODE_NAMES

__version__ = "0.1.0"
__all__ = ["Coordinate", "HSNAxis", "HOUSE_NAMES", "SPHERE_NAMES", "NODE_NAMES"]
