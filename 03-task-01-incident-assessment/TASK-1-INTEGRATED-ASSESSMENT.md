# GRC105 Task 1 — Integrated Initial Incident Assessment

**Organisation:** Northbridge Skills Institute (fictional)
**Assessment point:** 08:45 WAT on Day 0
**Current initial severity:** **High — provisional**
**Scope:** Task 1 only. No Task 2–6 content is included.

## 1. Incident classification and initial assessment

The evidence is consistent with a suspected ransomware or destructive file-impact event involving possible identity misuse, possible unauthorized transfer, and possible backup compromise. The classification is not based solely on the ransom note. It is based on the combination of observed file and learner-service impact, unusual privileged activity, uncertain data transfer, time-critical examination impact, and uncertain recovery capability.

### Initial classification: High — provisional

High is justified by:

- E06: mass file changes on FIN-PC07 and .locked files plus a ransom note in FS01 shared folders;
- E07: learners cannot open materials or submit assessments, creating confirmed learner-facing availability impact;
- E08: the FS01 incident contact list is inaccessible and corporate email trust is unverified;
- E03: svc_backup made unusual remote administrator logons to FS01 and BAK01;
- E04: FIN-PC07 uploaded 1.2 GB over HTTPS to an unfamiliar cloud-storage destination;
- the 11:00 examination for 100 learners, the institute’s sensitive information holdings, limited staffing, and uncertain backup recoverability.

The assessment is not Critical at 08:45 because the evidence does not confirm institution-wide loss, broad data disclosure, compromise of every recovery path, or persistent attacker control. The portal login still loads, staff phones are available, and the event scope and causal chain remain unverified. These limitations do not remove the urgency; they explain the provisional High decision.

### Observed, suspected, and unconfirmed impact

| Category | Current assessment |
|---|---|
| Observed impact | E06 file-change indicators on FIN-PC07/FS01; E07 learner-facing portal functions unavailable; E08 contact-list access problem; E03 unusual privileged logons; E04 upload event. |
| Suspected impact | Ransomware or destructive file activity; privileged misuse or lateral movement; dependency-driven LMS01 disruption; possible identity misuse; possible backup-risk activity. |
| Unconfirmed consequences | Malicious execution from E01; account compromise from E02; personal-data transfer in E04; BAK01 tampering; malware family; institution-wide spread; attacker identity. |
| Additional evidence needed | Endpoint process/file telemetry; Microsoft 365/MFA/device data; Windows and backup logs; proxy/cloud metadata; application and dependency checks; isolated backup validation; broader scope hunt. |

Full four-tier criteria are in analysis/severity-classification.md and data/severity-criteria.csv.

## 2. Evidence-linked timeline and uncertainty

The complete E01–E08 chronology, Day minus 1/Day 0 distinction, 08:45 WAT control point, possible relationships, and unverified-link statements remain in:

- analysis/incident-chronology.md
- data/evidence-analysis-register.csv
- diagrams/incident-timeline.mmd

The observations/hypotheses/questions separation and alternative explanations remain in analysis/observations-hypotheses-questions.md. No Stage 2 conclusion changes the Stage 1 evidence record.

## 3. Assets and scope

The asset-impact register distinguishes assets with observed impact from assets that require investigation. At 08:45:

- **Affected or service-impacted for assessment:** FIN-PC07, FS01, and LMS01.
- **Requires urgent investigation but not confirmed affected:** BAK01, Microsoft 365 identity/email, svc_backup, the finance officer account, and supporting telemetry/coordination services.
- **Potentially affected data:** learner contact, admission, assessment, finance, credential, mailbox, shared-file, backup, and response-contact information. No data category is confirmed exfiltrated.

See data/asset-impact-register.csv for business functions, evidence, confirmed impact, potential impact, priority, and verification requirements.

## 4. CIA assessment

### Confidentiality

**Potential material impact — not established.** E02, E03, and E04 create possible access or transfer paths, but none proves account compromise, unauthorized reads, or the content of the 1.2 GB upload. The institution’s information holdings make the questions important, not resolved.

### Integrity

**Observed material anomaly; scope and cause unconfirmed.** E06 shows mass file changes and .locked files/ransom note indicators. E03 creates a privileged-access integrity concern. E05 does not establish backup integrity, application consistency, or cleanliness.

### Availability

**High observed impact to important services, with examination risk.** E06 and E08 show FS01 access/file problems. E07 shows learners cannot access materials or submit assessments. The stated LMS01 dependency on FS01 and the 11:00 examination make this time-critical. Availability impact is not evidence of data disclosure.

See analysis/cia-impact-assessment.md and data/cia-impact-matrix.csv for the separate property assessments.

## 5. Response priorities

The response priority order is:

1. Check life-safety or safeguarding consequences; none are stated in the supplied scenario.
2. Establish safe coordination using staff phones or another approved channel while email trust is checked.
3. Contain suspected active compromise while preserving high-value evidence.
4. Preserve endpoint, identity, network, server, backup, application, EDR, and helpdesk records with provenance.
5. Protect the finance officer account, Microsoft 365 identity, and svc_backup through an approved decision.
6. Hunt for broader scope and protect potentially sensitive institutional information.
7. Protect and validate backup options in isolation.
8. Make an evidence-informed examination-continuity decision; do not reopen the portal solely because of the deadline.
9. Prepare validated restoration and monitoring criteria for later recovery work.

The detailed matrix is in analysis/response-prioritisation.md and data/response-priority-matrix.csv. Detailed ordered actions, custody fields, restoration acceptance criteria, and communications remain in later Task 3/4 work and are not completed here.

## 6. Severity and scope reassessment

Severity should increase to Critical if evidence confirms severe examination or institution-wide disruption, broad compromise, material data disclosure, persistent privileged control, or loss of all viable recovery options. High should be maintained while material service impact, unresolved privileged activity, uncertain data impact, or unvalidated recovery persists.

Severity may reduce only after evidence supports bounded scope, authorized identity/privileged activity, a legitimate unrelated transfer, no active destructive activity, safe service continuity, and validated recovery. An asset may be excluded from confirmed affected scope only when records show no related unauthorized access, change, persistence, or service impact and the asset is not needed to explain another observation.

The complete trigger and validation register is in analysis/severity-reassessment-triggers.md.

## 7. Evidence gaps and limitations

The assessment does not have the original attachment, complete identity/mailbox logs, endpoint process/file telemetry, source hosts and commands for svc_backup, full server/application/backup logs, cloud-destination ownership/object data, forensic images, hashes, custody records, or restoration results. Server EDR coverage is incomplete. No forensic acquisition, hash verification, restoration test, account reset, containment action, notification, or service restoration is claimed.

The High classification is therefore a defensible initial decision under uncertainty, not a final finding about attacker identity, data theft, malware family, or total scope.

## 8. References

- ICDFA GRC105 Incident Response Assignment, Northbridge Skills Institute scenario, initial evidence pack E01–E08, Task 1 instructions, and marking rubric.
- ICDFA, Incident-Response-Planning.pptx, Week 20 slides 4, 6, 9, 10, and 11.
- Nelson, A., Rekhi, S., Souppaya, M., and Scarfone, K. (2025). NIST SP 800-61r3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile. [Official NIST publication](https://doi.org/10.6028/NIST.SP.800-61r3).
