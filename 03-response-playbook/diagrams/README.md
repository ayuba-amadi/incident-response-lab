# Task 3 — Editable Incident Response Diagrams

## Overview

This directory contains the two editable Mermaid
sources associated with the Task 3 operational playbook.

The Mermaid files preserve the diagram structures
for review and maintenance.

Rendered SVG and PNG versions are available in
[visuals/](../visuals/).

## Diagram 1 — Incident Response Workflow

![Incident Response Workflow](../visuals/response-workflow.png)

### Purpose

Illustrates the planned sequence of incident response activities, from assessment and containment through investigation, eradication planning, recovery and closure.

### Interpretation

The workflow is a proposed response model. It does not demonstrate that systems were isolated, evidence was collected, or recovery was completed.

### Available formats

- [Editable Mermaid source](response-workflow.mmd)
- [Scalable SVG](../visuals/response-workflow.svg)
- [Rendered PNG](../visuals/response-workflow.png)

## Diagram 2 — Recovery Decision Workflow

![Recovery Decision Workflow](../visuals/recovery-decision.png)

### Purpose

Illustrates the decision-making considerations associated with validating backups, restoring technical services and authorising operational use.

### Interpretation

Technical accessibility does not independently establish security clearance, data integrity or business acceptance.

### Available formats

- [Editable Mermaid source](recovery-decision.mmd)
- [Scalable SVG](../visuals/recovery-decision.svg)
- [Rendered PNG](../visuals/recovery-decision.png)

## Editable versus rendered files

| Format | Role |
|---|---|
| `.mmd` | Authoritative editable diagram definition |
| `.svg` | Scalable rendered visual |
| `.png` | Standard image preview |

The exported formats represent the existing
Mermaid diagram content.

A change to a source file requires regeneration
and visual review of the corresponding exports.

## Diagram maintenance safeguards

- Preserve incident-response stage relationships.
- Maintain distinction between planned and completed actions.
- Keep approval and decision boundaries consistent
  with Task 2.
- Do not introduce unsupported forensic findings.
- Verify readability after regeneration.
- Preserve the relationship between recovery validation
  and operational acceptance.

## Related documentation

- [Complete Response Playbook](../TASK-3-RESPONSE-PLAYBOOK.md)
- [Canonical Registers](../data/)
- [Visual Gallery](../visuals/)
- [Task 3 Overview](../README.md)
