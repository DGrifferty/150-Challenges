# 031
# Ask the user to enter the radius of a circle (measurement from the
# centre point to the edge). Work out the
# area of the circle (π*radius2).

from math import pi


def check_num(prompt: str) -> float:
    """Function to check if users input is a number"""

    while True:
        try:
            num = float(input(prompt))

            return num

        except Exception as e:
            print(e)


def circle_area(radius: float) -> float:
    """Calculates area of a circle from a given radius"""
    return pi * radius ** 2


if __name__ == '__main__':
    
    request = 'Please enter the radius of the circle you would like to ' \
              'calculate the area for: '
    
    print(circle_area(check_num(request)))





