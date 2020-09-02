# 134
# Create a new program that will generate two random whole numbers
# between 10 and 50. It should ask the user to add the numbers together
# and type in the answer. If they get the question correct, display
# a suitable image such as a tick; if they get the
# answer wrong, display another suitable image such as a cross. They
# should click on a Next button to get another question.

# Using code from challenge 58

import random
from typing import List, Tuple
import time
import tkinter as tk

dev = True


def _rgb(rgb: tuple):
    return "#%02x%02x%02x" % rgb


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


def get_mode() -> int:
    mode_dict = {
        'Rush mode - race against a timer': ['1'],
        'Slow mode - move at your own pace': ['2'],
        'Mix it up - a mix of slow and rush mode': ['3']
    }

    for mode, mode_number in mode_dict.items():
        print(mode, ' - ', mode_number)

    mode_choice = get_num_int('What mode would you like to play?: ')

    return mode_choice


def get_lower_higher_nums(difficulty: str, symbol: str) \
        -> Tuple[int, int]:
    num_dif_dict = {
        # + -, * /
        'e': [(1, 15), (1, 5)],
        'm': [(1, 100), (1, 10)],
        'h': [(1, 1000), (1, 50)]
    }
    if symbol == '+' or symbol == '-':
        return num_dif_dict[difficulty][0]
    else:
        return num_dif_dict[difficulty][1]


def get_equation(difficulty: str = 'medium') -> Tuple[str, float]:
    symbol = get_symbol()

    lowest_num, highest_num = get_lower_higher_nums(difficulty,
                                                    symbol)

    num1 = random.randint(lowest_num, highest_num)
    num2 = random.randint(lowest_num, highest_num)

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


def set_dif_easy():
    global difficulty
    difficulty = 'easy'


def set_dif_medium():
    global difficulty
    difficulty = 'medium'


def set_dif_hard():
    global difficulty
    difficulty = 'hard'


def difficulty_run():
    easy_btn = tk.Button(window, text='Easy',
                         command=set_dif_easy)
    medium_btn = tk.Button(window, text='Medium',
                           command=set_dif_medium)
    hard_btn = tk.Button(window, text='Hard',
                         command=set_dif_hard)
    easy_btn.place(x=0, y=0)
    medium_btn.place(x=0, y=20)
    hard_btn.place(x=0, y=40)

    if difficulty:
        easy_btn.destroy()
        medium_btn.destroy()
        hard_btn.destroy()
        print('Here')


def get_num_qs():
    num = num_qs_textbox.get()


def num_qs_frame_run(dif):
    num_qs_textbox = tk.Entry(num_qs_frame, justify='center')
    enter_num_qs_btn = tk.Button(text='Enter', command=get_num_qs)


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x600')
    window.title('Maths Quiz')
    difficulty = ''

    difficulty_run()
    
    window.mainloop()

    print('window closed')
    print(difficulty)

# Ideas -
# Current question in top right
# Score in top right
# Average time in top right
