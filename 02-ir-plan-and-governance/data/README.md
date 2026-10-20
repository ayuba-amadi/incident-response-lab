# Task 2 — Governance and Accountability Registers

## Purpose

This directory contains structured CSV records supporting
governance traceability, role coverage and accountability
in the Task 2 incident response framework.

These registers are supporting documentation for the
academic governance proposal, not evidence that a
real incident response organisation has been activated.

## Register catalogue

### 1. Authority Consistency Matrix

**File:** [authority-consistency-matrix.csv](authority-consistency-matrix.csv)

Records governance decision activities and normal primary authorities.

**Structure:** 14 data records, 9 columns.

### 2. Authority–RACI Crosswalk

**File:** [authority-raci-crosswalk.csv](authority-raci-crosswalk.csv)

Relates governance authority decisions to the operational RACI activities.

**Structure:** 16 data records, 9 columns.

### 3. CSIRT Role Register

**File:** [csirt-role-register.csv](csirt-role-register.csv)

Catalogues functional response roles and their organisational purposes.

**Structure:** 11 data records, 12 columns.

### 4. Duty Conflict and Coverage Register

**File:** [duty-conflict-and-coverage-register.csv](duty-conflict-and-coverage-register.csv)

Identifies role overlaps, capacity constraints and coverage considerations.

**Structure:** 7 data records, 10 columns.

### 5. Governance Requirements Matrix

**File:** [governance-requirements-matrix.csv](governance-requirements-matrix.csv)

Maps governance requirements to the supporting Task 2 material.

**Structure:** 19 data records, 8 columns.

### 6. Incident Decision Log Template

**File:** [incident-decision-log-template.csv](incident-decision-log-template.csv)

Provides a proposed structure for recording decision authority and incident-related approvals; it is not evidence of a completed decision.

**Structure:** 0 data records, 25 columns.

## Operational RACI Matrix

The authoritative Task 2 operational RACI is stored at
[../raci.csv](../raci.csv), at the task-directory root.

It contains 22 data rows.

It should be interpreted using the
[RACI Methodology](../csirt/raci-methodology-and-accountability.md).

## Authority versus activity accountability

The authority consistency matrix and operational RACI
serve different but related purposes.

The authority matrix represents decision rights.
The RACI represents participation and accountability
in defined activities.

The authority–RACI crosswalk provides traceability
between the two structures.

Do not treat the same governance decision as having
multiple independent primary authorities simply
because multiple roles assist with implementation.

## Decision log status

The incident decision log is a template.
Its existence does not indicate that an actual incident
decision was recorded or formally approved.

## Interpretation and maintenance

- Preserve identifiers and role definitions.
- Keep the approved academic model internally consistent.
- Do not change RACI accountability casually.
- Maintain distinctions between routine and emergency authority.
- Treat coverage and staffing constraints as planning concerns.
- Avoid substituting hypothetical staff assignments for
  confirmed organisational appointments.

## Related resources

- [CSIRT Documentation](../csirt/)
- [Incident Response Policy](../policy/)
- [Governance Plans](../plans/)
- [Task 2 Overview](../README.md)
