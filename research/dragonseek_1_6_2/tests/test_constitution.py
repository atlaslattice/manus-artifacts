import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ConstitutionRegistryTests(unittest.TestCase):
 def test_mandarin_dashboard_versioned(self):
  src=(ROOT/'index.html').read_text(encoding='utf-8')
  self.assertIn('lang="zh-CN"',src)
  self.assertIn('governance.html',src)
 def test_registry_is_not_misrepresented_as_complete(self):
  files=list((ROOT/'registry').glob('*.json'))
  for file in files:
   obj=json.loads(file.read_text())
   self.assertTrue(obj['source'])
   self.assertTrue(obj['entries'])
   for record in obj['entries']:
    self.assertTrue(record['id'])
    self.assertTrue(record['body'])
  self.assertEqual(len(files),7)
  self.assertFalse((ROOT/'registry'/'doctrines_05.json').exists())
  self.assertFalse((ROOT/'registry'/'doctrines_06.json').exists())
 def test_local_os_reports_missing(self):
  from sys import path
  path.insert(0,str(ROOT))
  from dragonseek_os import load
  records,missing=load()
  self.assertEqual(len(records),113)
  self.assertEqual(len(missing),2)
  self.assertTrue(any('doctrines_05' in p for p in missing))
 def test_offline_source_preserved(self):
  self.assertTrue((ROOT/'sources'/'Canon.tsx').is_file())
  self.assertTrue((ROOT/'sources'/'Invariants.tsx').is_file())
if __name__=='__main__':unittest.main()
