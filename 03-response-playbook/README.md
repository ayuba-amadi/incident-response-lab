# Task 3 — Incident Response Playbook and Evidence Preservation

## Overview

This directory contains the operational incident response
playbook developed for the fictional **Northbridge Skills
Institute** ransomware scenario in the ICDFA GRC105 assignment.

The playbook translates the initial incident assessment and
governance arrangements into a structured plan for:

- Initial incident response and coordination.
- Containment and evidence preservation.
- Investigation and scope determination.
- Credential security and eradication planning.
- Backup assessment and controlled service recovery.
- Monitoring, closure and post-incident improvement.

**Assessment status:** Task 3 was completed, reviewed and
incorporated into the final GRC105 coursework.

**Operational status:** The documented activities are planned
or simulated. They do not represent actual actions performed
against a live environment.

## Primary assessment deliverable

### Complete Response Playbook

**[Read TASK-3-RESPONSE-PLAYBOOK.md](TASK-3-RESPONSE-PLAYBOOK.md)**

This is the principal narrative document for Task 3.
It should be read alongside the canonical action and
evidence registers.

## Scenario and operational context

Northbridge Skills Institute is a fictional educational
institution with approximately 1,800 learners and 90 staff.

Its key systems include:

| Asset | Scenario relevance |
|---|---|
| FIN-PC07 | Finance workstation associated with suspicious activity |
| FS01 | Shared file server affected by the incident |
| LMS01 | Learning portal with dependencies on FS01 |
| BAK01 | Network backup infrastructure requiring validation |
| Microsoft 365 | Identity and communication environment |
| svc_backup | Privileged service account requiring investigation |

The initial incident assessment was made at **08:45 WAT,
Day 0**, with an online examination scheduled for
**11:00 WAT**.

The response must balance examination continuity with
security, evidence preservation and recovery assurance.

## Response lifecycle

### Phase 1 — Immediate response

The initial period focuses on incident coordination,
situation assessment, evidence protection, containment
decisions and appropriate escalation.

### Phase 2 — First 24 hours

The subsequent response develops the incident scope,
reviews affected systems and identities, and records
forensic collection requirements and protective decisions.

### Phase 3 — Investigation and containment

The playbook considers further evidence preservation,
lateral-movement concerns, privileged access,
affected endpoints and server dependencies.

### Phase 4 — Eradication and recovery preparation

Proposed recovery preparations address the suspected
entry point, persistence concerns, credential hygiene,
backup selection and verification.

### Phase 5 — Controlled restoration

Restoration planning distinguishes technical
functionality from security validation, data integrity,
business acceptance and any necessary management
risk decision.

### Phase 6 — Monitoring and closure

The response concludes with defined monitoring,
documentation, review and closure requirements.

## Two critical response trade-offs

### Containment versus evidence preservation

Rapid isolation can limit further harm but may
affect access to volatile evidence or alter the
state of affected systems.

The playbook documents the need for proportionate,
authorised decisions and defensible evidence handling.

### Examination continuity versus backup safety

The examination creates substantial operational pressure,
but successful backup-job completion is not sufficient
proof that a recovery source is safe or restorable.

The playbook therefore requires verification before
authorising a return to service.

## Repository navigation

| Directory | Purpose |
|---|---|
| [data/](data/) | Canonical action and evidence registers |
| [diagrams/](diagrams/) | Editable Mermaid workflow sources |
| [visuals/](visuals/) | Rendered figures with detailed interpretation |
| [deprecated-templates/](deprecated-templates/) | Historical empty CSV scaffolds |

## Canonical operational registers

### Response Actions Register

**[Open response-actions.csv](data/response-actions.csv)**

Contains 20 planned response-action records.

The register supports ordered execution planning,
responsibility assignment, approval requirements,
evidence preservation and completion checks.

### Evidence Register

**[Open evidence-register.csv](data/evidence-register.csv)**

Contains 6 evidence-planning records.

The register supports collection planning, chain of custody,
integrity verification, storage arrangements and access
accountability.

**Important:** Planned or not-collected entries do not
constitute forensic evidence actually acquired.

## Visual documentation

The following diagrams provide visual representations
of the response and recovery logic.


### Figure 1 — Incident Response Workflow

[![Figure 1 — Incident Response Workflow](visuals/response-workflow.png)](visuals/response-workflow.svg)

**Description:** Illustrates the planned sequence of incident response activities, from assessment and containment through investigation, eradication planning, recovery and closure.

**Interpretation:** The workflow is a proposed response model. It does not demonstrate that systems were isolated, evidence was collected, or recovery was completed.

**Available formats:**
[PNG](visuals/response-workflow.png) |
[SVG](visuals/response-workflow.svg) |
[Editable Mermaid](diagrams/response-workflow.mmd)



### Figure 2 — Recovery Decision Workflow

[![Figure 2 — Recovery Decision Workflow](visuals/recovery-decision.png)](visuals/recovery-decision.svg)

**Description:** Illustrates the decision-making considerations associated with validating backups, restoring technical services and authorising operational use.

**Interpretation:** Technical accessibility does not independently establish security clearance, data integrity or business acceptance.

**Available formats:**
[PNG](visuals/recovery-decision.png) |
[SVG](visuals/recovery-decision.svg) |
[Editable Mermaid](diagrams/recovery-decision.mmd)


For additional interpretation, see the
[complete visual gallery](visuals/).

## Evidence limitations

The Task 3 playbook preserves the evidence boundaries
established in Task 1.

In particular:

- Suspicious activity does not automatically establish
  confirmed malicious execution or identity compromise.
- Unusual network traffic does not prove data exfiltration.
- A successful backup job does not verify recoverability.
- Planned evidence collection is not a completed acquisition.
- A recovery plan is not a completed restoration.
- Technical restoration does not independently authorise
  a service's return to business use.

These distinctions are essential to a defensible
incident response assessment.

## Relationship to other tasks

- [Task 1 — Incident Assessment](../01-incident-assessment/)
  provides the underlying observations and initial severity.
- [Task 2 — Governance and CSIRT](../02-ir-plan-and-governance/)
  establishes the proposed authorities and responsibilities.
- [Task 4 — Communications](../04-communications/)
  provides stakeholder notification arrangements.
- [Task 5 — Tabletop Simulation](../05-tabletop-simulation/)
  explores response decisions in a fictional exercise.

## Academic interpretation

This directory contains an educational incident response
plan developed from supplied scenario information.

It is not a record of a real ransomware investigation,
a formal organisational incident declaration or an
operational recovery report.

[Return to repository overview](../README.md)
