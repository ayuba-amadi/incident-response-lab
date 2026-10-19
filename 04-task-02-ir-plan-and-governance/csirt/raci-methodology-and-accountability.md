# RACI Methodology and Accountability

**Status:** Task 2 Stage 2 draft — awaiting independent review  
**Related artifacts:** `../data/raci.csv`, `../data/authority-raci-crosswalk.csv`, and `../data/authority-consistency-matrix.csv`

## 1. Purpose

The RACI matrix translates the accepted Stage 1 authority model into operational responsibilities without changing decision rights. It identifies who performs an activity, who owns its outcome or decision, who must provide input, and who receives relevant information.

The matrix uses functional role IDs from `../data/csirt-role-register.csv`. It does not name employees or claim that external providers have been engaged.

## 2. Definitions

- **Responsible (R):** Performs or coordinates the activity. At least one R is required for each row.
- **Accountable (A):** Owns the outcome or decision and is answerable for the activity. Exactly one A is assigned per row.
- **Consulted (C):** Provides input before the activity or decision. Consultation does not transfer accountability.
- **Informed (I):** Receives relevant status or outcome information. Informed roles do not approve the activity unless separately assigned as A on another row.

The matrix keeps the A column separate from R, so a combined A/R assignment is not needed. A role may appear in more than one category only where the activity requires both execution and accountability; that occurrence is explained by the activity's governance basis.

## 3. Assignment criteria

Assignments follow these rules:

1. Match A to the approved decision authority or to the owner of a distinct execution gate.
2. Match R to the role with the competence and access to perform the work.
3. Use C for material technical, security, business, continuity, privacy, or communications input.
4. Use I for management, service, or stakeholder awareness without implying approval.
5. Separate normal containment from emergency containment.
6. Separate technical restoration, security validation, data-integrity verification, and business acceptance.
7. Keep institutional risk acceptance with Senior Management / Executive Sponsor.
8. Keep normal operational containment with the Incident Response Lead.
9. Keep technical execution with IT Operations within approved scope.

## 4. Authority and execution separation

The Incident Response Lead directs the incident and authorises normal containment. IT Operations executes approved technical work. The Security Analyst analyses evidence and validates security conditions but does not acquire disruptive authority through analysis alone. The BCC coordinates authorised continuity arrangements, while Senior Management retains material continuity activation and risk acceptance.

The RACI therefore avoids assigning the IT Operations Lead as accountable for normal containment, business acceptance, or security validation. It also avoids assigning the BCC authority to override containment or recovery gates.

## 5. Emergency decisions

Emergency containment is represented by a separate activity, `R07`. Its accountable role is IT Operations Lead for the constrained emergency authority only when the Incident Response Lead cannot be reached promptly and delay may materially worsen harm. A formally delegated senior IT/security authority may substitute, but the delegation must be recorded. The action remains minimum necessary, evidence-aware, notified, and subject to retrospective review.

This separate row prevents the emergency pathway from silently changing the normal containment authority in `R06`.

## 6. Deputisation and appointment

`R21` covers delegation of incident-response decisions by the Incident Response Lead within established authority. `R22` covers the distinct Senior Management / Executive Sponsor appointment of a replacement incident leader, acting incident director, or BCC deputy. The Incident Response Lead and BCC cannot self-appoint a management-designated deputy.

Delegations and appointments require scope, effective time, expiry or review, restrictions, approval/reference, notification, and revocation or replacement records. The decision-log template provides dedicated fields for these controls.

## 7. Multiple approval gates

The Stage 1 authority matrix identifies technical restoration work with security and business gates. The RACI decomposes this into:

- `R14` — technical restoration authorisation, accountable to IT Operations Lead;
- `R15` — security validation for recovery, accountable to Security Analyst;
- `R16` — data-integrity verification, accountable to IT Operations Lead;
- `R17` — business return-to-service acceptance, accountable to Business Service Owner; and
- `R20` — material or policy-level exception and institutional risk acceptance, accountable to Senior Management / Executive Sponsor.

No row assigns multiple Accountable roles. The decomposition does not remove any Stage 1 gate.

## 8. Role conflicts

The matrix should be read with `../data/duty-conflict-and-coverage-register.csv`. Examples include command competing with hands-on technical work, evidence preservation competing with disruptive containment, backup administration competing with integrity validation, and communications drafting competing with approval. Where a conflict occurs, the Incident Response Lead sequences work, records the tradeoff, assigns a deputy or requests external support.

## 9. Relationship to the 14-activity authority matrix

The crosswalk in `../data/authority-raci-crosswalk.csv` maps every Stage 1 authority activity to one or more RACI activities. One-to-many mappings are deliberate where an authority activity contains separate gates. The crosswalk records the relevant Accountable and Responsible roles and identifies any corrective issue rather than silently changing Stage 1 governance.

## 10. Review and maintenance

The Incident Response Lead owns operational review of the RACI. Senior Management approves changes affecting decision authority, risk acceptance, formal appointments, or material continuity. The RACI should be reviewed after a major incident, exercise, staffing change, significant system change, governance change, or identified duty conflict.

## 11. Sources and boundary

- ICDFA GRC105 Task 2 requirements and 20-mark rubric.
- Approved Stage 1 policy, governance plan, isolation procedure, documentation procedure, business-continuity plan, and 14-activity authority matrix.
- Week 20 teaching slides 10, 14, and 15.

This document does not create a Task 3 technical response playbook. Proposed Task 2 preparation improvements are recorded separately in `../readiness/preparation-improvements.md`.
