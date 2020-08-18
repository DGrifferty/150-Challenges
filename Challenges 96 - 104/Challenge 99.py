# 099
# Change your previous program to ask the user which row they
# want displayed. Display that row. Ask which column in that row they
# want displayed and display the value that is held there. Ask
# the user if they want to change the value. If they do, ask
# for a new value and change the data. Finally, display
# the whole row again

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


def yes_no_checker(string):
    """Gets user input, if yes returns True,
    else if no, returns false"""
    yes_list = ['yes', 'y', '1']
    no_list = ['no', 'n', '0']
    while True:
        try:
            answer = input(string)
            if answer.lower() not in yes_list and answer.lower() \
                    not in no_list:
                print('Please enter yes or no!')
                continue
            elif answer.lower() in yes_list:
                return True
            else:
                return False

        except Exception as e:
            print(e)


if __name__ == '__main__':

    lst = [[2, 5, 8],
           [3, 7, 4],
           [1, 6, 9],
           [4, 2, 0]]

    rows = len(lst)

    while True:

        user_row = get_num_int('Enter row: ')

        if 0 <= user_row <= rows - 1:
            print_list(lst[user_row])
            columns = len(lst[user_row])
            break
        else:
            print(f'Enter a number between 0 and {rows - 1}')

    while True:

        user_column = get_num_int('Enter column: ')

        if 0 <= user_column <= columns - 1:
            break
        else:
            print(f'Enter a number between 0 and {columns - 1}')

    print(lst[user_row][user_column])

    if yes_no_checker('Would you like to change this value?'):
        lst[user_row][user_column] = get_num_int('Enter new number: ')
        print_list(lst[user_row])
