# Isolation Authority and Emergency Decision Procedure

**Document identifier:** NSI-IR-PROC-002
**Version:** 0.1
**Status:** Stage 1 draft — governance procedure, not a technical containment playbook
**Owner:** Incident Response Lead — proposed role

## 1. Purpose

This procedure defines who may approve, direct, execute, document, and review an urgent isolation or other containment decision. It does not provide device commands, firewall rules, account-reset instructions, or a complete technical containment sequence. Those belong in Task 3.

## 2. Conditions supporting immediate containment

Immediate containment should be considered when one or more of the following applies:

- suspicious activity may still be continuing;
- file changes, service disruption, credential misuse, or transfer activity may propagate or cause further damage;
- a privileged account or recovery repository may remain exposed;
- delaying action is likely to increase operational, confidentiality, or integrity impact;
- a suspected active threat affects FIN-PC07, FS01, LMS01, BAK01, Microsoft 365, or a related identity; or
- the threat is time-critical and normal approval cannot be obtained without unacceptable delay.

The presence of a ransom note, unusual sign-in, or backup report alone does not prove the cause or authorise an unlimited response. The decision must identify the evidence basis and the smallest reasonable action that reduces risk.

## 3. Authority model

| Situation | Decision authority | Technical execution | Governance requirement |
|---|---|---|---|
| Normal containment consideration | Incident Response Lead | IT Operations Lead assigns an authorised IT operator; Security Analyst and Business Service Owner advise where relevant | Record approval, scope, expected effect, evidence to preserve, business impact, and review time before action where practicable. |
| File-server, learning-service, or backup isolation | Incident Response Lead; IT Operations Lead and Business Service Owner consulted where material service effects exist | IT Operations Lead assigns the operator | Consider FS01 dependency, LMS01 examination impact, BAK01 recovery risk, and evidence loss. |
| Privileged-account restriction | Incident Response Lead with Security Analyst and IT Operations Lead | Authorised identity or IT operator | Preserve relevant identity/session records before a reset or disablement where safely practicable. |
| Emergency action when the Incident Response Lead cannot be reached promptly and delay may materially worsen harm | IT Operations Lead or formally delegated senior IT/security authority | Authorised operator | Use the least disruptive effective action; record why delay was unsafe; preserve evidence where feasible; notify the Incident Response Lead or deputy and management; conduct retrospective review. |
| Critical or institution-wide decision | Senior management or Executive Sponsor, with Incident Response Lead directing response | IT Operations under approved scope | Coordinate continuity, communications, privacy/legal advice, and external support as needed. |

Decision authority is not the same as technical execution. A person who can execute an approved action may not independently expand its scope unless emergency authority is explicitly recorded.

## 4. Emergency decision procedure

### Step 1 — Identify the immediate risk

The Incident Response Lead records the suspected activity, relevant evidence IDs, affected or potentially affected assets, whether activity may be continuing, and the consequence of delay. For the Northbridge scenario this may include E03 `svc_backup` activity, E04 transfer activity, E06 file changes, E07 learner-service disruption, and E08 coordination impairment. These are observations and decision inputs, not proof of attacker control or causation.

### Step 2 — Consider operational and continuity impact

Before isolation, identify:

- whether LMS01 depends on the affected FS01 function;
- whether isolation may affect the 11:00 examination for 100 learners;
- whether staff or learner communications rely on the affected service;
- whether BAK01 or `svc_backup` is exposed to further change;
- whether an alternate service or coordination channel exists; and
- whether the action could destroy volatile evidence or change the interpretation of the event.

Security risk is not automatically overridden by examination pressure. If a continuity option is preferred, its security assumptions, owner, approval, and validation conditions must be recorded.

### Step 3 — Select the minimum necessary action

The decision record states the target, action boundary, duration or review point, expected security benefit, expected operational effect, and evidence-preservation plan. If a broader action is needed, the record explains why a narrower action is insufficient.

### Step 4 — Authorise or delegate

For normal containment, the Incident Response Lead authorises the action and specifies the approved scope. The IT Operations Lead assigns an authorised operator; the operator must not expand the scope. The Security Analyst and Business Service Owner are consulted where the action has material security or service consequences.

If the Incident Response Lead cannot be reached promptly and delay may materially worsen harm, the IT Operations Lead or formally delegated senior IT/security authority may authorise narrowly scoped emergency containment. The record must state why delay was unsafe, who exercised the emergency authority, the minimum action boundary, evidence-preservation considerations, business effect, notification due, and retrospective management review deadline. Emergency authority does not permit unrelated isolation, unrestricted access, unsafe restoration, or bypassing business acceptance. The authorised operator confirms execution status; this procedure does not claim that an action has occurred.

### Step 5 — Preserve and reconcile evidence

Relevant endpoint, identity, network, server, backup, application, and helpdesk records should be preserved before disruptive change where safe. If evidence may be lost, the record states what could be lost, why the operational action was necessary, and what alternative evidence will be sought. NIST SP 800-86 is used as supporting guidance for planning forensic techniques, with management and legal consultation where appropriate [N2].

### Step 6 — Notify and review

The Incident Response Lead notifies management, the affected Business Service Owner, the Business Continuity Coordinator, and continuity or privacy/legal advisers as appropriate. The decision is reviewed after the initial risk is reduced, when new evidence arrives, before extending or reversing isolation, and at closure. Any emergency exception is reviewed retrospectively by management or the designated Executive Sponsor.

## 5. Illustrative Northbridge decision contexts

| Context | Governance question | Required caution |
|---|---|---|
| FIN-PC07 | Could continued endpoint activity affect shared files, identities, or the E04 transfer investigation? | Do not infer malicious attachment execution; preserve endpoint and proxy evidence before disruptive action where safe. |
| FS01 | Could current file changes or privileged access continue? | Consider the LMS01 dependency and contact-list impact; do not treat isolation as proof of cause. |
| LMS01 | Could service access be safely maintained or isolated before the examination? | A working login page is not proof that materials or assessment submission are safe. |
| BAK01 | Could recovery data or configuration be altered? | Do not restore from a reported successful job until isolated validation establishes trust. |
| Microsoft 365 and identities | Could account or session activity continue? | Preserve sign-in, MFA, device, token, mailbox, and account-change records before protective identity action where safely practicable. |

## 6. Minimum emergency decision record

Record the incident ID, WAT timestamp, decision owner, authority or delegation, evidence references, suspected threat, affected assets, proposed action, alternative considered, security benefit, operational impact, evidence-preservation effect, execution owner, approval status, notification, review time, and final outcome. Use the fields in `incident-documentation-procedure.md` and `../data/incident-decision-log-template.csv`.

## 7. References and boundary

- [A1] GRC105 assignment, Task 2 policy/authority requirements and Task 3 containment tradeoff requirement.
- [S1] Week 20 teaching deck, slides 9–11 and 14–15.
- [N1] NIST SP 800-61r3, official publication: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- [N2] NIST SP 800-86, official publication: https://csrc.nist.gov/pubs/sp/800/86/final

This procedure stops at governance-level authority. Technical containment commands, ordered first-hour actions, evidence custody execution, eradication, restoration criteria, and monitoring belong to Task 3 and are not completed here.
