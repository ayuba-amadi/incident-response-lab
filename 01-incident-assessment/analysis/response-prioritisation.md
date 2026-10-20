# Northbridge Skills Institute — Response Prioritisation

**Assessment point:** 08:45 WAT on Day 0.
**Purpose:** Set evidence-based response priorities without replacing the ordered containment, evidence-custody, recovery, or communications procedures required in Task 3 and later tasks.

## Prioritisation basis

The priorities consider:

- life and safety or safeguarding consequences;
- asset criticality and current functional impact;
- possible data impact and sensitivity of institutional information;
- observed activity stage and potential for continued spread;
- privileged-account and recovery-infrastructure risk;
- the 11:00 examination for 100 learners;
- limited staffing of three IT staff and one security analyst;
- evidence-preservation needs and recovery uncertainty.

NIST SP 800-61r3 states that incidents should be prioritized using scope, likely impact, time-criticality, and resource availability, with factors such as asset criticality, functional impact, data impact, activity stage, threat-actor characterization, and recoverability. It also emphasizes balancing rapid recovery with the need to observe activity or conduct a thorough investigation. See [NIST SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), RS.MA-03, RS.AN-07, RS.AN-08, RS.MI-01, and RC.

## Priority order

The detailed matrix is in data/response-priority-matrix.csv. The order is a decision sequence, not a claim that any action has already occurred.

### Immediate priorities

1. **Maintain authoritative coordination and a safe channel.** E08 makes the normal contact list unavailable and corporate email unverified. Staff phones are available, so the Incident Response Lead should use an approved alternate channel while checking email trust.
2. **Contain suspected active compromise while preserving useful evidence.** E03, E04, E06, and E07 justify urgent containment consideration across the endpoint, file server, identities, and recovery infrastructure. The exact isolation or account action belongs in the approved response playbook and must document evidence and business effects.
3. **Preserve high-value evidence and provenance.** E01–E08 point to endpoint, identity, server, proxy, backup, application, EDR, and helpdesk records. Collection is proposed only; no acquisition is claimed.
4. **Protect credentials and privileged access.** E02 and E03 require validation of the finance officer account, Microsoft 365 identity, and svc_backup. A reset or disablement may reduce risk but may also change evidence or interrupt services, so it requires an explicit decision.
5. **Protect potentially sensitive information.** The institute holds learner, admission, assessment, and finance information. Review and communications should be access-controlled without asserting that personal data was transferred.
6. **Determine whether the event has spread.** Incomplete server EDR coverage means the absence of an alert is not proof of absence. Hunt across FS01, LMS01, BAK01, identities, endpoints, and relevant logs.

### Continuity and later recovery priorities

7. **Protect and validate recovery capability.** E05 reports successful FS01/LMS01 jobs, but the scenario states that network backups are not immutable and neither route has been restoration-tested in 90 days. Candidate restore points must be validated in isolation before production use.
8. **Make an examination-continuity decision.** E07 is a confirmed learner-facing impact and the 11:00 examination is time-critical. The examination owner should consider a safe alternative, delay, or controlled service path using current technical evidence; the portal should not be reopened solely because of the deadline.
9. **Prepare recovery readiness criteria.** After scope and backup validation, the team can plan clean rebuild/restore, integrity checks, monitoring, and business approval. Detailed ordered actions are intentionally left to Task 3.

## Dependencies and tradeoffs

| Dependency or tradeoff | Why it matters |
|---|---|
| Containment versus evidence | Isolation may prevent additional changes but can remove volatile evidence or affect examination access. The selected action and expected evidence loss must be documented. |
| Credential protection versus attribution | Resetting or disabling an account may stop misuse but can alter session evidence. Preserve relevant records first where safe. |
| Examination continuity versus recovery safety | The examination deadline creates urgency, but an unverified or compromised backup must not be treated as safe merely because the portal is needed. |
| Backup validation versus recovery speed | Testing a restore takes time, but production restoration from an unverified point could reintroduce compromise or corrupt learning data. |
| Scope hunting versus limited staff | Broad analysis is necessary because server telemetry is incomplete, but the small team must sequence high-value checks and obtain support if authorized. |
| Privacy review versus operational sharing | Incident data may contain sensitive learner or employee information; use only approved channels and share the minimum necessary information. |

## Status boundary

All matrix rows are marked Not Started. This document sets priorities and decision dependencies; it does not report completed containment, collection, account changes, restoration, examination decisions, or notification outcomes.
