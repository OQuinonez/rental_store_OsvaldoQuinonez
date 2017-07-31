from disk import load_inventory, load_item, replacement_of
from disk import update_history, transaction_num, cost_of
from core import get_item, item_messages, tax_of, rent_time
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
    number = input('What is your number? ')
def main():
    print('1.\tCheck out store\n2.\tReturn items rented\n')
    answer = input('What would you like to do today (Please enter number) ?  ')
    if answer == '1':
        rules()
        store()
    elif answer == '2':
        return None
    else:
        print("Sorry invalid answer.")
if __name__ == '__main__':
    main()
