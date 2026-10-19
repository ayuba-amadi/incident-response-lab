# Northbridge Skills Institute — Incident Chronology

**Stage:** GRC105 Task 1, Stage 1 — evidence analysis only
**Timezone:** West Africa Time (WAT)
**Evidence basis:** The supplied GRC105 assignment brief and its initial evidence pack. Evidence IDs E01–E08 are retained exactly. No forensic acquisition, hash verification, restoration test, or attacker attribution is claimed.

## Time notation and control point

The assignment defines Day 0 as Monday and records the earlier event as **Day minus 1**. The timeline therefore keeps the supplied day notation instead of converting events into an inferred calendar date. The Incident Response Lead assumes control at **08:45 WAT on Day 0**, coinciding with the operations report in E08. That control point is a scenario fact and response decision, not a new forensic finding.

## Chronological sequence

| Time (WAT) | Evidence | Direct observation from the evidence pack | Working interpretation | What remains unverified |
|---|---|---|---|---|
| Day minus 1 16:40 | E01 | A finance officer opened an unexpected payroll attachment on FIN-PC07. | The attachment is a possible initial-access lead. | Malicious code execution, attachment content, process creation, and any relationship to later events are unverified. |
| Day 0 01:15 | E02 | The finance officer's Microsoft 365 account signed in from an unfamiliar IP and new device. | This is an identity anomaly that may be related to E01. | MFA outcome, device/user attribution, token use, account changes, and compromise are unverified. |
| Day 0 01:35 | E03 | svc_backup made remote administrator logons to FS01 and BAK01 outside its usual schedule. | This is a privileged-access anomaly affecting file and backup infrastructure. | Authorization, source host, commands, changes, and relationship to E01/E02 are unverified. |
| Day 0 01:50 | E04 | FIN-PC07 uploaded 1.2 GB over HTTPS to unfamiliar cloud storage. | The upload is a possible data-transfer or staging lead. | Content, destination ownership, process, completion, and personal-data involvement are unverified. |
| Day 0 02:00 | E05 | The backup console reported successful jobs for FS01 and LMS01. | The report may identify candidate recovery points. | Recoverability, application consistency, integrity, and absence of compromise are unverified. |
| Day 0 08:30 | E06 | Mass file changes occurred on FIN-PC07; FS01 shared folders contained .locked files and a ransom note. | The indicators are consistent with a ransomware working hypothesis affecting FIN-PC07 and FS01. | Malware execution path, family, encryption scope, attacker identity, and root cause are unverified. |
| Day 0 08:40 | E07 | The LMS01 login page loaded, but learners could not open materials or submit assessments. | The learner-facing service is impaired; FS01 dependency is a possible explanation. | LMS01 damage, cause, data impact, and examination recoverability are unverified. |
| Day 0 08:45 | E08 | The incident contact list on FS01 was inaccessible; staff phones were available and corporate email trust was unverified. | Normal coordination may be impaired, so phone-based coordination is available while email trust is checked. | Cause of contact-list inaccessibility and email trustworthiness are unverified. |
| Day 0 08:45 | Response control point | The Incident Response Lead assumes control. | This establishes the response-management starting point for subsequent planning. | It does not establish containment, evidence preservation, or any completed investigation. |

## Possible relationships between events

The sequence supports several **investigative relationships**, but the evidence pack does not prove causation:

1. E01 → E02 is a possible identity sequence: an attachment event precedes an unfamiliar Microsoft 365 sign-in. The timing makes the relationship worth testing; it does not prove execution, credential theft, or account compromise.
2. E02/E03 may indicate a broader identity or privileged-access path. The account types and systems differ, and the supplied records do not identify a common source, operator, token, or command.
3. E03 → E05 is operationally relevant because svc_backup has administrator access to FS01 and BAK01 and a later console report describes successful FS01/LMS01 jobs. This is a correlation requiring log and restore validation, not proof that the account altered backups or that the backups are safe.
4. E01/E04 may place FIN-PC07 in both the initial-access investigation and the transfer investigation. The proxy identifies the workstation as the upload source, but it does not establish who initiated the transfer or what it contained.
5. E03/E06 may connect privileged access with later file changes on FS01. This is a high-value hypothesis because FS01 contains .locked files and a ransom note, but the event records do not show the commands, source host, or causal chain.
6. E06/E07 may be related through the stated dependency of LMS01 on files stored on FS01. The portal impact could instead be an independent application, network, permission, or authentication fault.
7. E06/E08 show operational consequences in the same time window: affected FS01 content and an inaccessible contact list. The contact-list issue may be part of the same availability problem or a separate access/document issue.

### Correlation versus causation

Temporal proximity, shared assets, and a common account or workstation are **correlation signals**. They are not proof that one event caused another. Causation would require corroborating endpoint, identity, server, network, backup, and application evidence. No statement in this chronology should be read as confirming malicious execution from E01, compromise from E02, attacker access through svc_backup, personal-data transfer in E04, clean/restorable backups in E05, or a confirmed malware family in E06.

## Significant unverified links

- **E01–E02:** Unknown whether the attachment produced code execution, credential exposure, or any identity activity.
- **E02–E03:** Unknown whether the finance identity, a separate administrator, automation, or an attacker connects the Microsoft 365 and svc_backup anomalies.
- **E03–E05:** Unknown whether the remote logons changed backup state or whether the reported jobs are complete, restorable, and clean.
- **E01/E04:** Unknown whether the 1.2 GB upload was caused by the attachment, a legitimate process, or unrelated activity, and unknown what data it contained.
- **E03–E06:** Unknown whether svc_backup activity caused, enabled, or merely preceded the FS01 file changes.
- **E06–E07:** Unknown whether FS01 file availability caused the LMS01 impact or whether LMS01 has an independent fault.
- **E06–E08:** Unknown whether the inaccessible contact list is a consequence of the same FS01 condition or a separate permissions/share issue.

## Stage boundary

This artifact documents evidence, hypotheses, and investigation needs. It deliberately does **not** select a Critical/High/Medium/Low severity tier. Severity classification, CIA assessment in decision form, and the remaining Task 1 requirements require the next approved stage.
