# Task 1 — Editable Mermaid Diagrams

## Purpose

This directory preserves the editable Mermaid source files
used to create the five Task 1 assessment visuals.

A Mermaid `.mmd` file is the editable source.
The SVG and PNG files under `../visuals/` are rendered outputs.

The source files permit further review or adjustment without
having to reconstruct a static image.

## Diagram catalogue

### Diagram 1 — Incident Timeline

![Incident Timeline](../visuals/incident-timeline.png)

**Purpose:** Presents the chronological relationship between the reported incident observations. The timeline supports sequencing, but does not establish that each event was causally connected.

**Interpretation:** Read the events alongside the incident chronology and evidence-analysis register. Preserve reported WAT times and distinguish confirmed observations from hypotheses.

**Files:**
- [Editable Mermaid source](incident-timeline.mmd)
- [Scalable SVG](../visuals/incident-timeline.svg)
- [PNG preview](../visuals/incident-timeline.png)

### Diagram 2 — Investigation Relationships

![Investigation Relationships](../visuals/investigation-relationships.png)

**Purpose:** Maps relationships between relevant assets, accounts, observations and investigative questions.

**Interpretation:** Connections represent relationships that require analysis; a drawn connection is not proof of compromise, attribution or a confirmed attack path.

**Files:**
- [Editable Mermaid source](investigation-relationships.mmd)
- [Scalable SVG](../visuals/investigation-relationships.svg)
- [PNG preview](../visuals/investigation-relationships.png)

### Diagram 3 — Severity Decision Tree

![Severity Decision Tree](../visuals/severity-decision-tree.png)

**Purpose:** Illustrates the structured reasoning used for the initial incident classification and subsequent reassessment.

**Interpretation:** The initial classification is High — provisional at 08:45 WAT on Day 0. New verified findings may require reassessment under documented criteria.

**Files:**
- [Editable Mermaid source](severity-decision-tree.mmd)
- [Scalable SVG](../visuals/severity-decision-tree.svg)
- [PNG preview](../visuals/severity-decision-tree.png)

### Diagram 4 — CIA Impact Assessment

![CIA Impact Assessment](../visuals/cia-impact-visual.png)

**Purpose:** Provides a visual aid to the confidentiality, integrity and availability assessment.

**Interpretation:** Potential confidentiality exposure must not be confused with confirmed data theft. Service disruption and integrity concerns should also be evaluated separately.

**Files:**
- [Editable Mermaid source](cia-impact-visual.mmd)
- [Scalable SVG](../visuals/cia-impact-visual.svg)
- [PNG preview](../visuals/cia-impact-visual.png)

### Diagram 5 — Response Priority Workflow

![Response Priority Workflow](../visuals/response-priority-workflow.png)

**Purpose:** Illustrates how incident-response priorities can be sequenced while preserving evidence and maintaining appropriate operational decision controls.

**Interpretation:** This is a proposed decision-support workflow, not a record of actions actually executed against systems.

**Files:**
- [Editable Mermaid source](response-priority-workflow.mmd)
- [Scalable SVG](../visuals/response-priority-workflow.svg)
- [PNG preview](../visuals/response-priority-workflow.png)

## Editing and rendering

Edit only the applicable Mermaid source when a change
is genuinely required.

After editing, regenerate the SVG/PNG outputs with
an available Mermaid-compatible renderer, then verify
the rendered labels, shapes, connections and legibility.

The presence of these sources does not imply that
the diagrams need to be regenerated merely to read them.

## Interpretation controls

- Treat proposed relationships as analytical models.
- Do not use diagram connections as proof of compromise.
- Preserve evidence-ID and chronology consistency.
- Keep severity decisions distinguishable from findings.
- Do not confuse visual modelling with executed response actions.

## Navigation

- [Rendered Visual Gallery](../visuals/)
- [Supporting Analyses](../analysis/)
- [Task 1 Overview](../README.md)
