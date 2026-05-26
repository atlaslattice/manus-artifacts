from reference_impl.native_thread.packet import strongest_safe_claim


def test_caveat_added_when_raw_absent():
    claim = strongest_safe_claim({"raw_export_status": "summary_only", "strongest_safe_claim": "bounded claim"})
    assert "caveated" in claim
