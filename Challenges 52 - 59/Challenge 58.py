# 058
# Make a maths quiz that asks five questions by randomly generating
# two whole numbers to make the question (e.g. [num1] + [num2]).
# Ask the user to enter the answer. If they get it right add a
# point to their score. At the end of the quiz, tell them how
# many they got correct out of five.

import random
from typing import List, Tuple


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


def get_symbol() -> str:
    symbols = ['+', '-', '*', '/']
    return random.choice(symbols)


def get_difficulty():
    difficulty_dict = {
        'easy': ['e', 'easy', '1'],
        'medium': ['m', 'med', 'medium', '2'],
        'hard': ['h', 'hard', '3']
    }

    while True:
        try:
            answer = input('What difficulty would you like to play'
                           ' at?: ')
            for index, value in enumerate(difficulty_dict.values()):

                if answer.lower() in value:
                    break
                elif index == len(difficulty_dict.values()):
                    print('Please enter easy, medium or hard')

            for key in difficulty_dict.keys():
                if answer.lower() in difficulty_dict[key]:
                    return difficulty_dict[key][0]

        except Exception as e:
            print(e)


def get_equation(difficulty: str = 'medium') -> Tuple[str, float]:
    if difficulty == 'e':
        lowest_num, highest_num = 1, 10
    elif difficulty == 'm':
        lowest_num, highest_num = 1, 50
    elif difficulty == 'h':
        lowest_num, highest_num = 1, 100

    num1 = random.randint(lowest_num, highest_num)
    num2 = random.randint(lowest_num, highest_num)

    symbol = get_symbol()

    if symbol == '+':
        answer = num1 + num2
    elif symbol == '-':
        answer = num1 - num2
    elif symbol == '*':
        answer = num1 * num2
    elif symbol == '/':
        answer = num1 / num2

    equation = str(num1) + ' ' + symbol + ' ' + str(num2) + ' = '

    return equation, answer


if __name__ == '__main__':

    correct_count = 0

    num_questions = get_num_int('How many questions would you like? ')
    difficulty = get_difficulty()

    for i in range(num_questions):

        question, answer = get_equation(difficulty)

        user_answer = get_num_float(question)

        if user_answer == answer:
            print('correct!')
            correct_count += 1
            continue
        else:
            print('Incorrect')
            # while user_answer != answer:
            #     print('incorrect try again!')
            #     user_answer = get_num(question)

    print('------------------------------')
    print(f'Out of {num_questions} you got {correct_count} correct!'
          '\n'
          f'That is {(correct_count / num_questions) * 100}%!')

# todo: change lower number and higher number depending on difficulty
# and symbol
# Todo: Create timer to tell user how long it took
# todo: time each question
# todo: create mode where user rushes against timer
# todo: add square, square root functionality etc.
# todo: create gui
