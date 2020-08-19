# 101
# Using program 100, ask the user for a name and a region.
# Display the relevant data. Ask the user for the name
# and region of data they want to change and allow
# them to make the alteration to the sales figure.
# Display the sales for all regions for the name they choose

from typing import Dict, List


def get_num(prompt: str) -> float:
    """Function to check if users input is a number, and converts it
    to a float"""

    while True:
        try:
            number = float(input(prompt))
            return number

        except Exception as e:
            continue



def sort_dict(dic: Dict[int, str]) -> Dict[int, str]:
    """Sorts the keys into ascending order, filling in any gaps"""
    values = list(dic.values())
    print(values)
    dic.clear()

    for i in range(len(values)):
        print(i)
        print(values[i])
        dic[i + 1] = values[i]

    return dic


def print_dic(dic: Dict) -> str:
    """Allows you to print a dictionary in a cleaner way"""

    values = list(dic.values())
    keys = list(dic.keys())

    string = ''

    for i in range(len(keys)):

        if i == len(keys) - 1:
            string += f'{keys[i]} : {values[i]}.'
        else:
            string += f'{keys[i]} : {values[i]},\n'

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    print(string)


def print_list(lst: List):
    """prints a list in a cleaner way"""

    string = ''

    for i in range(len(lst)):

        if i == len(lst) - 1:
            string += f'{lst[i]}.'
        else:
            string += f'{lst[i]}, '

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    print(string)


if __name__ == '__main__':

    sales = {
        'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
        'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
        'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
        'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
    }

    # Get name

    print_dic(sales)

    while True:

        person = input('Please enter the name '
                        'of the salesman: ').title()

        if person in sales.keys():
            print(sales[person])
            break
        else:
            print(f'Please enter one of the following: ')
            print_list(list(sales.keys()))


    # Getting region

    while True:

        region = input('Please enter the region of interest').upper()

        if region in sales[person].keys():
            print(sales[person][region])
            break
        else:
            print('Please enter one of the following:')
            print_list(list(sales[person].keys()))

    # Getting new data

    new_data = get_num(input('Enter the new data for this saleman\'s'
                             ' region: '))

    sales[person][region] = new_data

    print(f'{person} : {sales[person]}')
