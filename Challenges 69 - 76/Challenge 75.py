# 075
# Create a list of four three-digit numbers. Display the list
# to the user, showing each item from the list on a separate line.
# Ask the user to enter a three-digit number. If the number they
# have typed in matches one in the list, display the position of
# that number in the list, otherwise display the message “That
# is not in the list”.

import random
from typing import List


def create_random_list(length: int = 50, lowest_num: int = 0,
                       highest_num: int = 5) -> List[int]:
    """Returns a random list at a user set len, and lower and upper
    bounds"""

    # used to test return_index function

    random_list = list()

    for i in range(length):
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


def return_index(tp, element) -> List[int]:
    """Returns all the indexes of an element"""

    indexes = []
    [indexes.append(index) for index, value in enumerate(tp)
     if value == element]

    return indexes


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


if __name__ == '__main__':

    lst = create_random_list(4, 100, 999)

    print(print_list(lst))

    while True:
        num = get_num_int('Enter a three digit number: ')

        if 100 <= num <= 999:
            break

    index = return_index(lst, num)
    if index:
        print(f'That number is at position {print_list(index)}')
    else:
        print('That number is not in the list.')
