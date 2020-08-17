# 073
# Ask the user to enter four of their favourite foods and store
# them in a dictionary so that they are indexed with numbers
# starting from 1. Display the dictionary in full, showing the
# index number and the item. Ask them which they want to get
# rid of and remove it from the list. Sort the remaining data
# and display the dictionary.

from typing import Dict


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


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
            string += f'{keys[i]} : {values[i]}, '

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    return string


if __name__ == '__main__':

    food_dict = {}

    for i in range(4):
        food_dict[i + 1] = input(f'Please enter food number {i + 1}: ')

    p = get_num_int('Please enter the number of the food you want to'
                    ' remove: ')

    food_dict.pop(p)
    food_dict = sort_dict(food_dict)

    print(f'Your favourite foods - {print_dic(food_dict)}')

