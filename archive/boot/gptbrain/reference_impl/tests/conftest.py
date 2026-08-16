"""
pytest configuration for the tests/ subdirectory.

Adds the parent reference_impl/ directory to sys.path so that
`dream_memory_palace_reference_impl` can be imported without installation.
"""
from __future__ import annotations
import sys
from pathlib import Path

# reference_impl/ is the parent of this tests/ directory
sys.path.insert(0, str(Path(__file__).parent.parent))
