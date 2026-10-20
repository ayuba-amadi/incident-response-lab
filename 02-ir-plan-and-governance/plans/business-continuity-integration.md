# Incident Response and Business Continuity Integration

**Document identifier:** NSI-IR-BC-001
**Version:** 0.1
**Status:** Stage 1 draft — awaiting approval
**Planning point:** 08:45 WAT on Day 0

## 1. Purpose

Incident response, business continuity, and disaster recovery have related but distinct responsibilities. Northbridge must protect the institute while preserving acceptable educational services, especially when a learner-facing examination is time-critical and recovery capability is uncertain.

## 2. Distinct responsibilities

| Function | Primary responsibility | Northbridge application |
|---|---|---|
| **Incident response** | Security investigation, incident declaration, containment governance, evidence preservation, threat-eradication planning, and security validation for recovery. | Assess E01–E08, protect identities and recovery infrastructure, preserve records, and advise whether LMS01 or FS01 can safely remain available. |
| **Business continuity** | Maintain acceptable educational services, coordinate examination contingencies, support learners, manage operational resources, and coordinate business communications. | The Business Continuity Coordinator (BCC) coordinates authorised arrangements and may initiate predefined low-risk preparations within written delegation. Senior Management retains authority for material activation and institutional risk acceptance. |
| **Disaster recovery** | Technical restoration planning, backup selection and validation, controlled system restoration, and recovery verification. | Assess FS01/LMS01 recovery points and BAK01 without assuming that E05's reported job success means a clean or restorable backup. |

Business continuity does not authorise bypassing security validation. Incident response does not decide academic policy alone. Disaster recovery does not approve its own business return to service.

The BCC is a proposed functional assignment and not necessarily a new full-time employee. Management must assign a deputy or alternate BCC and record the scope and duration of that assignment. The BCC cannot unilaterally override incident containment, security restrictions, technical recovery gates, or business acceptance requirements.

## 3. Coordination triggers

Simultaneous response and continuity involvement is required when:

- a critical learning, assessment, finance, or shared-file service is unavailable or materially impaired;
- an incident may affect the 11:00 examination for 100 learners;
- containment of FS01, LMS01, FIN-PC07, BAK01, or an identity may interrupt an important business function;
- backup trust or recoverability is uncertain;
- learner, staff, finance, assessment, or other institutional information may be exposed; or
- the available three IT personnel and one security analyst cannot safely support investigation, containment, continuity, and recovery decisions simultaneously.

At the Task 1 planning point, E07 provides confirmed learner-facing service impact, E08 creates a coordination constraint, and the examination creates urgency. The cause and extent of LMS01 impact remain unverified, and no decision to postpone, restore, or reopen the examination service is claimed.

## 4. Joint decision-making

The Incident Response Lead prepares the security situation and options and determines security restrictions. The Security Analyst explains evidence, uncertainty, and security consequences. The IT Operations Lead explains technical dependencies and execution risk. The BCC coordinates authorised continuity options and operational resources. The Business Service Owner and Academic Operations approve examination delivery arrangements within approved parameters and explain learner impact. Management approves material continuity activation, institutional risk acceptance, material deviations, extraordinary resources, and Critical-level decisions.

Where objectives conflict, the joint record must state:

1. the security risk and evidence basis;
2. the business or examination consequence;
3. the available options and their assumptions;
4. the evidence-preservation and service effects of each option;
5. the decision owner and approval authority;
6. the time or evidence condition for review; and
7. the contingency if the chosen option becomes unsafe.

For example, security may recommend isolating an affected service while academic operations seeks examination access. The BCC may coordinate a predefined low-risk alternative, but the relevant Business Service Owner must approve the examination delivery arrangement and management must approve material risk or deviation. Management may approve a continuity alternative only after the security restrictions, data integrity assumptions, and monitoring requirements are recorded. An unverified backup must not be treated as safe merely because the examination deadline is close.

## 5. Shared situation reporting

The response and continuity functions exchange a short, controlled situation report containing:

- incident ID and WAT reporting time;
- confirmed service status;
- affected and potentially affected assets;
- scope uncertainty and relevant evidence IDs;
- security restrictions and approved containment status;
- examination readiness and known learner impact;
- continuity options and their assumptions;
- backup/recovery trust status;
- decisions awaiting approval;
- communication owner and approved channel; and
- next review or decision point.

The report distinguishes confirmed observations from hypotheses and does not state that a service, backup, or account is safe without validation.

## 6. Examination continuity decision path

Before the 11:00 examination decision, the Incident Response Lead and Business Service Owner should establish the current LMS01 and FS01 functional status, security restrictions, safe communication route, and available alternatives. The BCC coordinates the options; the relevant Academic or Business Service Owner approves the examination delivery arrangement within approved parameters, while management approves material deviations or institutional risk acceptance. The decision must not assume that the portal login page loading means materials and submission functions are safe.

Any continuity option must identify learner communications, data-handling implications, technical prerequisites, responsible owner, approval, and review condition. The scenario does not establish that the examination was postponed or successfully restored.

## 7. Return-to-service authority

Return to service requires four separate confirmations:

1. **Technical availability:** the service performs its required functions in a controlled test.
2. **Security validation:** active compromise, unauthorised access, and relevant persistence risks are addressed or formally accepted.
3. **Data integrity:** files, application state, permissions, and relevant recovery data are validated.
4. **Business acceptance:** the Business Service Owner and management accept the service and continuity risk.

The IT Operations Lead may execute an approved restoration, but technical execution alone does not authorise business return. The Security Analyst does not certify a clean system without evidence. The proposed recovery planning, restore-testing, and acceptance criteria are documented in the [Task 3 response playbook](../../05-task-03-response-playbook/TASK-3-RESPONSE-PLAYBOOK.md); this Stage 1 document records their governance dependency without claiming that any restoration or test has occurred.

## 8. Resource constraints and external support

The small internal team must sequence high-value checks and avoid assigning every person to the same task. Management may authorise external incident response, forensics, backup recovery, privacy/legal, communications, or learner-support assistance when internal capacity or independence is insufficient. The need, scope, confidentiality conditions, availability, and approval must be recorded; no external engagement is assumed to exist.

## 9. References and boundary

- [A1] GRC105 assignment, Task 2 continuity requirement and Task 1 examination/backup context.
- [S1] Week 20 teaching deck, slides 6, 11, 14, and 17–18.
- [N1] NIST SP 800-61r3, official publication: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- [C1] CISA and partners, *#StopRansomware Guide*: https://www.cisa.gov/stopransomware/ransomware-guide

This document establishes governance integration only. It does not create recovery commands, an operational restoration sequence, or a Task 3 playbook. The separate Task 3 artifact contains proposed recovery criteria and actions and must be read with this governance boundary.
