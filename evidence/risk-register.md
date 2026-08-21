# VE×A Cybersecurity Risk Register — Sanitized External Version

Register date: 2026-08-21

Review cadence: quarterly and after a material incident, architecture, provider, data-flow, legal-authority, or threat change.

| ID | Sanitized risk | CSF areas | Impact | Current treatment | Status |
| --- | --- | --- | --- | --- | --- |
| R-001 | Public assurance evidence becomes stale or discloses sensitive implementation detail | GV.OV, ID.IM, PR.DS | High | Separate public/private evidence, disclosure classification, dated review and pre-publication scan | Mitigating |
| R-002 | Cross-case or cross-organization data access | PR.AA, PR.DS | Critical | Explicit case authorization, database row controls, backend checks, and negative-path regression tests | Mitigated / monitored |
| R-003 | Untrusted evidence is treated as safe or authoritative | PR.DS, DE.AE, RS.MI | High | Controlled intake, integrity and security validation, provenance, uncertainty, and investigator review | Mitigating; validation continuing |
| R-004 | Provider or collected data creates false identity/location certainty | GV.RM, ID.RA, PR.DS | High | Source authority, timestamp precision, uncertainty, lifecycle boundaries, corroboration, and no automatic identity collapse | Mitigating |
| R-005 | Credential or privileged-service exposure | PR.AA, PR.DS, RS.MI | Critical | Backend-only secrets, least privilege, redacted logs, revocation paths; production access review evidence required | Mitigating |
| R-006 | Critical provider, processing tier, or queue outage | GV.SC, PR.IR, RC.RP | High | Bounded retries, idempotency, durable job states, failure visibility; recovery exercise required | Tracked |
| R-007 | Software or dependency vulnerability reaches production | ID.RA, PR.PS, RV | High | Review, dependency/build checks, regression suites, remediation tracking; public vulnerability process required | Mitigating |
| R-008 | Synthetic validation data contaminates real investigations or analytics | PR.DS, DE.AE | High | Structural case classification, selector origin, ordinary-directory exclusion, and negative-path regression tests | Mitigated / monitored |
| R-009 | Lawful-purpose or data-minimization controls are bypassed | GV.OC, GV.RM, PR.AA | Critical | Authorized professional-use policy, case scoping, auditability, provider-specific limits; production operating review required | Mitigating |
| R-010 | Backup, rollback, or incident recovery is not sufficiently proven | PR.IR, RS.MI, RC.RP | High | Controlled recovery exercises and retained internal evidence; broader authorized-data and service-failure scenarios remain in progress | Mitigating |

Detailed attack paths, affected components, owners, due dates, findings, and acceptance rationales remain in the restricted register.
