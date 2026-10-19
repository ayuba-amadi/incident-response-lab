# Task 2 Rendered Visuals

## Editable sources and exports

| Mermaid source | SVG export | PNG export |
|---|---|---|
| `../diagrams/incident-declaration-activation.mmd` | `incident-declaration-activation.svg` | `incident-declaration-activation.png` |
| `../diagrams/severity-escalation-workflow.mmd` | `severity-escalation-workflow.svg` | `severity-escalation-workflow.png` |
| `../diagrams/emergency-isolation-authority.mmd` | `emergency-isolation-authority.svg` | `emergency-isolation-authority.png` |
| `../diagrams/ir-business-continuity-coordination.mmd` | `ir-business-continuity-coordination.svg` | `ir-business-continuity-coordination.png` |
| `../diagrams/csirt-organisational-structure.mmd` | `csirt-organisational-structure.svg` | `csirt-organisational-structure.png` |
| `../diagrams/csirt-staffing-and-escalation.mmd` | `csirt-staffing-and-escalation.svg` | `csirt-staffing-and-escalation.png` |
| `../diagrams/raci-accountability-workflow.mmd` | `raci-accountability-workflow.svg` | `raci-accountability-workflow.png` |
| `../diagrams/recovery-approval-gates.mmd` | `recovery-approval-gates.svg` | `recovery-approval-gates.png` |

## Rendering method

The diagrams were rendered with cached Mermaid CLI version 12.0.0 using:

```text
npx --no-install --package @mermaid-js/mermaid-cli mmdc
```

No dependency was installed during this stage. SVG files are the scalable report outputs. PNG files were rendered at scale 2 for compatibility and inspection.

## Validation results

- All eight SVG and PNG files exist and are non-empty.
- Mermaid CLI completed without syntax errors.
- SVG files parse as XML.
- PNG files were opened and inspected for clipping, overlapping labels, contrast, hierarchy, and legibility.
- Evidence-linked scenario references, proposed-action boundaries, role distinctions, and decision paths remain readable.
- No clipped text was observed.

The four Stage 1 exports were retained from the approved governance work. The four Stage 2 exports were generated for the CSIRT structure, staffing escalation, RACI accountability, and recovery approval gates. The Stage 2 PNG exports were opened and inspected for clipping, overlap, contrast, hierarchy, and legibility.

The declaration, severity, and isolation diagrams are tall and should be inserted at a readable size. The business-continuity diagram is wide and is best placed at full report width. These are presentation limitations, not additional operational claims.
