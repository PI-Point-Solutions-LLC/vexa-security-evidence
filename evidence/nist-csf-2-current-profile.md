# VE×A NIST CSF 2.0 Current-Profile Evidence Matrix

Reviewed: 2026-08-19

This category-level current profile is intentionally conservative. **Verified** requires current reproducible evidence; **Implemented** means a control exists but production corroboration is restricted or incomplete; **Tracked** is open work.

| Function / category | Status | Public evidence or required next evidence |
| --- | --- | --- |
| GV.OC Organizational Context | Implemented | [Assurance boundary](assurance-boundary.md); authorized professional-investigation purpose and sensitive-data scope documented |
| GV.RM Risk Management Strategy | Implemented | [Risk register](risk-register.md); treatment and review rules documented |
| GV.RR Roles, Responsibilities, Authorities | Implemented | [Control ownership](control-ownership.md) |
| GV.PO Policy | Implemented | Private security policy is version controlled; sanitized publication and policy lifecycle remain tracked |
| GV.OV Oversight | Implemented | [Internal review](internal-review-2026-08-18.md); independent assessment not claimed |
| GV.SC Cybersecurity Supply Chain Risk Management | Tracked | Provider review exists in private engineering records; sanitized vendor register and dated review are required |
| ID.AM Asset Management | Implemented | Private source, data, provider, and infrastructure inventories exist; sanitized asset classes remain required |
| ID.RA Risk Assessment | Implemented | [Risk register](risk-register.md); vulnerability and architecture reviews retained privately |
| ID.IM Improvement | Verified | Dated checkpoints, regression tests, and remediation commits support iterative control improvement |
| PR.AA Identity Management, Authentication, Access Control | Verified | Automated organization/case authorization, security-definer ACL, access-boundary regression suites, and live case-authorized private-delivery revalidation; production tenant evidence remains restricted |
| PR.AT Awareness and Training | Tracked | Secure handling rules exist; dated training/acknowledgment record is required before production operations |
| PR.DS Data Security | Verified | Case isolation, immutable provenance, evidence hashing, private storage, quarantine, fail-closed trust transitions, separate ordinary/restricted storage contracts, and digest-only short-lived delivery grants have automated and sanitized live evidence |
| PR.PS Platform Security | Verified | Security checks, schema lint, dependency/build validation, and protected backend boundaries are exercised; provider configuration is restricted evidence |
| PR.IR Technology Infrastructure Resilience | Implemented | Idempotent jobs, bounded retries, failure states, scale-to-zero processing, and rollback-aware migrations exist; a production deployment rollback/restore passed, while data restore and wider service recovery remain tracked |
| DE.CM Continuous Monitoring | Implemented | Health, job, audit, and security-result telemetry exist; external alert delivery and production operating evidence remain tracked |
| DE.AE Adverse Event Analysis | Implemented | Security-relevant states and append-only results support analysis; production triage exercise remains tracked |
| RS.MA Incident Management | Tracked | Fail-closed containment paths exist; approved incident plan and exercise record remain required |
| RS.AN Incident Analysis | Implemented | Immutable audit/provenance and security-result records support reconstruction; operating evidence is restricted |
| RS.CO Incident Response Reporting and Communication | Tracked | Owner exists; approved internal/external communication plan and tested contacts remain required |
| RS.MI Incident Mitigation | Implemented | Revocation, rejection, quarantine, retry, and deployment rollback mechanisms exist; a controlled production deployment rollback/restore passed, while broader incident exercises remain required |
| RC.RP Recovery Plan Execution | Tracked | Backup/provider capabilities and migration rollback practices exist; dated restore and service-recovery exercise required |
| RC.CO Recovery Communication | Tracked | Owner identified; tested stakeholder communication record required |
| RC.IM Recovery Improvement | Implemented | Checkpoints and regression additions capture lessons; recovery-exercise findings remain required |

## Priority closure order

1. Publish and approve sanitized security, vulnerability-reporting, incident, and continuity policies.
2. Complete production privileged-access, tenant-configuration, backup/restore, and alert-delivery evidence.
3. Publish a sanitized vendor register and dated critical-vendor review.
4. Run and record incident, credential-revocation, rollback, and recovery exercises.
5. Reassess this profile after production deployment and every material architecture or data-flow change.
