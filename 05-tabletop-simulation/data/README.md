# Task 5 — Canonical Exercise Data Registers

## Purpose

This directory contains the authoritative structured records
supporting the fictional Northbridge tabletop simulation.

The CSV files document simulated exercise decisions and
proposed corrective actions.

They should be interpreted alongside the
[main exercise document](../TASK-5-TABLETOP-EXERCISE.md).

## Register 1 — Exercise Decision Log

**[Open exercise-decision-log.csv](exercise-decision-log.csv)**

### Purpose

This register records the decisions made within the
documented fictional tabletop scenario.

Each record links an exercise development to a simulated
decision, decision owner, rationale, communication response
and expected operational consequence.

### Dataset structure

- Records: **6**
- Columns: **8**

| CSV column | Meaning |
|---|---|
| `Exercise minute` | Elapsed minute within the simulated 60-minute exercise. |
| `Inject` | Scenario development presented to exercise participants. |
| `Decision` | Simulated response or management decision. |
| `Decision owner` | Role expected to own or authorise the decision. |
| `Rationale` | Reasoning supporting the simulated decision. |
| `Communication` | Proposed information-sharing or notification response. |
| `Effect on response or recovery` | Expected consequence for the simulated response. |
| `Simulation status` | Explicit indication that the record is simulated. |


### Interpretation

The exercise-minute field refers to the simulated exercise
schedule, not the clock time of a verified real-world event.

Decisions represent expected or documented simulated choices.
They should not be treated as authorisations issued during
a real incident.

## Register 2 — Corrective Action Register

**[Open corrective-actions.csv](corrective-actions.csv)**

### Purpose

This register converts observations from the tabletop
discussion into practical recommendations for improving
incident response preparedness.

It provides structured accountability through priorities,
responsible owners, completion targets and measurable
evidence requirements.

### Dataset structure

- Records: **6**
- Columns: **8**

| CSV column | Meaning |
|---|---|
| `Action ID` | Unique corrective-action identifier. |
| `Priority` | Relative importance or urgency of the improvement. |
| `Finding` | Exercise observation or weakness prompting improvement. |
| `Corrective action` | Proposed remediation or readiness measure. |
| `Owner` | Role accountable for progressing the improvement. |
| `Target completion` | Proposed completion target. |
| `Measurable evidence` | Evidence that would demonstrate completion. |
| `Status` | Recorded state of the proposed corrective action. |


### Interpretation

A recommendation with an owner and target does not mean
implementation has occurred.

The measurable-evidence field describes what would be needed
to demonstrate that a corrective action was completed.

The status column must be interpreted according to
the recorded simulation or implementation status.

## Relationship between both registers

The decision log captures the simulated response to
scenario developments.

The corrective-action register identifies weaknesses
or improvement opportunities emerging from the exercise.

Together, they provide a traceable connection between
exercise decision-making and subsequent readiness planning.

They are not interchangeable datasets.

## Data provenance

The files in this directory are the canonical Task 5 records.

Earlier root-level variants were preserved in
[deprecated-templates/](../deprecated-templates/).

Those variants include overlapping identifiers but
different wording and detail.

Do not merge them into these canonical records or
count them as additional exercise decisions.

## Data integrity and maintenance

- Preserve exercise-minute and decision identifiers.
- Retain the distinction between simulated and actual actions.
- Preserve approval and ownership relationships.
- Do not fabricate completion evidence.
- Do not silently import outdated dataset variants.
- Keep any future changes consistent with the exercise narrative.

## Related documentation

- [Tabletop Exercise](../TASK-5-TABLETOP-EXERCISE.md)
- [Timeline Diagram Sources](../diagrams/)
- [Rendered Timeline](../visuals/)
- [Task 5 Overview](../README.md)
