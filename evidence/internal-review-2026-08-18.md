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

A same-day material-change review also verified a controlled production deployment rollback and restore with health checks, a successful hosted build/deploy workflow, and a private-storage contract test covering tenant/case linkage, separate ordinary and restricted roles, immutable object and event identity, legal holds, conflicting-event rejection, idempotency, and denial to browser roles. A subsequent material-change review verified the ordinary private-object event path through a dedicated durable queue, exact canonical reconciliation, automatic private processing, bounded byte/hash validation, and immutable clean and standard antivirus-test-file outcomes. Clean content cleared only after the immutable scanner result; the antivirus fixture was rejected. The restricted compartment remained empty and unbound, and no evidence cutover is claimed. Exact resource, object, account, deployment, key, and scanner-signature details remain restricted.

A subsequent subject-free production transaction verified the fail-closed private-processing boundary from quarantined object through authenticated queue dispatch, isolated malware scanning, immutable scanner-result persistence, trust-state clearance, and bounded extraction. The primary queue and dead-letter queue returned to zero backlog. Exact object, account, deployment, scanner-signature, and topology evidence remains restricted.

A later material-change review verified case-authorized delivery of a cleared ordinary private-storage original. The browser received a short-lived opaque bearer but no bucket name or object key. The service rechecked active case and organization membership, evidence clearance, ordinary-storage role, expiry, and exact object version before each request; only the bearer digest was retained. Issuance and successful delivery produced purpose-linked immutable audit events. Fabricated bearers returned a non-distinguishing unavailable response, restricted storage remained unbound, and a live legacy-storage mismatch failed closed. That mismatch led to an immediate eligibility-projection correction so the R2-only action is shown only for an exact cleared ordinary R2 original. Exact account, object, user, grant, and deployment identifiers remain restricted.

A follow-on live boundary review verified the maximum short-lived grant interval without violating its database bound, successful metadata-only `HEAD`, one satisfiable byte range, denial of multi-range and unsatisfiable-range requests, reuse only while the capability remained active, and nondisclosing denial after both revocation and expiry. Issuance and each accepted redemption remained separately auditable. This evidence validates bounded delivery behavior; it does not authorize storage cutover, which remains gated by recovery, legal-hold/deletion, reconciliation, and cost controls.

The restricted-evidence control plane now requires an explicit expiring case grant in addition to ordinary case membership, separates metadata/reviewer/custodian authority, and limits authorization to four named defensive or review operations. Registration, state change, access, and operation allow/deny events are immutable. Ordinary document and media projections exclude restricted records and receive only non-content placeholders without filename, hash, match detail, media, derivative, or storage coordinates. Potential match, incident, and reporting states remain distinct. Clean schema replay and metadata-only synthetic tests passed role separation, ordinary-pipeline exclusion, immutable denial evidence, and direct-update denial without using restricted test material. The restricted bucket remains empty and unbound pending a separately validated byte runtime.

The reviewed development baseline also added an immutable association-candidate control with bounded producers for separately typed co-presence, communication, synchronized-movement, and shared-asset screening. Same-case endpoints and exact source observations are enforced; source independence, alternative explanations, and limitations are retained; cross-case access is denied; review decisions are append-only; and graph publication requires an explicit authenticated investigator acceptance action. Communication requires a versioned two-party canonical contract and excludes ambiguous or single-selector records. Synchronized movement requires exact, accuracy-qualified, lifecycle-bounded endpoints and retains all four observations. Shared-asset screening requires two source-faithful records attributed to distinct case entities against one canonical asset. The control does not convert proximity, communication metadata, device data, or shared assets into an automatic identity, authorship, ownership, possession, companionship, coordination, occupancy, operation, or exact-presence claim.

The reviewed baseline also distinguishes unresolved, possible, probable, confirmed, conflicting, disproven, rejected, and irrelevant candidate states. Candidate meaning is append-only and deterministically ordered; insufficient evidence is not automatically rejected or discarded. New observations related to candidate endpoints enter a bounded, case-scoped re-evaluation queue, and prior evidence and assessments remain preserved. Association, extracted-document, case-media, mobile-association, entity-resolution, property-attribution, vehicle-attribution, court-record, and social/public-profile candidates are integrated. Document parser refreshes preserve every prior interpretation as an immutable version and reopen the candidate for review; investigator acceptance remains possible evidence rather than confirmed fact. New media derivatives trigger review without converting restricted handling into evidentiary rejection. Mobile attribution preserves identifier-to-device, device-to-person, and telemetry-to-location as separate assessed components; missing components remain unresolved, complete chains are only possible, and later telemetry or identifier lifecycle boundaries trigger review without automatically bridging reset events or asserting person presence. Possible-same and possible-distinct entity pairs retain their basis and limitations; new evidence affecting either side triggers review, while merge, explicit rejection, and later split remain distinct confirmed, rejected, and conflicting meanings. Property and vehicle records retain the source observation's attributed party separately from the canonical asset node; later same-asset records trigger review without automatically establishing current residence, occupancy, ownership, possession, operation, or person presence. Court names, allegations, filings, dispositions, and events do not automatically establish identity, liability, guilt, relationship, or current location. Public profile metadata does not automatically establish identity, account control, authorship, relationship, or current presence; investigator acceptance remains only possible evidence. Unified projection across analytical consumers remains tracked work.

The case-scoped relationship graph now projects candidate lifecycle counts and canonical observed-activity time onto affected nodes. Activity recency uses event time rather than retrieval or database-creation time, retains timestamp precision, and represents undated nodes separately. The visual presentation includes a case-relative date legend and redundant non-color unresolved cues. This projection does not change candidate meaning or promote graph structure into identity, importance, influence, association strength, or location conclusions.

The reviewed baseline now also supplies a bounded case-authorized “where and with whom” screening summary. Recurring-place calculations require entity attribution, exact canonical event time, explicit reported accuracy within the configured ceiling, and repeated observations within the spatial threshold. Imprecise, inaccurate, unattributed, rejected, irrelevant, and merged observations remain preserved outside that exact calculation. Repeated association summaries canonicalize entity pairs, retain candidate kinds and the latest append-only uncertainty states, and do not convert repetition into current presence, residence, workplace, companionship, coordination, household, ownership, or identity. Focused tests cover filtering, recurrence, pair grouping, unresolved retention, entity scope, and tenant denial.

The canonical findings substrate now distinguishes findings from hypotheses and records interpretation through immutable, append-only assessments. Exact supporting, contradicting, and contextual observation links are same-case guarded and immutable. Contradiction remains distinct from disproval; new same-subject evidence appends a review-required signal while retaining the prior substantive state. Investigator assessment requires written rationale, and authorized views disclose assessment origin and exact evidence linkage without weakening tenant isolation. Focused tests cover state seeding, contradiction retention, automatic re-evaluation, investigator assessment, immutability, cross-case denial, and outsider denial.

Canonical workspace context now supports case-bound URL selection and independent exact-object retrieval for observations, findings/hypotheses, and association candidates. Exact-object authorization occurs before lookup; cross-case identifiers return no object, unsupported object kinds are rejected, and bounded list pagination does not prevent an authorized investigator from reopening a previously selected object. Detail projections retain uncertainty, rationale, limitations, alternatives, and direct evidence links without exposing storage coordinates or bypassing case authorization.

Seeded relationship expansion now supports up to six hops. Depths above three require a specific authorized seed and tighter node and edge ceilings; unseeded deep traversal and requests beyond the deep ceilings are rejected before traversal. The interface discloses the active bound and states that truncation is a coverage limit rather than evidence that no further relationship exists. Focused tests cover far-hop reachability, structural selector retention, unsafe-bound rejection, and tenant denial.

## Required follow-up

- approve and publish the sanitized policy set;
- enable continuous public-evidence freshness and disclosure checks;
- complete production deployment evidence and privileged-access review;
- verify alert delivery and run incident, data-restore, and broader service-recovery exercises;
- establish the sanitized vendor register and periodic review;
- reassess after each material production or investigative-data-flow change.
