# Northbridge Skills Institute — Severity and Scope Reassessment Triggers

**Current position:** High — provisional at 08:45 WAT on Day 0.
**Purpose:** Define evidence-based conditions for changing or narrowing the assessment. No trigger below is claimed to have occurred.

## Increase the severity to Critical

| Trigger condition | Evidence or validation required | Assessment effect |
|---|---|---|
| The 11:00 examination or another essential institutional function cannot be delivered, and no safe continuity alternative exists. | Business-owner decision, controlled LMS01 tests, dependency checks, and continuity records. | Escalates functional and time-critical impact from material to severe. |
| Confirmed destructive or persistent activity extends across multiple core systems, including FS01/LMS01 plus FIN-PC07, BAK01, Microsoft 365, or other critical assets. | EDR/server telemetry, Windows and identity logs, file-event analysis, and validated scope inventory. | Escalates from suspected multi-asset exposure to confirmed broad compromise. |
| BAK01 or all viable recovery paths are confirmed deleted, tampered with, encrypted, or unusable, with no validated clean alternative. | Backup audit/configuration records, snapshot metadata, isolated restoration, and recovery-owner validation. | Converts recovery uncertainty into severe availability and resilience impact. |
| Unauthorized access or transfer of a material population of learner, finance, admission, assessment, credential, or mailbox data is confirmed. | File-access and identity logs, endpoint/proxy/cloud records, destination ownership, and privacy/legal assessment. | Escalates confidentiality impact and may require formal reporting decisions. |
| Confirmed identity compromise provides continuing privileged access or broad M365 control. | MFA/token/session records, account-change audit, source-host analysis, and authorized account-owner interview. | Escalates threat persistence and likely scope. |

## Maintain High

| Condition | Evidence or validation required | Reason |
|---|---|---|
| FS01 or LMS01 disruption remains material, the examination remains at risk, and the cause or scope is unresolved. | Controlled service tests, examination-owner status, application/server logs, and updated impact record. | Availability remains high even without confirmed data disclosure. |
| E03 remains unexplained or shows unauthorized privileged activity, while BAK01 trust is unresolved. | Source-host, command, authorization, backup-console, and configuration analysis. | Privileged and recovery uncertainty continue to justify urgent response. |
| E04 content and E02 identity status remain unknown while relevant data could plausibly be involved. | Cloud/object, endpoint, Microsoft 365, and data-owner checks. | Confidentiality risk remains material but unconfirmed. |
| The event is contained to the currently known assets but recovery is not yet validated. | Scope hunt, containment records, backup validation, and integrity testing. | High remains appropriate until safe recovery and bounded scope are demonstrated. |

## Support reducing severity

| Condition | Evidence or validation required | Possible result |
|---|---|---|
| E02 and E03 are confirmed authorized, with no related account, file, configuration, or persistence changes. | Microsoft 365, Windows, backup-console, task, source-host, and owner records. | Removes a major suspected compromise path; may support Medium if availability is bounded. |
| E04 is verified as an approved transfer of unrelated, non-sensitive content and no recurrence or suspicious process is found. | Endpoint process/file records, proxy/cloud metadata, approved-transfer records, and destination confirmation. | Reduces confidentiality concern and may narrow scope. |
| E06 is explained by a localized non-malicious fault or authorized operation, with no malware indicators or spread. | EDR/process analysis, file metadata, independent technical validation, and scope hunt. | Reduces the suspected ransomware/destructive-impact component. |
| LMS01 and examination workflows are restored or safely supported, FS01 impact is bounded, and no other critical assets are affected. | Controlled functional tests, business-owner confirmation, and dependency validation. | May reduce availability impact to Medium if recovery is trustworthy. |
| A clean, complete, application-consistent recovery point is validated in isolation and recovery remains available. | Isolated restoration, integrity checks, malware-indicator checks, and backup-owner sign-off. | Reduces recoverability uncertainty; it does not by itself remove current impact. |

Low would require a stronger showing: no material CIA impact, no credible active-compromise signal, and a bounded benign explanation. The current E06/E07/E08 observations make Low inappropriate unless material impact is disproved.

## Expand incident scope

Scope expands if validation identifies:

- persistence, file changes, or suspicious access on hosts beyond FIN-PC07 and FS01;
- LMS01 application, database, authentication, or content changes;
- unauthorized Microsoft 365 mailbox, token, MFA, consent, or forwarding-rule activity;
- unauthorized use of the finance officer account or svc_backup;
- BAK01 configuration, retention, snapshot, or restore-point changes;
- additional cloud destinations, repeated transfers, or content linked to institutional information;
- access to learner, admission, assessment, finance, credential, or response-contact data.

Each expansion requires corroborating logs, artifacts, interviews, or controlled validation. It must not be inferred from time proximity alone.

## Support excluding an asset from confirmed affected scope

An asset may be excluded from the **confirmed affected** scope only when the relevant records show no related unauthorized access, file/configuration change, persistence, or service impact, and the asset is not required to explain another confirmed observation. Exclusion from confirmed scope does not mean the asset was never investigated or can be ignored in a broader hunt.

## Reassessment discipline

Record the evidence reviewed, the decision owner, the time and WAT, the resulting severity/scope decision, and any remaining uncertainty. Reassessment should occur after the first high-value validation results and before restoration, major account changes, or reopening a critical service.
