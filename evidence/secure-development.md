# Secure Software Development Evidence

Reviewed: 2026-08-21

VE×A uses NIST SP 800-218 SSDF 1.1 as the primary secure-development reference. The mapping below states current evidence without asserting formal conformity or certification.

| SSDF practice group | Current evidence | Status |
| --- | --- | --- |
| PO — Prepare the Organization | Security objectives, ownership, release checkpoints, and public/private evidence boundaries are version controlled. | IMPLEMENTED |
| PS — Protect the Software | Source, credentials, build inputs, and detailed assurance evidence are protected and access controlled. | IMPLEMENTED — VALIDATION CONTINUING |
| PW — Produce Well-Secured Software | Security-relevant changes receive automated and human validation across authorization, data handling, processing, and release quality. | IMPLEMENTED — VALIDATION CONTINUING |
| RV — Respond to Vulnerabilities | Risk and remediation tracking operate; the public reporting process and recurring response exercises remain in progress. | PARTIALLY IMPLEMENTED |

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
