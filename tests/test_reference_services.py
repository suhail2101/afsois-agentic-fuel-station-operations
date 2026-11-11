from decimal import Decimal as D
import pytest
from afsois.services.wetstock import expected_closing_stock, stock_residual, interpolate_dip_chart
from afsois.services.meter import meter_delta, sales_value

def test_expected_stock(): assert expected_closing_stock(D("5000"),D("2000"),D("1500")) == D("5500")
def test_residual_sign(): assert stock_residual(D("5480"),D("5500")) == D("-20")
def test_interpolation(): assert interpolate_dip_chart(D("5"),[(D("0"),D("0")),(D("10"),D("100"))]) == D("50")
def test_no_extrapolation():
    with pytest.raises(ValueError): interpolate_dip_chart(D("11"),[(D("0"),D("0")),(D("10"),D("100"))])
def test_meter_delta(): assert meter_delta(D("10"),D("25")) == D("15")
def test_meter_reset_flagged():
    with pytest.raises(ValueError): meter_delta(D("25"),D("10"))
def test_sales_value(): assert sales_value(D("10"),D("100.50")) == D("1005.00")
