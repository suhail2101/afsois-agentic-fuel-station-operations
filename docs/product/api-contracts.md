# API Contract Outline
All endpoints require authentication, server-side role/station scope and versioned routes. Event submissions use idempotency keys.

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v1/shifts/{id}/meter-readings` | Submit meter reading |
| POST | `/api/v1/tanks/{id}/dip-readings` | Submit dip with chart version |
| POST | `/api/v1/deliveries` | Create delivery draft |
| POST | `/api/v1/deliveries/{id}/evidence` | Attach POD/evidence |
| POST | `/api/v1/shifts/{id}/close` | Submit shift close |
| GET | `/api/v1/shifts/{id}/reconciliation` | Read reconciliation |
| GET | `/api/v1/tanks/{id}/wetstock` | Read wetstock result |
| POST | `/api/v1/approvals` | Request approval |
| POST | `/api/v1/approvals/{id}/decision` | Human approval decision |
| POST | `/api/v1/assistant/query` | Read-only assistant |

Example response: `{"status":"REVIEW_REQUIRED","expected_closing_litres":"5500.000","measured_closing_litres":"5480.000","residual_litres":"-20.000","evidence_refs":["dip_demo_22","meter_demo_81"],"policy_version":"demo-2026-01"}`.

Errors: 400 schema/unit; 401 unauthenticated; 403 unauthorised; 404 out of scope/not found; 409 idempotency/stale approval; 422 domain validation; 503 policy/calculation dependency unavailable. This is an API design, not a running API in this release.
