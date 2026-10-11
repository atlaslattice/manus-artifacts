#!/usr/bin/env python3
"""DJK-001 v0.5 atomic allocation research prototype (SQLite).

No actual contracts verified, no industrial site connection, no data rights granted.
Proof checking delegated to trusted external verification; mocked in tests.
"""
from __future__ import annotations
import sqlite3
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class TransferRequest:
    allocation_id: str
    lot_id: str
    destination_scope: str
    destination_event: str
    amount_kg: int
    contract_evidence_id: str
    origin_scale_evidence_id: str
    destination_scale_evidence_id: str
    transport_permission_id: str

    def signature(self) -> tuple:
        return (self.lot_id, self.destination_scope, self.destination_event,
                self.amount_kg, self.contract_evidence_id,
                self.origin_scale_evidence_id,
                self.destination_scale_evidence_id, self.transport_permission_id)


def connect(path: str) -> sqlite3.Connection:
    db = sqlite3.connect(path, isolation_level=None, timeout=10)
    db.execute('PRAGMA foreign_keys=ON')
    db.execute('PRAGMA busy_timeout=10000')
    db.executescript("""
    CREATE TABLE IF NOT EXISTS lot (
        lot_id TEXT PRIMARY KEY,
        source_scope TEXT NOT NULL,
        source_event TEXT NOT NULL UNIQUE,
        material_type TEXT NOT NULL,
        evidence_state TEXT NOT NULL CHECK(evidence_state = 'MEASURED'),
        wet_mass_kg INTEGER NOT NULL CHECK(wet_mass_kg >= 0),
        remaining_kg INTEGER NOT NULL CHECK(remaining_kg >= 0 AND remaining_kg <= wet_mass_kg)
    );
    CREATE TABLE IF NOT EXISTS allocation (
        allocation_id TEXT PRIMARY KEY,
        lot_id TEXT NOT NULL REFERENCES lot(lot_id),
        destination_scope TEXT NOT NULL,
        destination_event TEXT NOT NULL UNIQUE,
        amount_kg INTEGER NOT NULL CHECK(amount_kg > 0),
        contract_evidence_id TEXT NOT NULL,
        origin_scale_evidence_id TEXT NOT NULL,
        destination_scale_evidence_id TEXT NOT NULL,
        transport_permission_id TEXT NOT NULL
    );
    """)
    return db


def add_measured_lot(db: sqlite3.Connection, *, lot_id: str,
                     source_scope: str, source_event: str,
                     material_type: str, wet_mass_kg: int,
                     verified_meter: bool) -> None:
    """Boolean is the EXTERNAL verifier result, not proof validation itself."""
    if not verified_meter:
        raise PermissionError('Measurement evidence not independently verified')
    if not all((lot_id, source_scope, source_event, material_type)):
        raise ValueError('Missing lot identity or scope')
    if isinstance(wet_mass_kg, bool) or not isinstance(wet_mass_kg, int) or wet_mass_kg < 0:
        raise ValueError('Mass must be nonnegative integer kg')
    db.execute('INSERT INTO lot VALUES (?,?,?,?,?,?,?)',
               (lot_id, source_scope, source_event, material_type,
                'MEASURED', wet_mass_kg, wet_mass_kg))


def allocate(db: sqlite3.Connection, request: TransferRequest,
             proof_verifier: Callable[[TransferRequest], bool]) -> str:
    """Idempotent atomic booking. No real-world authorization is conferred."""
    fields = (request.allocation_id, request.lot_id, request.destination_scope,
              request.destination_event, request.contract_evidence_id,
              request.origin_scale_evidence_id,
              request.destination_scale_evidence_id, request.transport_permission_id)
    if any(not isinstance(v, str) or not v.strip() for v in fields):
        raise ValueError('Missing transfer fields')
    if request.destination_scope != 'DONGJIAKOU_ECONOMIC_AREA':
        raise ValueError('DJK-specific booking cannot allocate to other scope')
    if isinstance(request.amount_kg, bool) or not isinstance(request.amount_kg, int) or request.amount_kg <= 0:
        raise ValueError('Mass must be positive integer kg')
    if not proof_verifier(request):
        raise PermissionError('Independent evidence verification failed')

    db.execute('BEGIN IMMEDIATE')
    try:
        existing = db.execute("""
            SELECT lot_id,destination_scope,destination_event,amount_kg,
                   contract_evidence_id,origin_scale_evidence_id,
                   destination_scale_evidence_id,transport_permission_id
            FROM allocation WHERE allocation_id=?""", (request.allocation_id,)).fetchone()
        if existing is not None:
            if tuple(existing) != request.signature():
                raise ValueError('Idempotency key reused for different allocation')
            db.execute('COMMIT')
            return 'IDEMPOTENT_EXISTING'
        changed = db.execute("""
            UPDATE lot SET remaining_kg = remaining_kg - ?
            WHERE lot_id=? AND evidence_state='MEASURED' AND remaining_kg >= ?""",
            (request.amount_kg, request.lot_id, request.amount_kg)).rowcount
        if changed != 1:
            raise ValueError('Missing lot or insufficient measured, unallocated mass')
        db.execute('INSERT INTO allocation VALUES (?,?,?,?,?,?,?,?,?)',
                   (request.allocation_id, request.lot_id,
                    request.destination_scope, request.destination_event,
                    request.amount_kg, request.contract_evidence_id,
                    request.origin_scale_evidence_id,
                    request.destination_scale_evidence_id,
                    request.transport_permission_id))
        db.execute('COMMIT')
        return 'BOOKED_RESEARCH_ONLY'
    except Exception:
        db.execute('ROLLBACK')
        raise


def remaining(db: sqlite3.Connection, lot_id: str) -> int:
    row = db.execute('SELECT remaining_kg FROM lot WHERE lot_id=?', (lot_id,)).fetchone()
    if row is None:
        raise KeyError(lot_id)
    return row[0]


def balance(db: sqlite3.Connection, lot_id: str) -> tuple[int,int,int]:
    """Return total, booked, remainder, always in integer kilograms."""
    row = db.execute("""
        SELECT l.wet_mass_kg, COALESCE(SUM(a.amount_kg),0), l.remaining_kg
        FROM lot l LEFT JOIN allocation a ON a.lot_id=l.lot_id
        WHERE l.lot_id=? GROUP BY l.lot_id""", (lot_id,)).fetchone()
    if row is None:
        raise KeyError(lot_id)
    if row[0] != row[1]+row[2]:
        raise AssertionError('Nonconserving allocated mass ledger')
    return tuple(row)
