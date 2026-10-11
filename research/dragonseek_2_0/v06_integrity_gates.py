#!/usr/bin/env python3
"""DragonSeek v0.6 proof-of-concept: no production authenticity, licenses or food approval.

The decisions below only assess mock evidence supplied by a separately trusted party.
Unknown data, absent documents and discrepancies fail closed for allocations.
"""
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from enum import Enum
from typing import Mapping

class Scope(str, Enum):
    QINGDAO_CITY = 'QINGDAO_CITY'
    WEST_COAST_NEW_AREA = 'WEST_COAST_NEW_AREA'
    DJK_ECON_ZONE = 'DJK_ECON_ZONE'
    DJK_PORT_AREA = 'DJK_PORT_AREA'

class Evidence(str, Enum):
    MEASURED = 'MEASURED'
    REPORTED = 'REPORTED'
    DESIGNED = 'DESIGNED'
    SCENARIO = 'SCENARIO'
    UNKNOWN = 'UNKNOWN'
    QUARANTINED = 'QUARANTINED'

@dataclass(frozen=True)
class MaterialBoundary:
    origin: Scope
    destination: Scope
    source_evidence: Evidence
    signed_transport_authorization: bool
    origin_ticket_verified: bool
    receiver_ticket_verified: bool
    # Distinct administrative reporting scopes can physically overlap.
    # An evidence-backed transfer is needed to book an amount between ledgers.

def boundary_allows_measured_transfer(rec: MaterialBoundary) -> bool:
    return all((rec.source_evidence is Evidence.MEASURED,
                rec.signed_transport_authorization,
                rec.origin_ticket_verified, rec.receiver_ticket_verified))

@dataclass(frozen=True)
class TruckWeighing:
    origin_ticket_id: str
    carrier_manifest_ticket_id: str
    source_lot_id: str
    manifest_lot_id: str
    weighed_net_kg: int
    manifest_net_kg: int
    period_source: str
    period_manifest: str
    meter_calibration_verified: bool
    carrier_authorization_verified: bool
    destination_receipt_id: str
    destination_receipt_verified: bool

def exact_manifest_gate(w: TruckWeighing) -> bool:
    """No automatic 'close enough' reconciliation. Correction needs a new review event."""
    return bool(w.origin_ticket_id and w.carrier_manifest_ticket_id
        and w.origin_ticket_id == w.carrier_manifest_ticket_id
        and w.source_lot_id and w.source_lot_id == w.manifest_lot_id
        and w.period_source and w.period_source == w.period_manifest
        and isinstance(w.weighed_net_kg, int) and not isinstance(w.weighed_net_kg, bool)
        and isinstance(w.manifest_net_kg, int) and not isinstance(w.manifest_net_kg, bool)
        and w.weighed_net_kg > 0 and w.weighed_net_kg == w.manifest_net_kg
        and w.meter_calibration_verified and w.carrier_authorization_verified
        and w.destination_receipt_id and w.destination_receipt_verified)

REQUIRED_FOOD_PANEL = frozenset({
    'salmonella', 'listeria', 'e_coli', 'aflatoxin', 'ochratoxin',
    'lead', 'cadmium', 'arsenic', 'mercury', 'chromium',
    'plastic_contaminants', 'allergens', 'food_contact_migration'
})

@dataclass(frozen=True)
class FoodSafetyEvidence:
    feedstock_class: str
    origin_certification_id: str
    chain_of_custody_verified: bool
    food_grade_feedstock_verified: bool
    strain_identity_verified: bool
    organism_safety_review_verified: bool
    haccp_reference: str
    process_validation_verified: bool
    lab_panel: Mapping[str, str]
    lab_accreditation_verified: bool
    target_product_class_approved: bool
    current_regulatory_path_verified: bool

def food_safety_gate(e: FoodSafetyEvidence) -> bool:
    """Boolean is hypothetical authorization gate, never a food-production permit.

    Results must be independently compared with product-specific limits, methods,
    and exposure: an unqualified 'PASS' from an external source is insufficient.
    """
    if e.feedstock_class in {'MIXED_MUNICIPAL_FOOD_WASTE','HAZARDOUS_WASTE','SEWAGE_SLUDGE'}:
        return False
    return all((e.origin_certification_id, e.chain_of_custody_verified,
        e.food_grade_feedstock_verified,e.strain_identity_verified,
        e.organism_safety_review_verified,e.haccp_reference,
        e.process_validation_verified,e.lab_accreditation_verified,
        e.target_product_class_approved,e.current_regulatory_path_verified,
        REQUIRED_FOOD_PANEL <= set(e.lab_panel),
        all(e.lab_panel.get(k) == 'INDEPENDENTLY_VERIFIED_COMPLIANT' for k in REQUIRED_FOOD_PANEL)))

def phosphogypsum_design_ratio(gypsum_tonnes, acid_tonnes):
    """Design output/feed, not measured chemical conversion yield."""
    try:
        g, a = Decimal(str(gypsum_tonnes)), Decimal(str(acid_tonnes))
    except InvalidOperation as exc:
        raise ValueError('Non-numeric masses') from exc
    if g <= 0 or a < 0 or not g.is_finite() or not a.is_finite():
        raise ValueError('Invalid plant design mass')
    return a/g

def normalized_mass_t(value, unit):
    """Chinese 万吨 and SI megatonnes differ by factor 100."""
    d = Decimal(str(value))
    factors = {'吨':1,'万吨':10_000,'Mt':1_000_000,'kt':1_000}
    if unit not in factors or not d.is_finite() or d < 0:
        raise ValueError('Unverified mass unit or value')
    return d*Decimal(factors[unit])

@dataclass(frozen=True)
class DeclaredCapacity:
    geographic_scope: Scope
    commodity_group: str
    annual_design_tonnes: Decimal
    source_year: int
    measured_actual_tonnes: Decimal | None = None

def may_report_as_actual_capacity(c: DeclaredCapacity):
    # A design declaration cannot become throughput unless there is a separately
    # evidenced site/year/commodity matched measurement. This only checks presence.
    return False if c.measured_actual_tonnes is None else c.measured_actual_tonnes >= 0
