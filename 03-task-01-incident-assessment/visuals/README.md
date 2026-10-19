# Task 1 Rendered Visuals

## Sources and expected outputs

The five editable Mermaid sources are in `../diagrams/`:

- `incident-timeline.mmd` → `incident-timeline.svg`, `incident-timeline.png`
- `investigation-relationships.mmd` → `investigation-relationships.svg`, `investigation-relationships.png`
- `severity-decision-tree.mmd` → `severity-decision-tree.svg`, `severity-decision-tree.png`
- `cia-impact-visual.mmd` → `cia-impact-visual.svg`, `cia-impact-visual.png`
- `response-priority-workflow.mmd` → `response-priority-workflow.svg`, `response-priority-workflow.png`

## Rendering and validation status

All five diagrams have been rendered with the cached Mermaid CLI version 12.0.0 using `npx --no-install --package @mermaid-js/mermaid-cli mmdc`. SVG files are report-quality vector outputs; PNG files were rendered at scale 2 for presentation compatibility. No dependency was installed.

The SVG and PNG outputs were checked for existence and non-zero size, opened for visual inspection, and reviewed for syntax errors, clipping, overlapping labels, hierarchy, contrast, evidence-ID legibility, and observation/hypothesis distinction. No clipped text was observed. The investigation-relationships diagram has dense relationship routing and should be inserted at full report width or in landscape orientation. The editable Mermaid sources remain authoritative.
