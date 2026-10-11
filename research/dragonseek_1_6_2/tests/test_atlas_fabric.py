import sys,unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from atlas_fabric import (run_uws_readonly,query_sheldonbrain,ReceiptGraph,
                          cycle_plan,dream_packet,compare_brains,endpoint_allowed)

class FabricTests(unittest.TestCase):
    def test_uws_dry_run_and_write_denial(self):
        self.assertEqual(run_uws_readonly(["drive","files","list"])["state"],"DRY_RUN")
        self.assertEqual(run_uws_readonly(["gmail","users","messages","send"],execute=True)["state"],"DENIED")
        self.assertEqual(run_uws_readonly(["drive","files","delete"],execute=True)["state"],"DENIED")
    def test_sheldonbrain_optin(self):
        self.assertEqual(query_sheldonbrain("verify receipt")["state"],"DRY_RUN")
        self.assertEqual(query_sheldonbrain("private",base_url="https://example.com")["state"],"DENIED")
        self.assertTrue(endpoint_allowed("http://127.0.0.1:8080/query"))
        self.assertFalse(endpoint_allowed("http://example.com/query",True))
    def test_receipt_kg(self):
        g=ReceiptGraph()
        g.add_node(node_id="s1",kind="SourceArtifact",title="Source",source="git:x",receipt="sha:a")
        g.add_node(node_id="c1",kind="Claim",title="Candidate",source="git:y",receipt="sha:b",status="claim_candidate")
        g.add_edge("c1","s1","DERIVED_FROM","receipt:123")
        self.assertEqual(len(g.search("Candidate")),1)
        self.assertEqual(len(g.linked("c1")),1)
        with self.assertRaises(ValueError):
            g.add_node(node_id="s1",kind="SourceArtifact",title="Silent rewrite",source="git:x",receipt="sha:a")
        self.assertEqual(g.search("Source")[0]["status"],"raw")
    def test_dream_is_unbounded_ideas_bounded_execution(self):
        phases=cycle_plan()
        self.assertEqual([x["phase"] for x in phases],["DREAM","PLAY","WORK"])
        self.assertEqual(phases[-1]["end_hour"],24)
        p=dream_packet(["git:abc"],"New cross-domain idea")
        self.assertEqual(p["status"],"NON_CANON")
        self.assertFalse(p["no_native_memory_or_model_training_claim"] is False)
        self.assertEqual(p["permission"],"NO_EXTERNAL_ACTIONS")
    def test_independent_brain_reports_are_advisory(self):
        x=compare_brains({"model":"a","lineage":"A","text":"Claim 1","receipts":["1","2"]},
                         {"model":"b","lineage":"B","text":"Contradiction","receipts":["2","3"]})
        self.assertTrue(x["independent_lineages_declared"])
        self.assertEqual(x["shared_receipts"],["2"])
        self.assertEqual(x["state"],"REVIEW_REQUIRED")
        self.assertEqual(compare_brains({}, {})["state"],"INSUFFICIENT_EVIDENCE")
if __name__=="__main__":unittest.main()
