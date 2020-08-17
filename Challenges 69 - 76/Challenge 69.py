# 069
# Create a tuple containing the names of five countries and display
# the whole tuple. Ask the user to enter one of the countries that
# have been shown to them and then display the index number
# (i.e. position in the list) of that item in the tuple.

# nice

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
    """Prints a list in a cleaner way"""

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

    user_choice = get_input_tuple(countries, f'Choose a country - '
                                 f'{print_list(countries)}')

    index_user_choice = return_index(countries, user_choice)

    print(f'{user_choice} is at index: '
          f'{print_list(index_user_choice)}')

















