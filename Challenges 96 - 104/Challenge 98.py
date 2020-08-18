# 098
# Using the 2D list from program 096, ask the user which row they would
# like displayed and display just that row. Ask them to enter a new
# value and add it to the end of the row and display the row again.

from typing import List

def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))
            return number

        except Exception as e:
            print(e)

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

    lst = [[2, 5, 8],
           [3, 7, 4],
           [1, 6, 9],
           [4, 2, 0]]

    rows = len(lst)

    while True:

        user_row = get_num_int('Enter row: ')

        if 0 <= user_row <= rows - 1:
            break
        else:
            print(f'Enter a number between 0 and {rows - 1}')


    user_num = get_num_int('Enter number to add to end of row: ')

    lst[user_row].append(user_num)

    print_list(lst[user_row])



        



