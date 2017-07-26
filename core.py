def get_item(inventory, item):
    ''' str, str_> str, float, float
    Functions recieves an item and if 
    it is found in the inventory 
    it returns the item information.
    '''
    msg = 'Item could not be found'
    for elements in inventory:
        if item.title() in elements:
            return elements[0:5]
    return msg

def item_messages(inventory, item):
    ''' str, str_> str
    Function returns a different message if
    the item is in the inventory or if the items is not
    in the inventory
    '''
    good_msg = 'Here is the item, followed by the quantity left and the price per item'
    bad_msg = 'We are sorry, but we do not have the item for rent'
    for elements in inventory:
        if item.title() in elements:
            return good_msg
    return bad_msg
