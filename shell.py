from disk import load_inventory
def main():
    print('Hello, welcome to Party Room Rentals.\n Here is what we have for today.')
    items = load_inventory()
    print(items)
    answer = input('Which one would you like to look at?')



if __name__ == '__main__':
    main()