# 123
# In Python, it is not technically possible to directly delete a
# record from a .csv file. Instead you need to save the file to
# a temporary list in Python, make the changes to the list and
# then overwrite the original file with the temporary list.
# Change the previous program to allow you to do this.Your menu should
# now look like this:
#
# 1) Add to file
# 2) View all records
# 3) delete a record
# 4) Quit program
#
# Enter the number of your selection:

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
3) Delete a record
4) Quit Program
Enter 1, 2 or 3: '''
    while True:
        choice = get_num_int(menu)
        if 1 <= choice <= 3:
            break
    return choice


def add_salary(file_name: str):

    name = input('Enter name: ')
    salary = get_num_float('Enter salary: ')

    with open(file_name, 'a') as f:
        f.write(name + ', £' + str(salary) + '\n')


def print_csv_table(lst: List, print_row_num: bool = False,
                    prt: bool = True):
    """prints a csv table in a cleaner way"""

    string = ''

    if print_row_num:
        for i in range(len(lst)):
            string += f'{i} {lst[i]}'
    else:
        for i in range(len(lst)):
            string += f'{lst[i]}'

    if prt:
        print(string)

    return string


def delete_record(file_name: str):
    with open(file_name, 'r+') as f:
        print_csv_table(f.readlines(), True)
        f.seek(0, 0)
        lst = f.readlines()
        if len(lst) == 0:
            print('File empty.')
            return

        while True:
            row_to_delete = get_num_int('Enter row to remove: ')
            if 0 <= row_to_delete <= len(lst) - 1:
                break
            else:
                print(f'Enter number between 0 and {len(lst) - 1}')

        del lst[row_to_delete]

        f.truncate(0)
        for element in lst:
            f.write(element)
        print('Row deleted!')
        f.seek(0, 0)
        print_csv_table(f.readlines(), True)


if __name__ == '__main__':
    file_name = 'Salaries.csv'

    while True:

        user_choice = get_menu_choice()

        if user_choice == 1:
            add_salary(file_name)
        elif user_choice == 2:
            with open('Salaries.csv', 'r') as f:
                print_csv_table(f.readlines())
        elif user_choice == 3:
            delete_record(file_name)
        else:
            print('Thank you!')
            break
