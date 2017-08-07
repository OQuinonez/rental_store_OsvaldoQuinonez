import core
import disk
import time
from datetime import datetime
def rules():
    print('\nHello, welcome to Party Room Rentals.\n\n')
    print ('We would like you to know some things before you rent an item.\n\n')
    print('The price of all items is the price per hour\n\nYou also have to pay a 10% deposit of replacement value.\n\n')
    print('Here is what we have for today.\n\n')
def inventory():
    inventory = disk.load_inventory()
    print(inventory)
def valid_product():
    product = input('Which one would you like to look at? ').strip()
    store = disk.load_item()
    valids = core.get_item(store, product)
    print(valids)
    all_inventory = disk.load_history()
    message = core.item_messages(all_inventory, product)
    print(message)
    amounts = input('\nHow many would you like? ').strip()
    hours = input('\nFor how many hour(s) would you like to rent this item?')
    money = disk.cost_of(amounts, product, hours)
    tax = core.tax_of(float(money))
    disk.take_away(product, amounts)
    if disk.take_away(product, amounts) == False:
        print('Sorry, we do not have that many items.')
    else:
        print('We would like to remind you that there is a 10% replacement value required fee. \n')
        replacing = disk.replacement_of(product, amounts)
        print('Ok your total with tax is $', float(money), '\nYou also have to pay a deposit of $', float(replacing))
        time_out = core.rent_time(product)
        renting = float(money) + float(replacing)
        print('Your total for today is $', renting)
        number = disk.transaction_num(product)
        disk.update_history(str(number), float(money), product, int(amounts), float(hours), time_out, replacing)
        print('Thanks for stopping by your number is ', number, ' you will need it when you come back.')
def store():
    rules()
    inventory()
    valid_product()
def returning():
    inventory = disk.load_inventory()
    history = disk.load_history()
    print(inventory)
    number = input('What is your number? ')
    depo = core.return_deposit(history, number)
    print('Here is your deposit of $', depo)
    print('\n 1.  Yes\t2.  No')
    option = input('Would you like to look through the store again? ')
    if option == '1':
        store()
    else:
        print('Thank you we hoped you enjoyed your party.')

def main():
    print('\n1.\tCheck out store\n2.\tReturn items rented\n')
    answer = input('What would you like to do today (Please enter number) ?  ')

    if answer == '1':
        store()
    elif answer == '2':
        returning()
    else:
        print("Sorry invalid answer.")
if __name__ == '__main__':
    main()