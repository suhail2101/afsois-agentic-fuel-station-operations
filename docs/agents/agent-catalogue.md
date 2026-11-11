# Agent Catalogue

## Authority levels
- **A0 Observe:** read authorised records.
- **A1 Analyse:** call deterministic read/compute tools and explain.
- **A2 Recommend:** draft proposal; cannot execute.
- **A3 Execute after approval:** a workflow executes the exact approved payload; agent cannot approve itself.
- **Prohibited:** safety hardware control, money movement, silent ledger edits.

## 1. Operations Orchestrator
Purpose: coordinate requests and events. Inputs: intent, identity/role scope, event refs, policy version. Tools: workflow registry, typed tool router, approval and audit services. Output: workflow state and result refs. Authority: routing only; cannot bypass rules. Escalate ambiguous intent, missing data, policy conflict or failed validation. Evaluate routing, delegation bounds and audit completeness.

## 2. Operations Assistant — A0/A1
Purpose: answer questions from authorised records. Tools: read-only search, shift/stock summary, policy lookup. Output: answer, source record IDs, missing-data notice and uncertainty. Must not guess deposits, assignments, profit, dues or stock. Evaluate groundedness, abstention and access compliance.

## 3. Wetstock Investigator — A1/A2
Purpose: investigate expected-versus-measured stock differences. Inputs: opening stock, receipts, meter sales, approved adjustments, closing dip, chart version and sensor provenance. Tools: dip conversion, meter service, wetstock calculation, evidence lookup, incident draft. Output: expected stock, measured stock, signed residual, data-quality status, evidence-backed hypotheses. Must not declare theft/leak/misconduct from variance alone, invent allowable loss or modify stock. Escalate missing/stale dip, chart mismatch, sensor conflict or unexplained residual. Evaluate arithmetic, sign convention, traceability and uncertainty.

## 4. Delivery Evidence Analyst — A1/A2
Purpose: assemble delivery evidence and identify incomplete/disputed deliveries. Inputs: supplier claim, pre/post dip, chart version, POD, timestamps and recorder. Tools: dip conversion, variance calculator, evidence verifier, incident draft. Output: completeness, measured increase, variance and review status. Must not accept delivery or release payment autonomously. Escalate missing POD, out-of-range dip, timestamp conflict or tolerance breach. Evaluate evidence completeness and false acceptance rate.

## 5. Reconciliation Analyst — A1/A2
Purpose: compare validated sales with cash, digital payment and credit allocations. Tools: sales-value, payment reconciliation and credit exposure services. Output: expected/recorded totals, variance by channel, missing references and review draft. Must not transfer funds, approve refund, issue credit, write off or edit ledger. Evaluate arithmetic, duplicate detection and unsupported conclusions.

## 6. Procurement Advisor — A1/A2
Purpose: recommend restocking options. Inputs: stock, demand, lead time, supplier terms, dues and approved policy. Tools: inventory summary, forecast, supplier policy and purchase draft. Output: suggested quantity, assumptions, options, constraint flags and approval draft. Must not place order or override credit policy. Escalate conflicting dues, stale prices, missing inputs or ambiguous rules. Evaluate constraint adherence and freshness.

## 7. Reporting Agent — A0/A1
Purpose: summarise validated daily/weekly aggregates. Output includes period, completeness, KPI definitions and exception links. Must not call gross margin net profit or invent missing values. Evaluate numerical consistency and disclosure.

## Deliberately deterministic capabilities
Meter/sales calculation, dip/inventory calculation, cash/credit ledger, policy/approval, safety notification/runbook and workforce constraint solver are services/workflows, not LLM agents.
