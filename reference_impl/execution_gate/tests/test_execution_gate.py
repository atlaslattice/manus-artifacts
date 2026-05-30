"""
Tests for D-Φ-1 / CAS-001-A Execution Gate
NOT CANON — NOT DEPLOYABLE — reference implementation only
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from dphi_gate import dphi_check, DPhiGateResult
from cas001a_anchor import cas001a_anchor, CASAnchorStore
from execution_request import (
    ExecutionRequest, GateChainState, process_execution_request,
    ExecutionRequestResult,
)


def make_passing_gates() -> GateChainState:
    return GateChainState(
        provenance_gate="pass",
        safety_gate="pass",
        governance_gate="pass",
        data_residency_gate="pass",
        human_permission_gate="pass",
        receipt_gate="pass",
    )


def make_request(
    content_type="execution_request",
    gates: GateChainState = None,
    receipt_id="receipt-001",
    **kwargs,
) -> ExecutionRequest:
    if gates is None:
        gates = make_passing_gates()
    return ExecutionRequest(
        request_id="req-001",
        content_type=content_type,
        actor_id="LucernaBrain",
        gate_states=gates,
        description="Test execution request",
        receipt_id=receipt_id,
        **kwargs,
    )


class TestDPhiGate:
    def test_missing_receipt_fails(self):
        result = dphi_check(
            request_id="req-001",
            has_receipt=False,
            has_human_permission=True,
            safety_gate_status="pass",
            content_type="execution_request",
        )
        assert result.passed is False
        assert "receipt" in result.reason.lower()

    def test_missing_human_permission_fails(self):
        result = dphi_check(
            request_id="req-001",
            has_receipt=True,
            has_human_permission=False,
            safety_gate_status="pass",
            content_type="execution_request",
        )
        assert result.passed is False
        assert "human permission" in result.reason.lower()

    def test_safety_gate_not_pass_fails(self):
        result = dphi_check(
            request_id="req-001",
            has_receipt=True,
            has_human_permission=True,
            safety_gate_status="pending",
            content_type="execution_request",
        )
        assert result.passed is False
        assert "safety" in result.reason.lower()

    def test_all_conditions_pass(self):
        result = dphi_check(
            request_id="req-001",
            has_receipt=True,
            has_human_permission=True,
            safety_gate_status="pass",
            content_type="execution_request",
        )
        assert result.passed is True


class TestCASAnchor:
    def test_creates_audit_anchor(self):
        store = CASAnchorStore()
        result = cas001a_anchor(
            request_id="req-001",
            actor_id="LucernaBrain",
            gate_states={"safety_gate": "pass"},
            content_type="execution_request",
            anchor_store=store,
        )
        assert result.passed is True
        assert result.anchor is not None
        assert result.anchor.request_id == "req-001"

    def test_code_execution_requires_tidelock(self):
        store = CASAnchorStore()
        result = cas001a_anchor(
            request_id="req-code",
            actor_id="TIDELOCKBrain",
            gate_states={},
            content_type="code",
            anchor_store=store,
        )
        assert result.anchor.tidelock_required is True
        assert result.anchor.tidelock_lane_metadata is not None
        assert result.anchor.tidelock_lane_metadata["lane"] == "tidelock"

    def test_non_code_does_not_require_tidelock(self):
        store = CASAnchorStore()
        result = cas001a_anchor(
            request_id="req-synthesis",
            actor_id="LucernaBrain",
            gate_states={},
            content_type="synthesis",
            anchor_store=store,
        )
        assert result.anchor.tidelock_required is False


class TestExecutionRequestProcessing:
    def test_valid_request_approved(self):
        request = make_request(gates=make_passing_gates())
        store = CASAnchorStore()
        result = process_execution_request(request, store)
        assert result.approved is True
        assert result.audit_anchor_id is not None

    def test_request_without_receipt_rejected(self):
        gates = make_passing_gates()
        gates.receipt_gate = "fail"
        request = make_request(gates=gates, receipt_id=None)
        store = CASAnchorStore()
        result = process_execution_request(request, store)
        assert result.approved is False
        assert "receipt" in result.rejection_reason.lower()

    def test_request_without_human_permission_rejected(self):
        gates = make_passing_gates()
        gates.human_permission_gate = "pending"
        request = make_request(gates=gates)
        store = CASAnchorStore()
        result = process_execution_request(request, store)
        assert result.approved is False

    def test_request_without_safety_pass_rejected(self):
        gates = make_passing_gates()
        gates.safety_gate = "fail"
        request = make_request(gates=gates)
        store = CASAnchorStore()
        result = process_execution_request(request, store)
        assert result.approved is False
        assert "safety" in result.rejection_reason.lower()

    def test_approved_request_creates_atlas_audit_event(self):
        """Passed execution request creates atlas-audit-event (CAS anchor)."""
        request = make_request(gates=make_passing_gates())
        store = CASAnchorStore()
        result = process_execution_request(request, store)
        assert result.approved is True
        assert result.audit_anchor_id is not None
        # Verify anchor exists in store
        anchor = store.get(result.audit_anchor_id)
        assert anchor is not None
        assert anchor.resolved is True
        assert anchor.resolution == "approved"

    def test_repo_code_routes_to_tidelock(self):
        """Repo/code execution requests route to TIDELOCK lane."""
        request = make_request(content_type="code", gates=make_passing_gates())
        store = CASAnchorStore()
        result = process_execution_request(request, store)
        assert result.tidelock_required is True
        assert result.tidelock_lane_metadata is not None
        assert result.tidelock_lane_metadata["lane"] == "tidelock"
