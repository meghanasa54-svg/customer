
from shopping_bill import calculate_bill

def test_bill_calculation():
    assert calculate_bill(5000, 45000, 15000) == 65000

def test_zero_prices():
    assert calculate_bill(0, 0, 0) == 0

def test_another_bill():
    assert calculate_bill(4000, 1000, 2000) == 7000
