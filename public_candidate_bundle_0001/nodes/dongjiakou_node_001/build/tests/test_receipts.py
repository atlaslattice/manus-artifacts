"""Tests for the field-research receipt ledger.

The protocol is the point: a NULL is a receipt, and a FOUND-CONTRADICTS is the
most valuable outcome, because it corrects an assumption before that assumption
propagates to 120 localities.
"""

from __future__ import annotations

import pytest

from models import locality as loc
from models import receipts as rc


def test_every_receipt_uses_a_declared_outcome():
    for r in rc.receipts():
        assert r["outcome"] in rc.OUTCOMES, r["qid"]


def test_undeclared_outcome_is_rejected():
    with pytest.raises(ValueError):
        rc._r("Q-X", "test", "PROBABLY", "finding")


def test_receipt_ids_are_unique():
    ids = [r["qid"] for r in rc.receipts()]
    assert len(ids) == len(set(ids))


def test_a_null_is_an_unknown_evidence_class_not_a_failure():
    for r in rc.nulls():
        assert r["evidence_class"] == "UNKNOWN"


def test_a_found_receipt_is_reported_evidence():
    for r in rc.by_outcome("FOUND"):
        assert r["evidence_class"] == "REPORTED"


def test_outcome_counts_sum_to_the_total():
    counts = rc.outcome_counts()
    assert sum(counts.values()) == len(rc.receipts())


def test_four_contradictions_were_found():
    """Round 1: construction waste and CERT-01 scope.
    Round 2: the PPP investment figure and the circular-plan project count.
    """
    assert {r["qid"] for r in rc.contradictions()} == {
        "Q-F2", "Q-F5", "Q-B1-2", "Q-A1-2",
    }


def test_round_two_is_recorded_separately():
    s = rc.round_summary()
    assert s["rounds"] == 2
    assert s["round_1"]["answered"] == 32
    assert s["round_2"]["answered"] == 5
    assert s["round_2"]["outcomes"]["FOUND"] == 2
    assert s["round_2"]["outcomes"]["FOUND-CONTRADICTS"] == 2
    assert s["round_2"]["outcomes"]["NULL"] == 1


def test_ppp_investment_contradiction_is_retained_with_dates():
    r = next(r for r in rc.receipts() if r["qid"] == "Q-B1-2")
    assert "CNY 450M" in r["finding"]
    assert "CNY 900M" in r["finding"]
    assert "retained with dates" in r["finding"]


def test_outfall_instrument_carries_the_wrong_outfall_warning():
    """The distinction that may undermine the INV-19 evidence base."""
    r = next(r for r in rc.receipts() if r["qid"] == "Q-C4-2")
    assert "WASTEWATER" in r["finding"]
    assert "WRONG outfall" in r["effect_on_register"]


def test_cas_patent_is_recorded_with_its_number():
    r = next(r for r in rc.receipts() if r["qid"] == "Q-H4-2")
    assert "CN121446313A" in r["finding"]
    assert "高军" in r["finding"]


def test_2026_tariff_reconfirmed_null_and_escalated_to_a_request():
    r = next(r for r in rc.receipts() if r["qid"] == "Q-B3-2")
    assert r["outcome"] == "NULL"
    assert "INSTITUTIONAL REQUEST" in r["effect_on_register"]


def test_every_receipt_declares_its_round():
    for r in rc.receipts():
        assert r["round"] in (1, 2), r["qid"]


def test_construction_waste_contradiction_is_recorded():
    c = {r["qid"]: r for r in rc.contradictions()}
    assert "LACKS construction waste" in c["Q-F2"]["finding"]


def test_cert_veto_scope_contradiction_is_recorded():
    c = {r["qid"]: r for r in rc.contradictions()}
    assert "no classification-society" in c["Q-F5"]["finding"]


def test_the_2026_tariff_is_a_null():
    """Still the highest-value missing receipt."""
    ids = {r["qid"] for r in rc.nulls()}
    assert "Q-B3" in ids
    b3 = next(r for r in rc.receipts() if r["qid"] == "Q-B3")
    assert "0.555" in b3["finding"]
    assert "NO 2026" in b3["finding"]


def test_primary_ouc_data_is_a_null():
    """ECO-01 stays unresolved on secondary summaries alone."""
    assert "Q-C3" in {r["qid"] for r in rc.nulls()}


def test_every_receipt_has_a_search_or_source():
    for r in rc.receipts():
        assert r["search_terms"] or r["source"], r["qid"]


def test_round_summary_reports_the_discipline_note():
    s = rc.round_summary()
    assert "promoted on the strength of a model agreeing with another model" in s["discipline_note"]
    assert "plan is not an allocation" in s["discipline_note"]
    assert "operator claim is not an independent measurement" in s["discipline_note"]
    assert "expectation of commercial operation is not operation" in s["discipline_note"]


def test_register_folds_in_the_field_research():
    r = loc.run()
    assert r["field_research"]["rounds"] == 2
    assert r["field_research"]["questions_answered"] == len(rc.receipts())


def test_locality_contradictions_proxy_works():
    assert {c["qid"] for c in loc.contradictions()} == {
        "Q-F2", "Q-F5", "Q-B1-2", "Q-A1-2",
    }


# ---------------------------------------------------------------------------
# Price anchors
# ---------------------------------------------------------------------------
def test_take_or_pay_clause_is_binding():
    """Actual 2025 offtake is BELOW the contractual minimum."""
    pa = loc.price_anchors()
    assert pa["take_or_pay_is_binding"] is True
    assert pa["actual_2025_m3_per_day"] < pa["guaranteed_minimum_m3_per_day"]
    assert pa["take_or_pay_shortfall_m3_per_day"] == pytest.approx(20_876.7, abs=0.5)


def test_distribution_margin_is_negative():
    """A policy-driven loss subsidised by the district government."""
    pa = loc.price_anchors()
    assert pa["water_resale_cny_per_m3"] < pa["water_treatment_fee_cny_per_m3"]
    assert pa["resale_margin_cny_per_m3"] < 0


def test_2026_electricity_remains_unknown():
    """The waiver expired at end-2025, so the 2018-2020 figure cannot be carried forward."""
    assert loc.price_anchors()["electricity_2026"] == "UNKNOWN"


def test_price_anchor_findings_flag_the_subsidy_dependency():
    joined = " ".join(loc.price_anchors()["findings"])
    assert "FINANCIAL-RISK" in joined
    assert "genuinely UNKNOWN rather than merely unpublished" in joined


# ---------------------------------------------------------------------------
# The rule the ledger must never break
# ---------------------------------------------------------------------------
def test_no_receipt_created_a_credit():
    """Field research changes evidence, never the credit rule."""
    assert loc.run()["counts"]["streams_realizing_credit"] == 0


def test_node_pass_still_not_established():
    assert loc.run()["node_pass"]["verdict"] == "NODE_PASS_NOT_ESTABLISHED"
    assert len(loc.run()["node_pass"]["unresolved"]) == 5


def test_operational_hosts_are_confirmed_but_uncredited():
    """Zhongfa and Special Steel are real; the reuse loop is already claimed by one party."""
    r = loc.run()
    g2 = next(x for x in rc.receipts() if x["qid"] == "Q-G2")
    assert "20,000 m3/day" in g2["finding"]
    assert r["counts"]["streams_realizing_credit"] == 0
