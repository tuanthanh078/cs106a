"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""

INPUT_FILE = 'bill1.txt'


def print_dict(dict):
    for key in dict:
        print(f'{key}: ${dict[key]}')


def main():
    """
    This program tracks how much money you are spending at each store in
    a given month. It reads a data file containing credit card bill for a
    given month and prints to the screen the total amount that was purchased
    at each store on the bill.
    """
    stores = {}
    with open(INPUT_FILE) as file:
        for line in file:
            infos = line.strip()
            infos.find('[')
            store_name = infos[infos.find('[') + 1:infos.find(']')]
            store_amount = int(infos[infos.find('$') + 1:])
            if store_name in stores:
                stores[store_name] += store_amount
            else:
                stores[store_name] = store_amount
    print_dict(stores)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
