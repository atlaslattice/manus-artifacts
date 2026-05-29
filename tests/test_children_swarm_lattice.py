"""test_children_swarm_lattice.py — Wave 4, Task 42.

Validates the Children Swarm derived-lattice exporter and derived-lattice files.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
GLOBAL_INDEX = ROOT / "docs" / "generated" / "LATTICE_GLOBAL_INDEX.json"
SWARM_EXPORT_DIR = ROOT / "docs" / "generated" / "swarm_exports"
EXPORTER = ROOT / "scripts" / "export_children_swarm_lattice.py"
CHILDREN_SWARM_DOC = ROOT / "docs" / "CHILDREN_SWARM_LATTICE.md"
EVIDENCE_BUNDLE_DOC = ROOT / "docs" / "EVIDENCE_BUNDLE_FORMAT.md"


class TestExporterScript:
    def test_exporter_exists(self):
        assert EXPORTER.exists(), f"exporter script missing: {EXPORTER}"

    def test_validate_only_passes(self):
        result = subprocess.run(
            [sys.executable, str(EXPORTER), "--validate-only"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        assert result.returncode == 0, f"validate-only failed:\n{result.stdout}\n{result.stderr}"
        assert "valid" in result.stdout.lower(), "expected 'valid' in output"

    def test_validate_only_reports_nodes_and_edges(self):
        result = subprocess.run(
            [sys.executable, str(EXPORTER), "--validate-only"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        assert result.returncode == 0
        assert "nodes" in result.stdout
        assert "edges" in result.stdout

    def test_export_writes_json(self, tmp_path):
        out_file = tmp_path / "test_swarm.json"
        result = subprocess.run(
            [
                sys.executable,
                str(EXPORTER),
                "--agent-id",
                "test-agent-pytest",
                "--agent-type",
                "copilot",
                "--out",
                str(out_file),
            ],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        assert result.returncode == 0, f"export failed:\n{result.stdout}\n{result.stderr}"
        assert out_file.exists(), "output file not created"

    def test_export_json_structure(self, tmp_path):
        out_file = tmp_path / "swarm.json"
        subprocess.run(
            [
                sys.executable,
                str(EXPORTER),
                "--agent-id",
                "test-struct-check",
                "--out",
                str(out_file),
            ],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        data = json.loads(out_file.read_text())
        assert "agent_id" in data
        assert "agent_type" in data
        assert "session_date" in data
        assert "parent_lattice" in data
        assert "nodes" in data
        assert "edges" in data
        assert "provenance" in data
        assert "metrics" in data

    def test_export_nodes_have_required_fields(self, tmp_path):
        out_file = tmp_path / "swarm_fields.json"
        subprocess.run(
            [sys.executable, str(EXPORTER), "--out", str(out_file)],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        data = json.loads(out_file.read_text())
        for node in data["nodes"]:
            assert "id" in node, f"node missing 'id': {node}"
            assert "type" in node, f"node {node['id']} missing 'type'"
            assert "path" in node, f"node {node['id']} missing 'path'"
            assert "links" in node, f"node {node['id']} missing 'links'"

    def test_export_edges_have_required_fields(self, tmp_path):
        out_file = tmp_path / "swarm_edges.json"
        subprocess.run(
            [sys.executable, str(EXPORTER), "--out", str(out_file)],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        data = json.loads(out_file.read_text())
        for edge in data["edges"]:
            assert "from" in edge, f"edge missing 'from': {edge}"
            assert "to" in edge, f"edge missing 'to': {edge}"
            assert "rel" in edge, f"edge missing 'rel': {edge}"

    def test_no_orphan_nodes_in_export(self, tmp_path):
        out_file = tmp_path / "swarm_orphan.json"
        subprocess.run(
            [sys.executable, str(EXPORTER), "--out", str(out_file)],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        data = json.loads(out_file.read_text())
        orphans = [n["id"] for n in data["nodes"] if not n.get("links")]
        assert not orphans, f"orphan nodes found: {orphans}"

    def test_parent_lattice_field(self, tmp_path):
        out_file = tmp_path / "swarm_parent.json"
        subprocess.run(
            [sys.executable, str(EXPORTER), "--out", str(out_file)],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        data = json.loads(out_file.read_text())
        assert data["parent_lattice"] == "LATTICE_GLOBAL_INDEX"


class TestSwarmDocumentation:
    def test_children_swarm_doc_exists(self):
        assert CHILDREN_SWARM_DOC.exists(), f"Children Swarm doc missing: {CHILDREN_SWARM_DOC}"

    def test_evidence_bundle_doc_exists(self):
        assert EVIDENCE_BUNDLE_DOC.exists(), f"Evidence Bundle doc missing: {EVIDENCE_BUNDLE_DOC}"

    def test_children_swarm_doc_has_schema_section(self):
        text = CHILDREN_SWARM_DOC.read_text(encoding="utf-8")
        assert "Derived-Lattice Schema" in text or "schema" in text.lower()

    def test_evidence_bundle_doc_has_required_sections(self):
        text = EVIDENCE_BUNDLE_DOC.read_text(encoding="utf-8")
        assert "manifest.json" in text
        assert "provenance.md" in text
        assert "Bundle Structure" in text or "bundle" in text.lower()


class TestSwarmExportFiles:
    def test_swarm_export_dir_has_valid_json_files(self):
        if not SWARM_EXPORT_DIR.exists():
            pytest.skip("no swarm exports directory yet")
        json_files = list(SWARM_EXPORT_DIR.glob("*.json"))
        if not json_files:
            pytest.skip("no swarm export files found")
        for jf in json_files:
            data = json.loads(jf.read_text(encoding="utf-8"))
            assert "agent_id" in data, f"{jf.name}: missing agent_id"
            assert "nodes" in data, f"{jf.name}: missing nodes"
            assert len(data["nodes"]) > 0, f"{jf.name}: empty nodes list"
