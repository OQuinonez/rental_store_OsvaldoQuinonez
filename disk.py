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