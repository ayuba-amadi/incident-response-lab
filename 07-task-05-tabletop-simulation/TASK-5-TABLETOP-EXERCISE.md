# Northbridge Skills Institute — Task 5 Tabletop Exercise

**Status:** Fictional individual tabletop design and simulated outcome record — awaiting independent review.  
**Duration:** 60 minutes.  
**Scenario point:** High — provisional suspected ransomware incident, Day 0, with the 11:00 examination dependency.

## 1. Exercise purpose and boundaries

This tabletop tests the approved Task 1 assessment, Task 2 governance, Task 3 response playbook and Task 4 communication controls. It is an individual simulation in which the analyst takes the role of each functional participant. Every decision and result is simulated; it is not a record of live response, system restoration, evidence collection or notification.

## 2. Objectives

- Test whether the team preserves evidence while controlling active encryption and privileged-account risk.
- Test whether the Incident Response Lead, IT Operations, Security Analyst, BCC and Academic/Business Service Owner make distinct decisions under the 11:00 deadline.
- Test backup uncertainty and the prohibition on unsafe restoration.
- Test fact-bounded communications when a data-theft claim and media query are unverified.
- Produce measurable preparation improvements for backup, communications, monitoring, training and closure discipline.

## 3. Participants and roles

| Participant role | Exercise responsibility |
|---|---|
| Incident Response Lead | Directs the simulated incident, authorises normal containment, records decisions and escalates material risk. |
| Security Analyst | Analyses evidence, maintains uncertainty and validates security conditions. |
| IT Operations and Recovery Lead | Performs simulated technical assessment, backup validation and recovery decisions within authority. |
| Digital Forensics/Evidence Custodian | Preserves planned evidence and identifies custody or evidence-loss concerns. |
| Business Continuity Coordinator | Coordinates authorised continuity options and learner-service planning. |
| Academic/Business Service Owner | Decides whether an examination arrangement is acceptable within approved parameters. |
| Senior Management / Executive Sponsor | Accepts material institutional risk, approves material exceptions and communications. |
| Legal/Privacy Adviser | Advises on data claims, evidence confidence and possible reporting obligations. |
| Communications Coordinator | Drafts fact-bounded internal and external messages and records approval. |

The role set is functional; it does not imply that Northbridge has nine dedicated employees.

## 4. Agenda and injects

| Minute | Activity |
|---:|---|
| 0–5 | Briefing, assumptions, role assignment and success criteria. |
| 5–10 | Review E01–E08 and establish the simulated situation record. |
| 10 | Required inject 1: management requests reopening before the 11:00 examination despite unverified backup safety. |
| 20 | Required inject 2: an attacker claims possession of all 1,800 learner records; screenshot authenticity is uncertain. |
| 35 | Required inject 3: the latest network backup fails a simulated test restoration with an unreadable snapshot error. |
| 45 | Required inject 4: social media claims cancellation and a journalist asks about learner-information exposure. |
| 50 | Additional inject: Microsoft 365 audit export is delayed and the finance officer cannot immediately confirm the unfamiliar sign-in. |
| 55–60 | Closure discipline, corrective actions, debrief and simulated handover to post-incident review. |

The editable timeline is [tabletop-timeline.mmd](diagrams/tabletop-timeline.mmd).

## 5. Measurable success criteria

1. By minute 10, the simulated record identifies E01–E08, the High provisional classification, the examination dependency, the unverified backup position and at least three unresolved questions.
2. By minute 20, the participants preserve the attacker claim as unverified, assign a Legal/Privacy assessment and avoid stating that learner records were stolen.
3. By minute 35, the participants reject restoration from the failed or unvalidated source and record an alternative continuity path.
4. By minute 45, the participants produce an approved fact-bounded holding message without confirming cancellation or data exposure.
5. By minute 60, every simulated decision has an owner, rationale, communication, effect and follow-up record, and at least five corrective actions are assigned.

## 6. Individual simulated decision walkthrough

The detailed decision log is [data/exercise-decision-log.csv](data/exercise-decision-log.csv). The six outcomes are labelled `Individual simulated tabletop outcome` and are not evidence from the fictional incident.

### Inject 1 — minute 10

The simulated decision is not to reopen LMS01 from an unvalidated backup. The IRL, Senior Management and Academic/Business Service Owner retain separate security, risk and service decisions while the BCC prepares an alternative. This preserves recovery safety and leaves the examination status unresolved until an authorised decision.

### Inject 2 — minute 20

The claim and screenshot are preserved for validation. The simulated team does not confirm theft, attacker identity or authenticity. Legal/Privacy receives the potential personal-data issue, while Communications prepares only a fact-bounded holding line.

### Inject 3 — minute 35

The simulated unreadable snapshot result blocks use of that candidate recovery source. It does not prove that all backups fail. IT Operations requests specialist support and records recovery uncertainty; BCC and academic operations continue contingency planning.

### Inject 4 — minute 45

The simulated team treats the social-media post as a rumour, not an examination decision. Communications prepares an approved holding statement; Legal/Privacy and Senior Management review any external message. No exposure claim is confirmed.

### Additional inject — minute 50

The delayed Microsoft 365 export and unavailable finance officer leave E02 unresolved. The simulated response preserves the provider request and uses other planned sources rather than inventing an account-compromise conclusion.

### Closure decision — minute 55

The exercise remains under simulated recovery rather than closing. Open evidence, recovery, learner-impact and approval items receive owners and next reviews. The decision tests whether closure is treated as a governance gate rather than an administrative convenience.

## 7. Corrective actions and post-incident review

Six proposed corrective actions are recorded in [data/corrective-actions.csv](data/corrective-actions.csv). They cover backup testing, alternative communication, server monitoring, dual-hat training, privacy/communications decision support and closure gates. Target completion times are relative to simulated exercise closure and are not claims of implementation.

For this exercise, the simulated post-incident review deadline is **within two weeks of simulated incident closure**, consistent with the Week 20 lessons-learned teaching point. The Incident Response Lead coordinates the review; Senior Management closes corrective actions after evidence of completion is accepted by the named owner and relevant technical/business reviewer. No actual review or closure has occurred.

## 8. Sources and boundaries

- ICDFA, *GRC105 Incident Response Planning Assignment*, Task 5 and rubric.
- ICDFA, *Incident Response Planning*, Week 20 slides 12–13 and 16–18.
- Approved Task 1–Task 4 planning artifacts.
- NIST, *SP 800-61 Rev. 3*: https://csrc.nist.gov/pubs/sp/800/61/r3/final

All outcomes in this document are explicitly simulated. No live response, evidence acquisition, backup restoration or communication is represented.
