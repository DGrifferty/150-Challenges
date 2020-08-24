# 122
# Create the following menu:

# 1) Add to file
# 2) View all records
# 3) Quit Program

# If the user selects 1, allow them to add to a file called
# Salaries.csv which will store their name and salary. If they
# select 2 it should display all records in the Salaries.csv file.
# If they select 3 it should stop the program. If they select an
# incorrect option they should see an error message. They
# should keep returning to the menu until they select option 3.
from typing import List

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


def get_menu_choice() -> int:
    menu = '''
1) Add to file
2) View all records
3) Quit Program
Enter 1, 2 or 3: '''
    while True:
        choice = get_num_int(menu)
        if 1 <= choice <= 3:
            break
    return choice

def add_salary():

    name = input('Enter name: ')
    salary = get_num_float('Enter salary: ')

    with open('Salaries.csv', 'a') as f:
        f.write(name + ', £' + str(salary) + '\n')


def print_csv_table(lst: List, print_row_num: bool = False,
                    prt: bool = True):
    """prints a csv table in a cleaner way"""

    string = ''

    if print_row_num:
        for i in range(len(lst)):
            string += f'{i + 1} {lst[i]}'
    else:
        for i in range(len(lst)):
            string += f'{lst[i]}'

    if prt:
        print(string)

    return string


if __name__ == '__main__':

    while True:

        user_choice = get_menu_choice()

        if user_choice == 1:
            add_salary()
        elif user_choice == 2:
            with open('Salaries.csv', 'r') as f:
                print_csv_table(f.readlines())
        else:
            print('Thank you!')
            break
