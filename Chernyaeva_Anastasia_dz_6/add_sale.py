import sys


def add_sale(new_sale: str):
    with open('bakery.csv', 'a', encoding='utf-8') as users_file:
        users_file.write(f"{new_sale}\n")


add_sale(sys.argv[1])
