# Incident Documentation and Recordkeeping Procedure

**Document identifier:** NSI-IR-PROC-003
**Version:** 0.1
**Status:** Stage 1 draft — awaiting approval
**Owner:** Incident Response Lead — proposed role

## 1. Purpose

This procedure defines the minimum record needed to make Northbridge incident decisions traceable, preserve evidence references, support continuity and recovery decisions, and enable post-incident review. It does not claim that any record, acquisition, containment action, or restoration test has occurred.

## 2. Minimum incident record

Each declared or materially investigated incident must have a controlled situation record containing:

- Incident ID.
- Event date and time, with WAT where relevant.
- Reporting source.
- Reporter role.
- Description of the report or observation.
- Relevant evidence IDs, logs, records, or source references.
- Initial classification and subsequent severity changes.
- Affected or potentially affected assets.
- Observed impact, working hypothesis, unresolved questions, and assumptions.
- Decision taken or proposed.
- Decision owner.
- Required approval and approval status.
- Delegation/deputy, delegating authority, scope, start time WAT, expiry or review time WAT, justification, and approval/reference where authority is delegated.
- Action owner.
- Execution status: proposed, approved, in progress, completed, cancelled, or not applicable.
- Supporting evidence reference.
- Business impact and continuity consequence.
- Communication reference, audience, channel, and approval.
- Next review time, using WAT where relevant.
- Closure authorisation and unresolved follow-up actions.

The blank operational template is `../data/incident-decision-log-template.csv`. It contains headers only and must not be treated as a completed event log.

## 3. Recordkeeping controls

### Access restriction and confidentiality

Incident records are limited to the Incident Response Lead, authorised security and IT personnel, relevant management, affected service owners, and advisers with a legitimate need to know. Personal, learner, staff, credential, finance, or forensic information must be minimised in general communications and shared only through an approved channel.

### Integrity and version history

The controlled record must preserve the original entry, author, WAT timestamp, amendment reason, and version history. Corrections must be made as an additional dated entry or controlled revision; an original observation or decision must not be silently overwritten. If a central system is unavailable, an approved offline record may be used and reconciled into the controlled record when service is trustworthy.

### Decision traceability

Every material decision links to its decision owner, authority, evidence references, alternatives considered, expected security and business effects, approval, execution status, and next review point. A plan or recommendation must be labelled proposed; it must not be written as completed action.

### Delegation and deputy controls

Delegation must be recorded whenever the normal decision-maker is unavailable, assigns a defined decision to another role, or uses emergency authority. The Incident Response Lead may delegate within approved policy authority. Senior Management or the designated Executive Sponsor may appoint an incident director, deputy, or alternate Business Continuity Coordinator. The IT Operations Lead may assign technical execution but does not thereby delegate incident-direction authority.

Each delegation record must identify the delegating authority, receiving role, scope, start time in WAT, expiry or review time in WAT, justification, constraints, required approval/reference, and the person responsible for review. Delegation may not be passed onward unless the original authority or an expressly authorised management decision permits it. Delegation is revoked when the normal authority resumes, the expiry or review condition is reached, the incident scope changes materially, or the delegating authority withdraws it; revocation must be recorded.

Emergency delegation is limited to the minimum necessary protective action. The Incident Response Lead or designated deputy must be notified as soon as practicable, management must review material consequences retrospectively, and the record must identify any unavoidable evidence loss, business effect, follow-up decision, and deadline. No delegation authorises unsafe restoration, unrestricted system access, or bypassing business acceptance.

### Evidence references

Evidence IDs such as E01–E08, log identifiers, file references, ticket references, interview records, or planned collection identifiers must be used consistently. If evidence has not been collected, record “planned / not collected” rather than inventing a hash, custody event, acquisition time, or validation result.

### Retention responsibility

The Incident Response Lead is responsible for ensuring that the incident record is retained and transferred to the approved records owner at closure. The actual retention period must follow Northbridge's approved records schedule, contractual requirements, and applicable legal or privacy advice. No statutory retention period is asserted by this procedure.

## 4. Alternative documentation when normal systems are unavailable

If FS01, LMS01, Microsoft 365, the service desk, or the normal contact list is unavailable or untrusted:

1. Use an approved alternate channel or controlled offline record.
2. Record each entry with author, WAT timestamp, incident ID, and source.
3. Restrict access to the minimum response group.
4. Preserve the record and prevent casual alteration.
5. Reconcile the record into the controlled system after trust and availability are established.
6. Record the reconciliation time, person, differences, and any missing information.

Staff phones are available in the scenario, but their use for sensitive content remains subject to management-approved communication controls.

## 5. Review and closure

The Incident Response Lead reviews the record after declaration, after material evidence or impact changes, before restoration or service return, after closure approval, and during the post-incident review. Closure requires confirmation that immediate response decisions are recorded, unresolved risks and actions have owners, business and security acceptance are documented where applicable, communications are referenced, and the management or delegated closure authority has approved closure.

## 6. References

- [A1] GRC105 assignment, Task 2 documentation requirements and Task 3 evidence-register requirements.
- [S1] Week 20 teaching deck, slides 10, 13, and 14.
- [N1] NIST SP 800-61r3, official publication: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- [N2] NIST SP 800-86, official publication: https://csrc.nist.gov/pubs/sp/800/86/final
