"""Reviewed additive overlay; recovered locality.py remains a historical snapshot."""
from copy import deepcopy
from . import locality

REVIEW_SOURCE = 'https://www.notion.so/3f20c1de73d9811491b5fd911ff37fa2'


def validate_stream(stream, nodes):
    sinks = stream.get('sink_nodes', [])
    if len(sinks) > 1 and stream['sink_subnode'] is not None:
        raise ValueError('A multi-sink hyperedge cannot carry a canonical sink')
    endpoints = [stream['source_subnode']] + sinks
    if stream['sink_subnode'] is not None:
        endpoints.append(stream['sink_subnode'])
    if any(n not in nodes for n in endpoints):
        raise ValueError('Unregistered endpoint')
    if stream['realized_credit'] != 0:
        raise ValueError('This reviewed snapshot has no metered credits')


def run():
    nodes = {k: v for k, v in locality.SUBNODES.items() if k != 'IND01'}
    nodes.update(QSS01='Qingdao Special Steel', JNC01='Jinneng Chemical',
                 BTN01='Bangtuo New Materials', LDC01='Louis Dreyfus food park',
                 QOL01='Human QOL / Eden outcome and stewardship register')
    meta = {}
    for node in nodes:
        kind = ('FUNCTIONAL_AGGREGATE' if node == 'QOL01' else 'FACILITY_ASSET' if node in ('QSS01', 'JNC01', 'BTN01', 'LDC01')
                else 'GOVERNANCE' if node in ('ECO01', 'GOV01')
                else 'EXTERNAL_BOUNDARY' if node == 'EXT01' else 'PROCESS_ASSET')
        status = ('OPERATIONAL' if node in ('W01', 'P01', 'QSS01', 'JNC01', 'BTN01', 'ECO01', 'GOV01')
                  else 'UNDER_CONSTRUCTION' if node in ('LDC01', 'E02')
                  else 'NOT_APPLICABLE' if node == 'EXT01' else 'UNKNOWN')
        meta[node] = dict(node_kind=kind, asset_status=status,
                          functional_roles=[nodes[node]], source=REVIEW_SOURCE)
    streams = deepcopy(locality.known_streams())
    streams = [s for s in streams if s['stream_id'] != 'S-MAT01-EXT-01']
    for s in streams:
        s['realized_credit'] = 0
        s['review_source'] = REVIEW_SOURCE
        s['sink_nodes'] = [s['sink_subnode']]
        if s['stream_id'] == 'S-W01-IND-01':
            s.update(sink_subnode=None, sink_nodes=['QSS01', 'JNC01', 'BTN01'],
                     sink_disaggregated=False, quantity_total_m3_y=17930000,
                     quantity_year=2025, contract_minimum_m3_day=70000,
                     quantity_by_sink=None, boundary_crossing='UNKNOWN_MIXED',
                     internal_quantity=None, external_quantity=None,
                     additional_buyer='West Coast Water Affairs: location and downstream allocation UNKNOWN')
        if s['stream_id'] in ('S-MAT01-M01-01', 'S-MAT01-M01-02'):
            s['stream_id'] = ('S-MAT01-EXT-02' if s['stream_id'].endswith('-01') else 'S-MAT01-EXT-03')
            s.update(sink_subnode='EXT01', sink_nodes=['EXT01'], allocation_owner='NONE')
        if s['stream_id'] == 'S-E02-IND-01':
            s['stream_id'] = 'S-E02-P01-01'
        if s['stream_id'] == 'S-MAT01-M01-C1':
            s['review_note'] = 'Construction waste processing capability gap; outsourced service is not a dedicated processing facility.'
    template = next(s for s in streams if s['stream_id'] == 'S-MAT01-M01-C1')
    for suffix, note in [('C2', 'Tire-derived carbon black to AM: quality, trial and offtake UNKNOWN.'),
                         ('C3', 'Slag to AM: existing cement/material use does not establish surplus.')]:
        s = deepcopy(template)
        s.update(stream_id='S-MAT01-M01-' + suffix, quantity='UNKNOWN',
                 evidence_class='UNKNOWN', review_note=note)
        streams.append(s)
    for s in streams:
        validate_stream(s, nodes)
    vetoes = deepcopy(locality.veto_register())
    vetoes['INV-19'].update(stream_identity_match='SUPPORTED_SECONDARY',
        evidence_basis='SECONDARY_ONLY', permit_limits=None,
        primary_monitoring=None, veto_clearance='INSUFFICIENT')
    vetoes['INV-20'] = dict(state='UNRESOLVED',
        definition='Marine discharge earns no net-positive credit without measured ecosystem benefit.',
        current_evidence_class='NO_MEASURABLE_HARM', meets_net_positive_standard=False)
    physical = sum(s['edge_state'] in locality.PHYSICAL_EDGE_STATES for s in streams)
    from .qol import evaluate
    qol = evaluate()
    observation_links = [dict(source_subnode=n,sink_subnode='QOL01',kind='PROPOSED_OBSERVATION_OR_SERVICE_LINK',material_flow=False,realized_credit=0) for n in ['ECO01','P01','E02','C01','W01']]
    return dict(qol=qol, observation_links=observation_links, classification='REVIEWED_PUBLIC_CANDIDATE_NON_CANON',
        source_package='recovered historical Manus ZIP plus reviewed Notion overlay; not the unavailable latest Manus source',
        source=REVIEW_SOURCE, nodes=nodes, node_meta=meta, streams=streams,
        counts=dict(boundary_units=len(nodes), internal_units=len(nodes)-1,
                    streams=len(streams), physical=physical, opportunity=len(streams)-physical),
        vetoes=vetoes, locality_clearance='NOT_ESTABLISHED', realized_credit=0,
        lng=dict(project_status='UNDER_CONSTRUCTION_REPORTED_2026_06',
            projected_generation_GWh_y=26, projected_avoided_cooling_grid_GWh_y=8,
            combined_electrical_system_impact_GWh_y=34, current_credit=0,
            rule='Separate generation and avoided consumption; do not call the sum a delivered energy stream.',
            source='https://epaper.qingdaonews.com/qdrb/html/2026-06/02/content_144591_3494474.htm'))
