def load_inventory():
    """ -> [str]
    returns inventory
    """
    with open("inventory.txt", 'r') as file:
        file.readline()
        items = file.readlines()
    inventory = []
    for element in items:
        pieces = element.split(', ')
        inventory.append(pieces[0])
    return inventory


def load_item():
    """ -> list[list]
    returns the info of the item choosen
    """
    with open("inventory.txt", 'r') as file:
        file.readline()
        items = file.readlines()
    products = []
    for purchases in items:
        individual = purchases.split(', ')
        products.append([
            individual[0],
            individual[1],
            individual[2].strip()
        ])
    return products


def cost_of(amount, item, hours):
    """ int, str, float _> float
    Function will recieve an item and look for it in the
    inventory and if it is found it will return 
    the price of it multiplied by the hours
    """
    with open('inventory.txt', 'r') as file:
        file.readline()
        inventory = file.readlines()
    msg = 'Sorry there was an error during the purchase'
    for items in inventory:
        if item[0].title() in inventory:
            cost = item[2]
            total = cost * float(amount) * float(hours)
            return total
    return msg

def replacement_of(item, amount):
    ''' str, int _> float
    Function will recive and item and the amount rented
    for the item and it will return the replacement value 
    for the amount of the same items rented
    '''
    with open('inventory.txt', 'r') as file:
        file.readline()
        elements = file.readlines()
    msg = 'Sorry there was an error.'
    for items in elements:
        if item.title() in items:
            pieces = items.split(', ')
            replace = float(pieces[3])
            value = (float(replace) * .10) * float(amount)
            return '{:0.2f}'.format(value)
    return msg

def update_history(number, payed, item, amount, hours_rent, time):
    ''' str, float, float _> None
    '''
    msg = str(number) + ', ' + payed + ', ' + item + ', ' + str(amount) + ', ' + hours_rent + ', ' + time + '\n'
    with open('history.txt', 'a') as file:
        file.write(msg)
    return None
def transaction_num(name):
    ''' str _> int
    Function will get the name after every
    purchase and it will give the customer a 
    special number for when they return an item
    '''
    with open('history.txt', 'r') as file:
        num = file.readlines()
        numbers = len(num)
        numbers += 1
    return numbers
# >>> from datetime import datetime
# >>> st = datetime.now()
# >>> end = datetime.now()
# >>> end - st
# datetime.timedelta(0, 10, 646110)
# >>> d = end - st
# >>> d.days
# 0
# >>> d.min
# datetime.timedelta(-999999999)
# >>> d.total_seconds
# <built-in method total_seconds of datetime.timedelta object at 0x7f9ca9b5f968>
# >>> d.total_seconds()
# 10.64611
# >>> d.total_seconds() / 60 / 60
# 0.002957252777777778
