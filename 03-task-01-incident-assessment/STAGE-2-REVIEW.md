# GRC105 Task 1 — Stage 2 Review

**Scope:** Severity classification, CIA assessment, asset impact, response prioritisation, and reassessment triggers.
**Assessment point:** 08:45 WAT on Day 0.
**Status:** Stage 2 complete; awaiting independent review. No severity work beyond this assessment and no Task 2–6 work was performed.

## Files created

| File | Purpose |
|---|---|
| analysis/severity-classification.md | Four-tier severity definitions and evidence-based High provisional classification. |
| analysis/cia-impact-assessment.md | Separate confidentiality, integrity, and availability analysis. |
| analysis/response-prioritisation.md | Immediate versus later response priorities, dependencies, and tradeoffs. |
| analysis/severity-reassessment-triggers.md | Conditions to increase, maintain, reduce severity, expand scope, or exclude assets from confirmed scope. |
| data/severity-criteria.csv | Reusable four-tier criteria register. |
| data/asset-impact-register.csv | Confirmed, potential, and investigation-only asset status register. |
| data/cia-impact-matrix.csv | Asset-by-property CIA matrix with evidence and verification requirements. |
| data/response-priority-matrix.csv | Evidence-linked response priority matrix with status fields. |
| diagrams/severity-decision-tree.mmd | Editable severity decision aid. |
| diagrams/cia-impact-visual.mmd | Editable CIA impact visual. |
| diagrams/response-priority-workflow.mmd | Editable priority workflow; not a Task 3 playbook. |
| TASK-1-INTEGRATED-ASSESSMENT.md | Consolidated Task 1 assessment that references Stage 1 without duplicating its full evidence tables. |

## Requirement-to-artifact mapping

| Task 1 rubric requirement | Supporting evidence |
|---|---|
| Four-tier severity definitions | analysis/severity-classification.md; data/severity-criteria.csv; diagrams/severity-decision-tree.mmd |
| Initial severity and justification | analysis/severity-classification.md; TASK-1-INTEGRATED-ASSESSMENT.md |
| E01–E08 timeline | Stage 1 analysis/incident-chronology.md; Stage 1 data/evidence-analysis-register.csv; Stage 1 diagrams/incident-timeline.mmd |
| Confirmed observations, hypotheses, unknowns | Stage 1 analysis/observations-hypotheses-questions.md; Stage 1 evidence register; integrated assessment |
| At least two alternative explanations | Stage 1 analysis/observations-hypotheses-questions.md |
| Confirmed and potentially affected assets | data/asset-impact-register.csv; TASK-1-INTEGRATED-ASSESSMENT.md |
| Confidentiality assessment | analysis/cia-impact-assessment.md; data/cia-impact-matrix.csv; diagrams/cia-impact-visual.mmd |
| Integrity assessment | analysis/cia-impact-assessment.md; data/cia-impact-matrix.csv; diagrams/cia-impact-visual.mmd |
| Availability assessment and examination deadline | analysis/scenario-context-and-impact.md; analysis/cia-impact-assessment.md; E07/E08 evidence; response priority matrix |
| At least three investigation questions and validation checks | Stage 1 data/investigation-priorities.csv; Stage 1 analysis/observations-hypotheses-questions.md |
| Examination and backup priorities | analysis/response-prioritisation.md; data/response-priority-matrix.csv; diagrams/response-priority-workflow.mmd |
| Conditions changing severity or scope | analysis/severity-reassessment-triggers.md |
| Traceable source use | Stage 1 source references; Week 20 slides 4, 6, 9–11; official NIST SP 800-61r3 reference in Stage 2 analysis and integrated assessment |

## Initial decision summary

The initial classification is **High — provisional**. The decision reflects observed learner-facing and shared-file availability impact, anomalous privileged access involving the recovery repository, the imminent examination, sensitive information holdings, limited staffing, and unverified recovery capability. It does not assert broad compromise, personal-data exfiltration, attacker identity, clean or compromised backups, or completed investigation.

## Validation results

- Original source integrity: passed via python3 tools/check_project.py.
- Original source materials: no modifications detected.
- E01–E08 preservation: Stage 1 evidence register and chronology remain unchanged; all eight IDs and timestamps remain present.
- CSV validation: new CSV files parse as UTF-8 with consistent column counts and non-empty required fields.
- Severity consistency: High criteria, initial rationale, CIA findings, asset statuses, priorities, and reassessment triggers use consistent qualitative language and avoid numeric false precision.
- Evidence linkage: every asset-impact and CIA row contains one or more E01–E08 references or explicit scenario context.
- Mermaid structural inspection: all five Task 1 diagrams contain flowchart declarations, balanced node delimiters, evidence labels, legends, and distinct confirmed/potential conventions.
- Rendered visual validation: passed with cached Mermaid CLI version 12.0.0 via `npx --no-install --package @mermaid-js/mermaid-cli mmdc`; all five SVG and PNG outputs were generated and visually inspected.
- Repository boundary: changes remain within 03-task-01-incident-assessment/.
- Git: no commit, push, or deployment performed.

## Remaining limitations

- The investigation-relationships diagram has dense relationship routing; full-width or landscape placement is recommended for Word insertion. No clipped text was observed during PNG inspection.
- The severity decision is provisional and must change if later evidence meets a reassessment trigger.
- No forensic acquisition, hash verification, account action, containment, restoration, notification, or examination-continuity decision has been completed.
- This workspace does not yet contain the later Task 2–6 deliverables.

## Readiness

Task 1 Stage 2 is complete and ready for independent review. The Task 1 workspace now contains the evidence analysis, initial severity classification, CIA assessment, affected-asset analysis, investigation priorities, response priorities, reassessment conditions, and integrated assessment. The work stops here pending review.
