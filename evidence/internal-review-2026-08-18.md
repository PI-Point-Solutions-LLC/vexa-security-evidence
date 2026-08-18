# Internal Security Review Record — Sanitized

Review date: 2026-08-18

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

| Result | Count |
| --- | ---: |
| CSF 2.0 categories assessed | 23 |
| Verified | 4 |
| Implemented | 13 |
| Tracked | 6 |
| Certification or independent attestation claimed | 0 |

## Current verified development evidence

The reviewed private baseline includes successful application tests, production build, database reset/migration validation, focused database security tests, and a no-finding database security-advisor result. A private processing-container baseline also verified clean-file and industry-standard antivirus test-file handling. Exact revisions, logs, provider identifiers, and configuration remain restricted.

A same-day material-change review also verified a controlled production deployment rollback and restore with health checks, a successful hosted build/deploy workflow, and a private-storage contract test covering tenant/case linkage, separate ordinary and restricted roles, immutable object and event identity, legal holds, conflicting-event rejection, idempotency, and denial to browser roles. The storage tier remained empty and unbound during this review; no evidence cutover is claimed.

A subsequent subject-free production transaction verified the fail-closed private-processing boundary from quarantined object through authenticated queue dispatch, isolated malware scanning, immutable scanner-result persistence, trust-state clearance, and bounded extraction. The primary queue and dead-letter queue returned to zero backlog. Exact object, account, deployment, scanner-signature, and topology evidence remains restricted.

The reviewed development baseline also added an immutable association-candidate control for separately typed co-presence, communication, synchronized-movement, and shared-asset screening. Same-case endpoints and observations are enforced; alternative explanations and limitations are mandatory; cross-case access is denied; review decisions are append-only; and graph publication requires an explicit authenticated investigator acceptance action. Communication screening additionally requires a versioned two-party canonical contract with distinct case-resolved endpoints; ambiguous and single-selector provider records are excluded, and reported direction is retained only after explicit review and publication. The control does not convert proximity, communication metadata, device data, or shared assets into an automatic identity, authorship, companionship, coordination, possession, or exact-presence claim.

## Required follow-up

- approve and publish the sanitized policy set;
- enable continuous public-evidence freshness and disclosure checks;
- complete production deployment evidence and privileged-access review;
- verify alert delivery and run incident, data-restore, and broader service-recovery exercises;
- establish the sanitized vendor register and periodic review;
- reassess after each material production or investigative-data-flow change.
