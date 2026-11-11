# Decision Register and Source Ambiguities

| ID | Topic | Source issue | Design treatment |
|---|---|---|---|
| D-01 | Tank capacity | Source notes contain conflicting petrol/diesel capacity figures and chart headings | Do not treat as verified; synthetic chart fixtures only |
| D-02 | Dip chart | Geometry/calibration provenance incomplete | Tank-specific versioned chart; no extrapolation |
| D-03 | Allowable loss | Suggested range not established as universal | Unconfigured until qualified local validation and approval |
| D-04 | Wetstock equation | Differing sign conventions and inconsistent worked arithmetic | Use documented equation and signed residual; regression tests |
| D-05 | Vendor dues | Aggregate versus per-vendor threshold unclear | Business owner must define and version policy |
| D-06 | Customer credit | Example balances do not reconcile to aggregate | Recalculate from transaction ledger; synthetic only |
| D-07 | Profit terminology | Per-litre margin confused with total margin | Separate per-litre gross margin and total gross margin; net profit needs other costs |
| D-08 | Machine/operator | Shared-machine attribution needs separate dimensions | Keep machine meter and operator/shift accountability distinct |
| D-09 | Safety response | Earlier notes suggested AI-triggered till lock/safety actions | Excluded; notify and record only |
| D-10 | Sensor priority | Probe/dip priority varies across notes | Store provenance; conflict requires review |

Before a real pilot, confirm tank IDs/capacity/geometry/calibration; approve chart versions; define tolerance/loss policy; resolve vendor dues and customer credit policies; define meter reset/rollover; define business-day timezone; review retention and privacy.
