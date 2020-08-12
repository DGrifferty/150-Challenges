# 036 
# Alter program 035 so that it will ask the user to enter their 
# name and a number and then display their name that number of times. 
from typing import Tuple

def check_input_str_num(prompt: str) -> Tuple[str, int]:
    while True:
        try:
            user_input = input(prompt)

            user_input = user_input.split(' ')

            if len(user_input) != 2:
                raise Exception('Please enter your name and a number'
                                'separated by a space.')

            return user_input[0], int(user_input[1])

        except Exception as e:
            print(e)


if __name__ == '__main__':

    request = 'Please enter you first name and the number of times'\
               '\nyou would like it to be printed in the console: '

    name, num = check_input_str_num(request)

    for i in range(num):
        print(name)
