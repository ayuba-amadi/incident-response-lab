# ICDFA GRC105 — Incident Response Planning & Ransomware Response Simulation

**Project status:** Task 1 is completed and committed at `506b89b`. Tasks 2–6 are drafted and validation-checked, awaiting final independent acceptance and the final Git checkpoint. The final Word document has not been assembled.

## Purpose and submission boundary
A single, auditable workspace for the **GRC105 Week 20 individual assessment**. It supports evidence-grounded incident assessment, policy and CSIRT design, a ransomware response playbook, communications, a simulated tabletop, and a critical case study. All fictional Northbridge material must remain explicitly labelled as scenario/simulation content. **No real-world ransomware or live forensic acquisition is needed.**

**Official submission:** One Word document uploaded to ICDFA E-Campus named `GRC105_IRP_Assignment_StudentID.docx`. Figures, CSVs, Mermaid diagrams and project records are **working artifacts** to be embedded or summarized in that document as needed, **not additional required submissions**.

## Repository navigation

| Folder | Purpose |
|---|---|
| `00-project-management/` | Master requirements, checkpoints, traceability, decisions |
| `01-source-materials/GRC105/` | Original GRC105 assignment and teaching deck (unaltered) |
| `01-source-materials/GRC205-deferred/` | Related course material, **out of scope until separately authorized** |
| `02-research-and-references/` | Authoritative reference register, citations and source verification |
| `03-task-01-incident-assessment/` | E01–E08 timeline, incident severity, CIA and investigation priorities |
| `04-task-02-ir-plan-and-governance/` | IR policy, CSIRT, RACI, readiness actions |
| `05-task-03-response-playbook/` | Sequenced response, evidence custody, restoration criteria |
| `06-task-04-communications/` | Stakeholder matrix, briefings and learner notice |
| `07-task-05-tabletop-simulation/` | 60-minute exercise, injects, simulated decisions, improvements |
| `08-task-06-case-study/` | Healthcare case study (slide 16), critical reflection |
| `09-cross-task-assets/` | Shared editable visuals and templates |
| `10-final-submission/` | Final consolidated DOCX only after approvals |
| `tools/` | Repository validation scripts |

## Current completion state

- **Task 1:** Completed and committed at `506b89b`; approved Task 1 artifacts remain unchanged.
- **Tasks 2–6:** Drafted, validated and awaiting final independent acceptance and a final Git checkpoint; no organisational approval or live operational execution is claimed.
- **Final DOCX:** Not yet assembled. The required filename is `GRC105_IRP_Assignment_StudentID.docx`.
- **Original training materials:** Preserved and verified unchanged.
- **Editable diagrams:** Mermaid source files remain in the relevant task `diagrams/` directories.
- **Rendered visuals:** SVG and PNG exports remain in the relevant task `visuals/` directories.

## Working rules

1. Proceed **one task at a time**; review and approve each task before advancing.
2. Do not change the source documents. Maintain hashes and source provenance.
3. All conclusions must distinguish **observed evidence, hypotheses, unknowns, and assumptions**. Cite E01–E08 in relevant decisions.
4. Planned forensic activities must be labelled **planned / not collected**; do not fabricate hashes, custody events, restoration test results, or threat attribution.
5. Use **visual-first**, accessible documentation: editable Mermaid diagrams, clear matrices, timelines, decision trees and charts; include explanatory text and source attribution.
6. Do not confuse illustrative teaching stages with the current NIST SP 800-61r3 / CSF 2.0 alignment (the assignment explicitly flags this).
7. Keep simulated tabletop results separate from observed scenario evidence.
8. Follow the assignment rubric and word limits exactly; cite the slides and at least two authoritative sources.
9. Make final decisions, assumptions, and AI assistance transparent; ensure the student can explain and validate the output.

## First action
Review `00-project-management/requirements-traceability.csv` and begin **Task 1**, using the untouched evidence pack on page 2 of the assignment. Record a review decision in `00-project-management/review-gates.md` before Task 2.

## On your Ubuntu machine
```bash
unzip grc105-incident-response-lab.zip
cd grc105-incident-response-lab
git status
python3 tools/check_project.py
```

The downloaded ZIP includes a local Git repository in the working directory. No GitHub remote or push is configured. This working copy must not be reinitialised or committed during the current review stage.
