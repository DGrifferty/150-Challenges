# 070
# Add to program 069 to ask the user to enter a
# number and display the country in that position.

from typing import Tuple, List
import random


def get_input_tuple(tp: Tuple[str], prompt: str) -> bool:

    tplow = list((x.lower() for x in tp))

    while True:
        try:

            user_input = input(prompt)
            if user_input.lower() in tplow:
                return tp[tplow.index(user_input)]
            else:
                continue

        except Exception as e:
            print(e)


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


def return_index(tp, element) -> List[int]:
    """Returns all the indexes of an element"""

    indexes = []
    [indexes.append(index) for index, value in enumerate(tp)
     if value == element]

    return indexes


def create_random_list(len: int = 50, lowest_num: int = 0,
                       highest_num: int = 5) -> List[int]:
    """Returns a random list at a user set len, and lower and upper
    bounds"""

    # used to test return_index function

    random_list = list()

    for i in range(len):
        random_list.append(random.randint(lowest_num, highest_num))

    return random_list


def print_list(lst: List[float]):
    """returns a string allowing you to print a list in a cleaner way"""

    string = ''

    for i in range(len(lst)):

        if i == len(lst) - 1:
            string += f'{lst[i]}.'
        else:
            string += f'{lst[i]}, '

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    return string

if __name__ == '__main__':

    countries = ['England', 'Scotland', 'USA', 'Wales', 'France',
                 'Guernsey']

    print(print_list(countries))

    while True:
        user_choice_in = get_num_int(
            'Enter the index of your selection: ')

        if user_choice_in < 0 or user_choice_in > len(countries) - 1:
            print(f'Please enter a number between 0 and '
                  f'{len(countries) -1}')
        else:
            break

    print('------------------')
    print(f'You selected - {countries[user_choice_in]}!')

