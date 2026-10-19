# Northbridge Skills Institute — Task 3 Response Playbook

**Status:** Fictional operational plan — all actions are planned, not executed.  
**Incident position:** High — provisional at 08:45 WAT on Day 0.  
**Scenario basis:** E01–E08 and approved Task 1/Task 2 governance artifacts.

## 1. Operating rules

This playbook is a proposed response sequence for the suspected ransomware incident. It does not report live containment, acquisition, eradication, restoration, or monitoring results. Action owners are functional roles from the approved Task 2 CSIRT design. The Incident Response Lead (IRL) authorises normal containment; IT Operations executes within scope. Emergency containment is limited to the approved condition where normal approval is unavailable and delay may materially worsen harm.

All times are WAT. E01–E08 are source observations. Hypotheses, proposed actions, and unverified consequences remain labelled as such. Planned evidence is recorded in [data/evidence-register.csv](data/evidence-register.csv).

## 2. Ordered response actions

The structured action register is [data/response-actions.csv](data/response-actions.csv). It contains the first 60 minutes, the remainder of the first 24 hours, and later recovery/closure stages.

### First 60 minutes — 08:45 to 09:45 WAT

1. Establish the incident record at 08:45, preserve the approved High — provisional classification, and record E01–E08, uncertainty and the 11:00 examination dependency.
2. Use verified telephone calls because the FS01 contact list is inaccessible and corporate email trust is unverified (E08).
3. Preserve accessible EDR, Windows, proxy, Microsoft 365 and backup-console records before disruptive changes where delay is safe.
4. Contain FIN-PC07 under IRL authorisation, recording scope and expected operational impact (E01, E04, E06).
5. Protect the finance officer account and `svc_backup` through a documented identity-control decision, preserving sign-in and administrator-logon records first where practicable (E02–E03).
6. Assess FS01 and LMS01 dependency and contain FS01 if active propagation or continued encryption is suspected; document the availability tradeoff (E06–E07).
7. Preserve the E04 proxy record and request provider-side metadata; do not infer the uploaded content or personal-data disclosure.
8. Remove BAK01 from potentially exposed administrative paths or backup jobs only within approved scope; do not restore from an unvalidated backup (E03, E05).
9. Convene the IRL, Security Analyst, IT Operations, BCC and Academic/Business Service Owner to decide whether the 11:00 examination can safely proceed, requires an alternative arrangement, or must remain pending.
10. Record the next decision point and issue a fact-bounded internal update through an approved channel.

### Remainder of first 24 hours — 09:45 Day 0 to 08:45 Day 1

11. Correlate FIN-PC07, FS01, LMS01, BAK01, Microsoft 365, `svc_backup`, proxy and EDR records to test the entry-point and lateral-movement hypotheses.
12. Determine whether the finance attachment was executed; preserve mail headers, attachment metadata and endpoint execution artifacts. Do not assume execution from E01.
13. Investigate the unfamiliar Microsoft 365 sign-in, new device, MFA state, session/token activity and finance-user involvement (E02).
14. Investigate `svc_backup` logon source, schedule deviation, command or service activity and BAK01 access (E03); do not equate unusual activity with attacker control.
15. Assess whether the E04 transfer is connected to the incident and what content, if any, can be established from proxy, endpoint and cloud-provider records.
16. Search for persistence and broader compromise across endpoints, servers, identity, scheduled tasks, services, remote administration, privileged groups, email rules, tokens and network indicators.
17. Define the eradication plan: preserve required evidence, remove persistence, rebuild or reimage affected systems from known-good sources, close the entry point, rotate credentials, revoke sessions and apply compensating controls.
18. Validate BAK01 and any candidate backup in an isolated environment. Check malware indicators, permissions, timestamps, application consistency, expected files and recovery logs before considering restoration.
19. Restore only approved services in dependency order after technical, security, integrity and business gates pass: controlled identity/communications dependencies, FS01 or an approved alternative, then LMS01 and other priority services. FIN-PC07 returns only after endpoint rebuild and credential controls.
20. Monitor restored systems and privileged activity for recurrence, record exceptions and unresolved scope questions, and obtain Business Service Owner acceptance before return to normal service.
21. Close only when evidence, decisions, impact, communications, residual risk, follow-up owners and management/business approvals are recorded; otherwise keep the incident open or under recovery.

## 3. Difficult decisions

### Containment versus evidence preservation

E06 shows active mass file changes and locked files, while E01–E04 provide possible entry, identity, privileged-access and transfer leads. The default is to preserve volatile and high-value records before disruptive changes where safe. If active encryption, propagation or privileged exposure makes delay materially dangerous, the IRL may authorise immediate, least-disruptive containment; IT Operations records the scope, expected evidence loss, business impact and retrospective review. No responder should wait for perfect attribution before stopping ongoing harm.

### Examination availability versus unverified backup safety

The 11:00 examination creates material availability pressure (E07–E08), but E05 only reports successful jobs; it does not establish a clean or restorable backup. Northbridge must not reopen LMS01 from an unvalidated backup solely to meet the deadline. The BCC and Academic/Business Service Owner should prepare an alternative examination arrangement while the IRL and Security Analyst define restrictions and IT Operations validates an isolated recovery candidate. Any material continuity risk acceptance belongs to Senior Management. The decision and its effect on learners must be recorded even if the examination status remains pending.

## 4. Persistence, entry point and credential protection

The likely entry point remains a hypothesis. Investigators should test the payroll attachment path, mail records, endpoint execution evidence, identity activity, remote administration, exposed services, scheduled tasks, services, registry run keys, email rules, tokens and other persistence locations. E01 does not prove malicious execution.

Credential protection should include, as authorised and evidence-aware actions: disable or reset the finance account if compromise risk warrants it; rotate `svc_backup` and other exposed privileged credentials; revoke active sessions and tokens; review privileged-group membership; enforce MFA and conditional access where available; and use separate recovery credentials. The action log must state whether each control is planned, authorised, executed or awaiting evidence.

## 5. Recovery targets and acceptance criteria

The following are proposed planning targets requiring Senior Management and service-owner approval; they are not observed service levels:

- **Examination decision target:** reach a documented safe-service or alternative-arrangement decision by 10:30 WAT on Day 0.
- **LMS01 service target:** seek a four-hour recovery objective after security clearance, but do not trade security validation for the target.
- **Data-loss planning assumption:** the last disconnected backup is Day minus 3 at 17:00 WAT, so a potential gap of up to approximately 72 hours must be explicitly assessed and accepted by the Business Service Owner and Senior Management if relevant. No data-loss acceptance has occurred.

Before return to service, require:

1. Technical restoration completion and execution record.
2. Security validation showing no unresolved known persistence or unauthorised access condition within the assessed scope.
3. Data-integrity verification for files, permissions, application state and required assessment materials.
4. Monitoring enabled for recurrence and privileged-account activity.
5. Business Service Owner confirmation that learner and staff impact is acceptable.
6. Senior Management approval where High/Critical material risk or an exception remains.
7. A documented rollback, hold or further-investigation decision if any gate fails.

## 6. Sources and boundaries

- ICDFA, *GRC105 Incident Response Planning Assignment*, Task 3 and rubric.
- ICDFA, *Incident Response Planning*, Week 20 slides 9–13 and 16–18.
- Approved Task 1 evidence analysis and Task 2 governance/authority model.
- NIST, *SP 800-61 Rev. 3*: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- NIST, *SP 800-86 Guide to Integrating Forensic Techniques into Incident Response*: https://csrc.nist.gov/pubs/sp/800/86/final
- CISA and partners, *#StopRansomware Guide*: https://www.cisa.gov/stopransomware/ransomware-guide

No hash, acquisition, restoration test, malware result, clean-backup determination, or business acceptance is claimed.
