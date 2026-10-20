# Task 1 — Visual Evidence and Assessment Gallery

## Overview

This gallery presents all five rendered Task 1 diagrams,
with explanations and links to their editable sources.

Each PNG is embedded directly in this README, allowing
GitHub visitors to view the diagrams without opening
individual image files.

Clicking an image opens the corresponding SVG.

These figures are analytical illustrations for the
fictional Northbridge incident response assignment.

## Visual catalogue

---

## Figure 1 — Incident Timeline

[![Figure 1: Incident Timeline](incident-timeline.png)](incident-timeline.svg)

### Purpose

Presents the chronological relationship between the reported incident observations. The timeline supports sequencing, but does not establish that each event was causally connected.

### How to interpret the figure

Read the events alongside the incident chronology and evidence-analysis register. Preserve reported WAT times and distinguish confirmed observations from hypotheses.

### Available files

| Format | File | Use |
|---|---|---|
| PNG | [incident-timeline.png](incident-timeline.png) | Quick preview and image insertion |
| SVG | [incident-timeline.svg](incident-timeline.svg) | Scalable report-quality visual |
| Mermaid | [incident-timeline.mmd](../diagrams/incident-timeline.mmd) | Editable diagram source |

---

## Figure 2 — Investigation Relationships

[![Figure 2: Investigation Relationships](investigation-relationships.png)](investigation-relationships.svg)

### Purpose

Maps relationships between relevant assets, accounts, observations and investigative questions.

### How to interpret the figure

Connections represent relationships that require analysis; a drawn connection is not proof of compromise, attribution or a confirmed attack path.

### Available files

| Format | File | Use |
|---|---|---|
| PNG | [investigation-relationships.png](investigation-relationships.png) | Quick preview and image insertion |
| SVG | [investigation-relationships.svg](investigation-relationships.svg) | Scalable report-quality visual |
| Mermaid | [investigation-relationships.mmd](../diagrams/investigation-relationships.mmd) | Editable diagram source |

---

## Figure 3 — Severity Decision Tree

[![Figure 3: Severity Decision Tree](severity-decision-tree.png)](severity-decision-tree.svg)

### Purpose

Illustrates the structured reasoning used for the initial incident classification and subsequent reassessment.

### How to interpret the figure

The initial classification is High — provisional at 08:45 WAT on Day 0. New verified findings may require reassessment under documented criteria.

### Available files

| Format | File | Use |
|---|---|---|
| PNG | [severity-decision-tree.png](severity-decision-tree.png) | Quick preview and image insertion |
| SVG | [severity-decision-tree.svg](severity-decision-tree.svg) | Scalable report-quality visual |
| Mermaid | [severity-decision-tree.mmd](../diagrams/severity-decision-tree.mmd) | Editable diagram source |

---

## Figure 4 — CIA Impact Assessment

[![Figure 4: CIA Impact Assessment](cia-impact-visual.png)](cia-impact-visual.svg)

### Purpose

Provides a visual aid to the confidentiality, integrity and availability assessment.

### How to interpret the figure

Potential confidentiality exposure must not be confused with confirmed data theft. Service disruption and integrity concerns should also be evaluated separately.

### Available files

| Format | File | Use |
|---|---|---|
| PNG | [cia-impact-visual.png](cia-impact-visual.png) | Quick preview and image insertion |
| SVG | [cia-impact-visual.svg](cia-impact-visual.svg) | Scalable report-quality visual |
| Mermaid | [cia-impact-visual.mmd](../diagrams/cia-impact-visual.mmd) | Editable diagram source |

---

## Figure 5 — Response Priority Workflow

[![Figure 5: Response Priority Workflow](response-priority-workflow.png)](response-priority-workflow.svg)

### Purpose

Illustrates how incident-response priorities can be sequenced while preserving evidence and maintaining appropriate operational decision controls.

### How to interpret the figure

This is a proposed decision-support workflow, not a record of actions actually executed against systems.

### Available files

| Format | File | Use |
|---|---|---|
| PNG | [response-priority-workflow.png](response-priority-workflow.png) | Quick preview and image insertion |
| SVG | [response-priority-workflow.svg](response-priority-workflow.svg) | Scalable report-quality visual |
| Mermaid | [response-priority-workflow.mmd](../diagrams/response-priority-workflow.mmd) | Editable diagram source |

---

## Rendering and quality considerations

The existing Task 1 SVG and PNG exports were previously
reported as rendered with Mermaid CLI v12.0.0.

The investigation-relationships diagram is comparatively
dense and may require full-width display when used in
a formal report.

The images in this directory are retained as existing
repository artifacts; this README update does not alter
or regenerate them.

## Important evidentiary limitation

Visual representations summarise the assignment's reported
events and proposed analyses. They do not verify attack
attribution, actual data theft, successful evidence acquisition
or completed recovery.

## Related documentation

- [Editable Mermaid Sources](../diagrams/)
- [Incident Chronology](../analysis/incident-chronology.md)
- [Evidence Analysis Register](../data/evidence-analysis-register.csv)
- [Integrated Task 1 Assessment](../TASK-1-INTEGRATED-ASSESSMENT.md)
- [Task 1 Overview](../README.md)
