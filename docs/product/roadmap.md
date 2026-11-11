# Implementation Roadmap

## Phase 0 — Design and reference prototype (current)
Architecture, agent specs, workflows, governance, synthetic fixtures and small tested Python calculation services.

## Phase 1 — Deterministic operations core
Schemas, versioned dip-chart registry, meter/sales, wetstock, payment allocation, idempotent ingestion, PostgreSQL/migrations, synthetic simulator. **Exit:** core truth and arithmetic work without LLM.

## Phase 2 — Workflow and approval
Shift close, delivery verification, payload-hash approvals, append-only audit, RBAC, retries and recovery. **Exit:** full audit trace.

## Phase 3 — Read-only agents
Operations Assistant, Wetstock Investigator, Delivery Evidence Analyst, Reconciliation Analyst; retrieval with citations and golden evaluation set. **Exit:** grounding, abstention, schema and permission gates pass.

## Phase 4 — Recommendations and advisory ML
Procurement Advisor, Reporting Agent, demand forecast and anomaly baselines, monitoring and drift. **Exit:** assumptions visible; human review required.

## Phase 5 — UI and pilot preparation
Role-based dashboard, exception inbox, approval screen, synthetic demo, usability/security review and qualified local legal/metrology/fire-safety/privacy review before any real deployment.

No live hardware or financial integrations are included in this portfolio scope.
