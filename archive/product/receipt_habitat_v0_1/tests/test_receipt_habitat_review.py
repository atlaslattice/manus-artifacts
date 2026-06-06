from receipt_habitat.overclaim import scan_text, verdict_from_findings
from receipt_habitat.review import review_packet


def base_packet(**overrides):
    packet = {
        "schema_version": "receipt_habitat.ingestion.v0.1",
        "artifact_id": "TEST-001",
        "title": "Test packet",
        "source_surface": "chatgpt",
        "raw_export_status": "summary_only",
        "thread_time_range": {
            "start": "2026-05-30T00:00:00Z",
            "end": "2026-05-30T01:00:00Z",
            "timezone": "America/Chicago",
        },
        "access_scope": "project_shared",
        "privacy_status": "mixed",
        "canon_status": "not_canon",
        "deployment_status": "not_deployable",
        "authority_scope": "none",
        "runtime_status": "local_dry_run_only",
        "claims": [
            {
                "claim_text": "This is a local non-canon review aid.",
                "claim_type": "derived_inference",
                "claim_confidence": "C1_SIGNAL",
                "evidence_ref": None,
                "public_claim_allowed": False,
            }
        ],
        "next_safest_action": "Keep local and attach raw receipts before public use.",
    }
    packet.update(overrides)
    return packet


def test_summary_only_cannot_create_public_claim():
    result = review_packet(base_packet(raw_export_status="summary_only"))
    assert result.public_claim_allowed is False
    assert result.review_verdict == "approve"


def test_missing_access_scope_blocks_review():
    packet = base_packet()
    packet.pop("access_scope")
    result = review_packet(packet)
    assert result.review_verdict == "block"
    assert result.blocker_level == "blocking"
    assert "access_scope" in result.missing_receipts


def test_unavailable_raw_requires_unavailable_sources():
    packet = base_packet(raw_export_status="unavailable")
    result = review_packet(packet)
    assert result.review_verdict == "block"
    assert "unavailable_sources" in result.missing_receipts


def test_canon_phrase_without_receipt_returns_patch():
    findings = scan_text("This artifact is ratified canon and final.")
    assert verdict_from_findings(findings) == "patch"
    assert {finding.term for finding in findings} >= {"ratified", "canon", "final"}


def test_deployment_phrase_without_receipt_returns_block():
    findings = scan_text("Runtime active and deployed in production-ready mode.")
    assert verdict_from_findings(findings) == "block"


def test_review_packet_detects_overclaim_terms():
    packet = base_packet(
        claims=[
            {
                "claim_text": "This is canonically registered and fully reconciled.",
                "claim_type": "derived_inference",
                "claim_confidence": "C1_SIGNAL",
                "evidence_ref": None,
                "public_claim_allowed": False,
            }
        ]
    )
    result = review_packet(packet)
    assert result.review_verdict == "patch"
    assert "canonically registered" in result.overclaims_detected


def test_full_raw_without_missing_fields_can_allow_public_claim_in_principle():
    result = review_packet(base_packet(raw_export_status="full_raw"))
    assert result.public_claim_allowed is True
    assert result.review_verdict == "approve"
