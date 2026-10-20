# Task 4 — Stakeholder Communication and Escalation

## Overview

This directory contains the stakeholder communication and
escalation component of the ICDFA GRC105 incident response
assignment.

The work is based on the fictional ransomware incident at
**Northbridge Skills Institute**.

Its purpose is to establish how incident information should
be communicated to affected stakeholders while preserving
accuracy, confidentiality, accountability and consistency.

**Assessment status:** The Task 4 materials have been completed
and included in the GRC105 assignment package.

**Operational status:** All communications are proposed or
simulated. No message is represented as actually sent.

## 1. Primary deliverables

| Document | Description |
|---|---|
| [Communication Plan](TASK-4-COMMUNICATION-PLAN.md) | Main narrative, stakeholder communications, messages and escalation arrangements |
| [Stakeholder Matrix](stakeholder-matrix.csv) | Structured communication responsibilities, triggers and channels |
| [Completion QA](TASK-4-COMPLETION-QA.md) | Recorded quality and assessment checks |

The communication plan is the primary narrative document.
The stakeholder matrix provides structured supporting detail.

## 2. Scenario communication challenges

The fictional incident affects learning-related services
at Northbridge Skills Institute and creates uncertainty
about the availability of learning materials and examination
arrangements.

An online examination for approximately 100 learners
is scheduled for 11:00 WAT on Day 0.

The initial assessment is High — provisional, at
08:45 WAT on Day 0.

Communications must balance operational urgency with
the need to avoid unsupported conclusions.

Important constraints include:

- Access to response contacts through FS01 is disrupted.
- The trustworthiness of corporate email is not established.
- Service recovery and examination arrangements require
  authorised decisions.
- Suspicious transfer activity does not independently
  establish confirmed personal-data theft.
- Stakeholders require timely, accurate and consistent updates.

## 3. Stakeholder communication framework

The assessment documents communication arrangements for
eight stakeholder groups.

The communication framework considers:

1. Who needs the information.
2. What event triggers communication.
3. Which role prepares the communication.
4. Who must authorise its release.
5. Which channel should be used.
6. How frequently updates should be provided.
7. What alternative channel is appropriate when a
   primary service is unavailable or untrusted.
8. How relevant communications and approvals are recorded.

The actual assignments and details are documented in
the [Stakeholder Matrix](stakeholder-matrix.csv).

## 4. Stakeholder matrix

### Purpose

The matrix supports consistent communication planning
throughout incident response and service recovery.

It helps distinguish information-sharing activities from
decision-making and message approval.

**[Open the complete stakeholder matrix](stakeholder-matrix.csv)**

### Dataset summary

- Stakeholder records: **8**
- Columns: **7**

### Fields in the actual CSV

| Column | Interpretation guidance |
|---|---|
| `Stakeholder` | Consult the register values and communication plan for the field's meaning. |
| `Trigger` | Consult the register values and communication plan for the field's meaning. |
| `Message owner` | Consult the register values and communication plan for the field's meaning. |
| `Channel` | Consult the register values and communication plan for the field's meaning. |
| `Alternative channel` | Consult the register values and communication plan for the field's meaning. |
| `Approver` | Consult the register values and communication plan for the field's meaning. |
| `Update frequency` | Consult the register values and communication plan for the field's meaning. |

The CSV is the authoritative structured communications
dataset in this folder.

The README is intended to explain its purpose, not replace
the complete records.

## 5. Executive briefing

The communication plan includes an executive briefing
for incident leadership and relevant management.

### Purpose

The briefing is designed to support timely decisions
while distinguishing reported incident impact from
unverified findings.

Its key communication objectives include:

- Presenting the current incident position.
- Explaining important operational consequences.
- Identifying material uncertainties.
- Highlighting decisions requiring management attention.
- Supporting an appropriate subsequent update.

### Word-count requirement

**Required:** 150–200 words.

**Previously validated:** 196 words.

The authoritative briefing text remains in the
[Communication Plan](TASK-4-COMMUNICATION-PLAN.md).

## 6. Learner notification

The plan also includes a proposed learner-facing notice.

### Purpose

The notice is intended to communicate practical information
about affected learning or examination services without
creating unnecessary alarm or announcing decisions that
have not yet been approved.

It should distinguish confirmed service conditions
from pending examination arrangements.

### Word-count requirement

**Required:** 100–150 words.

**Previously validated:** 147 words.

The authoritative learner-notice text remains in the
[Communication Plan](TASK-4-COMMUNICATION-PLAN.md).

## 7. Message ownership and approval

Incident communications require coordination between
incident leadership, stakeholder communications, technical
responders and relevant management or advisers.

The roles involved in drafting, reviewing, approving
and delivering a communication may differ.

A person authorised to communicate information is not
automatically authorised to approve technical restoration
or accept institutional risk.

For the proposed governance arrangements, see
[Task 2 — IR Plan and Governance](../02-ir-plan-and-governance/).

## 8. Alternative communication channels

The Northbridge scenario highlights the importance of
communications arrangements that do not depend exclusively
on affected systems.

Where normal email or internal file services are
unavailable or untrusted, authorised personnel should
use an appropriate verified alternative channel.

The selection of an alternative must account for:

- Recipient identity verification.
- Message confidentiality.
- Authorised sender identity.
- Availability of current contact information.
- Recording of decisions and notifications.
- Avoidance of sensitive information through
  unverified or inappropriate channels.

The proposed arrangements do not establish that an
independent contact system was already implemented.

## 9. Legal and privacy escalation

The scenario raises potential confidentiality concerns,
but possible data exposure is not equivalent to a
confirmed personal-data breach.

Legal and privacy assessment should consider the
available evidence, applicable obligations and
organisational decision authority.

Operational incident updates and formal regulatory
notifications are different communication activities.

This README does not assert that a reportable breach
occurred or that a statutory notification deadline
has been triggered.

## 10. Relationship to the incident response lifecycle

| Related task | Connection |
|---|---|
| [Task 1 — Incident Assessment](../01-incident-assessment/) | Supplies evidence, severity and uncertainty boundaries |
| [Task 2 — Governance](../02-ir-plan-and-governance/) | Establishes roles, approvals and escalation authority |
| [Task 3 — Response Playbook](../03-response-playbook/) | Provides operational status and response decisions |
| [Task 5 — Tabletop Simulation](../05-tabletop-simulation/) | Exercises communication challenges in a simulated setting |

Communications should reflect the verified information
available at the time, rather than anticipating outcomes
of investigation or recovery.

## 11. Quality assurance and evidence limitations

The completed assessment documentation reports:

- Eight stakeholder groups.
- An executive briefing within the required word limit.
- A learner notice within the required word limit.
- Communication triggers and responsibilities.
- Alternative-channel considerations.
- Legal and privacy escalation boundaries.

See the [Task 4 Completion QA](TASK-4-COMPLETION-QA.md)
for the recorded assessment checks.

These are coursework validation results, not proof that
notifications were delivered during a live incident.

## 12. Directory navigation

This folder intentionally contains only its primary
communication documents and structured matrix.

No additional subdirectories or decorative figures
are necessary.

[Return to repository overview](../README.md)
