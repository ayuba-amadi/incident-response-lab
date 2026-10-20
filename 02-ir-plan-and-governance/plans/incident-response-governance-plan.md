# Northbridge Skills Institute Incident Response Governance Plan

**Document identifier:** NSI-IR-PLAN-001
**Version:** 0.1
**Status:** Stage 1 draft — awaiting independent review and organisational approval
**Planning point:** 08:45 WAT on Day 0 for the Task 1 scenario
**Owner:** Incident Response Lead — proposed role

This plan translates the draft policy into governance procedures. It does not record executed response actions, completed investigation results, or a full Task 3 technical playbook.

## 1. Operational purpose

The plan provides a controlled path from detection and reporting through declaration, activation, analysis, containment decisions, continuity coordination, recovery governance, and improvement. It is designed for a small institute in which three IT staff and one security analyst may need to coordinate security, service delivery, evidence preservation, and examination continuity at the same time.

The Week 20 teaching stages are used as an organising aid:

1. Preparation — policy, contacts, tools, training, and support arrangements.
2. Detection and analysis — report, validate, classify, scope, and document.
3. Containment, eradication, and recovery — approve protective actions, validate recovery, and return services safely.
4. Post-incident activity — close records, review decisions, and improve readiness.

Separately, NIST SP 800-61r3 is applied as CSF 2.0-aligned guidance: Govern, Identify, and Protect support preparation; Detect, Respond, and Recover support incident response; and improvement feeds back across the functions [N1].

## 2. Operational status model

| Status | Meaning | Governance implication |
|---|---|---|
| **Security event** | An observed or reported occurrence that may be benign, accidental, or security-relevant. | Record the source and time; route for triage. |
| **Suspected security incident** | An event with a credible indication of unauthorised activity, policy breach, material impact, or recovery risk, but incomplete validation. | Preserve the report and evidence references; consider urgent protective action. |
| **Validated security incident** | Available information confirms that the event meets Northbridge's incident threshold, without requiring attacker attribution or final scope. | Create or update the incident record and assign initial severity. |
| **Declared incident** | The Incident Response Lead or authorised delegate has formally accepted incident governance responsibility. | Establish an incident ID, decision owner, review point, and authority record. |
| **Activated response** | The declared incident has brought the required security, IT, service, continuity, management, or specialist functions into coordinated response. | Allocate scarce personnel and establish controlled situation reporting. |
| **Escalated incident** | Severity, urgency, scope, business impact, uncertainty, or resource needs require a higher decision tier. | Notify the required authority and reassess response options. |
| **Incident under recovery** | Containment and investigation permit controlled restoration planning, but security, integrity, and business gates remain open. | Do not restore from an unvalidated backup or treat technical availability as acceptance. |
| **Incident closed** | The closure authority has confirmed records, unresolved risks, follow-up ownership, communications, and review outcomes. | Retain the record and transfer improvement actions to the appropriate owner. |

Validation, declaration, and urgent protective action may overlap during a time-sensitive incident. Protective action does not require proof of attacker attribution or final cause.

## 3. Initial incident declaration

### 3.1 Reporting channels

Reports may be made through the approved service desk, Incident Response Lead, Security Analyst, IT Operations Lead, line manager, or designated service provider contact. If the incident contact list or corporate email is unavailable or untrusted, staff phones are used for verified calls to known contacts. A controlled, independently maintained contact list and a pre-authorised secondary channel should be established as readiness controls; the scenario does not establish that either already exists. Sensitive incident details must not be sent through a channel whose trustworthiness is unverified.

For an out-of-band contact, the caller verifies the recipient against independently maintained contact information or a second trusted factor, shares only the minimum necessary information, and records the WAT time, recipient role, purpose, channel, and approval. Staff phones are an available scenario capability; a secure group, alternate platform, or independent directory is a proposed control unless separately approved and verified.

Any recipient of a report must preserve the original wording and time, avoid unnecessary forwarding, and route the report to the Incident Response Lead or delegated triage role. A report can be logged before it is validated.

### 3.2 Initial validation

The Incident Response Lead or delegated triage role records:

- what was reported and by whom;
- when the report was received, using WAT where relevant;
- immediate safety, service, examination, and privacy concerns;
- relevant evidence IDs, logs, or records already available;
- affected and potentially affected assets;
- whether suspicious activity may be continuing; and
- immediate protective options and their possible business or evidence effects.

Validation does not require certainty about attacker identity or root cause. The purpose is to determine whether the event meets an incident threshold and what urgent authority is required.

### 3.3 Declaration decision

The Incident Response Lead declares an incident when the available information indicates a credible security or policy event with material or potentially material confidentiality, integrity, availability, or recovery implications. If the Incident Response Lead is unavailable, the delegated senior IT/security decision-maker may declare and must record the delegation.

The declaration record creates a proposed incident identifier in the format `NSI-IR-YYYYMMDD-NNN`; the identifier is a naming convention, not an existing case number. The record includes the evidence basis, initial severity, uncertainty, decision owner, and next review point.

### 3.4 Application to the 08:45 scenario

At 08:45 WAT on Day 0, the approved Task 1 position is **High — provisional**. If the governance plan were applied, the Incident Response Lead would activate High-level coordination because E03, E04, E06, E07, and E08 indicate urgent privileged-access, transfer, file-integrity, learner-service, and coordination concerns, while E05 leaves recovery capability uncertain. The 11:00 examination creates a time-critical business decision. This is a proposed governance response, not a statement that it occurred.

## 4. Activation conditions

| Condition | Initial governance response | Additional capability that may be activated |
|---|---|---|
| Suspected ransomware or destructive file activity | Declare or validate an incident; protect evidence; assess active spread and affected shares/endpoints. | Incident Response Lead, Security Analyst, IT Operations, forensic support, and management. |
| Significant service disruption | Record the service effect, business owner, dependencies, and continuity options; assess severity. | Business continuity and affected service owner; communications if learners or staff are affected. |
| Suspected privileged-account misuse | Protect relevant records and assess whether access remains active; do not assume attacker control. | Identity administration, IT Operations, forensic support, and management decision authority. |
| Potential data compromise or suspicious transfer | Preserve source, proxy, cloud, identity, and file records; classify possible data categories without asserting disclosure. | Privacy/Legal Adviser and data owner; specialist support if required. |
| Uncertain backup integrity or recoverability | Protect recovery infrastructure and prohibit unvalidated production restoration. | Backup owner, IT Operations, forensic support, business owner, and management. |
| Threat to a time-critical examination | Establish a joint security and continuity decision path; do not reopen an unvalidated service solely because of the deadline. | Academic Operations, Business Service Owner, management, and communications. |

Initial declaration identifies the event. Activation brings the necessary decision-makers and resources into the response. A higher activation level does not prove a higher technical scope; it reflects urgency, potential impact, resource needs, or business risk.

## 5. Severity-based escalation

The following model is consistent with the approved Task 1 criteria. Internal response times are deliberately described qualitatively; no unapproved SLA is created.

| Severity | Trigger examples | Primary decision authority | Internal notification and urgency | Follow-up and reassessment |
|---|---|---|---|---|
| **Low** | Isolated anomaly with no material CIA impact and no credible active-compromise signal. | Incident Response Lead or delegated operational owner. | Record and route through the standard workflow; notify the relevant owner. | Validate the benign or bounded explanation and close or monitor. |
| **Medium** | Localised impact, essential operations continue, and a credible recovery path exists. | Incident Response Lead with IT/service owner. | Notify management as proportionate; coordinate security and technical response promptly. | Reassess if scope, data impact, recovery confidence, or business disruption changes. |
| **High** | Material critical-service or multi-asset impact; suspected compromise; time-critical examination; privileged or recovery infrastructure concern; or significant uncertainty. | Incident Response Lead directs; management is notified rapidly. | Activate coordinated security, IT, service-owner, and continuity involvement; use verified telephone fallback or another approved alternate channel if necessary. | Reassess after high-value validation and before restoration or major service return. |
| **Critical** | Severe or imminent institution-wide disruption, essential examination/core function cannot be delivered safely, broad compromise or disclosure is established, persistent control is confirmed, or viable recovery is lost. | Senior management or Executive Sponsor, with Incident Response Lead directing response. | Immediate full available mobilisation and executive coordination; obtain authorised external support where needed. | Maintain executive situation reporting and reassess continuously as evidence and business impact change. |

Escalation may be based on operational impact, affected assets, data sensitivity, uncertainty, recoverability, urgency, and resource constraints. It is not based solely on the presence of a ransom note.

## 6. Decision authority and delegation

The Incident Response Lead is the default incident director. The Lead may delegate a defined decision to the IT Operations Lead, Security Analyst, Business Service Owner, or another approved role, but the delegation must state its scope, duration, constraints, and review point.

The following rules apply:

- The Incident Response Lead authorises normal containment and specifies its scope, expected effect, evidence-preservation requirements, and review point. The IT Operations Lead, Security Analyst, and Business Service Owner are consulted when their technical, security, or service impacts are relevant.
- The IT Operations Lead assigns an authorised technical operator to execute an approved containment or recovery action. Technical operators may not expand the scope of an approval.
- The Security Analyst assesses evidence, severity, and security risk; analysis alone does not authorise disruptive action.
- The Incident Response Lead may approve a routine operational deviation within approved delegated authority when it has limited impact and does not materially weaken security controls or create significant privacy risk.
- Senior management or the designated Executive Sponsor approves material or policy-level exceptions, Critical escalation, material external commitments, extraordinary resource use, and institutional risk acceptance after relevant consultation.
- The Business Service Owner accepts operational risk for service continuity and confirms business readiness; this does not replace security validation.
- The Business Continuity Coordinator coordinates authorised continuity arrangements and may initiate predefined low-risk preparations within written delegation. Senior Management retains authority for material continuity activation and risk acceptance. Management assigns a deputy or alternate BCC and records the scope of that assignment.
- The Academic or Business Service Owner approves examination delivery arrangements within approved parameters; material deviations require management approval. The Incident Response Lead determines security restrictions.
- Privacy/Legal Advisers provide advice on data classification, contractual or regulatory questions, and formal notification decisions; they do not determine technical scope without evidence.
- Communications personnel prepare approved messages and do not release external statements without the required approval.
- If the Incident Response Lead cannot be reached promptly and delay may materially worsen harm, the IT Operations Lead or formally delegated senior IT/security authority may authorise narrowly scoped emergency containment under the isolation procedure. The action must be the least disruptive effective measure, notify the Incident Response Lead or deputy and management as soon as practicable, and be retrospectively reviewed.

## 7. Coordination constraints and support

Northbridge has three IT personnel and one security analyst. The plan therefore uses role-based sequencing rather than assuming simultaneous dedicated teams. At least one person must maintain incident records and decision traceability while others perform approved technical checks. The Incident Response Lead should identify conflicts between evidence preservation, containment, examination continuity, and restoration safety before allocating scarce staff.

The inaccessible FS01 contact list and unverified corporate email require an alternate approved coordination channel. Staff phones are available for verified calls, but the controlled contact list, secondary channel, and access controls remain readiness decisions. The FS01 dependency for LMS01 means that a file-server decision can affect learning services; the plan must not treat that relationship as proof of cause. BAK01 and `svc_backup` require urgent governance attention because backup trust affects safe recovery, not because compromise is established.

## 8. Escalation beyond available resources

The Incident Response Lead may recommend external support when internal capacity, specialist skill, independence, or recovery confidence is insufficient. Proposed support may include:

- specialist digital forensics and malware analysis;
- backup and recovery engineering;
- legal and privacy advice;
- communications and learner-support coordination; and
- an incident response firm or relevant service provider.

External engagement requires management authorisation, availability, appropriate confidentiality arrangements, and a confirmed scope of work. No contractual entitlement, provider response time, or completed engagement is assumed by this plan. The reason for escalation, information shared, decision owner, and expected decision value must be recorded.

## 9. Documentation and review checkpoints

The Incident Response Lead reviews the situation record after initial validation, after material new evidence, before restoration or major service return, after a severity change, and at closure. The minimum record fields are defined in `incident-documentation-procedure.md` and the blank template in `../data/incident-decision-log-template.csv`.

## 10. Stage boundary

This document is the historical Stage 1 governance baseline and intentionally does not duplicate later deliverables. The current proposed six-role CSIRT structure, 22-activity RACI, and readiness improvements are recorded in the [CSIRT design](../csirt/csirt-organisation-and-command.md), [RACI matrix](../raci.csv), and [preparation improvements](../readiness/preparation-improvements.md). The current communications and response playbook are maintained in [Task 4](../../06-task-04-communications/TASK-4-COMMUNICATION-PLAN.md) and [Task 3](../../05-task-03-response-playbook/TASK-3-RESPONSE-PLAYBOOK.md). These remain draft assessment artifacts and do not claim organisational approval or completed operational actions.

## 11. References

- [A1] GRC105 assignment, Task 2 and Task 2 marking criteria.
- [S1] Week 20 teaching deck, slides 6, 8–10, and 14–15.
- [N1] NIST SP 800-61r3, official publication: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- [C1] CISA and partners, *#StopRansomware Guide*: https://www.cisa.gov/stopransomware/ransomware-guide
