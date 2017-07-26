from disk import load_inventory, load_item, cost_of
from core import get_item, item_messages, tax_of
def rules():
    print('Hello, welcome to Party Room Rentals.\n\n')
    print ('We would like you to know some things before you rent an item.\n\n')
    print('The price of all items is the price per hour\n\nYou also have to pay a 10% deposit of replacement value.\n\n')
    print('Here is what we have for today.\n\n')
def store():
    inventory = load_inventory()
    print(inventory)
    product = input('Which one would you like to look at? ').strip()
    store = load_item()
    valid = get_item(store, product)
    print(valid)
    message = item_messages(inventory, product)
    print(message)
    amount = input('How many would you like? ').strip()
    hours = input('For how many hour(s) would you like to rent this item?')
    money = cost_of(amount, product, hours)
    # tax = tax_of(money)
    print('Your total is $', money)
    # print('Your total with tax is $', tax)
def main():
    rules()
    store()
if __name__ == '__main__':
    main()