"""UWS gateway contract tests. Mocked binary, no external provider traffic."""
import io, json, sys, unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from uws_gateway import run_uws, proposal, interactive_approval

def ok(stdout='{"ok":true}'):
    return SimpleNamespace(returncode=0,stdout=stdout,stderr="")
def bad():
    return SimpleNamespace(returncode=1,stdout="",stderr="PRIVATE TOKEN")

class FullCapabilityTests(unittest.TestCase):
    def test_full_provider_reads_are_not_globally_restricted(self):
        self.assertEqual(proposal(["sheets","spreadsheets","values","get"])["operation"],"READ")
        self.assertEqual(proposal(["ms-mail","messages","list"])["risk"],"LOW")
        self.assertEqual(proposal(["apple-calendar","events","list"])["operation"],"READ")
        self.assertEqual(proposal(["chrome-policy","resolve"])["operation"],"READ")
    def test_writes_are_supported_but_require_a_trusted_approval(self):
        for cmd in (["gmail","users","messages","send"],
                    ["drive","files","create"],["ms-mail","messages","update"],
                    ["sheets","spreadsheets","values","append"]):
            self.assertEqual(proposal(cmd)["operation"],"WRITE_OR_UNKNOWN")
        self.assertEqual(run_uws(["drive","files","create"])["state"],"PLAN_ONLY")
    def test_unsafe_commands_denied_without_shell(self):
        for cmd in (["gmail","send;rm"],["--help"],["drive","files","/bin/sh"],
                    ["drive","files","list;echo"]):
            self.assertEqual(proposal(cmd)["state"],"DENIED")
    @patch("uws_gateway.subprocess.run")
    def test_read_goes_directly_to_cli(self,run):
        run.return_value=ok('{"documents":[]}')
        r=run_uws(["drive","files","list"],params={"pageSize":4},
                  execute=True,binary="uws")
        self.assertEqual(r["state"],"EXECUTED")
        self.assertEqual(run.call_count,1)
        self.assertIn("--params",run.call_args.args[0])
    @patch("uws_gateway.subprocess.run")
    def test_write_runs_preflight_then_actual_only_after_approval(self,run):
        run.side_effect=[ok('{"dryRun":true}'),ok('{"id":"created"}')]
        approval=[]
        def human(p):
            approval.append(p)
            return p["preflight_preview"]=='{"dryRun":true}' and p["risk"]=="APPROVAL_REQUIRED"
        r=run_uws(["drive","files","create"],body={"name":"Test"},execute=True,
                  binary="uws",approval_callback=human)
        self.assertEqual(r["state"],"EXECUTED")
        self.assertEqual(run.call_count,2)
        self.assertIn("--dry-run",run.call_args_list[0].args[0])
        self.assertNotIn("--dry-run",run.call_args_list[1].args[0])
        self.assertEqual(r["data"]["id"],"created")
        self.assertEqual(len(approval),1)
    @patch("uws_gateway.subprocess.run")
    def test_write_without_approval_does_not_mutate(self,run):
        run.return_value=ok('{"preview":true}')
        r=run_uws(["gmail","users","messages","send"],execute=True,binary="uws")
        self.assertEqual(r["state"],"APPROVAL_REQUIRED")
        self.assertEqual(run.call_count,1)
        self.assertIn("--dry-run",run.call_args.args[0])
    @patch("uws_gateway.subprocess.run")
    def test_deny_and_provider_errors_hide_secrets(self,run):
        run.return_value=bad()
        r=run_uws(["drive","files","delete"],execute=True,binary="uws",
                  approval_callback=lambda p: True)
        self.assertEqual(r["state"],"PREFLIGHT_ERROR")
        self.assertNotIn("PRIVATE TOKEN",str(r))
        self.assertEqual(run.call_count,1)
if __name__=="__main__":unittest.main()
