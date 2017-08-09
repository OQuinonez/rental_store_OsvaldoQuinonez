import core, disk, time
from datetime import datetime


def print_rules():
    print('\nHello, welcome to Party Room Rentals.\n\n')
    print('We would like you to know some things before you rent an item.\n\n')
    print(
        'The price of all items is the price per hour\n\nYou also have to pay a 10% deposit of replacement value.\n\n'
    )
    print('Here is what we have for today.\n\n')


def get_item_decision(item_names):
    while True:
        item = input('Which one would you like to look at? ').strip()
        if item in item_names:
            return item
        print('uh-oh we do not have that')


def get_amount(max_amount):
    while True:
        amounts = input('\nHow many would you like? ').strip()
        if amounts.isnumeric():
            if int(amounts) <= max_amount:
                return amounts
        print('invalid choice')


def rent_an_item():
    products = disk.load_items()
    print_rules()
    item_names = core.get_item_names(products)
    print('\n'.join(item_names))
    item = get_item_decision(item_names)
    print(core.get_item(products, item))
    max_amount = core.get_max_amount(item, products)
    amounts = get_amount(max_amount)
    hours = input('\nFor how many hour(s) would you like to rent this item?')
    money = core.cost_of(amounts, item, hours, products)
    tax = core.tax_of(float(money))
    print(
        'We would like to remind you that there is a 10% replacement value required fee. \n'
    )
    deposit = core.replacement_of(item, amounts, products)
    print('Ok your total with tax is $',
          float(money), '\nYou also have to pay a deposit of $',
          float(deposit))
    renting = float(money) + float(deposit)
    products = core.rent_item(products, item, amounts)
    disk.update_history(money, item, amounts, hours, deposit)
    disk.update_inventory(products)
    print('Your total for today is $', renting)


def returning():
    inventory = disk.load_inventory()
    history = disk.load_history()
    print('Here is the list of the items you could have rented.\n')
    print(inventory)
    number = input('What is your number? ')
    depo = core.return_deposit(history, number)
    print('Here is your deposit of $', depo)
    amount = disk.get_amount_history(number)
    disk.add_back(number, amount)
    if disk.add_back(number, amount) == False:
        print('There has been an error')
    else:
        print('\n 1.  Yes\t2.  No')
        option = input('Would you like to look through the store again? ')
        if option == '1':
            store()
        else:
            print('Thank you we hoped you enjoyed your party.')


def total_revenue():
    depo = disk.sum_revenue()
    print("The total revenue for today is $", depo)
    print('Thanks have a good day !')


def manager():
    passw = "Everest1953"
    password = input(
        "Hello manager, can you please type in your password to get the total revenue. \n"
    )
    if password == passw:
        print('Calculating the total revenue for today.')
        print('Loading ...')
        time.sleep(3)
        total_revenue()
    else:
        print("Sorry wrong password please try again.")


def main():
    print('\n1.\tCheck out store\n2.\tReturn items rented\n3.\tManager\n')
    answer = input(
        'What would you like to do today (Please enter number) ? \n ')
    if answer == '1':
        rent_an_item()
    elif answer == '2':
        returning()
    elif answer == '3':
        manager()
    else:
        print("Sorry invalid answer.")


if __name__ == '__main__':
    main()