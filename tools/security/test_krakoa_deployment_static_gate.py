"""Regression checks for static Krakoa HOLD classifier; no source execution."""
from __future__ import annotations

from hashlib import sha256
import unittest

from krakoa_deployment_static_gate import inspect_bytes, MAX_BYTES


def codes(source: bytes) -> set[str]:
    return {x["code"] for x in inspect_bytes(source)["findings"]}


class KrakoaStaticGateTests(unittest.TestCase):
    def test_minimal_source_remains_review_only(self):
        report = inspect_bytes(b"def preview():\n    return {'synthetic': True}\n")
        self.assertEqual(report["status"], "STATIC_REVIEW_ONLY")
        self.assertIs(report["deployment_authorized"], False)
        self.assertIs(report["source_executed"], False)
        self.assertFalse(report["principal_authenticated"])

    def test_empty_source_holds(self):
        self.assertIn("SOURCE_MISSING_OR_OVER_SIZE", codes(b""))

    def test_oversize_source_holds(self):
        self.assertIn("SOURCE_MISSING_OR_OVER_SIZE", codes(b"#" + b"a"*MAX_BYTES))

    def test_syntax_error_holds(self):
        self.assertIn("UNPARSEABLE_OR_INVALID_SOURCE", codes(b"def bad(:\n pass\n"))

    def test_binary_source_holds(self):
        self.assertIn("UNPARSEABLE_OR_INVALID_SOURCE", codes(b"\xff"))

    def test_subprocess_import_holds(self):
        self.assertIn("PROCESS_EXECUTION_IMPORT", codes(b"import subprocess\n"))

    def test_subprocess_importfrom_holds(self):
        self.assertIn("PROCESS_EXECUTION_IMPORT", codes(b"from subprocess import run\n"))

    def test_mcp_server_import_holds(self):
        self.assertIn("REAL_MCP_SERVER_IMPORT_UNREVIEWED", codes(b"from mcp.server.fastmcp import FastMCP\n"))

    def test_subprocess_run_call_holds(self):
        self.assertIn("PROCESS_EXECUTION_CALL", codes(b"subprocess.run(['echo', 'x'])\n"))

    def test_sphere_write_tool_holds(self):
        self.assertIn("UNAUTHENTICATED_WRITE_SURFACE", codes(b"async def krakoa_sphere_write(x):\n return x\n"))

    def test_shadow_sweep_tool_holds(self):
        self.assertIn("LOCAL_HISTORY_COLLECTION_SURFACE", codes(b"async def krakoa_shadow_sweep(x):\n return x\n"))

    def test_device_haptics_tool_holds(self):
        self.assertIn("PHYSICAL_DEVICE_EFFECT_SURFACE", codes(b"async def krakoa_haptic_pulse(x):\n return x\n"))

    def test_cloud_tool_holds(self):
        self.assertIn("CLOUD_PROCESS_SURFACE", codes(b"async def krakoa_gcp_status(x):\n return x\n"))

    def test_filesystem_mutation_holds(self):
        self.assertIn("FILESYSTEM_MUTATION_CALL", codes(b"path.write_text('x')\n"))

    def test_directory_creation_holds(self):
        self.assertIn("FILESYSTEM_MUTATION_CALL", codes(b"path.mkdir(parents=True)\n"))

    def test_file_write_holds(self):
        self.assertIn("FILESYSTEM_WRITE_OPEN", codes(b"f = open('x', 'a')\n"))

    def test_file_read_does_not_trigger_write(self):
        self.assertNotIn("FILESYSTEM_WRITE_OPEN", codes(b"f = open('x', 'r')\n"))

    def test_dynamic_mode_holds(self):
        self.assertIn("DYNAMIC_FILE_OPEN_MODE", codes(b"f = open('x', mode=unknown)\n"))

    def test_local_history_reference_holds(self):
        self.assertIn("SENSITIVE_LOCAL_SOURCE_REFERENCE", codes(b"path='~/.bash_history'\n"))

    def test_untrusted_mcp_startup_holds(self):
        self.assertIn("ACTIVE_SERVER_ENTRYPOINT_UNREVIEWED", codes(b"mcp.run()\n"))

    def test_commented_out_dangerous_code_is_not_executed_or_flagged(self):
        report = inspect_bytes(b"# subprocess.run(['x'])\ndef preview(): return 1\n")
        self.assertEqual(report["status"], "STATIC_REVIEW_ONLY")

    def test_no_source_body_in_receipt(self):
        raw = b"private_sample='~/.zsh_history'\n"
        receipt = inspect_bytes(raw)
        self.assertNotIn(raw.decode(), str(receipt))
        self.assertEqual(receipt["source_sha256"], sha256(raw).hexdigest())

    def test_findings_stably_sorted(self):
        report = inspect_bytes(b"import subprocess\nmcp.run()\npath.mkdir()\n")
        self.assertEqual(report["findings"], sorted(report["findings"], key=lambda x: (x["line"], x["code"])))


if __name__ == "__main__":
    unittest.main()
