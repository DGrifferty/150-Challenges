# 102
# Ask the user to enter the name, age and shoe size for four people.
# Ask for the name of one of the people in the list and display
# their age and shoe size.
from typing import Dict


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


def get_num_float(prompt: str) -> float:
    """Function to check if users input a number"""

    while True:
        try:
            number = float(input(prompt))

            return number

        except Exception as e:
            print(e)


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

if __name__ =='__main__':

    name_shoe_size = dict()

    ####### need to get their age too!

    for i in range(4):

        name_shoe_size[get_num_int('Enter their shoe size size')] = \
            input(f'Enter name number {i+1}')


    name_shoe_size = {v:k for k,v in name_shoe_size.items}

    print_dic(name_shoe_size)

    while True:

        name = input('Enter the name: ')















