# Northbridge Preparation Improvements

**Status:** Proposed readiness actions for Task 2 completion; none are represented as implemented.  
**Baseline:** High — provisional incident classification at 08:45 WAT on Day 0; three IT staff and one security analyst.

These improvements address preparation weaknesses identified in the Northbridge scenario and in the Task 1 assessment. They support the course preparation stage and the NIST SP 800-61 Rev. 3 CSF 2.0-aligned preparation functions; they do not claim that a control is currently deployed.

## Improvement register

| ID | Control weakness | Proposed improvement | Accountable owner | Resources required | Priority | Measurable readiness check |
|---|---|---|---|---|---|---|
| PI-01 | The latest disconnected backup is from 17:00 WAT on Day minus 3; network backups are not immutable and restoration testing has not occurred in the preceding 90 days. | Define backup tiers, protect at least one offline or logically isolated copy, document backup ownership, and perform scheduled isolated restoration tests for FS01 and LMS01 with integrity and application checks. | Senior Management / Executive Sponsor, with IT Operations and Recovery Lead | Backup storage or isolation capability, test environment, documented runbook, protected test data, recovery specialist support if required | Critical preparation gap | A dated test record demonstrates restoration of representative FS01 and LMS01 data, records integrity results and limitations, and identifies an approved recovery decision. |
| PI-02 | The incident contact list is stored on FS01 and is inaccessible during the incident; corporate email trustworthiness is unverified. | Maintain an independently accessible, access-controlled contact list; record verified telephone contacts; approve an alternate communication channel; rehearse identity verification and sensitive-information handling. | Senior Management / Executive Sponsor, coordinated by Communications Coordinator and BCC | Controlled offline or separately hosted contact record, verified phone list, approved alternate channel, periodic access review and exercise | High | During an exercise, authorised responders retrieve the list without FS01, complete an out-of-band identity check, and record a notification without using untrusted email as the sole channel. |
| PI-03 | EDR covers workstations but server coverage is incomplete, reducing visibility across FS01, LMS01 and backup-related activity. | Complete a server-monitoring coverage assessment; deploy or approve compensating logging and alerting for FS01, LMS01 and BAK01; define retention, alert ownership and escalation paths. | IT Operations and Recovery Lead with Security Analyst | Server EDR or compensating telemetry, log storage, tuning time, service-owner coordination, provider support if needed | High | A coverage register shows each in-scope server, telemetry source, alert owner, retention setting and a documented test alert or approved exception. |
| PI-04 | Staff roles, dual-hatting, examination continuity and evidence-preservation decisions have not been exercised under the four-person technical capacity constraint. | Run role-based incident-response training and a tabletop covering command, containment, evidence, communications, continuity and recovery gates; record corrective actions and review the RACI. | Incident Response Lead, with Senior Management approval | Facilitator time, role briefings, scenario injects, communication fallback, decision log, protected exercise records | High | A completed exercise record shows each required role participating or assigned, at least three success criteria assessed, decisions recorded, and corrective actions assigned with evidence. |

## Implementation and governance notes

- These are proposed controls, not evidence of completed deployment, testing or engagement.
- Senior Management retains approval for material resource commitments, risk acceptance, formal appointments and material continuity decisions.
- The Incident Response Lead coordinates operational readiness reviews but cannot certify that a backup is clean or restorable without validation evidence.
- The BCC coordinates authorised continuity preparations and cannot override security validation, containment or business acceptance gates.
- Readiness evidence should be stored in a controlled location separate from the potentially affected FS01 service, with access restricted to authorised governance, security and technical roles.

## Sources

- ICDFA, *GRC105 Incident Response Planning Assignment*, Task 2 and rubric.
- ICDFA, *Incident Response Planning*, Week 20 slides 7–8, 14–15 and 18.
- NIST, *SP 800-61 Rev. 3*, CSF 2.0-aligned incident-response guidance: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- CISA and partners, *#StopRansomware Guide*: https://www.cisa.gov/stopransomware/ransomware-guide
