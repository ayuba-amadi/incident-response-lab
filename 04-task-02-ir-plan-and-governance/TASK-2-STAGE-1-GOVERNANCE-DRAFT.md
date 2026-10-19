# Northbridge Skills Institute — Task 2 Stage 1 Governance Draft

**Status:** Stage 1 draft — awaiting independent review and organisational approval
**Scope:** Incident response policy, governance, activation, escalation, isolation authority, recordkeeping, and business continuity integration
**Incident planning point:** 08:45 WAT on Day 0
**Approved Task 1 position:** High — provisional

This consolidated draft is intended for later report incorporation. Supporting procedures and editable diagrams remain authoritative for detail. No response action, forensic acquisition, restoration test, or notification is claimed.

## 1. Policy purpose, objectives and scope

Northbridge's proposed incident response mission is to protect educational services and learner/staff information, limit security and operational damage, preserve evidence, make accountable decisions, coordinate continuity, and enable safe recovery. The policy covers employees, contractors, relevant service providers, managed endpoints and servers, Microsoft 365 identities, privileged accounts, shared storage, backups, learning services, and institutional information.

The policy is a draft awaiting approval. Its objectives are to establish consistent reporting and validation, clear authority, evidence-preserving decisions, proportionate response, continuity coordination, safe return to service, and post-incident improvement.

See [incident-response-policy.md](policy/incident-response-policy.md) for document control, governance principles, exceptions, review, and source references.

## 2. Governance and decision authority

The proposed authority model separates governance ownership from technical execution:

| Decision | Proposed owner | Required control |
|---|---|---|
| Declare and direct the incident | Incident Response Lead | Record evidence basis, severity, uncertainty, and next review. |
| Authorise normal containment | Incident Response Lead | Consult IT Operations, Security Analysis, and the Business Service Owner where material effects exist; specify scope and review point. |
| Execute approved technical action | IT Operations Lead and assigned authorised operator | Stay within approved scope and record execution status. |
| Analyse evidence and validate security | Security Analyst | Make evidence-linked recommendations; do not assume authority from analysis alone. |
| Approve material exceptions or Critical action | Senior management / Executive Sponsor | Record risk acceptance, resources, continuity, and communications decisions. |
| Accept business service return | Business Service Owner with management as required | Confirm business readiness after technical and security validation. |
| Coordinate business continuity | Business Continuity Coordinator within written delegation; Senior Management retains material activation authority | Assign a deputy/alternate and record scope; do not bypass security controls. |

Emergency containment applies only when the Incident Response Lead cannot be reached promptly and delay may materially worsen harm. The IT Operations Lead or formally delegated senior IT/security authority may approve the minimum necessary action, with notification and retrospective review. This Stage 1 draft records the historical boundary; the detailed CSIRT membership and RACI matrix are now maintained in the [Stage 2 CSIRT/RACI draft](TASK-2-STAGE-2-CSIRT-RACI-DRAFT.md) and its supporting artifacts.

## 3. Incident declaration and activation

Reports may arrive through the service desk, Incident Response Lead, Security Analyst, IT Operations Lead, line manager, service provider, or approved phone channel. If the FS01 contact list or corporate email is unavailable or untrusted, staff phones are used for verified calls to known contacts. A controlled independent contact list and a pre-authorised secondary channel remain proposed readiness controls unless separately approved and verified.

The Incident Response Lead or delegated triage role records the report, WAT timestamp, source, immediate impact, evidence references, affected or potentially affected assets, continuing-threat concern, and protective options. The status model in the [incident-response-governance-plan.md](plans/incident-response-governance-plan.md) distinguishes security event, suspected incident, validated incident, declaration, activation, escalation, recovery, and closure. A credible security or policy event is declared as an incident; activation then brings the appropriate resources and governance into the response. Validation, declaration, and urgent protective action may overlap.

At 08:45 WAT on Day 0, the approved Task 1 position is **High — provisional**. If applied, this would justify urgent coordinated activation because E03, E04, E06, E07, and E08 indicate privileged-access, transfer, file-integrity, learner-service, and coordination concerns, while E05 leaves recovery trust uncertain. This is a proposed planning treatment, not a completed action.

The flow is shown in [incident-declaration-activation.mmd](diagrams/incident-declaration-activation.mmd).

## 4. Severity-based escalation

| Level | Governance treatment |
|---|---|
| Low | Standard documented workflow, bounded owner, validation, and monitoring or closure. |
| Medium | Prompt Incident Response Lead, IT, and service-owner coordination with proportionate management notification. |
| High | Rapid management notification, coordinated security/IT/continuity involvement, protection of identities and recovery assets, and reassessment before major service return. Northbridge is High — provisional. |
| Critical | Senior management or Executive Sponsor leads risk decisions, full available mobilisation is used, continuity is activated, and external support may be authorised. |

Escalation is driven by observed and potential operational impact, scope, data sensitivity, urgency, recoverability, and resources. It is not based solely on a ransom note. The decision flow is in [severity-escalation-workflow.mmd](diagrams/severity-escalation-workflow.mmd).

## 5. Emergency isolation authority

Immediate containment may be considered where activity may continue, propagation or further damage is possible, privileged or recovery assets may remain exposed, or delay is likely to worsen harm. Before action, the Incident Response Lead records the security benefit, operational effect, examination dependency, evidence-preservation tradeoff, action boundary, authority, technical executor, and review time.

Normal containment authority is the Incident Response Lead, with IT Operations, Security Analysis, and the Business Service Owner consulted where relevant. If the Incident Response Lead cannot be reached promptly and delay may materially worsen harm, the IT Operations Lead or formally delegated senior IT/security role may authorise the minimum necessary emergency action, notify the Incident Response Lead or deputy and management as soon as practicable, and arrange retrospective review. Emergency authority does not permit unrelated isolation, unsafe restoration, or bypassing business acceptance.

FIN-PC07, FS01, LMS01, BAK01, Microsoft 365, and `svc_backup` are governance decision contexts from Task 1, not proof of compromise. Restoration from an unverified backup is not authorised by this procedure. See [isolation-authority-and-emergency-decisions.md](plans/isolation-authority-and-emergency-decisions.md) and its diagram.

## 6. Documentation and recordkeeping

Every material incident decision must record its ID, WAT time, reporter/source, description, evidence IDs, classification, assets, decision, owner, approval, action owner, execution status, supporting evidence, business impact, communications, next review time, and closure authorisation.

Records are access-restricted, version-controlled, confidential, and linked to evidence references. Corrections are additive or controlled revisions; original observations are not silently overwritten. If central systems are unavailable or untrusted, an approved alternate record is used and reconciled later. Retention follows the approved records schedule; no statutory period is invented.

See [incident-documentation-procedure.md](plans/incident-documentation-procedure.md) and the headers-only [incident-decision-log-template.csv](data/incident-decision-log-template.csv).

## 7. Business continuity integration

Incident response investigates, contains, preserves evidence, and validates security. The Business Continuity Coordinator coordinates authorised continuity arrangements; business continuity maintains acceptable educational services, coordinates learner and examination contingencies, and allocates operational resources. Senior Management retains authority for material continuity activation and institutional risk acceptance. Disaster recovery plans and validates controlled restoration.

The 11:00 examination requires joint security, technical, academic, continuity, and management decision-making. The relevant Academic or Business Service Owner approves the examination delivery arrangement within approved parameters; material deviations require management approval. E07 confirms learner-facing impact; E05 does not confirm a safe restore point. No postponement, restoration, or reopening decision is assumed. A continuity option must document its security assumptions, business owner, approval, learner communications, and review condition.

Return to service requires separate confirmation of technical availability, security validation, data integrity, and business acceptance. See [business-continuity-integration.md](plans/business-continuity-integration.md) and [ir-business-continuity-coordination.mmd](diagrams/ir-business-continuity-coordination.mmd).

## 8. Operational limitations and residual risks

- Northbridge has three IT personnel and one security analyst; role allocation, external support, and sequencing require management attention.
- The incident contact list is inaccessible and corporate email trust is unverified. Staff phones are available for verified calls; a controlled independent contact list and secondary channel remain proposed readiness controls requiring approval.
- The FS01 dependency may affect LMS01, but it does not prove the cause of E07.
- `svc_backup` activity and the E04 transfer are observations requiring validation, not confirmed attacker actions or data theft.
- E05 reports successful jobs but does not establish backup integrity, recoverability, or cleanliness.
- Server EDR coverage is incomplete, so absence of an alert cannot establish absence of activity.
- No legal deadline, contractual right, external support engagement, or response SLA is assumed.

## 9. Sources and assumptions

- [A1] ICDFA, *GRC105 Incident Response Planning Assignment*, pp. 1–6, Task 2 and marking criteria.
- [S1] ICDFA, *Incident Response Planning*, Week 20 slides 6–10 and 14–18. The four course stages are used for organisation only.
- [N1] NIST, *SP 800-61 Revision 3*, 2025: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- [N2] NIST, *SP 800-86*, 2006: https://csrc.nist.gov/pubs/sp/800/86/final
- [C1] CISA and partners, *#StopRansomware Guide*: https://www.cisa.gov/stopransomware/ransomware-guide

Scenario facts and E01–E08 observations are drawn from the approved Task 1 materials. Proposed roles, authorities, channels, identifiers, and review controls are assumptions requiring organisational approval.

## 10. Outstanding Task 2 requirements

The following are intentionally deferred and must not be read as complete Task 2 requirements:

1. Define the complete CSIRT with at least six roles and detailed responsibilities.
2. Produce the final RACI for at least eight activities, with exactly one accountable role and at least one responsible role per activity.
3. Produce at least four preparation/readiness improvements with owner, resources, target completion, and measurable evidence.
4. Complete independent review, organisational approval, and the Task 2 review gate.

These items are tracked in [governance-requirements-matrix.csv](data/governance-requirements-matrix.csv). Task 3 technical containment, evidence custody execution, eradication, and recovery criteria are outside this stage.
