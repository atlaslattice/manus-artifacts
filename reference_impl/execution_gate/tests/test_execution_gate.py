"""
Tests for D-Φ-1 / CAS-001-A execution gate.

STATUS: CANDIDATE TESTS — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
"""

import pytest
from reference_impl.execution_gate.execution_request import (
    ExecutionRequest, process_execution_request
)


def make_request(
    receipt_id="receipt-001",
    safety_pass=True,
    human_permission=True,
    execution_type="general",
) -> ExecutionRequest:
    return ExecutionRequest(
        request_id="req-test-001",
        execution_type=execution_type,
        receipt_id=receipt_id,
        safety_pass=safety_pass,
        human_permission=human_permission,
        safety_check_id="safety-001",
        provenance_refs=["prov-001"],
        description="Test execution request",
    )


def test_execution_without_receipt_fails():
    req = make_request(receipt_id=None)
    result = process_execution_request(req)
    assert result.permitted is False
    assert result.blocked_by == "D-Phi-1"


def test_execution_without_safety_pass_fails():
    req = make_request(safety_pass=False)
    result = process_execution_request(req)
    assert result.permitted is False
    assert result.blocked_by == "CAS-001-A"


def test_execution_without_human_permission_fails():
    req = make_request(human_permission=False)
    result = process_execution_request(req)
    assert result.permitted is False
    assert result.blocked_by == "human_permission_gate"


def test_valid_execution_request_passes():
    req = make_request()
    result = process_execution_request(req)
    assert result.permitted is True
    assert result.atlas_audit_event is not None
    assert result.atlas_audit_event["outcome"] == "passed"


def test_passed_execution_creates_audit_event():
    req = make_request()
    result = process_execution_request(req)
    assert result.atlas_audit_event is not None
    assert result.atlas_audit_event["event_type"] == "execution_permitted"


def test_repo_execution_routes_to_tidelock():
    req = make_request(execution_type="repo")
    result = process_execution_request(req)
    assert result.permitted is True
    assert result.tidelock_required is True
    assert result.atlas_audit_event["tidelock_involved"] is True
    assert result.atlas_audit_event["tidelock_lane"] == "TIDELOCKBrain"


def test_code_execution_routes_to_tidelock():
    req = make_request(execution_type="code")
    result = process_execution_request(req)
    assert result.tidelock_required is True


def test_merge_execution_routes_to_tidelock():
    req = make_request(execution_type="merge")
    result = process_execution_request(req)
    assert result.tidelock_required is True


def test_general_execution_does_not_require_tidelock():
    req = make_request(execution_type="general")
    result = process_execution_request(req)
    assert result.permitted is True
    assert result.tidelock_required is False


def test_failed_execution_creates_audit_event():
    req = make_request(receipt_id=None)
    result = process_execution_request(req)
    assert result.atlas_audit_event is not None
    assert result.atlas_audit_event["event_type"] == "execution_denied"
