# 062
# Draw a circle.

# (using the turtle module)


import turtle


# turtle.circle(100) # Built in method

turtle.speed(0)

for i in range(360):
    # Much slower
    turtle.forward(1)
    turtle.right(1)

turtle.exitonclick()