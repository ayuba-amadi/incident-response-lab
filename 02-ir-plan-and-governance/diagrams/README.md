# Task 2 — Editable Governance and CSIRT Diagrams

## Purpose

This directory contains eight Mermaid source files
representing the proposed Task 2 governance framework.

Mermaid `.mmd` files provide editable workflow definitions.
The rendered PNG and SVG files are available under
[visuals/](../visuals/).

These diagrams are intended to clarify relationships,
decision rights, coordination and approval requirements.

## Diagram catalogue

### Diagram 1 — Incident Declaration and Activation

![Incident Declaration and Activation](../visuals/incident-declaration-activation.png)

**Purpose:** Explains the proposed relationship between incident recognition, formal declaration, response activation and command responsibilities.

**Interpretation:** Declaration and team activation are distinct governance decisions.

**Available files:**

- [Editable Mermaid source](incident-declaration-activation.mmd)
- [Full-size PNG](../visuals/incident-declaration-activation.png)
- [Scalable SVG](../visuals/incident-declaration-activation.svg)

### Diagram 2 — Severity and Escalation Workflow

![Severity and Escalation Workflow](../visuals/severity-escalation-workflow.png)

**Purpose:** Illustrates how severity assessment informs escalation and leadership involvement.

**Interpretation:** The Northbridge High classification remains provisional and subject to reassessment.

**Available files:**

- [Editable Mermaid source](severity-escalation-workflow.mmd)
- [Full-size PNG](../visuals/severity-escalation-workflow.png)
- [Scalable SVG](../visuals/severity-escalation-workflow.svg)

### Diagram 3 — Emergency Isolation Authority

![Emergency Isolation Authority](../visuals/emergency-isolation-authority.png)

**Purpose:** Shows the distinction between ordinary containment approval and limited emergency containment authority.

**Interpretation:** Emergency action requires the documented conditions, records and retrospective review; it is not unrestricted authority.

**Available files:**

- [Editable Mermaid source](emergency-isolation-authority.mmd)
- [Full-size PNG](../visuals/emergency-isolation-authority.png)
- [Scalable SVG](../visuals/emergency-isolation-authority.svg)

### Diagram 4 — Incident Response and Business Continuity Coordination

![Incident Response and Business Continuity Coordination](../visuals/ir-business-continuity-coordination.png)

**Purpose:** Illustrates coordination between security-led incident response, continuity planning and academic/business service decisions.

**Interpretation:** Operational continuity decisions and technical recovery approvals are not interchangeable.

**Available files:**

- [Editable Mermaid source](ir-business-continuity-coordination.mmd)
- [Full-size PNG](../visuals/ir-business-continuity-coordination.png)
- [Scalable SVG](../visuals/ir-business-continuity-coordination.svg)

### Diagram 5 — CSIRT Organisational Structure

![CSIRT Organisational Structure](../visuals/csirt-organisational-structure.png)

**Purpose:** Presents the functional roles and command relationships proposed for managing the incident.

**Interpretation:** The chart describes functions, not an assertion that each function is staffed by a separate employee.

**Available files:**

- [Editable Mermaid source](csirt-organisational-structure.mmd)
- [Full-size PNG](../visuals/csirt-organisational-structure.png)
- [Scalable SVG](../visuals/csirt-organisational-structure.svg)

### Diagram 6 — Staffing and Escalation

![Staffing and Escalation](../visuals/csirt-staffing-and-escalation.png)

**Purpose:** Illustrates how limited internal staffing, escalation, role coverage and conditional specialist support interact.

**Interpretation:** External support is a proposed escalation option, not a confirmed engaged service provider.

**Available files:**

- [Editable Mermaid source](csirt-staffing-and-escalation.mmd)
- [Full-size PNG](../visuals/csirt-staffing-and-escalation.png)
- [Scalable SVG](../visuals/csirt-staffing-and-escalation.svg)

### Diagram 7 — RACI Accountability Workflow

![RACI Accountability Workflow](../visuals/raci-accountability-workflow.png)

**Purpose:** Visualises responsibility and accountable decision ownership through the response lifecycle.

**Interpretation:** A RACI assignment is a proposed governance allocation, not evidence that any operational action occurred.

**Available files:**

- [Editable Mermaid source](raci-accountability-workflow.mmd)
- [Full-size PNG](../visuals/raci-accountability-workflow.png)
- [Scalable SVG](../visuals/raci-accountability-workflow.svg)

### Diagram 8 — Recovery Approval Gates

![Recovery Approval Gates](../visuals/recovery-approval-gates.png)

**Purpose:** Separates technical restoration from security checks, data integrity validation and business acceptance.

**Interpretation:** Technical accessibility alone does not mean a system is safe or approved to return to service.

**Available files:**

- [Editable Mermaid source](recovery-approval-gates.mmd)
- [Full-size PNG](../visuals/recovery-approval-gates.png)
- [Scalable SVG](../visuals/recovery-approval-gates.svg)

## Source management

Edit an `.mmd` file only if a substantive diagram
change is necessary.

After editing, regenerate the applicable export
and verify labels, line relationships, decision paths
and consistency with the policy and authority registers.

Do not modify a governance diagram in a way that
silently changes the approved academic authority model.

## Historical rendering information

The existing diagrams were reported as rendered
and inspected using Mermaid CLI v12.0.0.

This README update does not rerender or alter
the existing SVG or PNG files.

## Navigational links

- [Visual Gallery](../visuals/)
- [Governance Plans](../plans/)
- [CSIRT Documentation](../csirt/)
- [Task 2 Overview](../README.md)
