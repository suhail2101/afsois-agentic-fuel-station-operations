# Safety and Human Oversight

1. AI is advisory; physical safety systems remain independent.
2. Never let an LLM directly operate dispensers, pumps, valves, electrical controls, alarms or emergency shutdown equipment.
3. A variance is not a diagnosis. Do not infer theft, leakage, fraud or misconduct without evidence and human investigation.
4. For a reported hazard, the system may notify and log; a qualified person follows the approved site procedure.
5. Consequential actions require server-side role checks and human approval.

| Risk tier | Example | Handling |
|---|---|---|
| Low | Read-only daily summary | Automated response with source refs |
| Medium | Variance explanation / forecast | Advisory; uncertainty shown |
| High | Delivery dispute / credit exception / purchase proposal | Human review |
| Critical | Possible leak, fire or emergency | Qualified human and independent safety system; AI notify-and-record only |

If identity, policy, evidence or calculation cannot be validated, block the action. Separate facts, calculations, hypotheses and recommendations in the UI.
