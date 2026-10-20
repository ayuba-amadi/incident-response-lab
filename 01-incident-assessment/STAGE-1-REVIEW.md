# GRC105 Task 1 — Stage 1 Review

**Scope completed:** Evidence analysis and visual documentation for the fictional Northbridge Skills Institute scenario.
**Scope intentionally not completed:** Severity classification and the remaining Task 1 assessment requirements. No Task 2–6 work was changed.

## Files produced

| File | Purpose |
|---|---|
| data/evidence-analysis-register.csv | Traceable E01–E08 analytical register with direct observations, hypotheses, alternatives, questions, assets, CIA implications, planned verification, and limitations. |
| data/investigation-priorities.csv | Seven defensible investigation questions with evidence links, required checks, owners, decision value, scope/severity implications, and status. |
| analysis/incident-chronology.md | Day minus 1/Day 0 chronology, 08:45 WAT control point, relationship analysis, causation boundary, and uncertainty statements. |
| analysis/scenario-context-and-impact.md | Source-provided organisational, system, examination, staffing, backup, and coverage context separated from operational implications for later severity assessment. |
| analysis/observations-hypotheses-questions.md | Confirmed observations, working hypotheses, unresolved questions, alternative explanations, and evidence/procedure limitations. |
| diagrams/incident-timeline.mmd | Editable Mermaid timeline containing E01–E08 and the 08:45 response control point. |
| diagrams/investigation-relationships.mmd | Editable Mermaid relationship model for FIN-PC07, Microsoft 365 identity, svc_backup, FS01, BAK01, LMS01, and the unfamiliar cloud destination. |
| visuals/README.md | Records the five rendered SVG/PNG outputs, Mermaid CLI method, visual inspection results, and limitations. |
| exports/README.md | Points to the final visual exports and authoritative editable Mermaid sources. |
| deprecated-templates/timeline.csv | Preserved original empty timeline scaffold; not an authoritative deliverable. |
| deprecated-templates/investigation-priorities.csv | Preserved original empty investigation-priority scaffold; not an authoritative deliverable. |

The original empty scaffold CSVs were moved intact into deprecated-templates/ to avoid duplicate deliverable paths. The required Stage 1 deliverables above are the authoritative outputs in their requested subdirectories.

## Source references

- 01-source-materials/GRC105/ICDFA_GRC105_Incident_Response_Assignment_20_Percent.docx, especially the Northbridge scenario, initial evidence pack Table 2, Task 1 instructions, and submission/authoring constraints.
- 01-source-materials/GRC105/Incident-Response-Planning.pptx, Week 20 slides 4, 6, 9–13, and 16 for incident concepts, detection/correlation, evidence discipline, and the distinction between course teaching stages and evidence-based analysis.
- 00-project-management/requirements-traceability.csv for Task 1 mandatory checks and output boundary.
- README.md and 00-project-management/source-manifest.csv for repository working rules and source preservation.

## Requirement-to-artifact mapping

| Stage 1 requirement | Evidence in this delivery |
|---|---|
| Analyse E01–E08 using exact scenario facts | Evidence register; chronology; observation register |
| Preserve supplied timestamps and WAT | All register rows and chronology entries use Day minus 1/Day 0 plus WAT; E08 and the response control point are recorded at 08:45 WAT. |
| Separate observation, hypothesis, alternative, uncertainty | All three analytical files; dashed/solid legend in both diagrams |
| Record assets and CIA implications without overstating impact | Evidence register asset and CIA columns; observations register |
| Capture scenario-wide context needed for later severity assessment | analysis/scenario-context-and-impact.md |
| Provide planned verification without claiming completed work | Evidence register; investigation priorities, all marked Not Investigated |
| Provide at least five investigation questions | Seven rows in data/investigation-priorities.csv; ten unresolved questions in the analysis register |
| Visual incident timeline | diagrams/incident-timeline.mmd includes all E01–E08, Day distinction, timestamps, and response takeover |
| Visual investigative relationships | diagrams/investigation-relationships.mmd includes all required assets and observed/hypothetical legend |
| Preserve editable source | Both visuals are stored as Mermaid source; no generated image is presented as evidence |

## Evidence coverage

E01 through E08 each appear exactly once as a primary row in the evidence-analysis register, once in the chronology table, and once in the confirmed-observation table. The timeline diagram contains every evidence ID and a separate response control marker. The relationship diagram references each required asset, separates architecture/observations/hypotheses, and does not represent BAK01 as the confirmed destination of E05.

## Known uncertainties and assumptions

- The attachment in E01 may be relevant, but malicious code execution is not confirmed.
- E02 is an unfamiliar sign-in, not proof of account compromise.
- E03 is unusual svc_backup activity, not proof of attacker access.
- E04 records 1.2 GB transferred from FIN-PC07, not the content or presence of personal data.
- E05 records reported backup success, not restorability, integrity, or cleanliness.
- E06 is consistent with ransomware indicators, but malware execution path and family are unconfirmed.
- E07 shows learner-facing portal impact, not the cause or the extent of LMS01 damage.
- E08 shows an inaccessible FS01 contact list and unverified email trust; it does not establish the cause or email compromise.
- The diagrams use relationship lines for investigative triage. Dashed lines are hypotheses and are explicitly not causation; the relationship diagram now separates confirmed architecture, recorded observations, and hypotheses.
- Responsible role in the priorities register identifies the role that should lead the proposed check; it does not claim that the check has occurred.

## Missing evidence

The supplied pack does not include the original email/attachment, complete Microsoft 365 identity and mailbox audit data, source hosts or commands for svc_backup, endpoint process/file telemetry, cloud-destination ownership or object data, complete server/application/backup logs, forensic images, hashes, chain-of-custody records, or controlled restoration results. Data classification and legal/privacy conclusions are also not established by this stage.

## Visualization limitations

- SVG and PNG exports are now available in visuals/ and were rendered with the cached Mermaid CLI without installing dependencies. The investigation-relationships diagram has dense routing and should be inserted at full report width or in landscape orientation.
- The timeline is deliberately evidence-oriented and not to scale; spacing communicates sequence, not elapsed duration.
- Relationship arrows show confirmed architecture, recorded observations, or explicitly labelled hypotheses; they are not network paths, attacker movement, or causal proof.
- Color is supplementary only; labels, line styles, and the explicit legends carry the meaning for accessibility.

## Stage 2 follow-on items

1. Severity criteria and the provisional High classification are now in analysis/severity-classification.md and data/severity-criteria.csv.
2. CIA and asset impact assessments are now in analysis/cia-impact-assessment.md, data/cia-impact-matrix.csv, and data/asset-impact-register.csv.
3. Response priorities and reassessment triggers are now in analysis/response-prioritisation.md, data/response-priority-matrix.csv, and analysis/severity-reassessment-triggers.md.
4. The integrated Task 1 assessment and full Stage 2 mapping are in TASK-1-INTEGRATED-ASSESSMENT.md and STAGE-2-REVIEW.md.

## Verification and rendering results

The following checks were performed after creating the Stage 1 files:

- python3 tools/check_project.py — passed: source originals verified; 7 rubric sections tracked.
- CSV parsing and column-count check — passed for both new CSV files; UTF-8 decoding succeeded and all rows match their headers.
- Evidence coverage check — passed: E01–E08 are present in the register, chronology, observation table, and timeline source.
- Timestamp check — passed against the assignment brief: E01 Day minus 1 16:40 WAT; E02 Day 0 01:15 WAT; E03 01:35; E04 01:50; E05 02:00; E06 08:30; E07 08:40; E08 08:45; response control Day 0 08:45 WAT.
- Mermaid source inspection — passed structural review: both files contain balanced Mermaid flowchart structure, node/class declarations, relationship labels, and legends.
- Mermaid rendering — passed with cached Mermaid CLI version 12.0.0 via `npx --no-install --package @mermaid-js/mermaid-cli mmdc`; SVG and PNG outputs were generated for both Stage 1 diagrams.
- Visual inspection — passed: rendered PNGs were opened and checked for clipping, label overlap, hierarchy, contrast, evidence-ID legibility, and observation/hypothesis distinction. Relationship routing remains dense but labels are readable at full resolution.
- Git working tree review — performed with git status --short; changes remain confined to 03-task-01-incident-assessment/. No commit, push, deployment, or source-material modification was performed.

**Review status:** Stage 1 remediation was completed before the separate Stage 2 assessment. See STAGE-2-REVIEW.md for the current Task 1 review gate.
