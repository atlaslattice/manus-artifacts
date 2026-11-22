import copy
import json
from pathlib import Path
import pytest
from jsonschema import Draft202012Validator
from models.qol import evaluate, default_case, registry
from models.current_state import run

Q=Path(__file__).resolve().parents[1]/'qol'

def complete_case():
    c=default_case()
    c.update(node_id='TEST-ONLY',boundary_id='TEST-BOUNDARY',required_strata=['residents'],
             comparison=dict(design='CONTROLLED_ALIGNED',source='test design assertion'))
    c['gates']={k:dict(status='PASS',source='test receipt assertion') for k in c['gates']}
    for d in registry()['indicators']:
        def q(value,period):
            return dict(low=value,high=value,evidence_class='MEASURED_LOCAL',source='test only',
                        method='test fixture, not a field measurement',boundary_id='TEST-BOUNDARY',
                        protocol_id='same-test-protocol',period_end=period)
        value=.5 if d['maximum']==1 else 2
        c['observations'].append(dict(indicator_id=d['id'],stratum='residents',unit=d['unit'],sample_n=100,
            baseline=q(value,c['baseline_period_end']),followup=q(value,c['followup_period_end'])))
    return c

def test_unknowns_are_vector_dimensions_not_zero_or_score():
    out=evaluate()
    assert len(out['objective_vector'])==32*6
    assert out['composite_score'] is None
    assert out['decision']=='HOLD_MISSING_BASELINE_OR_RECEIPTS'
    assert all(o['change_interval'] is None for o in out['objective_vector'])
    assert out['realized_credit']==0

def test_complete_supplied_inputs_only_enable_independent_review():
    out=evaluate(complete_case())
    assert out['decision']=='ELIGIBLE_FOR_INDEPENDENT_REVIEW_ONLY'
    assert out['locality_clearance']=='NOT_ESTABLISHED'
    assert out['realized_credit']==0

def test_average_gain_never_masks_cohort_decline():
    c=complete_case(); r=c['observations'][0]
    r['followup'].update(low=5,high=5)
    d=copy.deepcopy(r);d['stratum']='shift_workers';d['followup'].update(low=1,high=1)
    c['observations'].append(d)
    assert evaluate(c)['decision']=='HOLD_DISTRIBUTIONAL_DECLINE'

@pytest.mark.parametrize('gate',['worker_safety','ecological_protection','privacy_and_consent','access_and_non_displacement','water_and_product_safety','maintenance_and_lifecycle'])
def test_failure_cannot_be_offset_by_beauty_or_production(gate):
    c=complete_case(); c['gates'][gate]['status']='FAIL'
    assert evaluate(c)['decision']=='BLOCKED_BY_NON_COMPENSABLE_GATE'

@pytest.mark.parametrize('change',['reference','synthetic','uncontrolled','protocol'])
def test_references_and_bad_design_do_not_become_local_attributed_benefits(change):
    c=complete_case();r=c['observations'][0];r['followup'].update(low=3,high=3)
    if change=='reference': r['followup']['evidence_class']='REPORTED_REFERENCE'
    if change=='synthetic': r['followup']['evidence_class']='SYNTHETIC'
    if change=='uncontrolled': c['comparison']['design']='OBSERVATIONAL'
    if change=='protocol':r['followup']['protocol_id']='changed instrument'
    out=evaluate(c)
    assert out['decision']=='HOLD_MISSING_BASELINE_OR_RECEIPTS'
    assert not any(o['state']=='IMPROVEMENT_SUPPORTED_BY_SUPPLIED_INPUTS' for o in out['objective_vector'])

def test_small_cohort_public_values_are_suppressed():
    c=complete_case(); c['observations'][0]['sample_n']=9
    out=evaluate(c)
    assert out['objective_vector'][0]['change_interval'] is None
    assert out['objective_vector'][0]['state']=='SUPPRESSED_PRIVACY_OR_SAMPLE_GATE'
    assert out['decision']=='HOLD_MISSING_BASELINE_OR_RECEIPTS'

@pytest.mark.parametrize('bad',['unit','interval','percent','boundary','period','duplicate','source','pii','date'])
def test_invalid_dimensions_provenance_and_personal_fields_are_rejected(bad):
    c=complete_case();r=c['observations'][0]
    if bad=='unit':r['unit']='kWh'
    if bad=='interval':r['baseline'].update(low=10,high=1)
    if bad=='percent':c['observations'][1]['followup'].update(low=101,high=101)
    if bad=='boundary':r['baseline']['boundary_id']='another-site'
    if bad=='period':r['followup']['period_end']='2024-01-01'
    if bad=='duplicate':c['observations'].append(copy.deepcopy(r))
    if bad=='source':r['baseline']['source']=None
    if bad=='pii':r['person_name']='private individual'
    if bad=='date':c['followup_period_end']=c['baseline_period_end']
    with pytest.raises(ValueError):evaluate(c)

def test_examples_validate_with_independent_jsonschema():
    s=json.loads((Q/'observation.schema.json').read_text())
    Draft202012Validator.check_schema(s)
    for p in (Q/'examples').glob('*.json'):
        c=json.loads(p.read_text());Draft202012Validator(s).validate(c);evaluate(c)

def test_qol_links_are_not_material_streams_and_vetoes_survive():
    out=run()
    assert out['node_meta']['QOL01']['node_kind']=='FUNCTIONAL_AGGREGATE'
    assert out['counts']==dict(boundary_units=20,internal_units=19,streams=23,physical=5,opportunity=18)
    assert len(out['observation_links'])==5
    assert all(not l['material_flow'] for l in out['observation_links'])
    assert len(out['vetoes'])==6
    assert all(v['state']=='UNRESOLVED' for v in out['vetoes'].values())
    assert out['qol']['first_class_objective']
