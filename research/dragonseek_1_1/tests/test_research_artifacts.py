import unittest,json,sys
from pathlib import Path
from datetime import datetime,timezone
from PIL import Image
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'engine'))
from dragonseek_v11 import release_gate
class Artifacts(unittest.TestCase):
 def test_46_unique_sources(self):
  d=json.loads((root/'evidence/planetary_data_adapter_inventory_v11.json').read_text());self.assertEqual(d['total'],46);self.assertEqual(len(set(v['id'] for v in d['adapters'])),46)
 def test_all_sources_unconnected(self):
  d=json.loads((root/'evidence/planetary_data_adapter_inventory_v11.json').read_text());self.assertTrue(all(v['runtime_connection_state']=='NOT_CONNECTED' for v in d['adapters']))
 def test_15_demo_events(self):
  d=json.loads((root/'evidence/demo_events_v11.json').read_text());self.assertEqual(len(d),15);self.assertTrue(all(release_gate(x)[0] for x in d))
 def test_celestial_not_geolocated(self):
  d=json.loads((root/'evidence/demo_celestial_v11.json').read_text());self.assertEqual(len(d),2);self.assertTrue(all('x' not in e and 'y' not in e and e['crs']=='NONE_CELESTIAL' and release_gate(e)[0] for e in d))
 def test_nodes_contain_explicit_crs(self):
  d=json.loads((root/'evidence/demo_nodes_v11.json').read_text());self.assertTrue(all(e['crs']=='EPSG:4326' and e['cii_operator_designation_status']=='UNKNOWN' for e in d))
 def test_basemap_14_10(self):
  with Image.open(root/'dashboard/china_oceans_basemap.png') as im:
   w,h=im.size
  self.assertEqual(w*10,h*14)
 def test_html_not_mobile_stretch(self):
  s=(root/'dashboard/index.html').read_text();self.assertNotIn('1/1.05',s);self.assertIn('aspect-ratio:14/10!important',s)
 def test_no_external_auto_poll(self):
  j=(root/'dashboard/app_v11.js').read_text();self.assertIn("$('weatherBtn').addEventListener('click',fetchWeather)",j);self.assertNotIn('setInterval(fetchWeather',j)
 def test_replenishment_label(self):
  s=(root/'dashboard/index.html').read_text();self.assertIn('INTENTIONALLY FAILING DEFAULT',s);self.assertIn('Compare storage-only vs solar replenishment',s)
 def test_cultural_asterisk(self):
  s=(root/'dashboard/index.html').read_text();self.assertIn('not astronomical causal evidence',s)
if __name__=='__main__':unittest.main()