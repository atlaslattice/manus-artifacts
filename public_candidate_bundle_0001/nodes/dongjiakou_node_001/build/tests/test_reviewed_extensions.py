import copy
import json
from pathlib import Path
import pytest
from jsonschema import Draft202012Validator
from models.current_state import run, validate_stream
from resource_gap.simulate import simulate

ROOT = Path(__file__).resolve().parents[1] / 'resource_gap'

def case(name='synthetic_biological_P'):
    return json.loads((ROOT / 'examples' / (name + '.json')).read_text())

def test_all_examples_match_standard_schema():
    schema = json.loads((ROOT / 'scenario.schema.json').read_text())
    Draft202012Validator.check_schema(schema)
    for p in (ROOT / 'examples').glob('*.json'):
        Draft202012Validator(schema).validate(json.loads(p.read_text()))

def test_mass_balance_and_reserve_flow_are_distinct():
    out = simulate(case())
    assert out['gap_plus_reserve_build_t_y'] == dict(low=4500, high=4500)
    assert out['routes'][0]['accepted_dry_feed_t_y']['low'] == pytest.approx(3420)
    assert out['routes'][0]['gross_product_t_y']['low'] == pytest.approx(68.4)
    assert out['remaining_gap_t_y']['low'] == pytest.approx(4431.6)
    assert out['realized_credit_t_y'] == 0

def test_unknown_is_not_zero_and_fail_does_not_pass():
    out = simulate(case('dongjiakou_unknown'))
    assert out['evidence_gated_total_t_y'] is None
    assert out['remaining_gap_t_y'] is None
    c = case(); c['routes'][0]['module_receipts']['ecology']['status'] = 'FAIL'
    out = simulate(c)
    assert out['routes'][0]['gate_state'] == 'BLOCKED'
    assert out['evidence_gated_total_t_y'] == dict(low=0,high=0)

def test_unknown_energy_prevents_gate_promotion():
    c = case(); q=c['routes'][0]['process']['energy_intensity']
    q.update(low=None,high=None,status='UNKNOWN',source=None)
    assert simulate(c)['routes'][0]['evidence_gated_product_t_y'] is None

@pytest.mark.parametrize('error', ['duplicate','basis','ceiling','stock_unit','fraction','pass_without_source','zero_horizon'])
def test_invalid_allocation_and_dimensions_are_rejected(error):
    c=case(); r=c['routes'][0]
    if error=='duplicate':
        duplicate=copy.deepcopy(r); duplicate['id']='other'; c['routes'].append(duplicate)
    if error=='basis': r['product_basis']='K2O'
    if error=='ceiling': r['process']['yield'].update(low=.1,high=.1)
    if error=='stock_unit': c['demand']['reserve_stock']['unit']='t_product/y'
    if error=='fraction': r['feed']['allocated_fraction']['high']=1.1
    if error=='pass_without_source': r['module_receipts']['yield']['source']=None
    if error=='zero_horizon': c['demand']['reserve_build_years']=0
    with pytest.raises(ValueError): simulate(c)

def test_reviewed_topology_never_collapses_water_buyer_sets():
    x=run()
    assert x['counts']==dict(boundary_units=20, internal_units=19, streams=23, physical=5, opportunity=18)
    assert set(x['nodes'])==set(x['node_meta'])
    water=next(s for s in x['streams'] if s['stream_id']=='S-W01-IND-01')
    assert water['sink_subnode'] is None
    assert water['sink_nodes']==['QSS01','JNC01','BTN01']
    assert water['boundary_crossing']=='UNKNOWN_MIXED'
    assert water['quantity_by_sink'] is None
    water['sink_subnode']='QSS01'
    with pytest.raises(ValueError): validate_stream(water,x['nodes'])

def test_ecology_and_lng_receipts_do_not_create_credit():
    x=run()
    assert len(x['vetoes'])==6
    assert all(v['state']=='UNRESOLVED' for v in x['vetoes'].values())
    assert x['vetoes']['INV-19']['evidence_basis']=='SECONDARY_ONLY'
    assert 'supports_INV19' not in x['vetoes']['INV-19']
    assert x['lng']['projected_generation_GWh_y']==26
    assert x['lng']['projected_avoided_cooling_grid_GWh_y']==8
    assert x['realized_credit']==0
    assert all(s['realized_credit']==0 for s in x['streams'])
