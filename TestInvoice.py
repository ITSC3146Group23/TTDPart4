import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

@pytest.fixture()
def input_value():
    input_value = {10, 2.45, 2}
    return input_value

def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalculateTotalQuantity(invoice, products):
    invoice.totalQuantity(products)
    assert invoice.totalQuantity(products) == 15

def test_CanCalculateTotalShipping(invoice, products):
    invoice.totalShipping(products)
    assert invoice.totalShipping(products) == 69.38 + 4.99