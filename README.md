# VE×A Security Evidence

Public, sanitized security-assurance evidence for VE×A, a professional investigative intelligence platform developed for authorized use by licensed private investigators.

This repository describes security outcomes, governance, verification methods, and known maturity gaps. It deliberately excludes credentials, customer or subject data, provider account identifiers, non-public source code, collector inventories, private architecture, exact defensive configurations, exploit paths, and operational investigation methods.

## Start here

- [Assurance and disclosure boundary](evidence/assurance-boundary.md)
- [NIST CSF 2.0 current-profile evidence matrix](evidence/nist-csf-2-current-profile.md)
- [Secure software development evidence](evidence/secure-development.md)
- [Security control ownership](evidence/control-ownership.md)
- [Sanitized risk register](evidence/risk-register.md)
- [Internal security review](evidence/internal-review-2026-08-18.md)
- [Restricted evidence attachment register](evidence/restricted-evidence-register.md)

## Framework use

VE×A uses the [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) to organize cybersecurity outcomes and improvement work. Secure-development practices are cross-referenced to [NIST SP 800-218 SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final); selected control objectives are informed by [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), the [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/), and the [OWASP API Security Top 10](https://owasp.org/API-Security/).

Framework alignment is not certification. VE×A does not claim NIST certification, FedRAMP authorization, SOC examination, ISO certification, or independent third-party attestation.

## Status language

- **IMPLEMENTED**: the control operates and supporting evidence is retained.
- **IMPLEMENTED — VALIDATION CONTINUING**: the control operates, with broader or recurring assurance work still underway.
- **PARTIALLY IMPLEMENTED**: part of the control objective operates and material maturity work remains.
- **PLANNED**: the control objective is recorded but is not represented as operating.
- **NOT APPLICABLE**: the objective is outside scope with a documented rationale.

Where useful, an entry also distinguishes design, implementation, production validation, and continuous assurance. Public status never substitutes for restricted technical evidence or independent certification.
