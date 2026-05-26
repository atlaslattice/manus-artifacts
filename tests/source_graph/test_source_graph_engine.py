from reference_impl.source_graph_engine.query import (
    blocked_from_public_use,
    evidence_supporting_claim,
    summary_only_nodes,
    where_claim_came_from,
)
from reference_impl.source_graph_engine.validator import validate_graph


def _sample_graph() -> dict:
    return {
        "nodes": [
            {"id": "src_raw_001", "type": "raw_source", "raw_export_status": "full_raw", "public_use_status": "source_complete"},
            {"id": "src_raw_002", "type": "raw_source", "raw_export_status": "summary_only", "public_use_status": "source_incomplete", "blocked_reason": "summary_only"},
            {"id": "fact_001", "type": "parsed_fact"},
            {"id": "claim_001", "type": "claim"},
            {"id": "claim_002", "type": "claim"},
            {"id": "evidence_001", "type": "evidence"},
            {"id": "review_001", "type": "review"},
            {"id": "action_001", "type": "action", "public_use_status": "blocked", "blocked_reason": "quarantined"},
        ],
        "edges": [
            {"src": "claim_001", "dst": "fact_001", "type": "derived_from"},
            {"src": "fact_001", "dst": "src_raw_001", "type": "derived_from"},
            {"src": "evidence_001", "dst": "claim_001", "type": "supports"},
            {"src": "action_001", "dst": "claim_002", "type": "quarantines"},
        ],
    }


def test_validator_rejects_claim_without_source_edge():
    ok, errors = validate_graph(_sample_graph())
    assert not ok
    assert any("claim claim_002 has no derived_from edge" in e for e in errors)


def test_graph_answers_definition_of_done_questions():
    g = _sample_graph()

    # Where did this claim come from?
    assert where_claim_came_from(g, "claim_001") == ["claim_001", "fact_001", "src_raw_001"]

    # What evidence supports it?
    assert evidence_supporting_claim(g, "claim_001") == ["evidence_001"]

    # What is still summary-only?
    assert "src_raw_002" in summary_only_nodes(g)

    # What is blocked from public use?
    blocked = blocked_from_public_use(g)
    assert "src_raw_002" in blocked
    assert "action_001" in blocked
