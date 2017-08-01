from disk import load_inventory, load_item, replacement_of
from disk import update_history, transaction_num, cost_of
from core import get_item, item_messages, tax_of, rent_time
from core import return_deposit, is_on_time
from disk import load_history, take_away
import time
from datetime import datetime
def rules():
    print('\nHello, welcome to Party Room Rentals.\n\n')
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
    amount = input('\nHow many would you like? ').strip()
    hours = input('\nFor how many hour(s) would you like to rent this item?')
    money = cost_of(float(amount), product, hours)
    tax = tax_of(float(money))
    take_away(product, amount)
    if take_away(product, amount) == False:
        print('Sorry, we do not have that many items.')
    else:
        print('We would like to remind you that there is a 10% replacement value required fee. \n')
        replacing = replacement_of(product, amount)
        print('Ok your total with tax is $', float(money), '\nYou also have to pay a deposit of $', float(replacing))
        time_out = rent_time(product)
        renting = float(money) + float(replacing)
        print('Your total for today is $', renting)
        number = transaction_num(product)
        update_history(str(number), float(money), product, int(amount), float(hours), time_out, replacing)
        print('Thanks for stopping by your number is ', number, ' you will need it when you come back.')
def returning():
    inventory = load_inventory()
    number = input('What is your number? ')
    history = load_history()
    depo = return_deposit(history, number)
    print('Let\'s see if you exceed your hours. ')
    print('Loading...')
    time.sleep(3)
    right_now = datetime.now()
    answer = is_on_time(history, right_now, number)
    print(answer)
    print('Here is your deposit of $', depo)
    print('\n 1.  Yes\t2.  No')
    option = input('Would you like to look through the store again? ')
    if option == '1':
        store()
    else:
        print('Thank you we hoped you enjoyed your party.')

def main():
    print('1.\tCheck out store\n2.\tReturn items rented\n')
    answer = input('What would you like to do today (Please enter number) ?  ')

    if answer == '1':
        rules()
        store()
    elif answer == '2':
        returning()
    else:
        print("Sorry invalid answer.")
if __name__ == '__main__':
    main()