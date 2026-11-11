from decimal import Decimal

def meter_delta(opening: Decimal, closing: Decimal) -> Decimal:
    if opening < 0 or closing < 0: raise ValueError("readings must be non-negative")
    if closing < opening: raise ValueError("closing below opening; investigate reset/rollover")
    return closing - opening

def sales_value(litres: Decimal, price_per_litre: Decimal) -> Decimal:
    if litres < 0 or price_per_litre < 0: raise ValueError("inputs must be non-negative")
    return litres * price_per_litre
