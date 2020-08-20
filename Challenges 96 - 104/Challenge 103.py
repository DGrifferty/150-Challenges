# 103
# Adapt program 102 to display the names and ages of all the
# people in the list but do not show their shoe size.

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

    name_age_size = dict()

    for i in range(4):

        name = input(f'Enter name number {i+1}: ')

        name_age_size[name] = {'Age': get_num_int('Enter their age: '),\
                               'Shoe size': get_num_int('Enter their '
                                                        'shoe size: ')}

    for key in name_age_size.keys():

        print(key, ' Age: ',  name_age_size[key]['Age'])

    while True:

        name = input('Enter the name: ')

        if name in name_age_size:

            print_dic(name_age_size[name])
            break
