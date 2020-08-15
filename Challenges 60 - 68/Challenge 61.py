# 061
# Draw a triangle.

# (using the turtle module)

import turtle


def draw_triangle(side_length: int = 100) -> None:
    turtle.color('black', 'red')
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(side_length)
        turtle.right(120)
    turtle.end_fill()


if __name__ == '__main__':

    sides = 400

    turtle.penup()

    turtle.left(180)
    turtle.forward(sides / 2)
    turtle.right(90)
    turtle.forward(sides / 2)
    turtle.right(90)

    turtle.pendown()

    turtle.pensize(3)

    draw_triangle(sides)

    turtle.exitonclick()

