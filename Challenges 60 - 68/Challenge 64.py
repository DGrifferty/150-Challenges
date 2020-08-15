# 064
# Draw a five-pointed star.

# (Using turtle module)

import turtle


def draw_triangle(side_length: int = 100) -> None:
    turtle.color('black', 'red')
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(side_length)
        turtle.right(120)
    turtle.end_fill()
