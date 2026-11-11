from decimal import Decimal
from typing import Sequence

D = Decimal

def expected_closing_stock(opening: Decimal, receipts: Decimal, sales: Decimal, approved_adjustments: Decimal = D("0")) -> Decimal:
    """Expected stock = opening + receipts - sales + approved signed adjustments."""
    if min(opening, receipts, sales) < 0:
        raise ValueError("opening, receipts and sales must be non-negative")
    return opening + receipts - sales + approved_adjustments

def stock_residual(measured_closing: Decimal, expected: Decimal) -> Decimal:
    """Positive means measured stock exceeds expected stock."""
    if measured_closing < 0 or expected < 0:
        raise ValueError("stock values must be non-negative")
    return measured_closing - expected

def interpolate_dip_chart(dip_cm: Decimal, chart: Sequence[tuple[Decimal, Decimal]]) -> Decimal:
    """Interpolate a versioned chart; reject extrapolation and duplicate dip points."""
    if len(chart) < 2: raise ValueError("chart requires at least two points")
    pts = sorted(chart, key=lambda p: p[0])
    if any(pts[i][0] == pts[i+1][0] for i in range(len(pts)-1)): raise ValueError("duplicate dip levels")
    if dip_cm < pts[0][0] or dip_cm > pts[-1][0]: raise ValueError("dip outside chart range")
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
        if x0 <= dip_cm <= x1:
            return y0 + (dip_cm-x0)/(x1-x0)*(y1-y0)
    raise AssertionError("interval not found")
