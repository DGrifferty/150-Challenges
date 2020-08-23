# 120
# Display the following menu to the user:
#
# 1) Addition
# 2) Subtraction
# Enter 1 or 2
#
# If they enter a 1, it should run a subprogram that will generate two
# random numbers between 5 and 20, and ask the user to add them
# together. Work out the correct answer and return both the user’s
# answer and the correct answer. If they entered 2 as their selection
# on the menu, it should run a subprogram that will generate one number
# between 25 and 50 and another number between 1 and 25 and ask them
# to work out num1 minus num2. This way they will not have to worry
# about negative answers. Return both the user’s answer and the
# correct answer. Create another subprogram that will check if the
# user’s answer matches the actual answer. If it does, display
# “Correct”, otherwise display a message that will say “Incorrect,
# the answer is” and display the real answer If they do not select a
# relevant option on the first menu you should display a suitable
# message.


# similar/more complex solutions that result in a
# more enjoyable program seen in challenge 58/117

import random
from typing import List, Tuple
import time

dev = False


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))
            return number

        except Exception as e:
            print(e)


def get_equation(menu_choice) -> Tuple[str, float]:

    if menu_choice == 1:
        symbol, num1, num2 = '+', random.randint(5, 20), \
                             random.randint(5, 20)
        answer = num1 + num2
    else:
        symbol, num1, num2 = '-', random.randint(25, 50),\
                             random.randint(1, 25)
        answer = num1 - num2

    equation = str(num1) + ' ' + symbol + ' ' + str(num2) + ' = '

    return equation, answer


if __name__ == '__main__':
    correct_count = 0
    time_list = list()

    while True:
        menu_choice = get_num_int(
            '1) Addition\n2) Subtraction\nEnter 1 or 2: ')
        if 1 <= menu_choice <= 2:
            break

    for i in range(3):

        question, answer = get_equation(menu_choice)

        if dev:
            print(answer)

        start_time = time.time()
        user_answer = get_num_int(question)
        time_took = time.time() - start_time
        time_list.append(time_took)

        if answer == user_answer:
            print('Correct!')
            print(f'You took - {time_took:.2f}s')
            correct_count += 1
            continue
        else:
            print('Incorrect')
            print(f'You took - {time_took:.2f}s')

    print('------------------------------')
    print(f'You got {correct_count} out of {3}!'
          '\n'
          f'Scoring {(correct_count / 3) * 100}%!')
    print(f'You took an average time of '
          f'{sum(time_list) / 3:.2f}s '
          f'to answer the questions.')
