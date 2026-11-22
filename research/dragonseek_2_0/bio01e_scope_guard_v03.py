#!/usr/bin/env python3
"""DJK-001 research-only accounting guards.

No plant connection, no official approval, no inferred feedstock availability.
This deliberately independent prototype does NOT replace simulator_v2.py.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Optional


class Scope(str, Enum):
    SHANDONG = "SHANDONG_PROVINCE"
    QINGDAO = "QINGDAO_CITY"
    WEST_COAST = "WEST_COAST_NEW_AREA"
    DONGJIAKOU = "DONGJIAKOU_ECONOMIC_AREA"


class Evidence(str, Enum):
    MEASURED = "MEASURED"
    REPORTED = "REPORTED"
    DESIGNED = "DESIGNED"
    SCENARIO = "SCENARIO"
    UNKNOWN = "UNKNOWN"
    QUARANTINED = "QUARANTINED"


@dataclass(frozen=True)
class MaterialRecord:
    event_id: str
    scope: Scope
    year: int
    material: str
    wet_t: Optional[float]
    evidence: Evidence
    source: str
    unit: str = "tonne_wet"
    prior_allocation_t: float = 0.0

    def validate(self) -> None:
        if not self.event_id or not self.material or not self.source:
            raise ValueError("Missing material event provenance")
        if self.unit != "tonne_wet":
            raise ValueError("Explicit unit mapping required")
        if not (1900 <= self.year <= 2200):
            raise ValueError("Invalid year")
        if self.wet_t is None and self.evidence != Evidence.UNKNOWN:
            raise ValueError("Missing amount cannot have known evidence state")
        if self.wet_t is not None and self.wet_t < 0:
            raise ValueError("Negative material flow")
        if self.prior_allocation_t < 0:
            raise ValueError("Negative prior allocation")
        if self.wet_t is not None and self.prior_allocation_t > self.wet_t:
            raise ValueError("Preallocated amount exceeds flow")


@dataclass(frozen=True)
class TransferEvidence:
    """Contract, matching gates and legal permission must all be documented."""

    origin_event_id: str
    destination_event_id: str
    contract_id: str
    origin_weighbridge_id: str
    destination_weighbridge_id: str
    legal_authorization_id: str
    already_committed_t: float = 0.0

    def validate(self) -> None:
        for name in ("origin_event_id", "destination_event_id", "contract_id",
                     "origin_weighbridge_id", "destination_weighbridge_id",
                     "legal_authorization_id"):
            if not getattr(self, name).strip():
                raise ValueError(f"Missing verified transfer evidence field: {name}")
        if self.already_committed_t < 0:
            raise ValueError("Existing commitments cannot be negative")


def book_to_djk(source: MaterialRecord, proposed_t: float,
                receipt: Optional[TransferEvidence]) -> float:
    """Book a documented measured DJK inbound transfer; never extrapolate."""
    source.validate()
    if source.evidence != Evidence.MEASURED:
        raise ValueError("Only measured physical flow can be booked as actual inbound")
    if source.wet_t is None or proposed_t <= 0:
        raise ValueError("Amount missing or nonpositive")
    if receipt is None:
        raise ValueError("No authorized contract and paired weighing receipts")
    receipt.validate()
    if receipt.origin_event_id != source.event_id:
        raise ValueError("Origin record mismatch")
    if proposed_t > source.wet_t - source.prior_allocation_t - receipt.already_committed_t + 1e-9:
        raise ValueError("Double counting or unavailable quantity")
    return proposed_t


def dry_solids(wet_t: float, moisture_fraction: float) -> float:
    if wet_t < 0 or not 0 <= moisture_fraction <= 1:
        raise ValueError("Bad wet mass or moisture")
    return wet_t * (1 - moisture_fraction)


def close_mass(inputs: Mapping[str, float], outputs: Mapping[str, float],
               *, tolerance_t: float = 1e-7) -> float:
    """Balance inputs vs all output/residue/emission/storage streams, in tonnes.

    A passing wet mass balance does not prove C/N/P/S, energy, salt, or safety.
    """
    if not inputs or not outputs or tolerance_t < 0:
        raise ValueError("Missing streams or bad tolerance")
    if any(v < 0 for v in list(inputs.values()) + list(outputs.values())):
        raise ValueError("Negative stream")
    error_t = sum(inputs.values()) - sum(outputs.values())
    if abs(error_t) > tolerance_t:
        raise ValueError(f"Unreconciled material mass: {error_t:.9f} t")
    return error_t


def design_year_capacity(day_rate: float, days: int = 365) -> float:
    """Theoretical design-throughput scenario only, NEVER measured deliveries."""
    if day_rate < 0 or not 0 <= days <= 366:
        raise ValueError("Invalid design input")
    return day_rate * days


def qingdao_food_sensitivity(city_scenario_t: float = 200_000.0) -> dict:
    """City-scale synthetic sensitivity. Never allocate these figures to DJK."""
    if city_scenario_t < 0:
        raise ValueError("Negative scenario")
    return {
        "scope": Scope.QINGDAO.value,
        "evidence": Evidence.SCENARIO.value,
        "djk_booked_actual_t": None,
        "city_eligible_sensitivity_t": {
            f"{round(p*100)}%": round(city_scenario_t * p, 6)
            for p in (0, .25, .50, .75, 1.00)
        },
    }


def desal_design_sensitivity(day_m3: float = 100_000.0,
                             kwh_per_m3: float = 2.2,
                             days: int = 365) -> dict:
    if day_m3 < 0 or kwh_per_m3 < 0:
        raise ValueError("Negative scenario inputs")
    design_m3 = design_year_capacity(day_m3, days)
    return {
        "scope": Scope.DONGJIAKOU.value,
        "evidence": Evidence.SCENARIO.value,
        "design_m3_per_year": design_m3,
        "scenario_kwh_per_year": design_m3 * kwh_per_m3,
        "measured_delivered_m3": None,
        "actual_brine_volume_m3": None,
    }


if __name__ == "__main__":
    import json
    print(json.dumps({
        "qingdao_food": qingdao_food_sensitivity(),
        "xiaojianxi_theoretical_tpy": design_year_capacity(500),
        "desal": desal_design_sensitivity(),
        "qingdao_2025_straw_arithmetic_uncommitted_UNKNOWN_t": 3_655_000 - 3_523_000,
    }, ensure_ascii=False, indent=2))
