# 064
# Draw a five-pointed star.

# (Using turtle module)

import turtle
import random


def random_colour_selector() -> None:

    outline, fill = [], []

    for i in range(3):
        outline.append(random.randint(0, 255))
        fill.append(random.randint(0, 255))

    turtle.color(tuple(outline), tuple(fill))


def draw_triangle(side_length: int = 100, random_colours: bool = True
                  ) -> None:
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(side_length)
        turtle.right(120)
        if random_colours:
            random_colour_selector()
    turtle.end_fill()


def draw_clover(no_of_points: int = 5):

    for i in range(no_of_points):
        draw_triangle()
        turtle.right(360/no_of_points)


def draw_star(side_length: int = 100, random_colours: bool = True):

    turtle.right(180)
    
    for i in range(5):
        turtle.forward(side_length)
        turtle.right(144)
        if random_colours:
            random_colour_selector()



if __name__ == '__main__':

    scr = turtle.Screen()
    scr.colormode(255)
    turtle.pensize(2)
    turtle.title('Drawing a five pointed star')
    turtle.speed(0)


    # draw_clover()
    
    draw_star()

    turtle.exitonclick()
