# Task 2 Stage 2 — CSIRT and RACI Review Record

**Status:** Stage 2 draft complete — awaiting independent review and organisational approval  
**Scope:** CSIRT structure, staffing capacity, RACI accountability, authority crosswalk, duty-conflict controls, and supporting visuals  
**Boundary:** Readiness improvements are documented as proposed controls; implementation evidence and Task 3 technical playbooks are deferred

## 1. Stage objective

This stage translates the accepted Stage 1 governance model into a functional CSIRT structure and an accountable RACI. The package preserves the approved Incident Response Lead command model, normal and constrained emergency containment authorities, Senior Management risk acceptance, Business Continuity Coordinator limits, and separate recovery approval gates.

No appointment, external engagement, forensic acquisition, restoration, or incident action is claimed as completed.

## 2. Files created and modified

### Created for Stage 2

- `csirt/csirt-organisation-and-command.md`
- `csirt/staffing-capacity-and-support-model.md`
- `csirt/raci-methodology-and-accountability.md`
- `data/csirt-role-register.csv`
- `data/authority-raci-crosswalk.csv`
- `data/duty-conflict-and-coverage-register.csv`
- `diagrams/csirt-organisational-structure.mmd`
- `diagrams/csirt-staffing-and-escalation.mmd`
- `diagrams/raci-accountability-workflow.mmd`
- `diagrams/recovery-approval-gates.mmd`
- `visuals/csirt-organisational-structure.svg` and `.png`
- `visuals/csirt-staffing-and-escalation.svg` and `.png`
- `visuals/raci-accountability-workflow.svg` and `.png`
- `visuals/recovery-approval-gates.svg` and `.png`
- `TASK-2-STAGE-2-CSIRT-RACI-DRAFT.md`
- `readiness/preparation-improvements.md`

### Updated within the Task 2 workspace

- `README.md` — records Stage 2 progress and the Stage 3 boundary.
- `raci.csv` — replaces the header-only scaffold with the Stage 2 matrix.
- `data/governance-requirements-matrix.csv` — records Stage 2 coverage and updates the CSIRT/RACI rows.
- `visuals/README.md` — records all eight Task 2 visual source/export sets and inspection results.
- `data/governance-requirements-matrix.csv` — records the four preparation improvements as Task 2 coverage.

Stage 1 policy, plans, and approved Task 1 files were not modified for this stage.

## 3. CSIRT role count and coverage — PASS

The role register contains 11 functional entries, including six core CSIRT functions required by the assignment:

1. Incident Response Lead / Incident Commander.
2. Security Analyst / Investigation Coordinator.
3. Digital Forensics and Evidence Custodian.
4. IT Operations and Recovery Lead.
5. Legal / Privacy Adviser.
6. Stakeholder Communications Coordinator.

Senior Management, the Business Continuity Coordinator, the Academic/Business Service Owner, and contingent Microsoft 365 and backup-provider interfaces are separated as governance, continuity, or external-support functions. The documents state that these are functional assignments and do not imply six dedicated cybersecurity employees.

## 4. Internal capacity and external support — PASS with operational limitations

The proposed staffing model uses the scenario-established resources as planning identifiers:

- IT Staff 1 — proposed Incident Response Lead.
- IT Staff 2 — proposed IT Operations and Recovery Lead.
- IT Staff 3 — technical operator and proposed evidence/forensics dual-hat.
- Security Analyst 1 — Security Analyst / Investigation Coordinator.

The model identifies concurrent work, sequencing requirements, incompatible dual-hatting risks, deputies, capacity exhaustion, and deferred low-priority work. It explicitly addresses the 11:00 examination, FS01/LMS01 dependency, E08 communication constraints, privileged-account concerns, BAK01 uncertainty, and the lack of dedicated forensic, legal, communications, or confirmed external personnel.

External support triggers cover specialist forensics, malware analysis, Microsoft 365 identity assistance, backup recovery support, legal/privacy advice, and communications support. Engagements remain proposed and require management approval; no supplier or retainer is treated as available.

## 5. RACI activity count and coverage — PASS

The matrix contains 22 activities and includes all eight instructor-mandated functions through explicit activity rows:

- Detection.
- Analysis.
- Normal containment, with emergency containment separated in R07.
- Evidence handling.
- Stakeholder communication preparation and coordination.
- Assessment of reporting obligations.
- Technical restoration authorisation, with separate security, integrity, and business gates.
- Closure and post-incident review.

Additional rows cover declaration, activation, severity escalation, backup integrity validation, continuity activation, examination continuity, exceptions, delegation, and appointment of incident leadership or a continuity deputy.

## 6. Single-accountability validation — PASS

The standard-library CSV validation confirmed:

- 22 unique activity IDs.
- Exactly one non-blank Accountable role ID on every row.
- At least one Responsible role ID on every row.
- All Responsible, Accountable, Consulted, and Informed identifiers resolve to the role register.
- Combined A/R is represented by separate columns; no ambiguous combined cell is required.

The RACI keeps decision authority distinct from technical execution. R06 preserves Incident Response Lead authority for normal containment; R07 is the constrained emergency-authorisation activity. R14–R17 separate technical restoration, security validation, data-integrity verification, and business acceptance. R20 preserves Senior Management accountability for material institutional risk acceptance.

## 7. Fourteen-activity authority crosswalk — PASS

All 14 Stage 1 authority activities are represented in the crosswalk. There are 16 mapping rows because technical restoration authority is deliberately decomposed into separate technical, security-validation, and data-integrity gates. Business acceptance is represented separately.

The crosswalk confirms:

- Normal containment remains accountable to `IRL-01` and executed by `OPS-01`.
- Emergency containment is constrained to `OPS-01` only when the approved emergency condition applies.
- Routine deviations remain with `IRL-01`; material exceptions remain with `MGT-01`.
- Incident-response delegation remains with `IRL-01`; formal appointment of replacement leadership or a continuity deputy remains with `MGT-01`.
- BCC coordination does not replace Senior Management risk acceptance.
- Technical, security, integrity, and business recovery gates are not collapsed.

No Stage 1 authority assignment was changed.

## 8. Role conflicts and mitigation — PASS with residual constraints

The duty-conflict register covers:

- Incident command versus hands-on technical execution.
- Evidence preservation versus destructive containment.
- Backup administration versus backup-integrity validation.
- Cloud account administration versus compromise investigation.
- Communications drafting versus message approval.
- Recovery implementation versus business acceptance.
- Examination continuity coordination versus security containment.

Controls are planning measures: sequencing, scoped authorisation, consultation, deputies, controlled records, and external support requests. They do not claim that a conflict has occurred or that specialist support is engaged.

Residual limitations remain because Northbridge has only three IT staff and one security analyst, the contact list on FS01 is inaccessible, corporate email trust is unverified, and specialist capability is not confirmed.

## 9. Diagram rendering and inspection — PASS

The four Stage 2 Mermaid sources rendered with cached Mermaid CLI v12.0.0 using `npx --no-install --package @mermaid-js/mermaid-cli mmdc`.

- SVG and PNG exports exist and are non-empty for all four sources.
- Mermaid CLI completed without syntax errors.
- The PNG exports were opened and inspected.
- No clipping or overlapping labels was observed.
- Role identifiers, proposed-role qualifiers, emergency distinctions, and recovery-gate labels remain legible.
- The organisational diagram distinguishes command, consultation/coordination, and contingent external support.
- The staffing diagram distinguishes known internal capacity, proposed allocations, escalation, and deferral.
- The RACI diagram shows one accountable decision owner and a separate emergency branch.
- The recovery diagram does not treat technical restoration as automatic business acceptance.

Presentation limitations: the staffing diagram is tall and the recovery-gates diagram is wide. They should be placed at an appropriate report width or on landscape pages. This is a layout consideration, not a substantive governance defect.

## 10. Source and evidence preservation — PASS

`python3 tools/check_project.py` passed with `Source originals verified.` and `7 rubric sections tracked.` The approved Task 1 directory and later-task directories have no working-tree changes. The Stage 2 documents preserve the approved High — provisional classification at 08:45 WAT on Day 0 and do not convert E01–E08 hypotheses or limitations into findings.

## 11. Requirements status

| Requirement | Status | Basis |
|---|---|---|
| At least six CSIRT roles covering required functions | PASS | Role register and CSIRT organisation document |
| Small-team capacity and additional-support model | PASS | Staffing model and duty-conflict register |
| At least eight RACI activities | PASS | 22-row `raci.csv` |
| Exactly one Accountable and at least one Responsible per activity | PASS | Standard-library validation and methodology |
| At least four preparation improvements with owner, resources and measurable check | PASS | `readiness/preparation-improvements.md` contains four proposed improvement records |
| Stage 1 authority preserved and crosswalked | PASS | Authority crosswalk and manual review |
| Implementation of readiness improvements | DEFERRED | Controls are proposed; deployment and testing evidence are not claimed |
| Task 3 technical response playbook | DEFERRED at Stage 2 | Explicitly outside this stage; the current Task 3 playbook is maintained separately |
| Independent acceptance and organisational approval | NOT VERIFIED | Requires a later reviewer and authorised approver |

## 12. Validation command results

- `python3 tools/check_project.py` — PASS.
- `git diff --check` — PASS.
- Standard-library CSV validation — PASS for all Task 2 CSVs.
- RACI validation — PASS: 22 activities, unique IDs, one A, at least one R, known role IDs.
- Authority crosswalk validation — PASS: all 14 authority activities represented across 16 mappings.
- Decision-log template check — PASS: header-only.
- Mermaid CLI v12.0.0 rendering — PASS for four Stage 2 diagrams in SVG and PNG.
- PNG visual inspection — PASS, with documented sizing limitations.
- Git scope check — PASS: current changes are confined to `04-task-02-ir-plan-and-governance/`.

## 13. Known limitations

- Proposed role assignments and deputies require management confirmation.
- External providers, retainers, secure alternate platforms, and legal/privacy availability are not confirmed.
- The RACI expresses governance intent; it is not evidence that any response action has been executed.
- Visual exports are report-ready but may require landscape placement or scaling.
- Readiness controls are documented, but implementation and test evidence remain outstanding.

## 14. Readiness for independent review

**PASS — Task 2 package is ready for independent review.** This is not an organisational approval or an official course grade. Implementation evidence for the proposed readiness controls and Task 3 remain deferred.
