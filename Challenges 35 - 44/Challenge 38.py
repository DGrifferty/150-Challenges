# 038
# Change program 037 to also ask for a number. Display their name
# (one letter at a time on each line) and repeat this for the
# number of times they entered.

from typing import Tuple


def check_input_str_num(prompt: str) -> Tuple[str, int]:
    while True:
        try:
            user_input = input(prompt)

            user_input = user_input.split(', ')

            if len(user_input) != 2:
                raise Exception('Please enter your name and a number'
                                'separated by - \', \' (a comma and'
                                'space)')

            return user_input[0], int(user_input[1])

        except Exception as e:
            print(e)


if __name__ == '__main__':

    request = 'Please enter you first name and the number of times' \
              '\nyou would like it to be printed in the console: '

    name, num = check_input_str_num(request)

    for i in range(num):
        for k in range(len(name)):
            print(name[k])
