import core


def test_get_item_names():
    l = [['a', 'b', 'c'], ['x', 'y', 'z']]
    assert core.get_item_names(l) == ['a', 'x']
    l = [['string_a', 'string_b'], ['string_x', 'string_y']]
    assert core.get_item_names(l) == ['string_a', 'string_x']


def test_cost_of():
    actual = core.cost_of(4, 'Chairs', 3.5, [['Chairs', 450, .25, 7.00]])
    expect = 3.5
    assert actual == expect


def test_get_item():
    actual = core.get_item([['Toys', 20, 2.00]], 'Toys')
    expect = ['Toys', 20, 2.00]
    assert expect == actual


def test_max_amount():
    actual = core.get_max_amount('Chairs', [['Chairs', '200', '300']])
    expect = 200
    assert expect == actual


def test_item_messages():
    actual = core.item_messages([['Toys', 20, 2.00]], 'Toys')
    expect = 'Here is the item, followed by the quantity left and the price per item'
    assert expect == actual
    actual = core.item_messages([['Toys', 20, 2.00]], 'Wheels')
    expect = 'We are sorry, but we do not have the item for rent.'
    assert expect == actual


def test_tax_of():
    actual = core.tax_of(1.00)
    expect = '1.07'
    assert expect == actual


# def test_replacement_of():
#     expect = core.replacement_of('Chair', 4, [['Chairs', '400', '.25',
#                                                '7.00']])
#     actual = 2.80
#     assert expect == actual


def test_return_deposit():
    actual = core.return_deposit('4', 'Chairs',
                                 [['Chairs', '450', '.25', '7.00']])
    expect = '2.8'
