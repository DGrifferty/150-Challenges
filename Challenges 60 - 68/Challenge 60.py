# 060
# Draw a square.

# (using Turtle module)

import turtle


def draw_square(side_length: int = 100) -> None:
    turtle.color('black', 'red')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()


if __name__ == '__main__':

    draw_square()

    turtle.exitonclick()