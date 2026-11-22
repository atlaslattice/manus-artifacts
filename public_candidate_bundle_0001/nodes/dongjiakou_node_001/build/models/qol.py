"""First-class QOL outcome vector. No composite score, controls or realized credit."""
import json
from datetime import date
from pathlib import Path
from resource_gap.simulate import validate

ROOT = Path(__file__).resolve().parents[1] / 'qol'


def registry():
    return json.loads((ROOT / 'indicator_registry.json').read_text())


def default_case():
    return json.loads((ROOT / 'examples/dongjiakou_unknown.json').read_text())


def evaluate(case=None):
    case = default_case() if case is None else case
    validate(case, json.loads((ROOT / 'observation.schema.json').read_text()))
    definitions = {m['id']: m for m in registry()['indicators']}
    seen = set()
    outputs = []
    before = date.fromisoformat(case['baseline_period_end'])
    after = date.fromisoformat(case['followup_period_end'])
    if after <= before:
        raise ValueError('Followup must be later than baseline')
    if len(set(case['required_strata'])) != len(case['required_strata']):
        raise ValueError('Duplicate required stratum')
    gates = case['gates']
    for gate in gates.values():
        if gate['status'] == 'PASS' and not gate['source']:
            raise ValueError('PASS requires a source; assertions are not authenticated')
    for row in case['observations']:
        key = (row['indicator_id'], row['stratum'])
        if key in seen:
            raise ValueError('Duplicate indicator/cohort; allocate and aggregate explicitly')
        seen.add(key)
        if row['indicator_id'] not in definitions:
            raise ValueError('Unregistered QOL indicator')
        definition = definitions[row['indicator_id']]
        if row['unit'] != definition['unit']:
            raise ValueError('QOL unit mismatch')
        intervals = []
        for name in ('baseline', 'followup'):
            q = row[name]
            lo, hi = q['low'], q['high']
            if (lo is None) != (hi is None):
                raise ValueError('Both interval endpoints must be unknown or numeric')
            if (q['evidence_class'] == 'UNKNOWN') != (lo is None):
                raise ValueError('UNKNOWN is null, not zero')
            if lo is not None:
                if lo > hi:
                    raise ValueError('Inverted QOL interval')
                if lo < definition['minimum']:
                    raise ValueError('QOL value below domain')
                if definition.get('maximum') is not None and hi > definition['maximum']:
                    raise ValueError('QOL value above domain')
                if not q['source']:
                    raise ValueError('Known QOL inputs require source')
                if q['evidence_class'] == 'MEASURED_LOCAL' and not q['method']:
                    raise ValueError('Local measurement requires method/boundary documentation')
                if q['evidence_class'] == 'MEASURED_LOCAL':
                    if q['boundary_id'] != case['boundary_id'] or q['period_end'] != case[name + '_period_end']:
                        raise ValueError('Measurement boundary/period does not match declared comparison')
                    if not q['protocol_id']:
                        raise ValueError('Local measurement requires protocol identity')
            intervals.append(None if lo is None else (lo, hi))
        base, follow = intervals
        delta = None
        state = 'UNKNOWN'
        if base is not None and follow is not None:
            delta = (follow[0] - base[1], follow[1] - base[0])
            local = all(row[n]['evidence_class'] == 'MEASURED_LOCAL' for n in ('baseline','followup'))
            if not local:
                state = 'REFERENCE_OR_SCENARIO_ONLY'
            elif (not case['comparison']['source'] or case['comparison']['design'] != 'CONTROLLED_ALIGNED'
                  or row['baseline']['protocol_id'] != row['followup']['protocol_id']):
                state = 'CHANGE_OBSERVED_ATTRIBUTION_NOT_ESTABLISHED'
            else:
                signed = delta if definition['direction'] == 'HIGHER_BETTER' else (-delta[1], -delta[0])
                state = ('IMPROVEMENT_SUPPORTED_BY_SUPPLIED_INPUTS' if signed[0] > 0
                         else 'DECLINE_SUPPORTED_BY_SUPPLIED_INPUTS' if signed[1] < 0
                         else 'NO_CLEAR_CHANGE')
        privacy = gates['privacy_and_consent']['status']
        suppressed = privacy != 'PASS' or row['sample_n'] is None or row['sample_n'] < case['minimum_public_cohort_n']
        # Public output omits personal/small-cohort values even if submitted.
        if suppressed:
            delta = None
            state = 'SUPPRESSED_PRIVACY_OR_SAMPLE_GATE'
        outputs.append(dict(indicator_id=row['indicator_id'], stratum=row['stratum'],
            domain=definition['domain'], claim_dimension=definition['claim_dimension'],
            direction=definition['direction'], unit=row['unit'],
            change_interval=None if delta is None else dict(low=delta[0],high=delta[1]),
            state=state, realized_credit=0))
    required = {(m, s) for m in definitions for s in case['required_strata']}
    missing = sorted(required - seen)
    for metric, stratum in missing:
        d = definitions[metric]
        outputs.append(dict(indicator_id=metric,stratum=stratum,domain=d['domain'],
            claim_dimension=d['claim_dimension'],direction=d['direction'],unit=d['unit'],
            change_interval=None,state='UNKNOWN_MISSING_BASELINE_AND_FOLLOWUP',realized_credit=0))
    failure = any(g['status'] == 'FAIL' for g in gates.values())
    decline = any(o['state']=='DECLINE_SUPPORTED_BY_SUPPLIED_INPUTS' for o in outputs)
    unresolved = any(g['status'] != 'PASS' for g in gates.values())
    adequate = not missing and all(o['state'] in ('IMPROVEMENT_SUPPORTED_BY_SUPPLIED_INPUTS','NO_CLEAR_CHANGE') for o in outputs)
    decision = ('BLOCKED_BY_NON_COMPENSABLE_GATE' if failure
                else 'HOLD_DISTRIBUTIONAL_DECLINE' if decline
                else 'HOLD_MISSING_BASELINE_OR_RECEIPTS' if unresolved or not adequate
                else 'ELIGIBLE_FOR_INDEPENDENT_REVIEW_ONLY')
    return dict(schema_version='0.1',node_id=case['node_id'],qol_subnode='QOL01',
        classification='RESEARCH_CANDIDATE_NON_CANON', first_class_objective=True,
        composite_score=None, objective_vector=outputs, gates=gates,
        missing_indicator_strata=[dict(indicator_id=m,stratum=s) for m,s in missing],
        decision=decision, realized_credit=0, locality_clearance='NOT_ESTABLISHED',
        limitations=['Supplied measurement and PASS assertions are not authenticated by this engine.',
            'Change intervals are endpoint envelopes, not confidence intervals or causal effect estimates.',
            'CONTROLLED_ALIGNED is a supplied design assertion, not an automatic statistical analysis.',
            'No aesthetic, carbon, production or average gain compensates for a failed human/ecological gate.',
            'Privacy thresholds are project safeguards, not claimed statutory minima.',
            'Measured exposure, service availability and experienced QOL are separate outcomes.'])
