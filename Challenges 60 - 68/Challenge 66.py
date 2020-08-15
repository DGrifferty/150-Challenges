# 066
# Draw an octagon that uses a different colour
# (randomly selected from a list of six possible colours) for each line.
import turtle
import random


def random_colour_selector() -> None:

    outline, fill = [], []

    for i in range(3):
        outline.append(random.randint(0, 255))
        fill.append(random.randint(0, 255))

    turtle.color(tuple(outline), tuple(fill))


def draw_octagon(side_length: int = 100, random_colours = True):

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

    turtle.end_fill()


if __name__ == '__main__':

    pen = turtle.Pen()

    scr = turtle.Screen()
    scr.colormode(255)
    turtle.pensize(10)

    turtle.title('Drawing an octagon')
    turtle.speed(0)

    
    draw_octagon()

    turtle.exitonclick()
