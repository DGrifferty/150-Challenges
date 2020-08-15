# 067 
# Create the following pattern:

# shows pattern reproduced below

import turtle
import random


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
        turtle.right(360/i)

        
if __name__ == '__main__':

    scr = turtle.Screen()
    screen_width, screen_height = 1024, 600
    scr.setup(screen_width, screen_height)
    scr.colormode(255)
    turtle.speed(0)
    
    draw_pattern()

    turtle.hideturtle()
    turtle.exitonclick()
        


