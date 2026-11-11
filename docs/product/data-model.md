# Conceptual Data Model
```mermaid
erDiagram
 STATION ||--o{ TANK : has
 STATION ||--o{ MACHINE : has
 TANK ||--o{ DIP_CHART_VERSION : calibrated_by
 TANK ||--o{ DIP_READING : measured
 MACHINE ||--o{ NOZZLE : contains
 NOZZLE ||--o{ METER_READING : reports
 SHIFT ||--o{ SHIFT_ASSIGNMENT : assigns
 SUPPLIER ||--o{ DELIVERY : supplies
 DELIVERY ||--o{ EVIDENCE : supported_by
 CUSTOMER ||--o{ CREDIT_TRANSACTION : has
 SHIFT ||--o{ PAYMENT_ALLOCATION : allocates
 WORKFLOW ||--o{ APPROVAL : requires
 WORKFLOW ||--o{ AUDIT_EVENT : records
```
Core entities: stations, users/roles, tanks, dip-chart versions/points, dip readings, machines/nozzles, meter readings, shifts/assignments/handovers, sales/payment allocations, customers/credit transactions, suppliers/purchase requests/orders/deliveries, evidence, cash counts/deposits/reconciliations, incidents, approvals, agent runs, tool invocations and audit events.

Every station record carries station scope. Measurements carry unit, timestamp, source/recorder and validation state. Dip readings reference chart version. Financial amounts carry currency/decimal precision. Agent outputs reference source IDs and never become source records.
