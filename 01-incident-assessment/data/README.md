# Task 1 — Evidence and Assessment Registers

## Purpose

This directory contains the structured CSV files used to
support traceability, prioritisation and consistent interpretation
of the fictional incident evidence.

These are the authoritative structured Task 1 registers in
the current repository.

## Canonical datasets

### 1. Evidence Analysis Register

**File:** [evidence-analysis-register.csv](evidence-analysis-register.csv)

Structured interpretation of the available incident evidence, including the separation of observations and uncertainty.

**Dataset structure:** 8 data rows and 12 columns.

### 2. Asset Impact Register

**File:** [asset-impact-register.csv](asset-impact-register.csv)

Records relevant systems and their potential or observed operational impact.

**Dataset structure:** 8 data rows and 10 columns.

### 3. CIA Impact Matrix

**File:** [cia-impact-matrix.csv](cia-impact-matrix.csv)

Presents confidentiality, integrity and availability considerations in a structured format.

**Dataset structure:** 24 data rows and 10 columns.

### 4. Investigation Priorities

**File:** [investigation-priorities.csv](investigation-priorities.csv)

Organises investigation questions and priorities for the proposed response.

**Dataset structure:** 7 data rows and 9 columns.

### 5. Response Priority Matrix

**File:** [response-priority-matrix.csv](response-priority-matrix.csv)

Documents prioritised response concerns and the basis for their ordering.

**Dataset structure:** 10 data rows and 11 columns.

### 6. Severity Criteria

**File:** [severity-criteria.csv](severity-criteria.csv)

Supports consistent severity assessment and reassessment.

**Dataset structure:** 4 data rows and 9 columns.

## How to use the registers

The evidence-analysis register supports traceability to
the original scenario. The impact and severity datasets
help communicate the basis for assessments, while the
investigation and response priority datasets help organise
proposed next steps.

A row records a documented assessment or planned activity,
not necessarily an action executed in a live environment.

## Data interpretation rules

1. Preserve existing evidence identifiers.
2. Do not promote hypotheses into confirmed facts.
3. Maintain the original meaning of timestamps and WAT notation.
4. Treat classifications and priorities as subject to reassessment.
5. Do not infer completed forensic acquisition from planning records.
6. Do not use superseded empty templates as authoritative datasets.

## Relationships to other folders

- [Analysis and Rationale](../analysis/)
- [Integrated Task 1 Assessment](../TASK-1-INTEGRATED-ASSESSMENT.md)
- [Deprecated Templates](../deprecated-templates/)
- [Task 1 Overview](../README.md)
