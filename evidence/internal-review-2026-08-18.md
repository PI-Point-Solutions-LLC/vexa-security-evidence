# Internal Security Review Record — Sanitized

Review date: 2026-08-21

Frameworks: NIST CSF 2.0; NIST SP 800-218 SSDF 1.1; selected NIST SP 800-53 Rev. 5 and OWASP application/API references.

Assurance level: management-led internal review; not an independent audit or certification.

## Work performed

- established a separate public/private security-evidence boundary;
- reviewed current security policy invariants and representative security checkpoints;
- inventoried automated authorization, case-isolation, evidence-integrity, ingestion, job, and processing controls;
- mapped current outcomes conservatively to all NIST CSF 2.0 categories;
- recorded production and governance gaps instead of treating planned controls as complete;
- created a sanitized risk register and restricted-evidence attachment register;
- added secure-development and disclosure requirements to the ongoing roadmap.

## Baseline results

All 23 NIST CSF 2.0 categories were assessed. The current profile distinguishes implemented controls, controls under continuing validation, partially implemented objectives, and planned maturity work. No certification or independent attestation is claimed.

## Current assurance summary

VE×A uses case-scoped authorization, private evidence storage, integrity validation, malware scanning, controlled evidence delivery, immutable auditing, and fail-closed processing. These outcomes have been exercised through regression testing and controlled production validation; detailed technical evidence is retained internally.

Secure-development evidence includes reviewed changes, automated tests, database and authorization checks, dependency and build validation, deployment health checks, and remediation history. Implementation verified; technical artifacts, identifiers, commands, and logs are restricted.

Evidence handling preserves provenance, uncertainty, timestamp precision, unresolved candidates, contradictory material, and investigator review boundaries. New evidence can trigger re-evaluation without silently converting incomplete information into rejection or fact. Validation is continuing across additional source families and analytical consumers.

Private processing and ordinary evidence intake have completed controlled production exercises for quarantine, malware handling, extraction, delivery, rollback, and recovery-related controls. Restricted-evidence transport and broader recovery scenarios remain subject to separate validation. Detailed topology and defensive mechanics are restricted.

Tenant and case isolation, privileged administration, retention/legal-hold behavior, and auditability are covered by automated negative-path tests and controlled reviews. Broader continuous-assurance evidence, periodic privileged-access review, and recovery exercises remain in progress.

The relationship, geospatial, timeline, findings, and candidate-analysis controls are designed to present evidence and uncertainty without automatically asserting identity, ownership, presence, companionship, conduct, or current location. Assurance work continues as these capabilities expand toward production scope.

## Required follow-up

- approve and publish the sanitized policy set;
- enable continuous public-evidence freshness and disclosure checks;
- continue production assurance and privileged-access review;
- verify alert delivery and run incident, data-restore, and broader service-recovery exercises;
- establish the sanitized vendor register and periodic review;
- reassess after each material production or investigative-data-flow change.
