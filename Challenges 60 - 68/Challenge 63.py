# 063 Draw three squares in a row
# with a gap between each.Fill them using three different colours.
# (Using turtle module)

import turtle
from typing import Tuple
import random


def draw_square(side_length: int = 100) -> None:

    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()


def random_colour_selector() -> None:

    # colour =['black', 'red', 'yellow', 'green', 'purple', 'orange']
    # turtle.color(random.choice(colour), random.choice(colour))

    outline = (random.randint(0, 255), random.randint(0, 255),
               random.randint(0, 255))
    fill = (random.randint(0, 255), random.randint(0, 255),
            random.randint(0, 255))

    turtle.color(outline, fill)


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


if __name__ == '__main__':

    scr = turtle.Screen()
    scr.colormode(255)
    turtle.pensize(2)

    square_of_squares(2)

    # rotated_squares()

    turtle.exitonclick()

