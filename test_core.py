import core
def test_get_item():
    actual = core.get_item([['Toys', 20, 2.00]], 'Toys')
    expect = ['Toys', 20, 2.00]
    assert expect == actual