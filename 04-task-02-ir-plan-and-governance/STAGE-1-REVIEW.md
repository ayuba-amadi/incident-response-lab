# GRC105 Task 2 — Stage 1 Review

## 1. Stage objective

Develop a concise, evidence-based incident response policy and governance plan for Northbridge Skills Institute, covering mission, scope, declaration, activation, escalation, isolation authority, documentation, review, and business continuity integration. This review covers governance only and does not award a final Task 2 mark.

**Status:** Stage 1 remediation complete — awaiting independent acceptance. Organisational approval is not claimed.

## 2. Artifacts created

| Artifact | Purpose |
|---|---|
| `policy/incident-response-policy.md` | Draft policy, mission, objectives, scope, principles, authority, exceptions, and review. |
| `plans/incident-response-governance-plan.md` | Declaration, activation, escalation, delegation, resource constraints, and external-support governance. |
| `plans/isolation-authority-and-emergency-decisions.md` | Governance-level isolation authority, emergency delegation, tradeoffs, and review. |
| `plans/incident-documentation-procedure.md` | Minimum incident records, access, integrity, versioning, retention responsibility, and alternate records. |
| `plans/business-continuity-integration.md` | Distinct IR, continuity, and recovery responsibilities; examination coordination and return authority. |
| `data/incident-decision-log-template.csv` | Headers-only editable decision-log template. |
| `data/authority-consistency-matrix.csv` | Reviewer-facing authority mapping for normal, emergency, continuity, and closure decisions. |
| `data/governance-requirements-matrix.csv` | Stage 1 coverage and staged Task 2 requirement mapping. |
| `diagrams/*.mmd` | Four editable governance diagrams. |
| `TASK-2-STAGE-1-GOVERNANCE-DRAFT.md` | Consolidated report-ready Stage 1 governance draft. |
| `visuals/` | SVG and PNG exports if successfully rendered and inspected. |

At the time of this Stage 1 review, the `raci.csv` scaffold was preserved and the final RACI was explicitly deferred to Stage 2. The current Stage 2 package now contains the completed proposed RACI.

## 3. Requirement coverage

| Stage 1 requirement | Status | Supporting artifact |
|---|---|---|
| Mission, objectives, and scope | PASS | Policy Sections 1–3; integrated draft Section 1 |
| Incident declaration and activation | PASS | Governance plan Section 3; declaration diagram |
| Severity-based escalation | PASS | Governance plan Section 4; severity workflow; Task 1 High position retained |
| Authority to isolate systems | PASS | Policy Section 5; isolation procedure and diagram |
| Emergency delegation and review | PASS | Isolation procedure Sections 3–6; documentation delegation controls |
| Documentation and recordkeeping | PASS | Documentation procedure; expanded CSV template |
| Plan review, approval, and maintenance | PASS | Policy Section 8; document control fields |
| Business continuity integration | PASS | Business continuity procedure, BCC definition, and coordination diagram |
| Evidence-linked Northbridge application | PASS | E01–E08 references and scenario limitations in plan and integrated draft |
| Complete six-role CSIRT | PARTIAL / deferred at Stage 1 | Functional roles were referenced; the detailed CSIRT structure is now supplied by Stage 2 |
| Final eight-activity RACI | DEFERRED at Stage 1 | The current Stage 2 package supplies the proposed RACI |
| Four readiness improvements | DEFERRED at Stage 1 | The current readiness register supplies four proposed improvements |

The full mapping is in `data/governance-requirements-matrix.csv`.

## 4. Governance decisions proposed

- The Incident Response Lead declares, directs, and authorises normal containment unless authority is formally delegated or management appoints another incident director.
- IT Operations executes approved technical actions; Security Analysis provides evidence and security recommendations; technical operators may not expand an approved scope.
- Routine operational deviations are approved by the Incident Response Lead within delegated authority; material or policy-level exceptions require Senior Management or the designated Executive Sponsor.
- Emergency containment may be authorised by the IT Operations Lead or formally delegated senior IT/security authority only when the Incident Response Lead cannot be reached promptly and delay may materially worsen harm; notification and retrospective review are mandatory.
- The Business Continuity Coordinator coordinates authorised arrangements, while Senior Management retains material continuity activation and institutional risk-acceptance authority. A management-assigned deputy or alternate is required.
- Business continuity and academic operations coordinate examination alternatives with incident response and management; they do not bypass security validation.
- Return to service requires technical availability, security validation, data integrity, and business acceptance.

## 5. Evidence references

The governance documents retain the approved Task 1 classification of **High — provisional at 08:45 WAT on Day 0**. They use E03, E04, E05, E06, E07, and E08 when explaining urgent governance decisions and retain the Task 1 limitations: no confirmed malicious execution, account compromise, attacker control, data contents, backup safety, malware family, or attacker identity.

## 6. Assumptions and limitations

- Role titles are proposed organisational arrangements, not named employees or evidence of additional staff.
- Northbridge has three IT personnel and one security analyst; external specialist support is proposed only subject to authorisation, availability, and arrangements.
- The contact list is inaccessible and corporate email trust is unverified. Staff phones are available for verified calls; a controlled independent contact list and secondary channel remain proposed readiness controls requiring approval.
- No legal jurisdiction, statutory notification deadline, contractual entitlement, response SLA, or retention period is asserted.
- No response action, forensic acquisition, restoration test, notification, or service return is claimed.

## 7. Internal authority consistency assessment

**PASS:** The policy, governance plan, isolation procedure, documentation procedure, continuity procedure, authority matrix, diagrams, and integrated draft consistently assign incident direction and normal containment authority to the Incident Response Lead; technical execution to IT Operations; analysis and security validation to the Security Analyst; continuity coordination to the Business Continuity Coordinator; business acceptance to the Business Service Owner; and material risk approval to Senior Management. Emergency authority is limited, documented, notified, and retrospectively reviewed.

## 8. Business continuity integration assessment

**PASS:** Incident response, business continuity, and disaster recovery are separated. The BCC coordinates authorised continuity arrangements, while management retains material activation and risk-acceptance authority. The 11:00 examination is addressed without assuming postponement, restoration, or safe backup use. Return to service is separated into technical availability, security validation, integrity, and business acceptance.

## 9. Visual rendering and inspection results

The four Mermaid sources are:

- `diagrams/incident-declaration-activation.mmd`
- `diagrams/severity-escalation-workflow.mmd`
- `diagrams/emergency-isolation-authority.mmd`
- `diagrams/ir-business-continuity-coordination.mmd`

**PASS:** All four sources were rendered with cached Mermaid CLI version 12.0.0 using `npx --no-install --package @mermaid-js/mermaid-cli mmdc`. SVG and PNG outputs are present in `visuals/`. Each PNG was opened and inspected for clipping, overlap, contrast, hierarchy, and legibility. No clipped text was observed. The declaration, severity, and isolation diagrams are tall; the continuity diagram is wide. Full-width or appropriately sized report placement is recommended.

## 10. Validation results

- Repository preflight: PASS — existing uncommitted Task 2 Stage 1 work was identified and preserved; no unexpected Task 1 or later-task changes were present.
- Source integrity: PASS — `python3 tools/check_project.py` verified original sources.
- Task 1 boundary: PASS — no Task 1 files modified.
- Task 3–6 boundary: PASS — no later-task files modified.
- CSV validation and Markdown relative-link review: PASS — UTF-8 CSVs parse with consistent column counts, the headers-only decision log contains no incident rows, the authority matrix contains 14 unique activity rows with one normal primary authority each, and local Markdown links resolve.
- Mermaid rendering and visual inspection: PASS — all four sources pass cached Mermaid CLI syntax validation; the two affected diagrams were re-rendered and inspected after remediation, and the unchanged exports remain present and previously inspected.
- Git commit/push: not performed and not authorised in this stage.

## 11. Remediation findings addressed

1. Exception approval is now divided into routine operational deviation, material or policy-level exception, and emergency exception with explicit authorities and review controls.
2. Normal containment is assigned to the Incident Response Lead; emergency containment is constrained to the documented unavailable-authority condition and minimum necessary action.
3. Delegation/deputy fields and delegation lifecycle controls were added to the decision log and documentation procedure.
4. The Business Continuity Coordinator, deputy/alternate arrangement, examination approval gate, and fallback communication controls were defined without inventing existing personnel or platforms.
5. The operational status model now distinguishes events, suspected incidents, validation, declaration, activation, escalation, recovery, and closure.
6. The previously identified combined delegation row was split into separate incident-response decision delegation and Senior Management / Executive Sponsor appointment activities. The matrix now contains 14 activity rows, each with one identifiable normal primary authority.

## 12. Unresolved issues

1. The organisation must approve the proposed policy owner, approval authority, deputy arrangements, and emergency delegation.
2. Northbridge must define the authorised alternate communication channel and its access controls.
3. The final CSIRT role structure, RACI, and readiness improvements remain to be designed in Stage 2.
4. Legal/privacy advisers must determine any applicable jurisdiction, contractual duties, or formal notification requirements if evidence later supports them.

## 13. Requirements deferred to Stages 2 and 3

- Task 2 Stage 2: complete CSIRT role structure, final RACI, readiness-improvement register, and review of resource assumptions.
- Task 3: technical response playbook, ordered containment, evidence custody execution, eradication, restoration criteria, and monitoring.
- Task 4: communication matrix and approved executive/learner messages.

## 14. Readiness for independent review

**PASS for targeted remediation — awaiting independent acceptance.** This record assesses the governance-only Stage 1 scope at the time it was produced. The later Stage 2 package now supplies the CSIRT, RACI, and readiness artifacts; independent acceptance and organisational approval remain outstanding.
