#!/usr/bin/env python3
"""Research-only v0.5 tests: no actual external authorization verified."""
import os
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scope_ledger_v05 import connect, add_measured_lot, allocate, remaining, balance, TransferRequest


class AtomicLedgerResearchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = connect(os.path.join(self.tmp.name, 'ledger.sqlite'))
        add_measured_lot(
            self.db, lot_id='QD-lot-1', source_scope='QINGDAO_CITY',
            source_event='QD-source-1', material_type='organics',
            wet_mass_kg=1000, verified_meter=True,
        )
        self.req = TransferRequest(
            'A1', 'QD-lot-1', 'DONGJIAKOU_ECONOMIC_AREA', 'DJK-rec-1', 600,
            'C1', 'SC1', 'SC2', 'AUTH1',
        )

    def tearDown(self):
        self.db.close()
        self.tmp.cleanup()

    def test_mass_book_reconcile(self):
        self.assertEqual(allocate(self.db, self.req, lambda x: True), 'BOOKED_RESEARCH_ONLY')
        self.assertEqual(balance(self.db, 'QD-lot-1'), (1000, 600, 400))

    def test_duplicate_same_request_idempotent(self):
        allocate(self.db, self.req, lambda x: True)
        self.assertEqual(allocate(self.db, self.req, lambda x: True), 'IDEMPOTENT_EXISTING')
        self.assertEqual(remaining(self.db, 'QD-lot-1'), 400)

    def test_duplicate_key_different_amount_rejected(self):
        allocate(self.db, self.req, lambda x: True)
        with self.assertRaises(ValueError):
            allocate(self.db, replace(self.req, amount_kg=400), lambda x: True)

    def test_overallocation_rolls_back(self):
        allocate(self.db, self.req, lambda x: True)
        second = replace(self.req, allocation_id='A2', destination_event='DJK-rec-2', amount_kg=401)
        with self.assertRaises(ValueError):
            allocate(self.db, second, lambda x: True)
        self.assertEqual(balance(self.db, 'QD-lot-1'), (1000, 600, 400))

    def test_distinct_id_same_destination_receipt_rolls_back(self):
        allocate(self.db, self.req, lambda x: True)
        second = replace(self.req, allocation_id='A2', amount_kg=100)
        with self.assertRaises(Exception):
            allocate(self.db, second, lambda x: True)
        self.assertEqual(remaining(self.db, 'QD-lot-1'), 400)

    def test_verifier_fail_closed(self):
        with self.assertRaises(PermissionError):
            allocate(self.db, self.req, lambda x: False)
        self.assertEqual(remaining(self.db, 'QD-lot-1'), 1000)

    def test_missing_authorization_id(self):
        with self.assertRaises(ValueError):
            allocate(self.db, replace(self.req, transport_permission_id=''), lambda x: True)

    def test_wrong_scope(self):
        with self.assertRaises(ValueError):
            allocate(self.db, replace(self.req, destination_scope='SHANDONG_PROVINCE'), lambda x: True)

    def test_meter_not_verified(self):
        with self.assertRaises(PermissionError):
            add_measured_lot(
                self.db, lot_id='X', source_scope='DONGJIAKOU_ECONOMIC_AREA',
                source_event='x', material_type='biomass',
                wet_mass_kg=100, verified_meter=False,
            )

    def test_noninteger_or_negative_mass(self):
        for amount in (-1, 0, 1.5, True):
            with self.assertRaises(ValueError):
                allocate(self.db, replace(self.req, amount_kg=amount), lambda x: True)

    def test_unique_source_event(self):
        with self.assertRaises(Exception):
            add_measured_lot(
                self.db, lot_id='X', source_scope='QINGDAO_CITY',
                source_event='QD-source-1', material_type='organics',
                wet_mass_kg=100, verified_meter=True,
            )


if __name__ == '__main__':
    unittest.main()
