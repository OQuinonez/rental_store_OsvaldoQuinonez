def load_items():
    """ -> list[list]
    returns the info of the item choosen
    """
    with open("inventory.txt", 'r') as file:
        file.readline()
        items = file.readlines()
    products = []
    for purchases in items:
        individual = purchases.strip().split(', ')
        products.append(individual)
    return products


def update_inventory(products):
    """ 
    Function gets the item rented and the amount
    the customer rented and it will subtract it 
    from the inventory
    """
    str_l = ['item:, amount:, cost:, replacement value:']
    for item in products:
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)
    with open('inventory.txt', 'w') as file:
        file.write(message)


def update_history(money, item, amounts, hours, deposit):
    ''' str, float, float _> None
    Function will update the history text file with all the 
    parameters provided
    '''
    msg = '{}, {}, {}, {}, {}\n'.format(money, item, amounts, hours, deposit)
    with open('history.txt', 'a') as file:
        file.write(msg)


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


def get_amount_history(number):
    """ int -> int
    Function will receive a number and it 
    will look for it in the inventory and return
    the amount borrowed that corresponds with that number
    """
    with open('history.txt', 'r') as file:
        file.readline()
        element = file.readlines()
    msg = "Sorry, there has been an error"
    for item in element:
        if number in item:
            pieces = item.split(', ')
            amount = pieces[3]
            return int(amount)
    return msg


def add_back(number, amount):
    """ 
    Function gets the item rented and the amount
    the customer rented and it will subtract it 
    from the inventory
    """
    str_l = ['item:, amount:, cost:, replacement value:']
    items_left = in_history()
    for item in items_left:
        if item[0] == number:
            if int(amount) > int(item[1]):
                return False
            else:
                item[1] = int(item[1]) + (int(amount) // 2)
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
