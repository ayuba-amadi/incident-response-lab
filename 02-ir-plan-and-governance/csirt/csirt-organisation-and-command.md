# Northbridge Skills Institute — CSIRT Organisation and Command

**Status:** Task 2 Stage 2 draft — awaiting independent review and organisational approval  
**Scope:** Functional CSIRT design and command relationships; no response action is claimed  
**Planning point:** 08:45 WAT on Day 0; High — provisional remains the approved initial classification

## 1. Design principles

Northbridge needs a credible incident-response capability without assuming that six dedicated cybersecurity employees exist. The CSIRT is therefore a functional structure. Functions may be assigned to existing personnel, management-appointed business roles, or authorised external specialists. A role assignment is proposed unless identified as scenario-established.

The Incident Response Lead directs the incident and ordinarily authorises normal containment. Technical operators execute approved actions within scope. The Security Analyst provides evidence and security recommendations but does not acquire disruptive authority merely by identifying risk. Senior Management retains material risk-acceptance and appointment authority. These arrangements preserve the accepted Stage 1 governance model.

## 2. Command structure

### Senior Management / Executive Sponsor — governance authority

Senior Management provides institutional risk acceptance, approves material or policy-level exceptions, Critical decisions, extraordinary resources, material continuity activation, external commitments, and appointment of a replacement incident leader or continuity deputy. This is a governance authority, not a claim that a named executive or dedicated crisis office exists.

### Incident Response Lead / Incident Commander — command authority

**Purpose:** Direct the response, maintain the incident decision record, and coordinate security, technical, business, continuity, privacy, and communications functions.

**Responsibilities:** Declare and activate incidents; assign severity; authorise normal containment; coordinate emergency review; allocate scarce personnel; escalate to Senior Management; approve routine operational deviations; and recommend closure.

**Execution and authority:** Owns incident direction and decision traceability. Does not personally perform every technical action. May delegate defined incident-response decisions within approved authority, with scope, duration, restrictions, and review recorded.

**Reporting:** Reports material risk, High/Critical changes, continuity decisions, and unresolved constraints to Senior Management.

**Skills and staffing:** Incident coordination, risk-based decision-making, evidence-aware leadership, and service-impact assessment. Proposed assignment from the IT team; a deputy or management-appointed incident director is required if unavailable.

**Restrictions:** Cannot appoint a Senior Management-designated replacement or BCC deputy independently; cannot bypass security validation or business acceptance.

**Key deliverables:** Situation record, decisions, severity reassessments, authority/delegation records, escalation recommendations, and closure package.

### Security Analyst / Investigation Coordinator — core CSIRT function

**Purpose:** Coordinate detection and analysis, explain uncertainty, assess security implications, and provide recovery security validation.

**Responsibilities:** Triage security reports; correlate identity, endpoint, server, network, cloud, backup, and application information; maintain hypotheses and questions; advise on severity; coordinate scope validation; and assess whether recovery conditions are security-acceptable.

**Execution and authority:** Performs analysis and approved technical checks. Does not independently authorise disruptive containment or declare a clean system without evidence.

**Reporting:** Reports evidence, uncertainty, and recommendations to the Incident Response Lead; consults the Digital Forensics function and IT Operations.

**Skills and staffing:** Security monitoring, incident analysis, identity and cloud investigation, log interpretation, and clear technical reporting. One security analyst is scenario-established; specialist support is required if analysis capacity or expertise is insufficient.

**Restrictions:** No attacker attribution, compromise finding, or data-disclosure conclusion without evidence.

**Key deliverables:** Analysis notes, evidence-linked scope assessment, severity inputs, security validation statement, and unresolved-question register.

### Digital Forensics and Evidence Custodian — core CSIRT function

**Purpose:** Preserve relevant evidence and maintain traceable evidence references without claiming that acquisition or hashing has occurred.

**Responsibilities:** Identify high-value evidence; coordinate collection planning; preserve original records; maintain evidence references and custody documentation; advise on evidence-preservation tradeoffs; and coordinate external forensic collection when required.

**Execution and authority:** Performs authorised preservation and collection tasks within competence. Does not expand containment scope or approve restoration.

**Reporting:** Reports evidence status and loss risks to the Incident Response Lead and Security Analyst.

**Skills and staffing:** Evidence handling, secure storage, time-zone-aware records, chain-of-custody principles, and forensic tool competence. Proposed dual-hat assignment from IT Staff 3 or an authorised external specialist; a dedicated internal forensic investigator is not scenario-established.

**Restrictions:** No invented hashes, custody events, acquisition times, or forensic findings.

**Key deliverables:** Evidence plan, collection status, provenance references, preservation warnings, and custody records when collection is authorised.

### IT Operations and Recovery Lead — core CSIRT function

**Purpose:** Provide technical dependency knowledge and execute approved containment, restoration, identity, server, endpoint, and backup actions.

**Responsibilities:** Assign technical operators; assess FS01/LMS01 dependencies; protect BAK01 and privileged access; perform approved isolation; support Microsoft 365 and endpoint checks; validate technical restoration; and report execution status.

**Execution and authority:** Owns technical execution within approved scope. May authorise narrowly scoped emergency containment only under the Stage 1 unavailable-authority condition; this does not create unlimited isolation or restoration authority.

**Reporting:** Reports execution status, dependency risks, and technical recovery conditions to the Incident Response Lead.

**Skills and staffing:** Windows/server, endpoint, identity, backup, network, and service-dependency administration. Proposed assignment from IT Staff 2; IT Staff 3 is the alternate where capacity permits.

**Restrictions:** Must not independently expand an approved action, certify security cleanliness, or accept business service risk.

**Key deliverables:** Technical impact assessment, execution records, dependency assessment, restoration readiness input, and recovery verification evidence.

### Legal / Privacy Adviser — advisory CSIRT function

**Purpose:** Advise on information classification, privacy, contractual, legal, safeguarding, and reporting-obligation questions.

**Responsibilities:** Assess possible personal-data implications; advise on notification decision inputs; review proposed disclosures and external communications; identify jurisdiction or contractual questions; and document advice and uncertainty.

**Execution and authority:** Provides advice and does not determine technical scope. Formal risk acceptance and external communication approval remain with the authorities defined in Stage 1 governance.

**Reporting:** Advises the Incident Response Lead and Senior Management; works with the Communications Coordinator where sensitive information may be disclosed.

**Skills and staffing:** Privacy, legal, records, contractual, and regulatory analysis. No full-time legal department is scenario-established. Management must obtain internal advice or authorise external counsel when needed.

**Restrictions:** Must not invent a statutory deadline, confirm disclosure without evidence, or release a notification independently.

**Key deliverables:** Advice record, reporting-obligation assessment, disclosure constraints, and unresolved legal/privacy questions.

### Stakeholder Communications Coordinator — communications function

**Purpose:** Prepare and coordinate accurate internal and external communications through approved channels.

**Responsibilities:** Maintain an approved stakeholder list, draft fact-bounded messages, coordinate learner/staff updates, record channel and approval, and support communications when email trust is unverified.

**Execution and authority:** Prepares and coordinates messages. Senior Management approves external communications; the Coordinator does not release unapproved statements.

**Reporting:** Reports to the Incident Response Lead for incident facts and to Senior Management for approval of material communications.

**Skills and staffing:** Clear writing, audience management, privacy-aware handling, and alternate-channel coordination. A dedicated communications employee is not scenario-established; management may assign a non-IT staff member or authorise external support.

**Restrictions:** No speculation, unsupported attribution, sensitive forensic detail over an unverified channel, or independent external release.

**Key deliverables:** Draft messages, communication log, approval references, stakeholder coordination record, and channel-use record.

## 3. Supporting governance and continuity interfaces

| Function | Relationship to CSIRT | Authority boundary |
|---|---|---|
| Business Continuity Coordinator | Coordinates authorised continuity arrangements and low-risk preparations within written delegation. | Cannot override containment, security validation, technical recovery gates, or management risk acceptance. |
| Academic/Business Service Owner | Defines service impact and approves examination delivery arrangements within approved parameters. | Does not waive security restrictions or accept technical recovery risk without the required management gate. |
| Senior Management / Executive Sponsor | Approves material risk, Critical decisions, material exceptions, continuity activation, and formal appointments. | Does not perform technical execution by virtue of approval. |
| Microsoft 365 or identity provider liaison | Contingent technical interface for identity, mailbox, MFA, token, and provider records. | No provider engagement is assumed; management approval and availability are required. |
| Backup or recovery specialist/provider | Contingent specialist support for BAK01 validation and recovery engineering. | No clean or restorable backup is assumed; restoration remains subject to security and business gates. |

## 4. Command and consultation relationships

- **Command:** Senior Management appoints or oversees the Incident Response Lead; the Incident Response Lead directs the incident; IT Operations executes approved technical work.
- **Security analysis:** The Security Analyst advises the Incident Response Lead and coordinates with forensics and IT Operations.
- **Evidence:** The Digital Forensics and Evidence Custodian preserves evidence and reports tradeoffs; this function does not authorise disruptive action.
- **Continuity:** The BCC and Business Service Owner coordinate service options; Senior Management retains material risk acceptance; the Incident Response Lead defines security restrictions.
- **External support:** The Incident Response Lead recommends specialist support; Senior Management authorises engagement and information sharing.
- **Deputies:** Management assigns the incident-leadership and BCC deputy arrangements. The Incident Response Lead records response-decision delegation; delegation cannot be silently passed onward.

## 5. Northbridge staffing interpretation

The six core functions are not six employees. The initial model uses the three IT staff and one Security Analyst, with proposed non-IT support and contingent external specialists. Dual-hatting is acceptable only where it does not combine incompatible decision, evidence, execution, or acceptance duties. The capacity limits and sequencing are defined in [staffing-capacity-and-support-model.md](staffing-capacity-and-support-model.md).

## 6. Sources and boundaries

- [A1] ICDFA GRC105 Incident Response Planning Assignment, Task 2 and 20-mark rubric.
- [S1] Week 20 teaching presentation, slides 8–11 and 14–15.
- [G1] Approved Stage 1 policy, governance plan, authority-consistency matrix, documentation procedure, and business-continuity plan.
- [N1] NIST SP 800-61 Revision 3, CSF 2.0-aligned incident-response guidance.

This document does not create a Task 3 technical response playbook, tabletop result, forensic finding, or confirmed external engagement. Proposed preparation improvements are recorded separately in `../readiness/preparation-improvements.md`.
