"""Deterministic Node-001 models.

Every model in this package is a pure function of sourced inputs. None of them
performs Monte Carlo, samples a distribution, or imputes an UNKNOWN.
"""

from __future__ import annotations

from typing import Any, Callable

from . import run0, run1_solar, run2_hydro, run3_compute, run4a_biometabolic, s02_bess
from . import receipts

#: run_id -> callable producing the run's result mapping.
RUN_REGISTRY: dict[str, Callable[[], dict[str, Any]]] = {
    "RUN_0": run0.baseline,
    "RUN_0.2": run0.operating_2025,
    "RUN_1": run1_solar.run,
    "RUN_2": run2_hydro.run,
    "RUN_3": run3_compute.run,
    "RUN_4A": run4a_biometabolic.run,
    "S02": s02_bess.run,
}

__all__ = [
    "RUN_REGISTRY",
    "run0",
    "run1_solar",
    "run2_hydro",
    "run3_compute",
    "run4a_biometabolic",
    "s02_bess",
    "receipts",
]
