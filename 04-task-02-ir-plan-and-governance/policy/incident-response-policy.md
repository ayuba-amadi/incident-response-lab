# Northbridge Skills Institute Incident Response Policy

**Document identifier:** NSI-IR-POL-001
**Version:** 0.1
**Status:** Draft — awaiting organisational approval
**Effective date:** Not effective until approved
**Policy owner:** Incident Response Lead — proposed role
**Approval authority:** Institute Executive Sponsor or delegated senior management authority — proposed role
**Review frequency:** At least annually, and after a major incident, exercise, material system change, or significant governance change
**Information classification:** Internal — Sensitive

This policy is a fictional Northbridge Skills Institute working draft. It defines proposed governance arrangements; it does not record an approved organisational policy or a completed incident response.

## 1. Purpose and mission

Northbridge maintains an incident response capability to protect educational services, learner and staff information, and the integrity of institutional operations when a security event is suspected or confirmed. The mission is to identify and assess incidents, limit security and operational damage, preserve relevant evidence, make timely and accountable decisions, coordinate business continuity, and enable safe recovery.

The capability supports the institute's educational mission without assuming that technical availability alone means that a service is safe to use. Security validation, data integrity, business acceptance, and documented authority are required before a material service is returned to normal operation.

## 2. Objectives

The policy objectives are to:

- provide a consistent route for reporting and validating suspected incidents;
- establish clear authority for declaration, activation, escalation, containment, continuity, restoration, communications, and closure;
- preserve the provenance, confidentiality, and integrity of incident records and relevant evidence;
- distinguish observed facts, working hypotheses, decisions, and unresolved questions;
- prioritise learner-facing services, sensitive information, privileged access, and recovery infrastructure according to business impact and uncertainty;
- coordinate incident response with business continuity and technical recovery without treating an unverified backup as safe; and
- capture lessons and maintain the plan through approved review and improvement.

Operational response-time targets may be proposed in procedures, but no target becomes an institutional service level until management approves it and confirms the resources needed to meet it.

## 3. Scope

This policy applies to:

- employees, contractors, learners when using institute-managed services, and relevant external service providers;
- institution-managed endpoints, servers, learning services, shared storage, backup repositories, network services, and cloud services used for institute business;
- privileged accounts, Microsoft 365 identities, mailboxes, authentication services, and service accounts;
- learner, staff, admission, assessment, finance, credential, operational, and other institutional information; and
- incidents affecting confidentiality, integrity, availability, security policy, acceptable use, or the trustworthiness of response records.

External providers may need to supply logs, support, specialist services, or contractual notifications. This policy does not assume that Northbridge has a particular contractual right, response commitment, or regulatory reporting duty. Those matters must be checked against the applicable agreement and legal or privacy advice.

## 4. Governance principles

Northbridge response decisions will follow these principles:

1. **Evidence-based decisions:** record what is observed, what is inferred, what is unknown, and what is being proposed for verification.
2. **Proportionality:** match the response to likely impact, scope, urgency, recoverability, and available resources.
3. **Least privilege:** restrict response records, administrative access, and emergency actions to what is necessary.
4. **Separation of duties:** distinguish incident direction, technical execution, business acceptance, privacy or legal advice, and communications approval where resources permit.
5. **Accountability:** every material decision has an owner, authority basis, status, supporting evidence reference, and review point.
6. **Confidentiality:** use approved channels and minimum-necessary disclosure, particularly when personal or sensitive information may be involved.
7. **Evidence preservation:** preserve relevant records and provenance before disruptive actions where safely practicable.
8. **Business impact:** consider educational delivery, learner support, examinations, staff capacity, and service dependencies.
9. **Safe restoration:** do not restore a service or backup solely because a deadline exists; technical security validation and business approval are both required.

## 5. Policy authority

The following authority model is proposed for approval. It defines governance ownership, not a roster of named employees.

| Decision | Proposed authority | Execution or support | Required control |
|---|---|---|---|
| Report a suspected incident | Any staff member, contractor, service provider, or learner using an approved reporting route | Incident Response Lead or delegated triage role | Record the report and protect the reporter's information as appropriate. |
| Declare an incident | Incident Response Lead; delegated senior IT/security decision-maker if unavailable | Security analyst and IT operations support | Record the basis, initial severity, incident ID, and uncertainty. |
| Activate response procedures | Incident Response Lead | Available IT, security, business, privacy/legal, and communications functions as needed | Activation does not prove the suspected cause or scope. |
| Escalate severity | Incident Response Lead with management notification; management may direct a higher tier | Security analyst, IT operations, business owner, and advisers | Reassess when material evidence or business impact changes. |
| Authorise normal containment | Incident Response Lead | IT Operations Lead assigns an authorised technical operator; Security Analyst and Business Service Owner advise where relevant | Specify the approved scope, expected effect, evidence to preserve, business impact, and review time. |
| Authorise emergency containment | Incident Response Lead where available; IT Operations Lead or formally delegated senior IT/security authority only when the Lead cannot be reached promptly and delay may materially worsen harm | Authorised IT operator executes the minimum necessary action | Record urgency, scope, evidence-preservation effect, notification, and retrospective review. Emergency authority is not unlimited isolation authority. |
| Approve routine operational deviation | Incident Response Lead within approved delegated authority | Relevant technical, business, and security advisers | Limited impact; no material weakening of controls or significant privacy effect; record rationale and review condition. |
| Approve material or policy-level exception | Senior Management or designated Executive Sponsor | Relevant technical, business, and Privacy/Legal advisers | Record institutional risk acceptance, scope, duration, compensating controls, and review deadline. |
| Activate business continuity | Senior Management retains authority for material activation and institutional risk acceptance; Business Continuity Coordinator coordinates authorised arrangements | Business Continuity Coordinator, Business Service Owner, and Academic Operations with Incident Response Lead | The BCC may initiate predefined low-risk preparations within delegation; continuity must not bypass security validation. |
| Approve examination continuity arrangement | Relevant Academic or Business Service Owner within approved parameters; Senior Management approves material deviation or risk acceptance | Business Continuity Coordinator coordinates; Incident Response Lead defines security restrictions | Record learner impact, technical prerequisites, security assumptions, approval, and review condition. |
| Approve restoration or service return | IT Operations Lead and affected Business Service Owner, with Security Analyst validation; management approval for High or Critical events | IT operations executes the approved technical work | Record integrity, security, operational, and business acceptance checks. |
| Approve external communications | Senior management with Communications Coordinator and Privacy/Legal Adviser input | Communications function | Confirm facts, audience, channel, approval, and privacy constraints. |
| Close the incident | Incident Response Lead with management and affected Business Service Owner acceptance | Security, IT, privacy/legal, and communications contributors | Confirm unresolved risks, records, follow-up actions, and review outcome. |

The Incident Response Lead directs the incident unless management appoints another incident director. Normal containment requires the Incident Response Lead's approval; the IT Operations Lead, Security Analyst, and Business Service Owner are consulted when their technical, security, or service impacts are relevant. The IT Operations Lead owns technical execution within the approved scope. The Security Analyst provides analysis and security recommendations but does not acquire authority merely by identifying a risk. A deputy must be appointed in the incident record when the normal decision-maker is unavailable.

If the Incident Response Lead cannot be reached promptly and delay may materially worsen harm, the IT Operations Lead or a formally delegated senior IT/security authority may approve narrowly scoped emergency containment. The action must be the least disruptive effective measure, preserve evidence where feasible, notify the Incident Response Lead or deputy and management as soon as practicable, and receive retrospective review. Emergency delegation does not authorise unrelated isolation, unrestricted access, unsafe restoration, or bypassing business acceptance.

The Business Continuity Coordinator (BCC) is a proposed functional assignment, not necessarily a new full-time employee. Senior Management retains authority for material continuity activation and institutional risk acceptance. The BCC coordinates authorised arrangements and may initiate predefined low-risk preparations within written delegation. Management must assign a deputy or alternate BCC; that assignment and scope must be recorded.

This Stage 1 policy records the governance baseline. The detailed proposed CSIRT structure and RACI allocation are now documented in the [CSIRT organisation and command design](../csirt/csirt-organisation-and-command.md), the [RACI matrix](../raci.csv), and the [RACI methodology](../csirt/raci-methodology-and-accountability.md). Those artifacts remain proposed and do not represent organisational approval.

## 6. Incident declaration and activation

Any credible indication of unauthorised access, destructive file activity, material service disruption, suspected data compromise, privileged-account misuse, or recovery-system risk must be reported through an approved channel. A report is triaged and validated before it is described as an incident, but urgent protective action may occur while validation continues.

Declaration records must include the incident ID, reporting time, source, initial facts, relevant evidence references, affected or potentially affected assets, initial severity, decision owner, and unresolved questions. Activation adds coordinated response resources and governance; it is distinct from the initial declaration and does not establish attacker identity or final scope.

For the approved Task 1 scenario, the governance position at **08:45 WAT on Day 0** is **High — provisional**. If this policy were applied, the Incident Response Lead would record the learner-facing disruption, FS01 file-impact indicators, unusual `svc_backup` activity, possible transfer, uncertain backup trust, inaccessible contact list, and the 11:00 examination as the basis for urgent activation. This statement is a planning example, not a claim that the actions occurred.

When corporate email or the FS01 contact list is unavailable or untrusted, staff phones are the available scenario capability for verified telephone calls to known contacts. Northbridge should maintain a controlled, independently maintained contact list and approve a secondary channel before an incident. Before sensitive information is shared out of band, the recipient's identity must be verified using known contact details or a second trusted factor. Sensitive forensic material must not be sent through an unverified channel. Each notification and decision must be recorded with the WAT time, sender, recipient role, channel, purpose, and approval. The scenario does not establish that a secondary platform or independent contact directory already exists.

## 7. Exceptions and compliance

Exceptions are classified as follows:

1. **Routine operational deviation:** The Incident Response Lead may approve a limited deviation within approved delegated authority when operational impact is limited, no critical security control is materially weakened, and no unauthorised disclosure or significant privacy implication is introduced. The rationale, compensating control, duration, and review condition must be recorded.
2. **Material or policy-level exception:** Senior Management or the designated Executive Sponsor must approve institutional risk acceptance, material business disruption, significant security-control exceptions, or changes to this policy. Technical, business, and Privacy/Legal advisers must be consulted as relevant.
3. **Emergency exception:** The Incident Response Lead, or the constrained emergency authority defined above when the Lead cannot be reached promptly, may authorise proportionate protective action where waiting would materially increase harm. The record must state the urgency, action, authority, scope, evidence-preservation effect, business impact, notification, and retrospective management review deadline. An emergency exception does not automatically permit unsafe restoration, unrestricted access, or bypassing mandatory business acceptance.

An exception must be documented before action where practicable, or as soon as practicable after an emergency action. The record must state the risk, reason, decision owner, authority or delegation, affected systems or people, evidence-preservation impact, duration, compensating control, and review outcome.

Privacy, legal, contractual, safeguarding, and regulatory questions must be referred to the appropriate adviser. This policy does not assert a jurisdiction-specific notification deadline. Any formal notification decision must identify the relevant jurisdiction, duty, recipient, factual basis, approval, and deadline source before release.

## 8. Policy review and maintenance

The policy owner maintains the controlled master copy and proposes amendments. The approval authority must approve changes before publication. Review is required at least annually and after:

- a major or Critical incident;
- a tabletop exercise or other test;
- a significant change to identity, learning, storage, backup, communications, or monitoring services;
- a material change to staffing, suppliers, legal context, or organisational risk; or
- a post-incident review identifies a governance gap.

Published copies must identify the version, approval status, owner, and next review point. Superseded versions must be retained according to the approved records schedule and clearly marked as superseded.

## 9. Framework and source references

- **[A1]** ICDFA, *GRC105 Incident Response Planning Assignment*, pp. 1–6, especially Task 2 and the Task 2 marking criteria.
- **[S1]** ICDFA, *Incident Response Planning*, Week 20 teaching deck, slides 6–10 and 14–15. The four teaching stages are used as course-facing organisation only.
- **[N1]** NIST, *SP 800-61 Revision 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*, 2025. https://csrc.nist.gov/pubs/sp/800/61/r3/final
- **[N2]** NIST, *SP 800-86: Guide to Integrating Forensic Techniques into Incident Response*, 2006. https://csrc.nist.gov/pubs/sp/800/86/final
- **[C1]** CISA and partners, *#StopRansomware Guide*, 2023. https://www.cisa.gov/stopransomware/ransomware-guide

NIST SP 800-61r3 is treated as CSF 2.0-aligned guidance. The Week 20 Preparation, Detection and Analysis, Containment/Eradication/Recovery, and Post-Incident Activity stages are not attributed to Revision 3 as a standalone traditional lifecycle.
