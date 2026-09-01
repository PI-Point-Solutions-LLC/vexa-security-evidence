# VE×A NIST CSF 2.0 Current-Profile Evidence Matrix

Reviewed: 2026-09-01

This category-level current profile is intentionally conservative. Detailed proof is retained internally; public entries state only the control objective, maturity, validation posture, and remaining work.

| Function / category | Status | Public evidence or required next evidence |
| --- | --- | --- |
| GV.OC Organizational Context | IMPLEMENTED | Authorized-use purpose, stakeholders, and sensitive-data scope are documented and reviewed. |
| GV.RM Risk Management Strategy | IMPLEMENTED — VALIDATION CONTINUING | Risk treatment and review rules operate; broader operating evidence continues to mature. |
| GV.RR Roles, Responsibilities, Authorities | IMPLEMENTED | Security accountability and review cadence are documented. |
| GV.PO Policy | PARTIALLY IMPLEMENTED | Core policy is version controlled; sanitized policy publication and lifecycle evidence remain in progress. |
| GV.OV Oversight | IMPLEMENTED — VALIDATION CONTINUING | Management review is active; independent assessment is not claimed. |
| GV.SC Cybersecurity Supply Chain Risk Management | IMPLEMENTED — VALIDATION CONTINUING | Supplier risk review and approval operate; the sanitized vendor register and recurring review evidence continue to mature. |
| ID.AM Asset Management | IMPLEMENTED — VALIDATION CONTINUING | Private inventories cover relevant systems, data, software, and services; production validation and continuous assurance are expanding. |
| ID.RA Risk Assessment | IMPLEMENTED — VALIDATION CONTINUING | Risk, vulnerability, and architecture reviews are retained internally and revisited after material change. |
| ID.IM Improvement | IMPLEMENTED | Dated reviews, testing, and remediation history demonstrate iterative improvement. |
| PR.AA Identity Management, Authentication, Access Control | IMPLEMENTED — VALIDATION CONTINUING | Case-scoped and privileged-access outcomes are tested; broader periodic access review remains in progress. |
| PR.AT Awareness and Training | PARTIALLY IMPLEMENTED | Secure-handling rules exist; formal recurring acknowledgment evidence remains planned. |
| PR.DS Data Security | IMPLEMENTED — VALIDATION CONTINUING | Confidentiality, integrity, and availability controls for managed data have controlled production validation; technical evidence is restricted. |
| PR.PS Platform Security | IMPLEMENTED — VALIDATION CONTINUING | Secure-development and protected-runtime outcomes are exercised; new functionality remains fail closed until validation is complete and continuous configuration assurance is expanding. |
| PR.IR Technology Infrastructure Resilience | IMPLEMENTED — VALIDATION CONTINUING | Resilient processing, alerting, controlled rollback, and representative failure/recovery scenarios have been exercised; recurring assurance remains active. |
| DE.CM Continuous Monitoring | PARTIALLY IMPLEMENTED | Security, health, usage, and processing telemetry operate; broader alert delivery and response integration remain in progress. |
| DE.AE Adverse Event Analysis | IMPLEMENTED — VALIDATION CONTINUING | Auditable security and evidence states support analysis; recurring triage exercises remain planned. |
| RS.MA Incident Management | PARTIALLY IMPLEMENTED | Containment and ownership exist; the complete approved plan and exercise cycle remain in progress. |
| RS.AN Incident Analysis | IMPLEMENTED — VALIDATION CONTINUING | Audit and provenance evidence support reconstruction; recurring operating exercises remain planned. |
| RS.CO Incident Response Reporting and Communication | PARTIALLY IMPLEMENTED | Accountability exists; tested internal and external communication procedures remain in progress. |
| RS.MI Incident Mitigation | IMPLEMENTED — VALIDATION CONTINUING | Containment, revocation, and rollback outcomes have controlled validation; broader scenarios remain planned. |
| RC.RP Recovery Plan Execution | IMPLEMENTED — VALIDATION CONTINUING | Recovery paths for supported production data classes have passed controlled exercises, cadence checks, and integrity assurance; detailed evidence is retained internally. |
| RC.CO Recovery Communication | PLANNED | Accountable ownership exists; tested stakeholder communication evidence remains to be completed. |
| RC.IM Recovery Improvement | IMPLEMENTED — VALIDATION CONTINUING | Exercise lessons and remediation are tracked, and recurring fail-closed assurance is active. |

## Priority closure order

1. Publish and approve sanitized security, vulnerability-reporting, incident, and continuity policies.
2. Continue recurring privileged-access, tenant-configuration, backup/restore, and alert-delivery assurance.
3. Publish a sanitized vendor register and dated critical-vendor review.
4. Run and record incident, credential-revocation, rollback, and recovery exercises.
5. Reassess this profile after production deployment and every material architecture or data-flow change.
