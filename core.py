from datetime import datetime
def rent_time(item_name):
    '''str _> float
    Function will recive the item name and it will return
    the time it was rented
    '''
    time = datetime.now().strftime('%y/%m/%d %H:%M')
    return time
    # return time.strptime("%H:%M:%S, %B %d, 20%y", ???)
def get_item(inventory, item):
    ''' list[list], str_> str, float, float
    Functions recieves an item and if 
    it is found in the inventory 
    it returns the item information.
    '''
    msg = 'Item could not be found'
    for elements in inventory:
        if item.title() in elements:
            return elements[0:3]
    return msg

def return_deposit(inventory, number):
    ''' list[str], str _> str
    Function will get a number from the user and it
    will look for it in the history.txt file and if 
    it is found, it will return the deposit
    '''
    msg = 'Sorry could not find number'
    for elements in inventory:
        if number in elements:
            return elements[6]
    return msg
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
