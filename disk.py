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
        elements = file.readlines()
    msg = 'Sorry there was an error during the purchase'
    for items in elements:
        if item.title() in items:
            pieces = items.split(', ')
            cost = float(pieces[2])
            total = float(cost) * float(amount) * float(hours)
            return '{:0.2f}'.format(total)
    return msg