# 041
# Ask the user to enter their name and a number. If the number is less
# than 10, then display their name that number of times; otherwise
# display the message “Too high” three times
from typing import Tuple


def check_input_str_num(prompt: str) -> Tuple[str, int]:
    """A function to check the input of a user is a string and int
    separated by a comma and a space"""

    while True:
        try:
            user_input = input(prompt)

            user_input = user_input.split(', ')

            if len(user_input) != 2:
                raise Exception('Please enter your name and a number'
                                'separated by - \', \' (a comma and'
                                ' a space)')
            if int(user_input[1]) < 0:
                raise Exception('Please enter a number greater than 0.')

            return user_input[0], int(user_input[1])


        except Exception as e:
            print(e)


if __name__ == '__main__':
    request = 'Enter your name and how many times you would like it' \
              ' printed: '

    name, num = check_input_str_num(request)

    if num >= 10:
        for i in range(3):
            print('Too high')
    else:
        for i in range(num):
            print(name)


