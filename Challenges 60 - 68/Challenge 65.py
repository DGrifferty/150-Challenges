# 065
# Write the numbers as shown below, starting at the
# bottom of the number one.

# (numbers show are 1 2 and 3)

# added draw random functionality - not needed

import turtle
import random
from typing import Tuple

def random_colour_selector() -> None:
    outline, fill = [], []

    for i in range(3):
        outline.append(random.randint(0, 255))
        fill.append(random.randint(0, 255))

    turtle.color(tuple(outline), tuple(fill))


def random_move(line_lengths: Tuple[int, int] = (10, 200),
                angle_sizes: Tuple[int, int] = (5, 355)) -> None:

    turtle.forward(random.randint(line_lengths[0], line_lengths[1]))
    left_or_right = random.randint(0, 1)

    if left_or_right == 0:

        turtle.left(random.randint(angle_sizes[0], angle_sizes[1]))

    else:

        turtle.right(random.randint(angle_sizes[0], angle_sizes[1]))


def fix_turtle_pos_rand(rand: bool = True, cent_both: bool = True):

    x, y = turtle.pos()

    if abs(x) > screen_width/2:
        turtle.penup()

        if rand:
            turtle.goto(
                random.randint(-screen_width / 2, screen_width / 2), y)
        else:
            if cent_both:
                turtle.goto(0, 0)
            else:
                turtle.goto(0, y)

        turtle.pendown()

    if abs(y) > screen_height/2:
        turtle.penup()

        if rand:
            turtle.goto(x, random.randint(-screen_height / 2,
                                          screen_height / 2))
        else:
            if cent_both:
                turtle.goto(0, 0)
            else:
                turtle.goto(x, 0)
        turtle.pendown()



def random_pen_thickness() -> None:
    turtle.pensize(random.randint(1, 10))


def draw_random(number_of_lines: int = 100, pen_up: bool = False) -> None:

    for i in range(number_of_lines):

        random_colour_selector()
        random_pen_thickness()
        random_move()
        fix_turtle_pos_rand()

        if pen_up:
            turtle.penup()
            random_move()
            fix_turtle_pos_rand(False, False)
            turtle.pendown()

def draw_123() -> None:



if __name__ == '__main__':

    scr = turtle.Screen()
    screen_width, screen_height = 1024, 600
    scr.setup(screen_width, screen_height)
    scr.colormode(255)
    turtle.speed(0)


    draw_random(1000, True)

    turtle.exitonclick()


# todo: create lines out of cursor