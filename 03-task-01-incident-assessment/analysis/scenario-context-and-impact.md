# Northbridge Skills Institute — Scenario Context and Impact

**Stage:** GRC105 Task 1, Stage 1 evidence analysis
**Purpose:** Record source-provided context needed for the later severity assessment without selecting a severity level.

## Source-provided facts

The following facts are taken from the Northbridge scenario in the GRC105 assignment brief. They are not investigative results.

| Context area | Source fact |
|---|---|
| Organisation | Northbridge Skills Institute is a fictional education and training provider with 1,800 learners and 90 staff. |
| Information held | The institute holds learner contact details, admission documents, assessment records, and finance files. |
| Examination | An online examination for 100 learners is scheduled for 11:00 on Day 0. |
| Response control | The Incident Response Lead assumes control at 08:45 WAT on Day 0, a Monday. All scenario times are WAT. |
| Core systems | FIN-PC07 is a finance workstation; FS01 is the shared file server; LMS01 is the learning portal; BAK01 is the network backup repository. |
| Service dependency | LMS01 depends on files stored on FS01. |
| Identity and email | Microsoft 365 provides identity and email. |
| Privileged account | The svc_backup account has administrator access to FS01 and BAK01. |
| Backup context | The last disconnected backup is from 17:00 on Day minus 3, the preceding Friday. Network backups are not immutable. Neither backup route has undergone a restoration test in the last 90 days. |
| Detection coverage | EDR covers workstations, but server coverage is incomplete. |
| Available staffing | The IT team has three staff and one security analyst. |

## Operational implications for later assessment

These are analytical implications of the facts above, not findings about what has happened.

### Examination availability

The 11:00 examination creates a time-critical availability and continuity constraint. E07 records that learners cannot open materials or submit assessments, while LMS01 depends on FS01 files. The future assessment should distinguish confirmed learner-facing service impact from the still-unverified cause and extent of LMS01 damage. It should also consider whether any response action could preserve evidence while affecting examination access.

### Information confidentiality

The information categories held by the institute make identity anomalies, the E04 upload, shared-file access, and any cloud-destination activity relevant to confidentiality. The evidence pack does not establish that personal, finance, admission, assessment, or contact data was transferred. The 1.2 GB volume must not be treated as proof of personal-data exfiltration.

### Information integrity

E06 records mass file changes on FIN-PC07 and .locked files plus a ransom note in FS01 shared folders. These observations support an integrity investigation, but they do not establish the malware family, the execution path, the full set of changed files, or whether LMS01 data was altered. A reported backup job is not an integrity or cleanliness result.

### Information and service availability

The reported FS01 file condition, the LMS01 learner-facing restriction in E07, and the inaccessible FS01 contact list in E08 create potential availability consequences across shared files, learning services, examination workflows, and response coordination. The portal login page loading does not prove that LMS01 is fully available or that LMS01 itself is damaged.

### Limited staffing

Three IT staff and one security analyst may constrain simultaneous containment, evidence preservation, service validation, communications, and examination-continuity work. This is a response-capacity consideration, not evidence that a particular action has been delayed or completed.

### Uncertain backup recoverability

The last disconnected backup timestamp, lack of immutability for network backups, and absence of restoration testing in the preceding 90 days increase uncertainty around recovery options. E05 reports successful FS01/LMS01 jobs, but that report does not establish that a restore point is complete, usable, or free of compromise. Any later severity assessment should treat recoverability as requiring controlled validation.

## Inputs to the future severity assessment

The later Task 1 severity assessment should weigh:

- the confirmed learner-facing availability impact and the 11:00 examination deadline;
- the number and criticality of potentially affected systems, while separating confirmed from suspected scope;
- the categories of information held and the unresolved possibility of access or transfer;
- observed file changes and service disruption versus unverified ransomware, identity, and exfiltration hypotheses;
- the trustworthiness and tested recoverability of available backups;
- the limited local response capacity and the need to preserve evidence while maintaining essential services.

This document intentionally does **not** assign Critical, High, Medium, or Low severity. It provides context for that decision only.

## Source traceability

- ICDFA GRC105 Incident Response Assignment, Northbridge Skills Institute scenario and initial evidence pack, especially the organisation, systems, backup, staffing, and examination facts.
- Initial evidence pack: E05, E06, E07, and E08 for the observed backup, file, portal, and coordination conditions.
- Incident-Response-Planning.pptx, Week 20 slides 4, 6, 9–11 for CIA impact, classification inputs, correlation, containment, and recovery validation concepts.
