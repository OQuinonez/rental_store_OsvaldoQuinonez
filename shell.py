from core import only_items
def main():
    print('Hello, welcome to Party Room Rentals.\n Here is what we have for today.')
    items = only_items()
    print(items)
    answer = input('Which one would you like to look at?')
    


if __name__ == '__main__':
    main()