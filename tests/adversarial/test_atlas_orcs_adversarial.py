import pytest

from reference_impl.execution_gate.execution_request import process_execution_request


@pytest.mark.parametrize(
    "test_id,payload",
    [
        ("T01", {"request_id": "t01"}),
        ("T02", {"request_id": "t02", "receipt_present": True, "human_permission": False, "safety_pass": True}),
        ("T03", {"request_id": "t03", "receipt_present": True, "human_permission": True, "safety_pass": False}),
        ("T04", {"request_id": "t04"}),
        ("T05", {"request_id": "t05"}),
        ("T06", {"request_id": "t06"}),
        ("T07", {"request_id": "t07"}),
        ("T08", {"request_id": "t08", "receipt_present": True, "human_permission": False, "safety_pass": False}),
        ("T09", {"request_id": "t09"}),
        ("T10", {"request_id": "t10"}),
        ("T11", {"request_id": "t11"}),
        ("T12", {"request_id": "t12"}),
    ],
)
def test_adversarial_cases_fail_safely(test_id, payload):
    ok, data = process_execution_request(payload)
    assert ok is False
    assert "reason" in data
