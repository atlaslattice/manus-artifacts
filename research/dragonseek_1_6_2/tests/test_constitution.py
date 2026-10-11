import json,sys,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import dragonseek_os
import ai_bridge

class ConstitutionalIntegrationTests(unittest.TestCase):
 def test_local_dashboard_and_registry_ui(self):
  dashboard=(ROOT/"index.html").read_text(encoding="utf-8")
  ui=(ROOT/"governance.html").read_text(encoding="utf-8")
  self.assertIn('lang="zh-CN"',dashboard)
  self.assertIn('governance.html',dashboard)
  self.assertIn("constitutional_authority.json",ui)
  self.assertIn("05a",ui)
  self.assertIn("06b",ui)
 def test_complete_local_constitution(self):
  data=dragonseek_os.load()
  self.assertEqual(data["missing"],[],data["missing"])
  self.assertTrue(data["complete"])
  self.assertEqual(data["counts"],{"invariants":41,"doctrines":102})
  self.assertEqual(len(data["entries"]),143)
  self.assertEqual(len({(e["kind"],e["id"]) for e in data["entries"]}),143)
 def test_inv0_never_replaced(self):
  data=dragonseek_os.load()
  canon=[e for e in data["entries"] if e["id"]=="INV-0"]
  self.assertEqual(len(canon),1)
  self.assertEqual(canon[0]["name"],"Nothing Dies")
  self.assertTrue(any(e["name"]=="System Integrity" for e in data["historical_variants"]))
  self.assertEqual(data["authority"]["related_distinct"][0]["status"],"HISTORICAL_CONFLICT_NOT_ACTIVE_INV0")
 def test_source_archive_full_preserved(self):
  pieces=[(ROOT/"sources"/f"April2026_Complete_Doctrine_Invariant_Registry_v1.1.part{i:02d}.md").read_text(encoding="utf-8") for i in range(1,9)]
  whole="".join(pieces)
  self.assertEqual(len(whole),45615)
  self.assertIn("INV-0 (Nobody Dies)",whole)
  self.assertIn("As-If-Ratified-But-Mislabeled",whole)
  self.assertIn("INV-0: Nobody Dies",(ROOT/"sources"/"Declaration_of_Mutual_Life_v1.0.md").read_text())
 def test_ai_context_has_source_and_mandatory_invariant(self):
  data=dragonseek_os.load()
  refs=dragonseek_os.context(data,"INV-0")
  self.assertEqual(refs["state"],"CONSTITUTION_REFERENCE")
  self.assertEqual(refs["matches"][0]["name"],"Nothing Dies")
  p=ai_bridge.model_payload("How does INV-0 apply?","local-test-model")
  self.assertEqual(p["model"],"local-test-model")
  sysmsg=p["messages"][1]["content"]
  self.assertIn("Nothing Dies",sysmsg)
  self.assertIn("System Integrity",sysmsg)
  self.assertNotIn("tools",p)
 def test_reference_authorization_denies_side_effects(self):
  data=dragonseek_os.load()
  self.assertEqual(dragonseek_os.authorize_reference(data,"constitution.search")["decision"],"ALLOW_READ_ONLY")
  self.assertEqual(dragonseek_os.authorize_reference(data,"execute.remote_write")["decision"],"HUMAN_REVIEW_REQUIRED")
  self.assertEqual(dragonseek_os.authorize_reference(data,"autonomous lethal action")["decision"],"HUMAN_REVIEW_REQUIRED")
 def test_missing_corpus_fails_closed(self):
  from tempfile import TemporaryDirectory
  with TemporaryDirectory() as tmp,patch.object(dragonseek_os,"ROOT",Path(tmp)):
   data=dragonseek_os.load()
   self.assertFalse(data["complete"])
   self.assertEqual(dragonseek_os.context(data,"INV-0")["state"],"BLOCKED_INCOMPLETE_CORPUS")
   self.assertEqual(dragonseek_os.authorize_reference(data,"monitor.read")["decision"],"BLOCK")
if __name__=="__main__":unittest.main()
