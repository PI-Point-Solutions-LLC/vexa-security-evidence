# Secure Software Development Evidence

Reviewed: 2026-08-18

VE×A uses NIST SP 800-218 SSDF 1.1 as the primary secure-development reference. The mapping below states current evidence without asserting formal conformity or certification.

| SSDF practice group | Current evidence | Status |
| --- | --- | --- |
| PO — Prepare the Organization | Version-controlled security invariants, control ownership, roadmap checkpoints, explicit evidence/disclosure boundary | Implemented |
| PS — Protect the Software | Private source repository, backend-only secrets, reviewable migrations, dependency lock data, separation of public evidence from implementation | Implemented; production access evidence restricted |
| PW — Produce Well-Secured Software | Authentication/authorization tests, RLS and ACL tests, bounded-input contracts, SSRF-aware retrieval controls, immutable provenance, quarantine and malware-result enforcement, type/lint/build checks | Verified for the reviewed development baseline |
| RV — Respond to Vulnerabilities | Risk tracking and remediation commits exist; public reporting process, severity/service targets, and exercise record remain required | Tracked |

## Release evidence baseline

A security-relevant release should retain, as applicable:

- exact revision and change scope;
- successful type, lint, unit/integration, database-policy, and production-build checks;
- security-advisor and dependency findings with dispositions;
- migration forward/rollback reasoning;
- secrets and public-disclosure scan results;
- provider/infrastructure dry-run or deployment evidence;
- post-deployment health and authorization-boundary verification;
- an explicit list of deferred risks and owners.

Full logs remain restricted because they can expose private architecture, provider identifiers, and control details. Public records contain only sanitized aggregate outcomes.
