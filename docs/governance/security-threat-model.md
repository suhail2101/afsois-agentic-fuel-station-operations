# Security and Threat Model

## Assets and trust boundaries
Assets: operational readings, sales, cash/credit, supplier/customer records, employee assignments, evidence files, credentials, policy and audit history. Boundaries: client/API; API/database/object store; orchestrator/agent runtime; agent/tools; external documents/retrieval; approval UI/action executor.

| Threat | Control |
|---|---|
| Prompt injection in supplier PDF | Retrieved content is data, never executable instruction; tool allowlist |
| Excessive agency | No payment, hardware, unrestricted SQL or arbitrary write tools |
| Cross-role data leak | Server-side RBAC and station/row scope |
| Hallucinated deposit/stock fact | Evidence-backed answers; abstain if source absent |
| Duplicate event/replay | Idempotency keys and unique constraints |
| Tampered evidence | Content hash, metadata and restricted object access |
| Approval substitution | Payload hash binding, expiry and revalidation |
| Insider changes old records | Append-only corrections and audit trail |
| Policy/model outage | Fail closed for consequential actions |
| Data exfiltration | Scoped retrieval, redaction and export permissions |

Baseline: TLS; encryption at rest; short-lived tokens; least-privilege service identities; secrets outside Git; structured logs with redaction; rate limits; upload scanning; dependency checks; backups and restore tests. These are deployment requirements, not claims that the portfolio prototype already implements them.

No agent can operate dispensers, fire systems, emergency shutdowns, bank transfers or unrestricted SQL.
