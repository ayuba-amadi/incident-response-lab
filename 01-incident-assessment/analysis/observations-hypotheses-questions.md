# Observations, Hypotheses, and Unresolved Questions

**Scope:** GRC105 Task 1, Stage 1 evidence analysis for the fictional Northbridge Skills Institute scenario.
**Interpretation rule:** “Confirmed” means directly stated in the supplied evidence pack. “Working hypothesis” means a reasonable explanation to test. Neither category should be read as attacker attribution or a completed investigation.

## 1. Confirmed observations

| Evidence | Confirmed observation |
|---|---|
| E01 | A finance officer opened an unexpected payroll attachment on FIN-PC07. Execution of malicious code is not verified. |
| E02 | The finance officer's Microsoft 365 account signed in from an unfamiliar IP and new device. MFA status and user involvement are unknown. |
| E03 | svc_backup made remote administrator logons to FS01 and BAK01 outside its usual schedule. The reason is unknown. |
| E04 | FIN-PC07 uploaded 1.2 GB over HTTPS to unfamiliar cloud storage. The record does not identify the transferred content. |
| E05 | The backup console reported successful FS01 and LMS01 jobs. Recoverability and freedom from compromise are not established. |
| E06 | EDR/helpdesk records show mass file changes on FIN-PC07; FS01 shared folders contain .locked files and a ransom note. The malware family is unconfirmed. |
| E07 | The LMS01 login page loads, but learners cannot open materials or submit assessments. The scope of LMS01 damage is unknown. |
| E08 | The incident contact list on FS01 is inaccessible. Staff phones are available and corporate email trust is unverified. The Incident Response Lead assumes control at 08:45 WAT on Day 0. |

## 2. Working hypotheses

These hypotheses are investigation leads, not findings:

1. **Possible ransomware activity:** E06 is consistent with ransomware affecting FIN-PC07 and FS01 because of the combination of mass file changes, .locked files, and a ransom note. The malware family, execution path, and scope remain unconfirmed.
2. **Possible attachment-related initial access:** E01 may precede later identity, endpoint, or transfer activity. No malicious execution from the attachment has been confirmed.
3. **Possible identity misuse:** E02 may reflect stolen credentials, a stolen session, or another unauthorized use. An unfamiliar IP and device alone do not establish account compromise.
4. **Possible privileged lateral movement or backup-risk activity:** E03 may represent misuse of svc_backup and access to FS01/BAK01. It may also be authorized maintenance, automation, or schedule/logging drift.
5. **Possible data transfer or staging:** E04 may represent exfiltration or staging from FIN-PC07. The 1.2 GB volume does not establish that personal data, finance data, or any confidential data was transferred.
6. **Possible recovery-point uncertainty:** E05 may identify usable restore points, but a successful backup job is not evidence that the data is restorable, complete, or clean.
7. **Possible dependency-driven service impact:** E07 may be explained by LMS01's stated dependency on FS01, but an independent LMS01, network, authentication, or permissions fault remains plausible.
8. **Possible response-coordination impairment:** E08 may reflect FS01 availability or access-control impact. The contact list could instead be unavailable because of a document or permissions issue; email trust is not established.

### Plausible alternative explanations for ambiguous events

At least two alternatives must remain open while evidence is incomplete:

- **E01/E02 alternative:** the attachment was benign or only previewed, and the unfamiliar sign-in was legitimate use of a new device, VPN, proxy, or mobile network. This is not evidence that the later events are unrelated; it is a competing explanation to test.
- **E03/E05 alternative:** the svc_backup activity and backup success report reflect scheduled maintenance or an automated job with schedule drift, while the console reports completion without proving application-consistent restoration. This competes with the hypothesis of unauthorized privileged access.
- **E04 alternative:** the HTTPS upload was a legitimate backup, synchronization, software update, or approved large-file transfer. The proxy record alone cannot distinguish this from data staging.
- **E06/E07 alternative:** a software fault, authorized bulk operation, permissions issue, network problem, or application fault explains some observations without requiring a single ransomware chain. The ransom note and .locked files make this explanation important to test rather than accept or dismiss.

## 3. Unresolved investigation questions

1. Was the E01 attachment opened, previewed, or executed, and what process/file/network activity followed it?
2. Was the E02 Microsoft 365 sign-in authorized, how was MFA satisfied, and what mailbox, token, device, or identity changes followed?
3. What source hosts, commands, and changes were associated with the E03 svc_backup logons to FS01 and BAK01?
4. What process and files generated the E04 1.2 GB upload, who controlled the destination, and did the transfer complete?
5. Did the E03 activity alter, delete, encrypt, or expose BAK01 data or backup configuration?
6. Can an FS01/LMS01 restore point be restored in an isolated environment and checked for integrity, application consistency, and relevant indicators?
7. What process caused the E06 mass file changes and what is the confirmed extent of affected files, shares, hosts, and identities?
8. Is the E07 LMS01 impact caused by FS01 dependency, an LMS01 fault, or another access/network condition?
9. Could learner, finance, admission, assessment, credential, or response-contact data have been accessed or transferred?
10. Is corporate email trustworthy for incident coordination, and what alternate contact records are available while E08 remains unresolved?

## Evidence and procedure limitations

- The evidence pack contains observations, not acquired forensic images or a complete log set.
- No hashes, chain-of-custody events, restoration results, malware identification, or notification determinations exist at this stage.
- Server EDR coverage is incomplete; absence of a server alert would not prove absence of server activity.
- The scenario states that the last disconnected backup is from 17:00 on Day minus 3, network backups are not immutable, and neither backup route has been restoration-tested in the last 90 days. These are context facts, not evidence that any particular backup is compromised or unusable.
- All recommended collection, validation, interviews, and restoration checks remain planned/not investigated.
