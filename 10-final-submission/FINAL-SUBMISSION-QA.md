# Final submission QA

## Build outputs

- Final DOCX: [`GRC105_IRP_Assignment_2025-GCR-12684.docx`](../GRC105_IRP_Assignment_2025-GCR-12684.docx)
- File size: 181,602 bytes; non-zero and readable by LibreOffice.
- SHA-256: `b359153b3a1aa298ac016263a8837be12b218cbd959c294f19c4af21c19b926e`
- PDF used for visual QA: `qa/GRC105_IRP_Assignment_2025-GCR-12684.pdf`
- Previous rendered page count: **88**.
- New rendered page count: **60**.
- Page size: A4 (`595.304 x 841.89 pt`).
- Page orientation: **60 portrait pages; 0 landscape pages**. Wide registers were split into logically related keyed tables instead of being compressed into landscape pages.

## Content and word-count checks

- Tasks 1–6 appear in the required order.
- Contents references verified after the final render: Task 1 p. 3; Task 2 p. 21; Task 3 p. 39; Task 4 p. 49; Task 5 p. 53; Task 6 p. 59; References p. 59; AI acknowledgement p. 60.
- E01–E08, the provisional High classification at 08:45 WAT, the 22-activity RACI, canonical Task 3 registers, and canonical Task 5 registers are represented.
- Narrative word count: **918 words**, calculated from the generated Markdown after excluding tables, references and appendices.
- Executive briefing: **196 words**; required range 150–200.
- Learner notice: **147 words**; required range 100–150.
- Task 6 case study: **387 words**; required range 300–400.
- Student metadata, references and AI-assistance acknowledgement are present.

## Table and figure inspection

- Word tables: **40**, including the cover table, source-content tables and all split register tables.
- Embedded report figures: **2**; six monochrome SVG/PNG report exports are retained under `figures/` with editable report-only copies under `figures/sources/`.
- Corrected wide-table groups: **10** register families — evidence analysis, asset impact, investigation priorities, RACI, CSIRT role register, response actions, evidence register, stakeholder communication, tabletop decisions and corrective actions.
- Wide registers are split by stable identifiers and related fields; all source fields and records are preserved.
- Table text uses a 10-point Compact style; narrative remains Times New Roman 12-point with the report’s paragraph spacing.
- Header rows repeat using `w:tblHeader`; all table rows carry `w:cantSplit`. XML validation found 40 repeating header rows and 431 non-splitting row controls.
- Complete rendered-page review found no table row split across pages, no character-by-character table wrapping, no clipped table text, and no orphan generated register caption after the keep-with-next correction.
- Visible captions are present immediately below both embedded figures: Figure 1 — Initial severity decision logic; Figure 2 — Proposed CSIRT organisational structure.
- Report-only diagram legends use line, border and decision-shape semantics; colour names such as Gold, Red, Navy, Teal, Blue and Amber are absent from the rendered legend text.
- Figures were visually inspected as rendered PNG/PDF output. Both figures remain monochrome and legible at their report display sizes.

## Layout and styling review

- The complete 60-page PDF was rendered with `pdftoppm` at 72 dpi and reviewed in four-page contact sheets. Figure pages and representative pages for every split-register type were additionally inspected at 150 dpi.
- No blank pages, clipped figures, overlapping objects, inconsistent page orientations, or missing page numbers were observed.
- Heading numbering is generated once by Pandoc; the previous duplicated pattern such as `3.1 1.` is absent.
- The longer document remains intentionally data-complete. The reduction from 88 to 60 pages resulted from readable field grouping and removal of character-level wrapping, not removal of required records.
- Remaining presentation limitation: all pages are portrait, so some long tables occupy several pages; this is an intentional readability trade-off and not a content omission.

## Validation commands

- `python3 tools/check_project.py` — PASS: source originals verified; rubric sections tracked.
- `python3 tools/build_grc105_submission.py` — PASS: DOCX and PDF regenerated.
- `pdfinfo` — PASS: 60-page A4 PDF produced.
- `pdftotext`/contents check — PASS: section order and page references verified.
- CSV-derived table generation — PASS: all canonical registers parsed and rendered with stable identifiers.
- `git diff --check` — PASS.
- `git status --short` — reviewed; expected pre-existing Task 2–6 and final-submission working changes remain uncommitted. No source training material or Task 1 file was modified by this layout remediation.

## Remaining limitations

- The document is a final draft for academic review; no submission date or instructor name was invented.
- No Git commit, push or E-Campus submission was performed.
