import core
def test_get_item():
    actual = core.get_item([['Toys', 20, 2.00]], 'Toys')
    expect = ['Toys', 20, 2.00]
    assert expect == actual

def test_item_messages():
    actual = core.item_messages([['Toys', 20, 2.00]], 'Toys')
    expect = 'Here is the item, followed by the quantity left and the price per item'
    assert expect == actual
    actual = core.item_messages([['Toys', 20, 2.00]], 'Wheels')
    expect = 'We are sorry, but we do not have the item for rent.'
    assert expect == actual
