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

The reviewed development baseline also added an immutable association-candidate control with bounded producers for separately typed co-presence, communication, synchronized-movement, and shared-asset screening. Same-case endpoints and exact source observations are enforced; source independence, alternative explanations, and limitations are retained; cross-case access is denied; review decisions are append-only; and graph publication requires an explicit authenticated investigator acceptance action. Communication requires a versioned two-party canonical contract and excludes ambiguous or single-selector records. Synchronized movement requires exact, accuracy-qualified, lifecycle-bounded endpoints and retains all four observations. Shared-asset screening requires two source-faithful records attributed to distinct case entities against one canonical asset. The control does not convert proximity, communication metadata, device data, or shared assets into an automatic identity, authorship, ownership, possession, companionship, coordination, occupancy, operation, or exact-presence claim.

The reviewed baseline also distinguishes unresolved, possible, probable, confirmed, conflicting, disproven, rejected, and irrelevant candidate states. Candidate meaning is append-only and deterministically ordered; insufficient evidence is not automatically rejected or discarded. New observations related to candidate endpoints enter a bounded, case-scoped re-evaluation queue, and prior evidence and assessments remain preserved. Association, extracted-document, case-media, mobile-association, entity-resolution, property-attribution, vehicle-attribution, court-record, and social/public-profile candidates are integrated. Document parser refreshes preserve every prior interpretation as an immutable version and reopen the candidate for review; investigator acceptance remains possible evidence rather than confirmed fact. New media derivatives trigger review without converting restricted handling into evidentiary rejection. Mobile attribution preserves identifier-to-device, device-to-person, and telemetry-to-location as separate assessed components; missing components remain unresolved, complete chains are only possible, and later telemetry or identifier lifecycle boundaries trigger review without automatically bridging reset events or asserting person presence. Possible-same and possible-distinct entity pairs retain their basis and limitations; new evidence affecting either side triggers review, while merge, explicit rejection, and later split remain distinct confirmed, rejected, and conflicting meanings. Property and vehicle records retain the source observation's attributed party separately from the canonical asset node; later same-asset records trigger review without automatically establishing current residence, occupancy, ownership, possession, operation, or person presence. Court names, allegations, filings, dispositions, and events do not automatically establish identity, liability, guilt, relationship, or current location. Public profile metadata does not automatically establish identity, account control, authorship, relationship, or current presence; investigator acceptance remains only possible evidence. Unified projection across analytical consumers remains tracked work.

## Required follow-up

- approve and publish the sanitized policy set;
- enable continuous public-evidence freshness and disclosure checks;
- complete production deployment evidence and privileged-access review;
- verify alert delivery and run incident, data-restore, and broader service-recovery exercises;
- establish the sanitized vendor register and periodic review;
- reassess after each material production or investigative-data-flow change.
