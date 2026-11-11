# LinkedIn and Resume Copy

## LinkedIn project entry
**AFSOIS — Agentic Fuel Station Operations & Intelligence System | Independent System Design Project**

Designed a hybrid agentic-AI architecture for fuel-station operations covering wetstock monitoring, meter and sales reconciliation, delivery verification, cash/credit review and procurement decision support. Defined a workflow orchestrator with bounded specialist agents, deterministic calculation services, typed tool contracts, role-based permissions, human approval gates and auditability. Produced architecture, agent specifications, workflow diagrams, conceptual data model, API contracts, threat model, evaluation plan and synthetic reference datasets. Built small Python reference functions for meter and wetstock calculations with unit tests.

**Technology/design:** Python, Decimal arithmetic, pytest, Mermaid, GitHub Actions; FastAPI, PostgreSQL and LangGraph/state-machine orchestration in the proposed architecture.

**Status:** System design and early reference-service prototype; full platform and agent runtime not yet implemented.

## Resume bullets
- Designed AFSOIS, a hybrid agentic-AI system for fuel-station operations, combining deterministic inventory/financial calculations, bounded specialist agents and human-in-the-loop approvals.
- Authored agent specifications, workflows, data model, API contracts, security/threat model and evaluation strategy for wetstock, delivery, shift-close and reconciliation.
- Built tested Python reference services for meter deltas, sales values, dip-chart interpolation and wetstock reconciliation using Decimal arithmetic and synthetic data.

## Product / AI systems emphasis
- Translated operational workflows into a system design defining product scope, roles, exception handling, agent boundaries, approval flows and phased roadmap.
- Separated deterministic operational truth from LLM-based evidence synthesis and recommendations.
- Defined least-privilege tools, server-side RBAC, grounded outputs, approval payload integrity, audit events and exclusion of AI control over safety-critical hardware or financial transfers.

## LinkedIn post
I’ve been working on AFSOIS, an independent system-design project exploring how agentic AI can support fuel-station operations.

The challenge is to bring together physical inventory, meter readings, deliveries, shift records and financial reconciliation without allowing an AI model to become the source of truth.

I designed a hybrid architecture with deterministic calculation services, a workflow orchestrator, bounded specialist agents and human approval for consequential decisions. The project includes agent specifications, workflows, data model, API outline, governance controls, evaluation plan and synthetic examples, alongside a small tested Python reference layer.

The key principle: **AI should help investigate and explain operational exceptions; verified services and accountable people should remain in control.**

This is a system-design portfolio project and early prototype, not a production deployment. Feedback on the architecture and agent boundaries is welcome.

## Interview explanation
"I started with the operational workflow rather than adding agents everywhere. I separated physical-stock calculations and financial reconciliation into deterministic services. Agents are used where language understanding and evidence synthesis add value, such as investigating stock variance or explaining delivery discrepancies. I added strict permissions, approval gates and auditability because an operational AI system must not independently move money, alter records or control safety equipment."
