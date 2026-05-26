"""
Atlas/ORCS Module 1 schema contract tests.

STATUS: CANDIDATE TESTS — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
"""

from pathlib import Path
import pytest
import yaml


SCHEMA_DIR = Path(
    "/tmp/workspace/atlaslattice/manus-artifacts/schemas/atlas_orcs/v0_1"
)

REQUIRED_SCHEMA_FILES = {
    "atlas-artifact.schema.yaml",
    "atlas-provenance-receipt.schema.yaml",
    "atlas-claim.schema.yaml",
    "atlas-claim-relationship.schema.yaml",
    "atlas-contradiction-ledger.schema.yaml",
    "atlas-uncertainty-ledger.schema.yaml",
    "atlas-summary-lineage.schema.yaml",
    "atlas-intent-provenance.schema.yaml",
    "atlas-trust-state.schema.yaml",
    "atlas-ratification-event.schema.yaml",
    "atlas-failure-event.schema.yaml",
    "atlas-governance-profile.schema.yaml",
    "atlas-domain-module.schema.yaml",
    "atlas-quarantine-rule.schema.yaml",
    "atlas-audit-event.schema.yaml",
}


def _load_schema(name: str) -> dict:
    with (SCHEMA_DIR / name).open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def test_required_schema_files_present():
    """Module 1 requires exactly these 15 schema files."""
    existing = {p.name for p in SCHEMA_DIR.glob("*.yaml")}
    assert REQUIRED_SCHEMA_FILES.issubset(existing)
    assert len(REQUIRED_SCHEMA_FILES) == 15


@pytest.mark.parametrize("schema_name", sorted(REQUIRED_SCHEMA_FILES))
def test_schema_version_is_0_1(schema_name: str):
    schema = _load_schema(schema_name)
    assert schema.get("schema_version") == "0.1"


@pytest.mark.parametrize("schema_name", sorted(REQUIRED_SCHEMA_FILES))
def test_canon_and_deployment_defaults(schema_name: str):
    """
    Normalized contract:
      - canon_status default = not_canon
      - deployment_status default = not_deployable
    """
    schema = _load_schema(schema_name)
    fields = schema.get("fields", {})

    assert "canon_status" in fields
    assert fields["canon_status"].get("default") == "not_canon"

    assert "deployment_status" in fields
    assert fields["deployment_status"].get("default") == "not_deployable"


def test_no_object_can_self_ratify_constraints():
    """
    Explicit no-self-ratification controls must exist where ratification is modeled.
    """
    artifact = _load_schema("atlas-artifact.schema.yaml")
    claim = _load_schema("atlas-claim.schema.yaml")
    rat_event = _load_schema("atlas-ratification-event.schema.yaml")

    assert artifact["fields"]["self_ratification_allowed"]["default"] is False
    assert claim["fields"]["self_ratification_allowed"]["default"] is False
    assert rat_event["fields"]["self_ratification"]["default"] is False

    rat_constraints = "\n".join(rat_event.get("constraints", []))
    assert "self_ratification" in rat_constraints
    assert "must be false" in rat_constraints


def test_summary_not_equal_to_source_proof():
    """Acceptance proof: summary ≠ source."""
    schema = _load_schema("atlas-summary-lineage.schema.yaml")
    fields = schema["fields"]
    constraints = "\n".join(schema.get("constraints", []))

    assert fields["summary_equals_source"]["default"] is False
    assert fields["summary_replaces_source"]["default"] is False
    assert "summary_equals_source must be false" in constraints
    assert "summary_replaces_source must be false" in constraints


def test_receipt_not_truth_proof():
    """Acceptance proof: receipt ≠ truth."""
    schema = _load_schema("atlas-provenance-receipt.schema.yaml")
    fields = schema["fields"]
    constraints = "\n".join(schema.get("constraints", []))

    assert fields["receipt_is_truth"]["default"] is False
    assert "receipt_is_truth must be false" in constraints


def test_ratification_requires_explicit_event_proof():
    """Acceptance proof: ratification requires explicit event linkage."""
    trust = _load_schema("atlas-trust-state.schema.yaml")
    constraints = "\n".join(trust.get("constraints", []))

    assert "ratification_event_id required when trust_state in [ratified, active]" in constraints
    assert "canon_status = ratified_canon requires ratification_event_id" in constraints
