# Task 5 — Tabletop Simulation and Corrective Action Planning

## Overview

This directory contains the Task 5 tabletop exercise developed
for the fictional ransomware incident at **Northbridge Skills
Institute**, as part of the ICDFA GRC105 assignment.

A tabletop exercise is a structured, discussion-based method
of testing how individuals and teams would respond to a
developing incident. It examines decisions, coordination,
escalation, communication and continuity planning without
carrying out live technical response actions.

The Northbridge exercise uses a fictional incident scenario
involving disruption to institutional services, uncertainty
about data exposure and pressure to restore services before
a scheduled examination.

**Academic status:** The Task 5 exercise documentation has
been completed and incorporated into the GRC105 coursework.

**Simulation status:** The decisions and results are documented
individual simulated outcomes. They are not evidence that
a live incident response or an actual group exercise occurred.

## Primary assessment materials

| File | Purpose |
|---|---|
| [Complete Tabletop Exercise](TASK-5-TABLETOP-EXERCISE.md) | Main scenario, agenda, injects, decisions and evaluation |
| [Canonical Decision Log](data/exercise-decision-log.csv) | Structured record of simulated decisions |
| [Canonical Corrective Actions](data/corrective-actions.csv) | Proposed improvements with ownership and completion evidence |
| [Completion QA](TASK-5-COMPLETION-QA.md) | Recorded assessment-quality validation |
| [Editable Timeline](diagrams/tabletop-timeline.mmd) | Mermaid source for the exercise timeline |

## Scenario context

Northbridge Skills Institute is a fictional institution
supporting approximately 1,800 learners and 90 staff.

Its shared file server and dependent learning services
are affected by the ransomware scenario.

At the initial incident handover, **08:45 WAT on Day 0**,
the provisional severity classification is High.

An online examination is scheduled for 11:00 WAT,
creating pressure to restore learning services quickly.

However, the safety and recoverability of available backups
remain unverified, and possible data exposure has not
been established as confirmed exfiltration.

The exercise tests how the proposed incident response
structure handles these competing pressures.

## Exercise objectives

The tabletop evaluates the proposed ability to:

1. Apply incident leadership and escalation procedures.
2. Make defensible containment and recovery decisions.
3. Preserve evidence and uncertainty in incident reporting.
4. Coordinate with academic and business-continuity owners.
5. Respond consistently to stakeholder and media concerns.
6. Identify practical preparedness improvements.

Detailed participant assignments and measurable success
criteria are maintained in the complete exercise document.

## Exercise duration and structure

**Planned duration:** 60 minutes.

The exercise progresses through time-based injects and
associated decision discussions.

### Mandatory scenario injects

| Minute | Inject | Decision challenge |
|---|---|---|
| 10 | Management requests reopening before the examination despite unverified backup safety | Balance examination continuity against recovery assurance |
| 20 | An attacker claims possession of all 1,800 learner records; authenticity is uncertain | Handle potential exposure without declaring unverified theft |
| 35 | The latest network backup fails test restoration with an unreadable snapshot error | Reconsider recovery options and backup suitability |
| 45 | A social-media cancellation rumour appears and a journalist asks about learner-data exposure | Coordinate accurate, authorised external communications |

An additional inject at minute 50 is included in
the completed exercise.

The exact wording, expected responses and discussion
are preserved in the
[complete tabletop document](TASK-5-TABLETOP-EXERCISE.md)
and the [decision log](data/exercise-decision-log.csv).

## Decision-making and accountability

The exercise records **6 simulated decision entries**.

Decision documentation identifies the exercise minute,
inject, decision owner, rationale, communication and
anticipated effect on incident response or recovery.

The simulated decisions test the governance model from Task 2
and the operational response approach from Task 3.

They are analytical exercise records, not actual incident
decision logs or evidence of formal organisational approval.

## Corrective-action planning

The canonical improvement register contains
**6 corrective-action entries**.

Each entry documents a finding, proposed corrective action,
priority, owner, completion target, measurable evidence
and status.

The improvements should be interpreted as recommendations
arising from the simulated exercise.

An assigned target or owner does not establish that the
recommendation has been implemented.

## Directory navigation

| Directory | Contents |
|---|---|
| [data/](data/) | Canonical decision and corrective-action datasets |
| [diagrams/](diagrams/) | Editable Mermaid timeline source |
| [visuals/](visuals/) | Rendered exercise timeline with explanation |
| [deprecated-templates/](deprecated-templates/) | Superseded dataset variants retained for provenance |

## Visual exercise timeline

### Figure 1 — Tabletop Exercise Timeline

[![Tabletop exercise timeline](visuals/tabletop-timeline.png)](visuals/tabletop-timeline.svg)

**Description:** This diagram illustrates the progression
of the tabletop exercise across its planned 60-minute
duration, with time-based scenario developments and
opportunities for decision-making.

**Interpretation:** The timeline shows a planned and
documented simulation. It is not a timestamped record
of an actual ransomware attack or live emergency exercise.

**Available versions:**
[PNG](visuals/tabletop-timeline.png) |
[SVG](visuals/tabletop-timeline.svg) |
[Editable Mermaid](diagrams/tabletop-timeline.mmd)

For detailed figure documentation, visit the
[visual gallery](visuals/).

## Evaluation and learning

The exercise evaluates the quality of decisions rather
than the speed of actual technical recovery.

Its learning value includes identifying:

- Where recovery approval depends on unverified assumptions.
- How threat claims should be evaluated.
- Whether escalation and decision ownership remain clear.
- How communications can preserve accuracy under pressure.
- Whether backup readiness can support continuity objectives.
- Which weaknesses require measurable corrective action.

The exercise document records the applicable success
criteria and post-exercise review arrangements.

## Evidence and simulation limitations

This directory does not establish that:

- An attacker possessed learner records.
- The institution sent real notifications.
- An operational backup was actually restored or tested.
- The simulated decisions were formally approved in practice.
- Corrective actions have been implemented.
- A live incident exercise was conducted with actual participants.

All outcomes are confined to the documented fictional
exercise and its associated assessment analysis.

## Relationship to the other tasks

- [Task 1 — Incident Assessment](../01-incident-assessment/)
  supplies the reported scenario evidence and uncertainties.
- [Task 2 — IR Governance](../02-ir-plan-and-governance/)
  defines proposed authority and responsibility arrangements.
- [Task 3 — Response Playbook](../03-response-playbook/)
  supplies the planned operational response framework.
- [Task 4 — Communications](../04-communications/)
  supplies stakeholder messaging and notification boundaries.
- [Task 6 — Case Study](../06-case-study/)
  supports wider reflection on response and recovery lessons.

## Assessment status

The Task 5 deliverables were previously reviewed against
the assignment requirements and incorporated into the
completed submission package.

The technical exercise details remain in the main assessment
document and the canonical structured records.

[Return to repository overview](../README.md)
