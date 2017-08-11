from datetime import datetime


def get_item_names(products):
    """ [[str]] -> [str]
    returns a list of the first items in each list in products
    >>> get_item_names([['a', 'b'], ['c', 'd']])
    ['a', 'c']
    """
    names = []
    for item in products:
        names.append(item[0])
    return names


def cost_of(amount, item, hours, products):
    """ int, str, float , [[]] -> float
    Function will recieve an item and look for it in the
    inventory and if it is found it will return 
    the price of it multiplied by the hours
    """
    for items in products:
        if items[0] == item:
            return float(items[2]) * float(amount) * float(hours)


def get_item(inventory, item):
    ''' list[list], str_> str, float, float
    Functions recieves an item and if 
    it is found in the inventory 
    it returns the item information.
    '''
    for elements in inventory:
        if item.title() in elements:
            return elements[0:3]
    return 'Item could not be found'


def get_max_amount(item, products):
    ''' str, [[]] -> num
    returns the number of items in stock
    for a certain item '''
    for stock in products:
        if item == stock[0]:
            return int(stock[1])


def replacement_of(item, amount, products):
    ''' str, int, [[str]] _> str
    Function will recive and item and the amount rented
    for the item and it will return the replacement value 
    for the amount of the same items rented
    '''
    for items in products:
        if item == items[0]:
            # value = float(items[3]) * .10 * float(amount)
            return float(items[3]) * .10 * float(amount)


def return_deposit(number, item, products):
    ''' str, str, [[]] _> str 
    Function will get a number from the user and it
    will look for it in the history.txt file and if 
    it is found, it will return the deposit
    '''
    for items in products:
        if item == items[0]:
            answer = int(number) * float(items[3]) * 0.10
            return '{:0.2f}'.format(answer)


def item_messages(inventory, item):
    ''' list[list], str_> str
    Function returns a different message if
    the item is in the inventory or if the items is not
    in the inventory
    '''
    good_msg = 'Here is the item, followed by the quantity left and the price per item'
    bad_msg = 'We are sorry, but we do not have the item for rent.'
    for elements in inventory:
        if item.title() in elements:
            return good_msg
    return bad_msg


def tax_of(money):
    '''float _> float
    Return money multiplied by .07 and 
    added back to money
    >>> tax_of(1)
    '1.07'
    '''
    tax = (money) * .07
    total = money + tax
    return '{:0.2f}'.format(total)


def rent_item(products, item, amounts):
    """ [[str]], str, int -> [[str]]
    removes the amount an rented item from the inventory
    """
    for items in products:
        if item == items[0]:
            items[1] = str(int(items[1]) - int(amounts))
    return products


def add_item_back(products, item, amounts):
    """ [[str]], str, int -> [[str]]
    Adds back the amount rented to the inventory
    """
    for items in products:
        if item == items[0]:
            items[1] = str(int(items[1]) + int(amounts))
    return products
