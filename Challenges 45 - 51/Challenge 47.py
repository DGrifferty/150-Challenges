# 047
# Ask the user to enter a number and then enter another number. Add
# these two numbers together and then ask if they want to add another
# number. If they enter “y" ask them to enter another number and keep
# adding numbers until they do not answer “y”. Once the loop
# has stopped, display the total.
from typing import List


def get_num(prompt: str) -> float:
    """Function to check if users input is a number"""

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


def print_list(lst: List[float]):
    string = ''
    for i in range(len(lst)):
        string += f'{lst[i]}, '

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    return string


if __name__ == '__main__':

    request = 'Enter a number: '
    question = 'Would you like to add another number? : '
    summed = list()
    while True:

        summed.append(get_num(request))

        if len(summed) >= 2:
            if yes_no_checker(question):
                continue
            else:
                break

    print(f'After adding the following:\n{print_list(summed)}')
    print(f'The final total is: {sum(summed)}')
