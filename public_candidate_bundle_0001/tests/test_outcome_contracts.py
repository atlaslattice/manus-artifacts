"""Schema-only contract tests for Atlas outcomes v0.6 (no simulator mutations)."""
from __future__ import annotations

import json
import math
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

BUNDLE = Path(__file__).resolve().parents[1]
SCHEMAS = BUNDLE / "schemas"
FIXTURES = BUNDLE / "fixtures"

PAIRS = (
    ("atlas_outcome_ledger_v0.1.schema.json", "dongjiakou_outcomes_unknown_v0.1.json"),
    ("atlas_resource_allocation_v0.1.schema.json", "atlas_resource_allocation_synthetic_v0.1.json"),
    ("atlas_resilience_scenario_v0.1.schema.json", "atlas_resilience_synthetic_v0.1.json"),
)


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("schema_name,fixture_name", PAIRS)
def test_schema_and_fixture(schema_name, fixture_name):
    schema = read(SCHEMAS / schema_name)
    fixture = read(FIXTURES / fixture_name)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(fixture)


def test_metric_registry_unique_and_null_first():
    registry = read(FIXTURES / "outcomes_metric_registry_v0.1.json")
    ids = [m["metric_id"] for m in registry["metrics"]]
    assert len(ids) >= 100
    assert len(set(ids)) == len(ids)
    assert all(m["credit_status"] == "BLOCKED" for m in registry["metrics"])
    fixture = read(FIXTURES / "dongjiakou_outcomes_unknown_v0.1.json")
    assert fixture["realized_credit_total"] == 0
    assert all(m["metric_id"] in ids for m in fixture["metrics"])
    assert all(m["observed_value"] is None and m["credit"]["amount"] == 0 for m in fixture["metrics"])


def test_unknown_observed_value_rejected():
    schema = read(SCHEMAS / PAIRS[0][0])
    fixture = read(FIXTURES / PAIRS[0][1])
    fixture["metrics"][0]["observed_value"] = 1
    assert not Draft202012Validator(schema).is_valid(fixture)


def test_positive_realized_credit_rejected():
    schema = read(SCHEMAS / PAIRS[0][0])
    fixture = read(FIXTURES / PAIRS[0][1])
    fixture["metrics"][0]["credit"]["amount"] = 1
    assert not Draft202012Validator(schema).is_valid(fixture)


def test_no_counterfactual_rejected():
    schema = read(SCHEMAS / PAIRS[0][0])
    fixture = read(FIXTURES / PAIRS[0][1])
    del fixture["metrics"][0]["counterfactual"]
    assert not Draft202012Validator(schema).is_valid(fixture)


def test_biomass_allocation_mass_conservation():
    data = read(FIXTURES / PAIRS[1][1])
    for lot in data["source_lots"]:
        assert math.isclose(lot["qualified_dry_mass_t"], lot["wet_mass_t"] * lot["dry_matter_fraction"])
        available = lot["qualified_dry_mass_t"] - lot["soil_ecological_reserve_t"] - lot["existing_obligations_t"] - lot["collection_losses_t"]
        assert math.isclose(available, lot["allocatable_dry_mass_t"])
        assert sum(a["allocated_dry_mass_t"] for a in lot["allocations"]) <= available
    assert data["realized_credit_total"] == 0


def test_decadal_probability_vs_annual_hazard():
    data = read(FIXTURES / PAIRS[2][1])
    probability = data["probability"]
    p = 1 - (1 - probability["probability_at_least_once"]) ** (1 / probability["horizon_years"])
    assert math.isclose(p, probability["annual_hazard"], rel_tol=1e-9)
    assert math.isclose(data["gross_loss_usd"], data["gdp_reference_usd"] * data["gdp_loss_fraction"])
    assert math.isclose(data["gross_loss_usd"], 975e9)
    assert data["avoidable_fraction"] is None
    assert data["realized_credit_usd"] == 0
