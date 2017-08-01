from disk import load_inventory, load_item, replacement_of
from disk import update_history, transaction_num, cost_of
from core import get_item, item_messages, tax_of, rent_time
from core import return_deposit, is_on_time
from disk import load_history, take_away, add_back
import time
from datetime import datetime
def rules():
    print('\nHello, welcome to Party Room Rentals.\n\n')
    print ('We would like you to know some things before you rent an item.\n\n')
    print('The price of all items is the price per hour\n\nYou also have to pay a 10% deposit of replacement value.\n\n')
    print('Here is what we have for today.\n\n')
def inventory():
    inventory = load_inventory()
    print(inventory)
def valid_product():
    product = input('Which one would you like to look at? ').strip()
    return product
def valid():
    production = valid_product()
    store = load_item()
    valids = get_item(store, production)
    print(valids)
def msg():
    all_inventory = load_history()
    message = item_messages(all_inventory, product)
    print(message)
def amount():
    amounts = input('\nHow many would you like? ').strip()
    return amounts
def hour():
    hours = input('\nFor how many hour(s) would you like to rent this item?')
    return hours
def money_function():
    time = hour()
    quantity = amount()
    production = valid_product()
    money = cost_of(float(quantity), production, time)
    return money
def taxing():
    millions = money_function()
    tax = tax_of(float(millions))
    return tax
def store():
    rules()
    inventory()
    valid_product()
    valid()
    msg()
    quantity = amount()
    print(quantity)
    dinero = money_function()
    # product is now merchandise
    # quantity is now amount
    # time is now hour
    # dinero is now money
    # tax is now taxes
    time = hour()
    print(time)
    taxes = taxing()
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

    # print('Let\'s see if you exceed your hours. ')
    # print('Loading...')
    # time.sleep(3)
    # right_now = datetime.now()
    # answer = is_on_time(history, right_now, number)
    # print(answer)
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