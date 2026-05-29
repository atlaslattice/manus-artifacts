"""
Unit tests for codebases/other/artifact_sync.py (ArtifactSync + DualPlatformArchiver).

Run from repo root:
    python -m pytest codebases/tests/test_artifact_sync.py -v
"""
import importlib.util
import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# ---------------------------------------------------------------------------
# Import the module under test regardless of working directory
# ---------------------------------------------------------------------------
_MODULE_PATH = Path(__file__).parent.parent / "other" / "artifact_sync.py"
_spec = importlib.util.spec_from_file_location("artifact_sync", _MODULE_PATH)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

ArtifactSync = _mod.ArtifactSync
DualPlatformArchiver = _mod.DualPlatformArchiver


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_sync() -> ArtifactSync:
    return ArtifactSync()


# ---------------------------------------------------------------------------
# _generate_id
# ---------------------------------------------------------------------------

class TestGenerateId:
    def test_format(self):
        sync = _make_sync()
        artifact_id = sync._generate_id("/some/file.md")
        assert artifact_id.startswith("ART_"), f"Expected ART_ prefix, got {artifact_id}"
        parts = artifact_id.split("_")
        # ART_YYYYMMDD_HHMMSS_<hash8>
        assert len(parts) == 4, f"Unexpected ID format: {artifact_id}"
        assert len(parts[3]) == 8, "Hash suffix should be 8 chars"

    def test_different_paths_give_different_ids(self):
        sync = _make_sync()
        id1 = sync._generate_id("/path/a.md")
        id2 = sync._generate_id("/path/b.md")
        # Hash suffixes differ
        assert id1.split("_")[3] != id2.split("_")[3]


# ---------------------------------------------------------------------------
# sync_artifact – file not found
# ---------------------------------------------------------------------------

class TestSyncArtifactFileNotFound:
    def test_returns_error_dict(self):
        sync = _make_sync()
        result = sync.sync_artifact("/nonexistent/path/artifact.md")
        assert result["success"] is False
        assert "not found" in result["error"].lower()


# ---------------------------------------------------------------------------
# sync_artifact – happy path (mocked sub-calls)
# ---------------------------------------------------------------------------

class TestSyncArtifactHappyPath:
    def test_calls_all_platforms(self, tmp_path):
        artifact_file = tmp_path / "sample.md"
        artifact_file.write_text("# Hello World\nContent here.")

        sync = _make_sync()
        sync._sync_to_notion = MagicMock(return_value={"success": True, "url": "https://notion.so/x"})
        sync._sync_to_drive = MagicMock(return_value={"success": True, "path": "inbox/sample.md"})
        sync._sync_to_pinecone = MagicMock(return_value={"success": True, "id": "ART_x", "index": "manus-artifacts"})

        with patch.dict(os.environ, {"PINECONE_API_KEY": "fake-key"}):
            result = sync.sync_artifact(str(artifact_file))

        assert result["platforms"]["notion"]["success"] is True
        assert result["platforms"]["drive"]["success"] is True
        assert result["platforms"]["pinecone"]["success"] is True
        sync._sync_to_notion.assert_called_once()
        sync._sync_to_drive.assert_called_once()
        sync._sync_to_pinecone.assert_called_once()

    def test_skips_pinecone_when_no_key(self, tmp_path):
        artifact_file = tmp_path / "sample.md"
        artifact_file.write_text("content")

        sync = _make_sync()
        sync._sync_to_notion = MagicMock(return_value={"success": True})
        sync._sync_to_drive = MagicMock(return_value={"success": True})
        sync._sync_to_pinecone = MagicMock()

        env = {k: v for k, v in os.environ.items() if k != "PINECONE_API_KEY"}
        with patch.dict(os.environ, env, clear=True):
            result = sync.sync_artifact(str(artifact_file))

        sync._sync_to_pinecone.assert_not_called()
        assert result["platforms"]["pinecone"].get("skipped") is True


# ---------------------------------------------------------------------------
# _sync_to_pinecone – ImportError path
# ---------------------------------------------------------------------------

class TestSyncToPineconeImportError:
    def test_returns_error_on_missing_package(self):
        sync = _make_sync()
        with patch.dict(sys.modules, {"pinecone": None}):
            result = sync._sync_to_pinecone({"id": "x", "title": "t", "content": "c",
                                              "filename": "f.md", "sphere": "S1",
                                              "category": "Tech", "priority": "High",
                                              "timestamp": "2026-01-01", "hash": "abc"})
        assert result["success"] is False
        assert "pinecone" in result["error"].lower()


# ---------------------------------------------------------------------------
# _check_drive
# ---------------------------------------------------------------------------

class TestCheckDrive:
    def test_rclone_not_found(self):
        sync = _make_sync()
        with patch("subprocess.run", side_effect=FileNotFoundError):
            result = sync._check_drive("*.md")
        assert result["exists"] is False
        assert "rclone" in result["error"].lower()

    def test_rclone_returns_match(self):
        sync = _make_sync()
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "ART_20260101_120000_abcd1234.md\n"
        with patch("subprocess.run", return_value=mock_result):
            result = sync._check_drive("ART_*.md")
        assert result["exists"] is True
        assert len(result["files"]) == 1

    def test_rclone_returns_empty(self):
        sync = _make_sync()
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = ""
        with patch("subprocess.run", return_value=mock_result):
            result = sync._check_drive("ART_*.md")
        assert result["exists"] is False


# ---------------------------------------------------------------------------
# _check_prerequisites
# ---------------------------------------------------------------------------

class TestCheckPrerequisites:
    def test_all_missing(self):
        sync = _make_sync()
        env = {k: v for k, v in os.environ.items()
               if k not in ("NOTION_API_KEY", "PINECONE_API_KEY")}
        with patch.dict(os.environ, env, clear=True), \
             patch("subprocess.run", side_effect=FileNotFoundError):
            prereqs = sync._check_prerequisites()
        assert prereqs["notion"] is False
        assert prereqs["pinecone"] is False
        assert prereqs["drive"] is False

    def test_keys_set(self):
        sync = _make_sync()
        mock_run = MagicMock()
        mock_run.return_value = MagicMock(returncode=0)
        env_override = {"NOTION_API_KEY": "n-key", "PINECONE_API_KEY": "p-key"}
        with patch.dict(os.environ, env_override), \
             patch("subprocess.run", mock_run):
            prereqs = sync._check_prerequisites()
        assert prereqs["notion"] is True
        assert prereqs["pinecone"] is True
        assert prereqs["drive"] is True


# ---------------------------------------------------------------------------
# generate_sync_report
# ---------------------------------------------------------------------------

class TestGenerateSyncReport:
    def test_structure(self, tmp_path):
        artifact_file = tmp_path / "report_test.md"
        artifact_file.write_text("# Report test")

        sync = _make_sync()
        sync._sync_to_notion = MagicMock(return_value={"success": True})
        sync._sync_to_drive = MagicMock(return_value={"success": True})
        sync._sync_to_pinecone = MagicMock(return_value={"success": True})

        env = {k: v for k, v in os.environ.items() if k != "PINECONE_API_KEY"}
        with patch.dict(os.environ, env, clear=True):
            sync.sync_artifact(str(artifact_file))

        report = sync.generate_sync_report()
        assert "ARTIFACT SYNC REPORT" in report
        assert "notion" in report


# ---------------------------------------------------------------------------
# DualPlatformArchiver – keep unavailable path
# ---------------------------------------------------------------------------

class TestDualPlatformArchiver:
    def test_keep_unavailable_graceful(self):
        with patch("subprocess.run", side_effect=FileNotFoundError):
            archiver = DualPlatformArchiver()
        assert archiver.keep_available is False

    def test_archive_notion_only(self):
        with patch("subprocess.run", side_effect=FileNotFoundError):
            archiver = DualPlatformArchiver()

        mock_result = MagicMock()
        mock_result.returncode = 0
        with patch("subprocess.run", return_value=mock_result):
            result = archiver._archive_to_notion("content", "title", "High")
        assert result["success"] is True
