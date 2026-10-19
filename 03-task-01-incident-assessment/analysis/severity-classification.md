# Northbridge Skills Institute — Initial Severity Classification

**Assessment point:** 08:45 WAT on Day 0, when the Incident Response Lead assumes control.
**Initial classification:** **High — provisional**.
**Incident type:** Suspected ransomware or destructive file-impact event with possible identity misuse, possible unauthorized transfer, and possible backup compromise. The type remains subject to validation.

## Assessment method

The classification uses the confirmed evidence, the scenario context, and the distinction between observed impact, suspected impact, and unconfirmed consequences. It does not classify the event solely because a ransom note was reported. The decision considers asset criticality, functional impact, data impact, activity stage, suspected scope, recoverability, time-criticality, and limited response capacity.

This approach aligns with NIST SP 800-61r3 guidance to validate incident reports, estimate severity and urgency, categorize incidents, and prioritize them using scope, likely impact, time-criticality, resource availability, asset criticality, data impact, activity stage, threat-actor characterization, and recoverability. See the official [NIST SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), RS.MA-02, RS.MA-03, and the related discussion of risk evaluation factors.

## Four-tier severity criteria

| Level | Operational and business impact | CIA implications | Scope and escalation | Response expectation |
|---|---|---|---|---|
| **Critical** | Confirmed or imminent institution-wide disruption, multiple critical services affected, or an essential examination/core function cannot be delivered. | Confirmed broad disclosure, widespread destructive change, persistent control, or recovery mechanisms compromised. | Multiple core systems, identities, recovery assets, or business functions confirmed affected. Immediate executive escalation. | Immediate full mobilisation, containment, continuity activation, external support as authorised, and validated recovery governance. |
| **High** | Material impact to a critical service or multiple important assets; active or suspected compromise; a time-critical deadline; or significant uncertainty about scope/recoverability. | Potential material exposure of sensitive or personal information, observed material integrity anomalies, or material availability disruption without confirmed institution-wide loss. | Core systems plus related identities, privileged accounts, or recovery infrastructure involved or requiring urgent investigation. Rapid management escalation. | Contain suspected active compromise while preserving evidence; protect credentials/backups; scope assets; coordinate privacy and business owners; validate recovery. |
| **Medium** | Limited or localized impact with essential operations continuing and a credible recovery path. | Bounded or low-confidence confidentiality concern, localized integrity anomaly, or non-critical availability degradation. | One endpoint, account, or narrowly bounded service with no confirmed lateral movement or recovery compromise. | Proportionate containment, investigation, evidence retention, monitoring, and approved restoration. |
| **Low** | Isolated anomaly or policy event with no material CIA impact and no credible active-compromise signal. | No credible unauthorized disclosure and no material integrity or availability consequence. | Single low-criticality asset or event with no plausible spread. | Routine handling, documentation, validation, and closure or monitoring. |

The full criteria are also recorded in data/severity-criteria.csv for traceable reuse.

## Evidence at 08:45 WAT

### Observed impact

- **E06:** Mass file changes are reported on FIN-PC07; FS01 shared folders contain .locked files and a ransom note. The malware family is unconfirmed.
- **E07:** The LMS01 login page loads, but learners cannot open materials or submit assessments. This is a confirmed learner-facing availability impact.
- **E08:** The FS01 incident contact list is inaccessible. Staff phones are available and corporate email trust is unverified.
- **E03:** svc_backup made remote administrator logons to FS01 and BAK01 outside its usual schedule. The logons are observed; authorization and resulting changes are unknown.
- **E04:** FIN-PC07 uploaded 1.2 GB over HTTPS to an unfamiliar cloud-storage destination. The upload is observed; content and completion are unknown.

### Suspected impact

- E06 is consistent with ransomware or another destructive file-impact event affecting FIN-PC07 and FS01.
- E03 may represent unauthorized privileged access, lateral movement, or backup-risk activity.
- E01 and E02 may form an attachment-to-identity sequence, but execution, credential use, and account compromise are unverified.
- E07 may reflect the stated LMS01 dependency on FS01, but an independent LMS01, network, permission, or authentication fault remains possible.
- E05 may identify candidate recovery points, but backup recoverability, integrity, and cleanliness are unverified.

### Unconfirmed consequences

- Malicious code execution from the E01 attachment.
- Compromise of the finance officer account or Microsoft 365 identity.
- Attacker use of svc_backup.
- Personal-data, finance-data, or any confidential-data transfer in E04.
- Destruction, encryption, or tampering with BAK01.
- Institution-wide compromise, malware attribution, or confirmed causal links between the events.

## Rationale for High — provisional

High is appropriate because the evidence already demonstrates material availability impact to learner-facing functions shortly before an examination for 100 learners, suspicious activity involving a privileged account and the backup repository, file-impact indicators on a shared server, an inaccessible response contact list, and uncertain recovery capability. The institute also holds learner, admission, assessment, and finance information, and has only three IT staff and one security analyst.

The assessment is not Critical at this point because the evidence does not confirm institution-wide loss, broad data disclosure, compromise of all recovery options, or confirmed persistent attacker control. The portal login still loads, staff phones remain available, and the scope and cause of the file changes are not established. These facts do not make the situation safe; they explain why High is a provisional assessment rather than an asserted Critical classification.

The 11:00 examination matters because it converts the observed learner-facing disruption into a time-critical business decision. The privileged account and backup uncertainty matter because they could affect both the scope of compromise and the safety of restoration. Neither factor proves a compromise or dictates a particular recovery action.

## Initial response expectation

At High, management and the Incident Response Lead should be notified rapidly, the available team should coordinate containment and evidence preservation, credentials and recovery assets should receive immediate protection, and the examination owner should be engaged for continuity decisions. Severity should be reassessed after the first verification results or before any restoration or major service-return decision.

This is an initial working assessment, not a completed investigation and not a finding that every listed system or data category is compromised.

## Source references

- ICDFA GRC105 Incident Response Assignment, Task 1, Northbridge scenario, initial evidence pack E01–E08, and marking rubric.
- ICDFA, Incident-Response-Planning.pptx, Week 20 slides 4, 6, 9, 10, and 11.
- Nelson, A., Rekhi, S., Souppaya, M., and Scarfone, K. (2025), NIST SP 800-61r3, especially RS.MA-02, RS.MA-03, RS.AN-08, RS.MI-01, and RC. See the [official NIST publication](https://doi.org/10.6028/NIST.SP.800-61r3).
