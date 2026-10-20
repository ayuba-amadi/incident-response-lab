# Task 5 — Historical Dataset Variants

## Overview

This directory preserves two earlier CSV dataset versions
from the original Task 5 workspace.

They are retained for provenance and historical comparison.

They are **not the authoritative current tabletop records**.

## Historical files

### Historical Exercise Decision Log

[Open inject-decision-log.csv](inject-decision-log.csv)

- Historical records: **6**
- Classification: superseded dataset variant.

The current authoritative decision dataset is:

[Canonical Exercise Decision Log](../data/exercise-decision-log.csv)

### Historical Corrective Action Register

[Open corrective-actions.csv](corrective-actions.csv)

- Historical records: **6**
- Classification: superseded dataset variant.

The current authoritative improvement dataset is:

[Canonical Corrective Actions](../data/corrective-actions.csv)

## Why these are not simply empty templates

The older datasets contain populated exercise positions
and corrective-action identifiers.

They overlap with the canonical records but differ
in wording, role descriptions, rationale details
or status phrasing.

These differences mean they should not be treated
as additional independent exercise records.

## Preservation rationale

The variants remain available to document the
evolution of the project and its structured records.

Their presence is not evidence that the current
exercise is incomplete.

## Use restrictions

1. Do not merge historical rows into the canonical datasets.
2. Do not double-count decisions or corrective actions.
3. Do not use an outdated rationale instead of the approved
   canonical record.
4. Do not interpret simulation entries as live actions.
5. Use the current main exercise for context and interpretation.

## Current authoritative materials

- [Tabletop Exercise](../TASK-5-TABLETOP-EXERCISE.md)
- [Canonical Data Registers](../data/)
- [Timeline Visual](../visuals/)
- [Task 5 Overview](../README.md)
