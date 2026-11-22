import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import graph_bridge,dual_brain
from parser_bridge import normalize
from atlas_fabric import ReceiptGraph,run_uws_readonly
class IntegratedFabricTests(unittest.TestCase):
 def test_source_linked_143_registry_graph(self):
  g=ReceiptGraph()
  c=graph_bridge.seed_constitution(g)
  self.assertEqual(c["invariants"],41)
  self.assertEqual(c["doctrines"],102)
  self.assertTrue(g.search("INV-0"))
  proposed=g.search("D-98-CN")
  self.assertEqual(len(proposed),1)
  self.assertEqual(proposed[0]["status"],"claim_candidate")
  self.assertTrue(any(x["relation"]=="CONTRADICTS" for x in g.linked("dragonseek:invariants:INV-0")))
 def test_real_shugs_source_is_nonnative_proof(self):
  f=ROOT/"experimental/shugs_lattice_optimum_original.json"
  packet=json.loads(f.read_text())
  graph=ReceiptGraph()
  r=graph_bridge.add_shugs_packet(graph,packet,str(f),"element145:original")
  self.assertEqual(r["classification"],"THEORETICAL_OR_SIMULATED_NOT_PHYSICALLY_VALIDATED")
  self.assertEqual(len(graph.search("SHUGS")),1)
 def test_parser_keeps_hidden_traces_out(self):
  raw={"conversations":[{"conversation":{"id":"thread-1"},"responses":[
    {"response":{"sender":"human","message":"hi"}},
    {"response":{"sender":"assistant","message":"hello","thinking_trace":"sensitive"}}]}]}
  normalized=normalize(raw,"sha256:xyz")
  self.assertEqual(len(normalized),2)
  self.assertNotIn("thinking_trace",json.dumps(normalized))
 def test_dual_brain_prompt_preparation_stays_offline(self):
  p,r=dual_brain.prepare_pair("What is INV-0?","local-main","local-check")
  self.assertEqual(p["model"],"local-main")
  self.assertEqual(r["model"],"local-check")
  self.assertTrue(any("independent counter-review brain" in m["content"] for m in r["messages"]))
  self.assertNotIn("tools",p)
 def test_write_refusals(self):
  self.assertEqual(run_uws_readonly(["gmail","users","messages","send"],execute=True)["state"],"DENIED")
  graph=ReceiptGraph()
  with self.assertRaises(ValueError):
   graph.add_node(node_id="x",kind="Claim",title="auto",source="x",receipt="x",status="canon")
 def test_ui_has_real_draft_status(self):
  self.assertIn("双脑核验", (ROOT/"fabric.html").read_text())
  self.assertIn("./fabric.html",(ROOT/"index.html").read_text())
if __name__=="__main__":unittest.main()
