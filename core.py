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

# def check_time(inventory,timing_now, number):
#     ''' int _> float
#     Returns the difference in time to see 
#     if the customer owes more or not
#     '''
#     msg = 'Sorry there was an error'
#     for items in inventory:
#         if number in items:
#             time = items[5]
#             diff = timing_now - time
#             # Divided by 60 twice to get the mintues and hours
#             difference = diff.total_seconds()/60/60
#             hours = items[4]
#             if float(difference) > float(hours):
#                 x = float(difference) - float(hours)
#                 return 'You owe', x, 'hours'
#             return difference
#     return msg

def is_on_time(inventory, timing_now, number):
    ''' list[str]], date.time, int _> float
    Returns the number of hours different
    '''
    bad_msg = 'Sorry, there was an error during the transaction please try again.'
    msg = "You did not exceed the hours, unfortunatly we do not give refunds.  "
    for items in inventory:
        if number in items:
            x = datetime.strptime(items[5], "%d/%m/%y %H:%M")
            diff = timing_now - items[5]
            hours_diff = diff.total_seconds()/60/60
            if hours_diff < timing_now:
                total_hrs = hours_diff - timing_now
                return msg
            else:
                return float(total_hrs)
    return bad_msg



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