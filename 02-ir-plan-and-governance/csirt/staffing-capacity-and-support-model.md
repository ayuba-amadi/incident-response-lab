# Northbridge Skills Institute — Staffing, Capacity and Support Model

**Status:** Task 2 Stage 2 draft — proposed planning model awaiting approval  
**Known internal capacity:** IT Staff 1, IT Staff 2, IT Staff 3, and Security Analyst 1  
**Scenario constraint:** Three IT personnel and one security analyst; no dedicated forensics, legal, communications, or external supplier is confirmed

## 1. Planning assumptions

The identifiers below are planning labels, not invented employee identities. The allocations are proposed and require management confirmation. The model preserves one person for command and decision logging while others perform approved technical or analytical work. It does not assume simultaneous dedicated teams.

The 08:45 WAT Day 0 position is High — provisional. The 11:00 examination, inaccessible FS01 contact list, unverified corporate email, possible privileged-account activity, uncertain BAK01 trust, and limited staffing are capacity drivers. Staff phones are available for verified calls; a secure alternate collaboration platform is not confirmed.

## 2. Initial internal allocation

| Planning resource | Proposed primary function | Additional proposed function | Capacity limitation and conflict control |
|---|---|---|---|
| **IT Staff 1** | Incident Response Lead / Incident Commander | Decision logging or technical coordination when command load permits | Should not be assigned hands-on containment at the same time as critical command, escalation, or continuity decisions. |
| **IT Staff 2** | IT Operations and Recovery Lead | Authorised technical execution for server, endpoint, identity, or backup work | Must not approve its own business return or expand containment scope. Becomes emergency authority only under the Stage 1 condition. |
| **IT Staff 3** | Technical operator and proposed Digital Forensics/Evidence Custodian | Backup or endpoint evidence support; communications logistics if assigned | Evidence preservation and disruptive containment must be sequenced or separately supervised. No assumption of forensic-specialist competence. |
| **Security Analyst 1** | Security Analyst / Investigation Coordinator | Security validation and severity analysis | Analysis and security validation must not be treated as authority to perform disruptive action. Capacity may require external support. |

These are proposed assignments. Management must approve the Incident Response Lead, deputies, dual-hatting, and any assignment of non-IT personnel to communications, continuity, legal/privacy, or service-owner functions.

## 3. Concurrent and sequenced work

### Work that may operate concurrently

- The Incident Response Lead can establish the situation record and coordinate decisions while the Security Analyst performs evidence triage.
- IT Staff 2 can perform approved technical dependency checks while IT Staff 3 preserves accessible records or performs a separately scoped technical action.
- The BCC and Academic/Business Service Owner can develop examination alternatives while security and IT assess whether LMS01/FS01 can safely remain available.
- Legal/Privacy and Communications functions can prepare advice and fact-bounded drafts while technical analysis continues, provided sensitive material is restricted.

### Work that should be sequenced

- Evidence preservation should precede disruptive containment where safely practicable; if delay increases harm, the Incident Response Lead records the tradeoff.
- BAK01 protection and backup-integrity validation should be separated from any restoration decision.
- Microsoft 365 identity administration should preserve sign-in, MFA, device, token, mailbox, and account-change records before protective changes where safely practicable.
- Technical restoration, security validation, data-integrity verification, and business acceptance are separate gates.
- Stakeholder communication drafting precedes Senior Management approval and release.

### Work deferred if capacity is exhausted

Low-value historical review, broad non-priority reporting, nonessential service changes, and improvement activities should be deferred until active threat assessment, evidence preservation, privileged-access protection, examination continuity, and safe recovery decisions are covered. Deferral is recorded; it is not treated as completion.

## 4. Dual-hatting assessment

| Dual-hat combination | Plausibility | Control required |
|---|---|---|
| IT Staff 1 as Incident Response Lead and decision recorder | Plausible initially | A separate person maintains the record when command demand increases; the Lead does not perform simultaneous hands-on containment. |
| IT Staff 2 as IT Operations Lead and technical executor | Plausible for bounded actions | A different authority approves normal containment; the operator records execution and cannot expand scope. |
| IT Staff 3 as technical operator and evidence custodian | Plausible with sequencing | Preserve evidence before disruptive work where safe; obtain external forensic support if evidence volume or complexity exceeds competence. |
| Security Analyst as investigation coordinator and recovery security validator | Plausible but capacity-sensitive | Do not treat analysis as containment authority; obtain specialist support if validation cannot be independent or timely. |
| BCC and Academic/Business Service Owner | May be assigned to one non-IT functional person only with management approval | Separate continuity coordination from management risk acceptance and security restrictions. |
| Communications Coordinator and Privacy/Legal Adviser | Should not be assumed to be one person | Privacy review and communications approval remain distinct where personal data or external notification is possible. |

## 5. Required support by operational need

| Operational need | Initial internal coverage | Capacity concern | Escalation or sequencing response |
|---|---|---|---|
| Incident command and coordination | IT Staff 1 / Incident Response Lead | Command competes with technical work and recordkeeping. | Assign deputy; keep the Lead out of routine hands-on execution during high-impact decisions. |
| Evidence preservation | IT Staff 3 proposed custodian with Security Analyst coordination | No dedicated forensic investigator is established. | Request specialist forensics when evidence may be lost, collection is complex, or independence is needed. |
| Endpoint containment | IT Staff 2 or IT Staff 3 under IR Lead approval | Two technical actions may compete with FS01/BAK01 priorities. | Sequence by active-threat and propagation risk; record deferred work. |
| Server investigation | IT Staff 2 with Security Analyst | FS01 affects LMS01 and the examination. | Consult the Business Service Owner and preserve server/application records before disruptive changes where safe. |
| Backup protection and validation | IT Staff 2, Security Analyst, proposed backup specialist | Backup administration and validation may conflict. | Separate technical access from validation; request backup recovery support if trust or recoverability remains uncertain. |
| Microsoft 365 investigation | Security Analyst with IT support and provider liaison | Provider records or identity expertise may be unavailable. | Preserve identity records; request cloud identity assistance subject to management approval. |
| Examination continuity | BCC, Academic/Business Service Owner, IR Lead, management | Security and academic decisions compete for scarce attention. | Run a joint decision path; do not reopen an unvalidated service solely because of the deadline. |
| Stakeholder communication | Proposed Communications Coordinator with BCC/BSO input | No dedicated communications team is confirmed; email is untrusted. | Use verified phone fallback; obtain management-approved alternate channel and external communications support if needed. |
| Decision logging | Incident Response Lead or delegated recordkeeper | Command load can cause incomplete records. | Assign a separate recordkeeper and use the controlled offline record if central systems are unavailable. |

## 6. External support triggers

External support is proposed and contingent. No supplier, retainer, response time, or completed engagement is assumed.

| Support type | Trigger | Requesting role | Approval authority | Expected contribution | Limitation and engagement evidence |
|---|---|---|---|---|---|
| Specialist digital forensics | Evidence volume, volatile-data risk, complex acquisition, lack of internal competence, or independence requirement | Incident Response Lead with Security Analyst | Senior Management / Executive Sponsor | Collection planning, forensic acquisition, analysis support, custody advice | Availability, confidentiality, scope, and engagement approval must be recorded; engagement letter or approved work order is evidence of engagement. |
| Malware analysis | Suspicious executable or attachment requires specialist analysis | Security Analyst | Senior Management through Incident Response Lead recommendation | Determine malware behaviour and indicators without assuming execution | Original samples and handling controls are required; no analysis result is currently available. |
| Cloud identity assistance | Microsoft 365 records, tokens, conditional-access data, or provider support exceed internal capability | Security Analyst / IT Operations Lead | Senior Management | Provider-side identity, mailbox, MFA, device, and audit-log support | Provider access and contract terms are unverified; support ticket or approved provider engagement is required. |
| Backup recovery support | BAK01 trust, recoverability, or application-consistency questions exceed internal capability | IT Operations Lead | Senior Management | Isolated backup validation and recovery engineering advice | Does not certify a backup clean; validation evidence and approved scope are required. |
| Legal/privacy advice | Potential personal-data disclosure, reporting obligation, contractual issue, or uncertain jurisdiction | Incident Response Lead | Senior Management | Legal/privacy assessment and notification advice | No statutory deadline or legal conclusion is assumed; advice must be recorded. |
| External communications support | Learner, staff, media, or stakeholder communication volume exceeds internal capacity | Communications Coordinator / BCC | Senior Management | Message preparation, channel coordination, learner-support assistance | Does not approve its own release; approved messages and engagement records are required. |

## 7. Deputies and unavailability

Management assigns an incident-leadership deputy and BCC deputy or alternate. The Incident Response Lead records any incident-decision delegation with scope, start time, expiry or review, restrictions, and revocation conditions. The deputy does not automatically inherit unrestricted authority. If the Lead cannot be reached and delay may materially worsen harm, IT Operations may use the constrained emergency authority defined in Stage 1, with notification and retrospective review.

If Security Analyst 1 is unavailable, analytical conclusions should be limited to available evidence and external support requested where material decisions depend on specialist analysis. If IT capacity is exhausted, the Incident Response Lead escalates to Senior Management, records the operational tradeoff, and prioritises active-threat containment, evidence preservation, privileged-access protection, examination continuity, and recovery safety.

## 8. Sources and boundaries

- Approved Stage 1 policy, governance plan, isolation procedure, documentation procedure, business-continuity plan, and authority-consistency matrix.
- Approved Task 1 High — provisional assessment at 08:45 WAT on Day 0.
- ICDFA GRC105 Task 2 requirements and Week 20 teaching slides 8–11 and 14–15.

Readiness improvements are documented separately in [preparation-improvements.md](../readiness/preparation-improvements.md). This staffing model does not itself create a Task 3 playbook or evidence register, does not establish an external engagement, and does not claim that any response action or investigation has occurred.
