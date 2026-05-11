"""
Tests for the AtlasBrain hard-gate validator.

STATUS: IMPLEMENTATION TESTS — NOT CANON
PURPOSE: verify that atlasbrain_gate.py correctly enforces evidence-chain rules
         for benchmark, public-claim, and evidence-packet artifacts.
"""

from __future__ import annotations

from pathlib import Path

import pytest

import atlasbrain_gate as gate


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _write(tmp_path: Path, rel: str, content: str) -> Path:
    p = tmp_path / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return p


EVIDENCE_PACKET_LINK = (
    "EVIDENCE PACKET: archive/boot/atlasbrain/evidence_packets/SOME_PACKET_2026-05-10.md"
)
VALID_AUTHORITY = "authority_status: reviewed_claim"
VALID_BENCHMARK_STATUS = "benchmark_status: rubric_pending"
VALID_HUMAN_ROOT = "human_root_required: true"


def _valid_evidence_packet_body() -> str:
    return "\n".join([VALID_AUTHORITY, VALID_BENCHMARK_STATUS, VALID_HUMAN_ROOT])


# ---------------------------------------------------------------------------
# validate_benchmarks
# ---------------------------------------------------------------------------

class TestValidateBenchmarks:
    def test_passes_when_folder_missing(self, tmp_path: Path) -> None:
        report = gate.validate_benchmarks(tmp_path)
        assert report.passed
        assert report.checked == []

    def test_passes_when_only_readme(self, tmp_path: Path) -> None:
        _write(tmp_path, "benchmarks/README.md", "# Benchmarks README")
        report = gate.validate_benchmarks(tmp_path)
        assert report.passed

    def test_passes_when_benchmark_links_evidence_packet(self, tmp_path: Path) -> None:
        body = f"# Benchmark\n\n{EVIDENCE_PACKET_LINK}\n"
        _write(tmp_path, "benchmarks/SOME_BENCHMARK.md", body)
        report = gate.validate_benchmarks(tmp_path)
        assert report.passed
        assert len(report.checked) == 1

    def test_fails_when_benchmark_missing_evidence_packet_link(self, tmp_path: Path) -> None:
        _write(tmp_path, "benchmarks/SOME_BENCHMARK.md", "# Benchmark\n\nNo evidence link here.\n")
        report = gate.validate_benchmarks(tmp_path)
        assert not report.passed
        assert any("must_link_evidence_packet" in v.rule for v in report.violations)

    def test_violation_includes_filename(self, tmp_path: Path) -> None:
        _write(tmp_path, "benchmarks/BAD_BENCHMARK.md", "# no links")
        report = gate.validate_benchmarks(tmp_path)
        assert any("BAD_BENCHMARK" in v.file for v in report.violations)

    def test_multiple_benchmarks_each_checked(self, tmp_path: Path) -> None:
        _write(tmp_path, "benchmarks/GOOD.md", f"# Good\n{EVIDENCE_PACKET_LINK}")
        _write(tmp_path, "benchmarks/BAD.md", "# Bad\nno link")
        report = gate.validate_benchmarks(tmp_path)
        assert not report.passed
        assert len(report.checked) == 2
        assert len(report.violations) == 1


# ---------------------------------------------------------------------------
# validate_public_claims
# ---------------------------------------------------------------------------

class TestValidatePublicClaims:
    def test_passes_when_folder_missing(self, tmp_path: Path) -> None:
        report = gate.validate_public_claims(tmp_path)
        assert report.passed

    def test_passes_when_only_readme(self, tmp_path: Path) -> None:
        _write(tmp_path, "public_claims/README.md", "# Public Claims README")
        report = gate.validate_public_claims(tmp_path)
        assert report.passed

    def test_passes_with_reviewed_claim_authority(self, tmp_path: Path) -> None:
        body = f"# Claim\n\n{EVIDENCE_PACKET_LINK}\n{VALID_AUTHORITY}\n"
        _write(tmp_path, "public_claims/CLAIM.md", body)
        report = gate.validate_public_claims(tmp_path)
        assert report.passed

    def test_passes_with_human_root_approved_authority(self, tmp_path: Path) -> None:
        body = (
            f"# Claim\n\n{EVIDENCE_PACKET_LINK}\n"
            "authority_status: human_root_approved_public_claim\n"
        )
        _write(tmp_path, "public_claims/CLAIM.md", body)
        report = gate.validate_public_claims(tmp_path)
        assert report.passed

    def test_fails_when_no_evidence_packet_link(self, tmp_path: Path) -> None:
        body = f"# Claim\n\n{VALID_AUTHORITY}\n"
        _write(tmp_path, "public_claims/CLAIM.md", body)
        report = gate.validate_public_claims(tmp_path)
        assert not report.passed
        assert any("must_link_evidence_packet" in v.rule for v in report.violations)

    def test_fails_when_authority_is_evidence_only(self, tmp_path: Path) -> None:
        body = f"# Claim\n\n{EVIDENCE_PACKET_LINK}\nauthority_status: evidence_only\n"
        _write(tmp_path, "public_claims/CLAIM.md", body)
        report = gate.validate_public_claims(tmp_path)
        assert not report.passed
        assert any("insufficient_authority" in v.rule for v in report.violations)

    def test_fails_when_authority_is_quarantined(self, tmp_path: Path) -> None:
        body = f"# Claim\n\n{EVIDENCE_PACKET_LINK}\nauthority_status: quarantined\n"
        _write(tmp_path, "public_claims/CLAIM.md", body)
        report = gate.validate_public_claims(tmp_path)
        assert not report.passed
        assert any("quarantined" in v.rule for v in report.violations)

    def test_fails_when_authority_missing(self, tmp_path: Path) -> None:
        body = f"# Claim\n\n{EVIDENCE_PACKET_LINK}\n"
        _write(tmp_path, "public_claims/CLAIM.md", body)
        report = gate.validate_public_claims(tmp_path)
        assert not report.passed
        assert any("must_declare_authority_status" in v.rule for v in report.violations)

    def test_fails_when_authority_is_disputed(self, tmp_path: Path) -> None:
        body = f"# Claim\n\n{EVIDENCE_PACKET_LINK}\nauthority_status: disputed\n"
        _write(tmp_path, "public_claims/CLAIM.md", body)
        report = gate.validate_public_claims(tmp_path)
        assert not report.passed


# ---------------------------------------------------------------------------
# validate_evidence_packets
# ---------------------------------------------------------------------------

class TestValidateEvidencePackets:
    def test_passes_when_folder_missing(self, tmp_path: Path) -> None:
        report = gate.validate_evidence_packets(tmp_path)
        assert report.passed

    def test_passes_when_only_readme(self, tmp_path: Path) -> None:
        _write(tmp_path, "evidence_packets/README.md", "# EP README")
        report = gate.validate_evidence_packets(tmp_path)
        assert report.passed

    def test_passes_with_all_required_fields(self, tmp_path: Path) -> None:
        _write(tmp_path, "evidence_packets/EP.md", _valid_evidence_packet_body())
        report = gate.validate_evidence_packets(tmp_path)
        assert report.passed

    def test_fails_when_authority_status_missing(self, tmp_path: Path) -> None:
        body = "\n".join([VALID_BENCHMARK_STATUS, VALID_HUMAN_ROOT])
        _write(tmp_path, "evidence_packets/EP.md", body)
        report = gate.validate_evidence_packets(tmp_path)
        assert not report.passed
        assert any("authority_status" in v.rule for v in report.violations)

    def test_fails_when_benchmark_status_missing(self, tmp_path: Path) -> None:
        body = "\n".join([VALID_AUTHORITY, VALID_HUMAN_ROOT])
        _write(tmp_path, "evidence_packets/EP.md", body)
        report = gate.validate_evidence_packets(tmp_path)
        assert not report.passed
        assert any("benchmark_status" in v.rule for v in report.violations)

    def test_fails_when_human_root_required_missing(self, tmp_path: Path) -> None:
        body = "\n".join([VALID_AUTHORITY, VALID_BENCHMARK_STATUS])
        _write(tmp_path, "evidence_packets/EP.md", body)
        report = gate.validate_evidence_packets(tmp_path)
        assert not report.passed
        assert any("human_root_required" in v.rule for v in report.violations)


# ---------------------------------------------------------------------------
# validate_all
# ---------------------------------------------------------------------------

class TestValidateAll:
    def test_passes_on_empty_root(self, tmp_path: Path) -> None:
        report = gate.validate_all(tmp_path)
        assert report.passed
        assert report.checked == []
        assert report.violations == []

    def test_merges_violations_from_all_lanes(self, tmp_path: Path) -> None:
        _write(tmp_path, "benchmarks/BAD.md", "# no link")
        _write(tmp_path, "public_claims/BAD.md", f"{EVIDENCE_PACKET_LINK}\nauthority_status: no_authority\n")
        _write(tmp_path, "evidence_packets/BAD.md", "# missing fields")
        report = gate.validate_all(tmp_path)
        assert not report.passed
        assert len(report.violations) >= 3

    def test_summary_contains_pass_or_fail(self, tmp_path: Path) -> None:
        report = gate.validate_all(tmp_path)
        summary = report.summary()
        assert "PASS" in summary or "FAIL" in summary


# ---------------------------------------------------------------------------
# Real atlasbrain folder passes gate
# ---------------------------------------------------------------------------

class TestRealAtlasBrainFolder:
    def test_real_benchmarks_pass_gate(self) -> None:
        """The committed benchmark dossier must link an evidence packet."""
        if not gate.ATLASBRAIN_ROOT.exists():
            pytest.skip("atlasbrain folder not present in checkout")
        report = gate.validate_benchmarks()
        assert report.passed, report.summary()

    def test_real_evidence_packets_pass_gate(self) -> None:
        """The committed evidence packet must declare required fields."""
        if not gate.ATLASBRAIN_ROOT.exists():
            pytest.skip("atlasbrain folder not present in checkout")
        report = gate.validate_evidence_packets()
        assert report.passed, report.summary()

    def test_real_public_claims_pass_gate(self) -> None:
        """No premature public claims exist (folder should be empty of non-READMEs)."""
        if not gate.ATLASBRAIN_ROOT.exists():
            pytest.skip("atlasbrain folder not present in checkout")
        report = gate.validate_public_claims()
        assert report.passed, report.summary()
