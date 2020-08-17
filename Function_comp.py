from typing import List, Tuple
from math import pi
import math
import turtle
# todo: tidy list and put latest versions of functions in here and missing functions

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

def check_num(prompt: str) -> float:
    """Function to check if users input is a num"""

    while True:
        try:
            num = float(input(prompt))

            return num

        except Exception as e:
            print(e)


def input_checker(string):
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


def length(s1: str, l: int = 5) -> bool:
    if len(s1) < l:
        return True
    return False


def convert_pig(words):
    for index, value in enumerate(words):

        if words[index][0].lower() in 'aeiou':
            words[index] = words[index] + 'way'
            continue

        first_consonant = words[index][0]

        words[index] = words[index][1:] + first_consonant + 'ay'

    return words


def check_num_list(prompt: str, max_length: int = 0,
                   min_length: int = 0) -> List[float]:
    """Function to check if users input is a number, splitting number
    by spaces and checking that the correct amount of numbers are
    entered, returning them in a list"""

    while True:
        try:
            num = input(prompt)
            num = num.split(' ')
            if min_length:
                assert len(num) >= min_length, f'Please enter at least' \
                                               f' {min_length} numbers'
            if max_length:
                assert len(num) <= max_length, f'Please enter no more ' \
                                               f'than {max_length} ' \
                                               f'numbers'
            for index, value in enumerate(num):
                num[index] = float(value)

            return num

        except Exception as e:
            print(e)


def circle_area(radius: float) -> float:
    """Calculates area of a circle from a given radius"""
    return pi * radius ** 2


def cylinder_volume(radius_height: List[float]) -> float:
    """Calculates the volume of a cylinder from a given radius and
    height, from  a list"""

    return circle_area(radius_height[0]) * radius_height[1]


def integer_devision_remainder(nums: List[float]) -> str:
    return f'{nums[0]} / {nums[1]} = {nums[0] // nums[1]} with' \
           f' a remainder of {nums[0] % nums[1]}'


def square_area(side_length: float) -> float:
    return side_length * side_length


def triangle_area(base_height: List[float]) -> float:
    return 0.5 * base_height[0] * base_height[1]


def square_or_triangle() -> bool:
    print('Would you like to calculate the area of a square or '
          'triangle?')
    while True:
        try:

            print('1) square\n2) triangle')
            choice = int(input('Choose an option: '))

            if choice != 1 and choice != 2:
                raise Exception('Please enter 1 or 2.')

            if choice == 1:
                return True
            else:
                return False

        except Exception as e:
            print(e)


def random_colour_selector() -> None:
    outline, fill = [], []

    for i in range(3):
        outline.append(random.randint(0, 255))
        fill.append(random.randint(0, 255))

    turtle.color(tuple(outline), tuple(fill))


def draw_octagon(side_length: int = 100, random_colours=True,
                 fill: bool = False):
    if fill:
        turtle.begin_fill()

    for i in range(8):
        if random_colours:
            if i <= 6:  # Prevents calculating fill colours when they
                #  are not in use
                outline = []
                for _ in range(3):
                    outline.append(random.randint(0, 255))
                turtle.pencolor(tuple(outline))
            else:
                random_colour_selector()

        turtle.forward(side_length)
        turtle.right(45)

    if fill:
        turtle.end_fill()


def draw_pattern(i: int = 10):
    for x in range(0, i):
        draw_octagon()
        turtle.right(360 / i)


def draw_random_pattern():

    i = random.randint(0, 100)
    for x in range(i):
        draw_octagon(random.randint(1, 170))
        turtle.right(360/i)


def draw_square(side_length: int = 100) -> None:

    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()

def square_of_squares(sides) -> None:

    turtle.title('A square of squares!')

    for i in range(4):
        turtle.right(90)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        for i in range(sides-1):
            random_colour_selector()
            draw_square()
            turtle.forward(100)


def rotated_squares(no_of_squares: int = 10) -> None:

    turtle.title('A fan of squares!')

    for i in range(no_of_squares):
        turtle.right(360/no_of_squares)
        random_colour_selector()
        draw_square()

def draw_triangle(side_length: int = 100) -> None:
    turtle.color('black', 'red')
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(side_length)
        turtle.right(120)
    turtle.end_fill()

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


def get_lower_higher_nums(difficulty: str, symbol: str)\
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

    lowest_num, highest_num = get_lower_higher_nums(difficulty, symbol)

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

def heads_tails_checker(string:str) -> bool:
    """Function to check user enters an accepted input, then returns
    input as boolean"""
    heads_list = ['heads', 'head', 'h', '1']
    tails_list = ['tails', 'tail', 't', '0']
    while True:
        try:
            answer = input(string)
            if answer.lower() not in heads_list and answer.lower() \
                    not in tails_list:
                print('Please enter heads or tails!')
                continue
            elif answer.lower() in heads_list:
                return True
            else:
                return False

        except Exception as e:
            print(e)

def get_input_tuple(tp: Tuple[str], prompt: str) -> bool:

    tplow = list((x.lower() for x in tp))

    while True:
        try:

            user_input = input(prompt)
            if user_input.lower() in tplow:
                return tp[tplow.index(user_input)]
            else:
                continue

        except Exception as e:
            print(e)


def return_index(tp, element) -> List[int]:
    """Returns all the indexes of an element"""

    indexes = []
    [indexes.append(index) for index, value in enumerate(tp)
     if value == element]

    return indexes


def create_random_list(len: int = 50, lowest_num: int = 0,
                       highest_num: int = 5) -> List[int]:
    """Returns a random list at a user set len, and lower and upper
    bounds"""

    # used to test return_index function

    random_list = list()

    for i in range(len):
        random_list.append(random.randint(lowest_num, highest_num))

    return random_list


def print_list(lst: List):
    """returns a string allowing you to print a list in a cleaner way"""

    string = ''

    for i in range(len(lst)):

        if i == len(lst) - 1:
            string += f'{lst[i]}.'
        else:
            string += f'{lst[i]}, '

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    return string

