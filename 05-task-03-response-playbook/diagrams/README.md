<!-- TASK3-DOCUMENTATION-START -->
# Task 3 — Editable Workflow Diagrams

This directory contains the editable Mermaid source files for
the incident response and recovery decision diagrams.

These source files allow the diagrams to be reviewed and updated
without recreating them from static images.

## 1. Incident Response Workflow

**[View Mermaid source](response-workflow.mmd)**

The response workflow represents the planned incident response
sequence and helps readers understand the relationship between
investigation, containment, eradication and recovery activities.

![Incident Response Workflow](../visuals/response-workflow.png)

## 2. Recovery Decision Workflow

**[View Mermaid source](recovery-decision.mmd)**

The recovery decision diagram illustrates the need for
controlled validation and approval before affected systems
are returned to operational service.

![Recovery Decision Workflow](../visuals/recovery-decision.png)

## File formats

| Format | Purpose |
|---|---|
| `.mmd` | Editable Mermaid source. |
| `.svg` | Scalable diagram suitable for reports. |
| `.png` | Image suitable for GitHub previews and documents. |

Rendered outputs are maintained under
[visuals/](../visuals/).

[Return to Task 3 overview](../README.md)
<!-- TASK3-DOCUMENTATION-END -->
