# Restricted Evidence Attachment Register

Reviewed: 2026-08-18

The following evidence should be retained privately and disclosed only through an authorized, appropriately confidential review. The public repository records that evidence is required without publishing sensitive contents.

| Evidence class | Supports | Public redaction rule |
| --- | --- | --- |
| Source-control access and branch/release protection | GV.OV, PR.AA, PR.PS | Remove repository internals, personnel details, tokens, and private workflow data |
| Backend/database access review and security-advisor exports | PR.AA, PR.DS, DE.CM | Remove project identifiers, schema detail, row data, credentials, and connection information |
| Storage, backup, restore, and retention configuration | PR.DS, PR.IR, RC.RP | Remove bucket names, project/account identifiers, evidence metadata, and access paths |
| Processing-container, queue, secret, monitoring, and cost configuration | PR.PS, PR.IR, DE.CM | Remove account IDs, routes, image names, secrets, limits that aid attack, and private topology |
| Identity/MFA/session configuration and privileged access review | PR.AA, GV.OV | Remove user identities, recovery data, session details, and authenticators |
| Provider/vendor contracts, trust evidence, quotas, and incident contacts | GV.SC, RC.CO | Remove contract terms not authorized for disclosure, account IDs, credentials, and private contacts |
| Full test, security scan, dependency, deployment, and rollback logs | ID.RA, PR.PS, RS.MI | Publish only aggregate status/date/scope; remove paths, versions when risky, payloads, and findings under remediation |
| Incident, tabletop, vulnerability, and remediation records | RS.* , RC.IM | Publish a closure summary only when safe, lawful, and authorized |
| Case authorization, audit, provenance, and evidence-integrity records | PR.AA, PR.DS, DE.AE | Never disclose real case, investigator, subject, identifier, location, or evidence content |
| Association-candidate inputs, alternative explanations, investigator reviews, and graph-publication records | PR.AA, PR.DS, DE.AE | Never disclose case endpoints, relationship hypotheses, evidence links, reviewer identities, subject locations, or analytic parameters that expose private methods |

An evidence attachment is not considered current unless it records the observation date, accountable reviewer, system/environment scope, result, and any unresolved exception.
