# Task 3 — Canonical Operational Data Registers

## Overview

This directory contains the structured operational
planning records supporting Task 3.

The files are authoritative within the current
repository and are intended to be interpreted together
with the main response playbook.

They are not records of completed incident response
activities in a real environment.

## Register 1 — Planned Response Actions

**[Open response-actions.csv](response-actions.csv)**

### Purpose

The response-action register translates the playbook
into identifiable planned activities.

It supports traceability between response stages,
assigned roles, required approvals, evidence
preservation and defined completion conditions.

### File structure

- Data records: **20**
- Columns: **8**

| Column | Meaning / interpretation |
|---|---|
| `Action ID` | Record identifier used for traceability. |
| `Time/stage WAT` | Time or response phase associated with the record. |
| `Action` | Planned response activity or decision. |
| `Owner` | Responsible functional role or owner. |
| `Required approval` | Approval or decision authority requirement. |
| `Evidence to retain` | Record identifier used for traceability. |
| `Completion check` | Verification or completion condition. |
| `Status` | Planning or completion state as recorded. |


### How to interpret this register

Activities should be read in conjunction with the
playbook's explanation of the first 60 minutes,
first 24 hours and subsequent response stages.

A planned action does not indicate that the corresponding
technical activity has been completed.

---

## Register 2 — Evidence Preservation Register

**[Open evidence-register.csv](evidence-register.csv)**

### Purpose

The evidence register documents planned forensic
collection and preservation arrangements.

Its role is to support accountable acquisition,
integrity verification, secure storage, controlled
access and chain-of-custody tracking.

### File structure

- Data records: **6**
- Columns: **10**

| Column | Meaning / interpretation |
|---|---|
| `Item ID` | Record identifier used for traceability. |
| `Source` | Refer to the recorded values and main playbook for this field's specific meaning. |
| `Relevant evidence or purpose` | Record identifier used for traceability. |
| `Proposed collection method` | Proposed collection or verification method. |
| `Collector role` | Person or functional role assigned collection. |
| `Planned date/time WAT` | Time or response phase associated with the record. |
| `Integrity check (planned)` | Integrity verification or preservation method. |
| `Restricted secure storage` | Proposed evidence repository or storage control. |
| `Custody transfer (planned)` | Chain-of-custody information or requirement. |
| `Collection status` | Planning or completion state as recorded. |


### Evidence integrity considerations

Potential evidence must be handled using appropriate
authorisation, documentation and integrity controls.

The register should distinguish anticipated
collection procedures from evidence actually acquired.

Do not interpret a proposed hash or collection method
as a completed integrity verification.

---

## Data governance and provenance

The two populated CSV files in this folder are
the canonical structured Task 3 records.

The original header-only scaffolds are separately
retained in [deprecated-templates/](../deprecated-templates/).

Do not substitute those historical templates for
the completed response and evidence-planning datasets.

## Related documentation

- [Complete Response Playbook](../TASK-3-RESPONSE-PLAYBOOK.md)
- [Workflow Diagrams](../diagrams/)
- [Rendered Visual Gallery](../visuals/)
- [Task 3 Overview](../README.md)
