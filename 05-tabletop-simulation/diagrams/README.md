# Task 5 — Editable Tabletop Timeline

## Overview

This directory contains the editable Mermaid source
for the Task 5 tabletop simulation timeline.

The source describes the sequence of planned exercise
developments and supports visual communication of
the 60-minute exercise structure.

It is a modelling artifact, not a real incident log.

## Diagram 1 — Tabletop Exercise Timeline

![Tabletop exercise timeline](../visuals/tabletop-timeline.png)

### Purpose

The timeline provides a visual overview of the
exercise progression and its time-based decision points.

It helps readers connect the inject sequence to the
broader tabletop discussion and decision records.

### Exercise timing

The planned exercise lasts 60 minutes.

Required scenario injects are scheduled at
minutes 10, 20, 35 and 45, with an additional
exercise development at minute 50.

See the main tabletop exercise for the complete
scenario wording and discussion details.

### How to interpret the diagram

Timeline positions represent elapsed exercise
minutes rather than actual incident timestamps.

Connections are part of the exercise model.
They do not prove that particular operational
events occurred.

### Source and rendered files

- [Editable Mermaid source](tabletop-timeline.mmd)
- [Scalable SVG](../visuals/tabletop-timeline.svg)
- [PNG preview](../visuals/tabletop-timeline.png)

## Source management

The `.mmd` file is the editable diagram definition.

When revising the visual, retain consistency with
the canonical decision log and the main exercise.

After any source modification, regenerate and inspect
the rendered PNG and SVG exports.

Pay attention to:

- Correct timing and chronological order.
- Legible labels.
- No clipped text or overlapping annotations.
- Accurate distinction between injects and decisions.
- No unsupported claim of live exercise execution.

## Related resources

- [Decision Log](../data/exercise-decision-log.csv)
- [Corrective Actions](../data/corrective-actions.csv)
- [Rendered Timeline Gallery](../visuals/)
- [Main Tabletop Exercise](../TASK-5-TABLETOP-EXERCISE.md)
- [Task 5 Overview](../README.md)
