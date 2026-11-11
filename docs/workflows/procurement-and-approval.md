# Procurement and Human Approval
Procurement: low-stock/request trigger → read stock and recent sales → validate freshness → estimate requirement using approved rule/forecast → inspect supplier terms and dues → apply versioned policy → produce options and assumptions → human review → manual purchasing process.

An approval request binds action type, exact payload hash, requester, rationale, evidence refs, policy version, risk tier and expiry. Server revalidates role, policy, hash and expiry before execution. Any payload change invalidates approval. The agent that drafts a proposal cannot approve it.
