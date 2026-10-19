# Northbridge Skills Institute — Task 2 Stage 2 CSIRT and RACI Draft

**Status:** Task 2 Stage 2 draft — ready for independent review after validation  
**Scope:** CSIRT structure, staffing capacity, RACI accountability, authority crosswalk, and duty-conflict controls  
**Approved governance baseline:** Stage 1 authority model; High — provisional at 08:45 WAT on Day 0

No response action, forensic acquisition, external engagement, appointment, restoration, or investigation result is claimed.

## 1. Purpose and governance context

This Stage 2 package converts the accepted Stage 1 policy and 14-activity authority matrix into an operationally credible CSIRT and RACI. It preserves the Incident Response Lead's command and normal-containment authority, constrained emergency authority, Senior Management risk acceptance, BCC coordination role, and separate recovery gates.

The structure is functional rather than enterprise-scale. Northbridge has three IT personnel and one security analyst. Legal/privacy, communications, continuity, service-owner, and external specialist functions are proposed assignments or contingent support arrangements, not confirmed dedicated staff.

## 2. CSIRT organisational structure

The core CSIRT functions are:

1. Incident Response Lead / Incident Commander (`IRL-01`).
2. Security Analyst / Investigation Coordinator (`SEC-01`).
3. Digital Forensics and Evidence Custodian (`FOR-01`).
4. IT Operations and Recovery Lead (`OPS-01`).
5. Legal / Privacy Adviser (`LP-01`).
6. Stakeholder Communications Coordinator (`COM-01`).

Supporting governance and continuity interfaces are Senior Management / Executive Sponsor (`MGT-01`), Business Continuity Coordinator (`BCC-01`), Academic/Business Service Owner (`BSO-01`), and contingent Microsoft 365 and backup-provider interfaces.

See [csirt-organisation-and-command.md](csirt/csirt-organisation-and-command.md) and [csirt-organisational-structure.mmd](diagrams/csirt-organisational-structure.mmd).

## 3. Roles and responsibilities

The Incident Response Lead directs, declares, activates, escalates, authorises normal containment, and coordinates closure. The Security Analyst analyses evidence and performs security validation. The Digital Forensics function preserves evidence and provenance. IT Operations executes approved technical work. Legal/Privacy advises on data and reporting obligations. Communications prepares fact-bounded messages but does not approve its own external release.

Senior Management retains material risk acceptance, formal appointment, material exception, Critical, and continuity activation authority. The BCC coordinates authorised continuity arrangements. The Academic/Business Service Owner approves examination arrangements within parameters and accepts business service return after the technical and security gates are satisfied.

## 4. Internal capacity and staffing allocation

The proposed initial allocation is:

| Resource | Primary assignment | Main restriction |
|---|---|---|
| IT Staff 1 | IRL-01 | Does not perform simultaneous hands-on containment during command-critical decisions. |
| IT Staff 2 | OPS-01 | Does not expand scope or approve its own business return. |
| IT Staff 3 | Technical operator and proposed FOR-01 dual-hat | Evidence preservation and disruptive work must be sequenced or separately supervised. |
| Security Analyst 1 | SEC-01 | Analysis does not independently authorise disruptive action. |

The 11:00 examination, E08 communication constraint, E03 privileged activity, E04 transfer uncertainty, E05 backup uncertainty, and E06/E07 availability and integrity effects require deliberate sequencing. If capacity is exhausted, active-threat containment, evidence preservation, privileged-access protection, examination decision-making, and recovery safety take precedence over low-value review or improvement work.

See [staffing-capacity-and-support-model.md](csirt/staffing-capacity-and-support-model.md).

## 5. External support and escalation

The Incident Response Lead recommends external support when internal capacity, specialist skill, independence, or recovery confidence is insufficient. Senior Management authorises engagement, information sharing, extraordinary resources, and confidentiality arrangements. Potential support includes specialist forensics, malware analysis, Microsoft 365 identity assistance, backup recovery engineering, legal/privacy advice, and communications support.

No supplier, retainer, response time, or completed engagement is assumed. Evidence of engagement would be an approved work order, provider ticket, engagement letter, or equivalent controlled record.

## 6. RACI methodology

The RACI separates execution from decision ownership:

- R performs or coordinates the activity.
- A owns the outcome or decision; exactly one A is assigned per row.
- C provides required input.
- I receives status or outcome information.

Normal containment is R06 with `IRL-01` accountable. Emergency containment is separate in R07 with `OPS-01` accountable only under the constrained emergency authority. Technical restoration, security validation, data integrity, business acceptance, and management risk acceptance are separate rows.

The complete matrix is in [raci.csv](raci.csv). Explanatory rules are in [raci-methodology-and-accountability.md](csirt/raci-methodology-and-accountability.md).

## 7. RACI matrix summary

The matrix contains 22 activities, including all eight instructor-mandated activities:

- Detection and analysis.
- Containment and emergency containment.
- Evidence handling.
- Stakeholder communication.
- Assessment of reporting obligations.
- Restoration approval and its separate security, integrity, and business gates.
- Closure and review.

Additional rows cover declaration, activation, escalation, backup integrity, continuity activation, examination continuity, exceptions, delegation, and appointment of leadership or continuity deputies.

## 8. Authority consistency

The [authority-raci-crosswalk.csv](data/authority-raci-crosswalk.csv) maps all 14 Stage 1 authority activities to the RACI. The technical restoration authority is intentionally mapped to separate R14, R15, and R16 gates, with R17 for business acceptance and R20 for material institutional risk acceptance. No Stage 1 authority assignment is changed.

The crosswalk identifies the emergency containment substitution, delegation boundary, BCC limitation, and Senior Management appointment authority. The authority-consistency matrix remains the controlling source for governance authority.

## 9. Separation-of-duties risks

The duty-conflict register records conflicts involving command versus technical execution, evidence versus destructive containment, backup administration versus integrity validation, identity administration versus investigation, communications drafting versus approval, and recovery implementation versus business acceptance.

Mitigations rely on sequencing, explicit approval scope, independent consultation where available, deputies, controlled records, and external support requests. These are planning controls, not evidence that any conflict has occurred.

## 10. Visual exhibits

- [csirt-organisational-structure.mmd](diagrams/csirt-organisational-structure.mmd) — command, consultation, and contingent support relationships.
- [csirt-staffing-and-escalation.mmd](diagrams/csirt-staffing-and-escalation.mmd) — capacity, sequencing, and external escalation.
- [raci-accountability-workflow.mmd](diagrams/raci-accountability-workflow.mmd) — RACI decision path and emergency distinction.
- [recovery-approval-gates.mmd](diagrams/recovery-approval-gates.mmd) — technical, security, integrity, business, and management gates.

Rendered SVG and PNG exports are in `visuals/` after validation.

## 11. Sources and assumptions

- ICDFA GRC105 Incident Response Planning Assignment, Task 2 and 20-mark rubric.
- Week 20 teaching slides 8–11 and 14–15.
- Approved Task 1 integrated assessment and High — provisional severity classification.
- Approved Stage 1 policy, governance plan, isolation procedure, documentation procedure, business-continuity plan, and 14-activity authority matrix.
- NIST SP 800-61 Revision 3 as CSF 2.0-aligned guidance; course four-stage teaching model remains a course-facing organisation aid.

All staffing, deputy, external support, and role assignments are proposed unless identified as scenario-established. No personal names, investigation outcomes, or completed engagements are invented.

## 12. Preparation improvements

The readiness register is in [preparation-improvements.md](readiness/preparation-improvements.md). It covers four distinct improvements:

- Backup isolation, tested recoverability and integrity evidence.
- Independently accessible incident contacts and secure communication fallback.
- Server and endpoint monitoring coverage with alert ownership.
- Role-based training and tabletop exercise readiness.

Each improvement identifies the weakness, proposed control, accountable owner, required resources, priority and measurable readiness check. These are proposed improvements; implementation evidence is not claimed.

## 13. Remaining task boundaries

Task 3's technical response playbook, evidence register, eradication procedures and recovery acceptance workflow remain outside this Stage 2 governance package. No live action, forensic acquisition, restoration test or external engagement is claimed.
