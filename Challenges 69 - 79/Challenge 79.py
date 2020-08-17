# 079
# Create an empty list called “nums”. Ask the user to enter numbers.
# After each number is entered, add it to the end of the nums list
# and display the list. Once they have entered three numbers, ask
# them if they still want the last number they entered saved. If
# they say “no”, remove the last item from the list. Display the
# list of numbers.
from typing import List


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


def get_num_float(prompt: str) -> float:
    """Function to check if users input a number"""

    while True:
        try:
            number = float(input(prompt))

            return number

        except Exception as e:
            print(e)


def yes_no_checker(string):
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

    nums = list()

    for i in range(3):
        nums.append(get_num_float(f'Enter number {i + 1}: '))

    print_list(nums)

    if not yes_no_checker(f'Would you like to keep the number'
                          f'{nums[-1]}?\n: '):
        nums.pop()

        print_list(nums)









