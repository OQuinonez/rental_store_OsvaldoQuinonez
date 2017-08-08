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
        products.append([individual[0], individual[1], individual[2].strip()])
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
    for elements in inventory:
        if item[0].title() in elements:
            pieces = elements.split(', ')
            cost = pieces[2]
            total = float(cost) * float(amount) * float(hours)
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


def update_history(number, payed, item, amount, hours_rent, time, deposit):
    ''' str, float, float _> None
    Function will update the history text file with all the 
    parameters provided
    '''
    msg = str(number) + ', ' + str(payed) + ', ' + str(item) + ', ' + str(
        amount) + ', ' + str(hours_rent) + ', ' + str(time) + ', ' + str(
            deposit) + ', ' + '\n'
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
    return int(numbers)


def load_history():
    """ -> list[list]
    returns the info of the item choosen
    """
    with open("history.txt", 'r') as file:
        file.readline()
        items = file.readlines()
    products = []
    for purchases in items:
        individual = purchases.split(', ')
        products.append([
            individual[0], individual[1], individual[2], individual[3],
            individual[4], individual[5], individual[6].strip()
        ])
    return products


def in_inventory():
    ''' _> inventory
    Function returns everything in the inventory
    Made it to be used in take_away
    '''
    left = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([(split_string[0]), (split_string[1]), (split_string[2]),
                     (split_string[3])])
    return left


def take_away(item_rented, amount):
    """ 
    Function gets the item rented and the amount
    the customer rented and it will subtract it 
    from the inventory
    """
    str_l = ['item:, amount:,cost:, replacement value:']
    items_left = in_inventory()
    for item in items_left:
        if item[0].lower().title() == item_rented.lower().title():
            if int(amount) > int(item[1]):
                return False
            else:
                item[1] = int(item[1]) - (int(amount) // 2)
        item[2] = str(item[2])
        item[1] = str(item[1])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('inventory.txt', 'w') as file:
        file.write(message)
    return True


def in_history():
    """ 
    Small function that returns everything in
    the history text file as a list of list
    Made it for add_back
    """
    left = []
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([(split_string[0]), (split_string[1]), (split_string[2]),
                     (split_string[3]), (split_string[4]), (split_string[5]),
                     (split_string[6])])
    return left


def add_back(item_rented, amount):
    """ 
    Function gets the item rented and the amount
    the customer rented and it will subtract it 
    from the inventory
    """
    str_l = ['item:, cost:, amount of items avalaible:']
    items_left = in_inventory()
    for item in items_left:
        if item[0].lower().title() == item_rented.lower().title():
            if int(amount) > int(item[1]):
                return False
            else:
                item[1] = int(item[1]) - (int(amount) // 2)
        item[2] = str(item[2])
        item[1] = str(item[1])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('inventory.txt', 'w') as file:
        file.write(message)
    return True


def sum_revenue():
    """ _> float
    Function will get the total revenue when called
    in the manager branch in the shell
    """
    with open('history.txt', 'r') as file:
        file.readline()
        element = file.readlines()
    total = 0
    for item in element:
        pieces = item.split(', ')
        deposit = pieces[6]
        total += float(deposit)
    return total
