# Task 3 — Response playbook and preservation

**Status:** Draft complete — awaiting independent review. All response actions and evidence activities are planned; no live action or acquisition is claimed.

Primary outputs:

- [TASK-3-RESPONSE-PLAYBOOK.md](TASK-3-RESPONSE-PLAYBOOK.md)
- [response actions](data/response-actions.csv)
- [evidence register](data/evidence-register.csv)
- [response workflow source](diagrams/response-workflow.mmd)
- [recovery decision source](diagrams/recovery-decision.mmd)

The playbook covers the first 60 minutes, the remainder of the first 24 hours, containment, evidence preservation, investigation, eradication planning, credential protection, controlled recovery, monitoring and closure. It preserves the E01–E08 uncertainty boundaries and the approved Task 2 authority model.

The populated files under `data/` are the canonical structured outputs. The former root-level header-only scaffolds are preserved under [`deprecated-templates/`](deprecated-templates/); they contain no operational records and are retained only for provenance.

---

<!-- TASK3-DOCUMENTATION-START -->
# Task 3 — Incident Response Playbook and Evidence Preservation

## Overview

This directory contains the planned ransomware incident response
playbook for the fictional Northbridge Skills Institute scenario
in the ICDFA GRC105 assignment.

The playbook provides an organised framework for incident response,
evidence preservation, containment decisions, investigation,
eradication planning, system recovery, and closure.

All operational actions and evidence-collection activities are
proposed or simulated. This repository does not claim that
these actions were performed against a real environment.

## Main assessment document

**[Read the Complete Task 3 Response Playbook](TASK-3-RESPONSE-PLAYBOOK.md)**

The document addresses:

- Initial response during the first 60 minutes.
- Response priorities throughout the first 24 hours.
- Incident containment and evidence preservation.
- Investigation and scope determination.
- Credential security and eradication planning.
- Backup verification and recovery decisions.
- Controlled restoration and business acceptance.
- Post-incident monitoring and closure.

## Directory guide

| Directory | Description |
|---|---|
| [data/](data/) | Canonical response-action and evidence-register datasets. |
| [diagrams/](diagrams/) | Editable Mermaid diagram source files. |
| [visuals/](visuals/) | Rendered response and recovery diagrams with explanations. |
| [deprecated-templates/](deprecated-templates/) | Preserved original CSV scaffolds, not operational records. |

## Operational registers

| Register | Purpose |
|---|---|
| [Response Actions](data/response-actions.csv) | Ordered incident response activities and assigned responsibilities. |
| [Evidence Register](data/evidence-register.csv) | Planned evidence handling, custody, preservation and integrity controls. |

## Visual documentation

### Incident Response Workflow

[![Incident Response Workflow](visuals/response-workflow.png)](visuals/response-workflow.svg)

This diagram illustrates the proposed progression of incident
response activities, including analysis, containment, investigation,
recovery and closure.

[View the visual documentation](visuals/)

### Recovery Decision Workflow

[![Recovery Decision Workflow](visuals/recovery-decision.png)](visuals/recovery-decision.svg)

This diagram supports the distinction between restoring technical
services and authorising their return to operational use. Proposed
restoration depends on appropriate security, integrity and business
acceptance checks.

[View the editable diagram sources](diagrams/)

## Evidence and interpretation

The playbook uses the evidence identifiers and uncertainties
established in Task 1.

In particular:

- Suspicious activity does not automatically establish compromise.
- Unusual network traffic does not confirm data exfiltration.
- A successful backup job does not establish recoverability.
- Planned collection does not constitute acquired forensic evidence.
- Proposed recovery steps do not constitute completed restoration.

## Assessment status

Task 3 has been drafted, validated and incorporated into the
completed GRC105 submission package.

The scenarios, procedures and decisions remain educational
and do not represent a live incident response operation.
<!-- TASK3-DOCUMENTATION-END -->
