# Wetstock and Delivery
```mermaid
flowchart TD
 A[Opening stock and receipts] --> B[Validated meter sales]
 B --> C[Measured closing dip]
 C --> D{Valid readings and chart version?}
 D -->|No| E[INCOMPLETE / REVIEW_REQUIRED]
 D -->|Yes| F[Deterministic expected-stock calculation]
 F --> G[Signed residual]
 G --> H[Wetstock Investigator]
 H --> I{Unexplained variance?}
 I -->|No| J[Routine close]
 I -->|Yes| K[Evidence-backed incident draft]
 K --> L[Human review]
```
Delivery sequence: create draft; capture pre-dip and chart version; record offload/POD; capture post-dip; calculate tank increase; compare with approved versioned tolerance; mark review/dispute if evidence incomplete or variance exceeds policy; human disposition. No payment release is automated.

A stock discrepancy is a signal, not proof of theft or leakage. Possible hazardous conditions are escalated to qualified staff under the approved site procedure; AI does not control safety equipment.
