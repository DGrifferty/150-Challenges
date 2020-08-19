# 102
# Ask the user to enter the name, age and shoe size for four people.
# Ask for the name of one of the people in the list and display
# their age and shoe size.


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)

def get_num_float(prompt: str) -> float:
    """Function to check if users input a number"""

    while True:
        try:
            number = float(input(prompt))

            return number

        except Exception as e:
            print(e)

if __name__ =='__main__':

    



