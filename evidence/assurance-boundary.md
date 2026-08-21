# Assurance and Disclosure Boundary

Reviewed: 2026-08-21

## Public assurance scope

This repository may publish:

- security objectives and control outcomes;
- framework mappings and honest implementation status;
- sanitized descriptions of repeatable tests;
- dated review records and aggregate results;
- governance, ownership, cadence, and remediation expectations;
- restricted-evidence requirements without the sensitive evidence itself.

## Material that remains restricted

- credentials, tokens, keys, cookies, authentication headers, and secret names that reveal private integrations;
- real case, investigator, customer, subject, identifier, location, or evidence data;
- collector/provider inventories, acquisition tactics, private endpoints, quotas, and account configuration;
- source code, schema detail, internal file paths, exact infrastructure topology, and defensive values that materially aid attack;
- exact authorization logic, trust boundaries, object/storage design, queue or retry topology, internal role names, database function behavior, credential-handling mechanics, and enumeration-resistant response behavior;
- exact analytic traversal bounds, candidate-materialization algorithms, evidentiary state-transition mechanics, and unreleased collector or processing inventories;
- vulnerability reproduction steps, open attack paths, unremediated findings, and exact incident telemetry;
- contracts, invoices, provider account identifiers, personnel access lists, and unredacted console exports.

## Evidence classes

| Class | Public handling |
| --- | --- |
| Policy and governance | Publish sanitized current text |
| Test and build evidence | Publish aggregate result, date, scope, and method; retain full logs privately |
| Production configuration | Publish outcome; retain redacted console/export evidence privately |
| Security findings and incidents | Publish only a sanitized closure summary when disclosure is safe and authorized |
| Investigative capabilities and data sources | Do not enumerate publicly |
| Case/evidence records | Never publish |

## Assurance limitations

Public records support supplier and partner review but do not replace controlled due diligence. Production configuration, private-source implementation, access records, vulnerability findings, recovery exercises, and provider evidence may be reviewed under an appropriate confidentiality process.

Before publication, each statement must answer both questions:

1. Does the detail materially demonstrate a cybersecurity outcome or maturity claim?
2. Could the detail materially help an outsider probe, bypass, enumerate, exhaust, or target VE×A?

If the first answer is no or the second is yes, the detail remains in the private evidence record.
