"""S02 — BESS equivalence transfer function.

Reproduces the derived numerics of S02_BESS_TRANSFER_FUNCTION_v0_1.json.

Invariants exercised here:
  * baseline credit is ZERO: no hourly PV/load/curtailment trace exists, so no
    BESS size is recommended;
  * daily-average equivalence is not an optimum, dispatch result, autonomy
    claim, or curtailment estimate;
  * BESS power (MW) is a separate quantity from BESS energy (MWh).
"""

from __future__ import annotations

from typing import Any

from .common import UNKNOWN, require_number

DAYS_PER_YEAR = 365.0
S01_A_ANNUAL_GWH = 2.70619355
S01_B_ANNUAL_GWH = 2.917982611

ILLUSTRATIVE_BESS_MWH = (4.0, 8.0)

REQUIRED_FIRST_DATA = (
    "hourly PV AC output",
    "hourly plant load",
    "curtailment/export",
    "water demand/storage",
    "compute flexible-load trace",
)


def average_solar_mwh_day(annual_gwh: float) -> float:
    """Annual generation expressed as a daily average."""
    gwh = require_number(annual_gwh, "annual_gwh")
    return gwh * 1000.0 / DAYS_PER_YEAR


def equivalence(bess_mwh: float) -> dict[str, Any]:
    """Days-of-average-solar equivalence for one BESS energy size."""
    size = require_number(bess_mwh, "bess_mwh")
    if size < 0:
        raise ValueError("bess_mwh must be non-negative")
    return {
        "BESS_MWh": size,
        "days_of_average_S01_A": size / average_solar_mwh_day(S01_A_ANNUAL_GWH),
        "days_of_average_S01_B": size / average_solar_mwh_day(S01_B_ANNUAL_GWH),
    }


def run() -> dict[str, Any]:
    """S02 — equivalence table with a hard zero baseline credit."""
    return {
        "artifact_id": "DJK-NODE-001-S02-BESS-v0.1",
        "status": "EXECUTED_EQUIVALENCE_TRANSFER_FUNCTION_NON_CANON",
        "baseline_credit": 0,
        "reason": "No hourly PV/load/curtailment trace exists, so no BESS size is recommended.",
        "S01_annual_generation_GWh": {"A": S01_A_ANNUAL_GWH, "B": S01_B_ANNUAL_GWH},
        "average_solar_energy_MWh_day": {
            "A": average_solar_mwh_day(S01_A_ANNUAL_GWH),
            "B": average_solar_mwh_day(S01_B_ANNUAL_GWH),
        },
        "intuitive_energy_only_equivalence": [equivalence(mwh) for mwh in ILLUSTRATIVE_BESS_MWH],
        "guardrails": [
            "Daily-average equivalence is not an optimum, dispatch result, autonomy claim, or curtailment estimate.",
            "BESS power MW matters separately from energy MWh.",
            "Round-trip efficiency, SOC reserve, degradation and grid-services use must be included once sourced.",
            "Water storage, flexible compute, thermal storage and direct green power compete with BESS as alternative buffers.",
            "No BESS benefit is credited until measured hourly mismatch demonstrates a service.",
        ],
        "required_first_data": list(REQUIRED_FIRST_DATA),
        "output_rule": "Return sensitivity/transfer functions until measured time-series data exist.",
    }
