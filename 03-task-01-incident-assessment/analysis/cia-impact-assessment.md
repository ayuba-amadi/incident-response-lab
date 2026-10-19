# Northbridge Skills Institute — CIA Impact Assessment

**Assessment point:** 08:45 WAT on Day 0.
**Purpose:** Assess confidentiality, integrity, and availability separately without converting unverified consequences into findings.

## Assessment scale

- **High observed:** a material consequence is directly reported in the evidence pack.
- **High potential:** a material consequence is plausible and urgent, but not established.
- **Medium potential:** a meaningful consequence is possible and requires verification.
- **Medium observed:** a current operational or coordination effect is directly reported but is not yet institution-wide.
- **Unknown / not established:** the evidence is insufficient to determine impact.
- **Low current:** no direct material impact is reported for the property at this time.

These labels are analytical descriptions, not numeric scores and not a substitute for the overall High provisional severity decision.

## Confidentiality

**Overall assessment: Potential material confidentiality impact — not established.**

E02 records an unfamiliar Microsoft 365 sign-in and new device, but does not establish account compromise, MFA bypass, user involvement, mailbox access, or token theft. E03 records unusual administrator logons by svc_backup to FS01 and BAK01, but does not establish unauthorized access or data reads. E04 confirms a 1.2 GB HTTPS upload from FIN-PC07 to an unfamiliar cloud-storage destination, but the proxy record does not identify the content, destination owner, process, completion state, or whether personal data was involved.

The institute holds learner contact details, admission documents, assessment records, and finance files. That context makes the unresolved identity and transfer questions important, but it does not prove that any of those categories were accessed or transferred. The current assessment therefore separates the potential for material disclosure from confirmed disclosure.

**Evidence needed:** Microsoft 365 sign-in/MFA/token/mailbox records; finance-user interview; endpoint process and file telemetry; proxy/DNS/firewall records; cloud destination ownership and object metadata; FS01/BAK01 access logs; data-owner classification.

## Integrity

**Overall assessment: Observed material integrity anomaly; scope and cause unconfirmed.**

E06 directly records mass file changes on FIN-PC07 and .locked files plus a ransom note in FS01 shared folders. This is stronger than a simple anomaly and supports urgent investigation of file integrity, but it does not by itself prove malicious code execution, encryption, a malware family, attacker identity, or the full set of affected files. E03 creates a separate privileged-access integrity concern because svc_backup administers FS01 and BAK01. E05 does not establish backup integrity, application consistency, or cleanliness.

Integrity should be assessed separately for live files, identity/configuration state, backup configuration and restore points, LMS01 content, and the provenance of logs. A successful backup report cannot be used as an integrity conclusion.

**Evidence needed:** EDR and file-event data; FS01 share/file metadata; Windows, PowerShell, task, and administrator logs; LMS01 application and database checks; backup-console audit/configuration and snapshot metadata; isolated restoration and integrity validation.

## Availability

**Overall assessment: High observed availability impact to important services, with examination risk.**

E06 reports affected FS01 shared folders and E08 reports the contact list is inaccessible. E07 directly reports that learners cannot open materials or submit assessments even though the LMS01 login page loads. The scenario states that LMS01 depends on files stored on FS01. An online examination for 100 learners is scheduled for 11:00 on Day 0, so the learner-facing disruption is time-critical. The impact is material, but the evidence does not establish that LMS01 itself is encrypted, that all FS01 services are unavailable, or that the examination cannot be delivered by an approved alternative.

Availability is not confidentiality. The current availability finding does not imply that learner or finance data was disclosed.

**Evidence needed:** controlled LMS01 functional tests; FS01 share and dependency checks; application, database, authentication, and network logs; examination-owner decision on continuity options; safe restoration-readiness validation.

## Asset-level reference

The full asset-by-property assessment, including E01–E08 references and verification requirements, is in data/cia-impact-matrix.csv. The corresponding asset scope and status assessment is in data/asset-impact-register.csv.

## NIST and course alignment

The analysis follows the Week 20 teaching deck’s separation of detection/analysis, classification, containment, eradication, and recovery, while using the current NIST SP 800-61r3 emphasis on incident categorization, risk-based prioritization, magnitude validation, evidence provenance, containment, and validated recovery. See [NIST SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), RS.MA-03, RS.AN-07, RS.AN-08, RS.MI-01, and RC.
