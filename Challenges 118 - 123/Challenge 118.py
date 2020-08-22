# 118
# Define a subprogram that will ask the user to enter a number and
# save it as the variable “num”. Define another subprogram that will
# use “num” and count from 1 to that number.
import time


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


def count(num: int, ascending: bool =True,
          sleep: bool = False) -> None:
    """Counts to a number, and waits a second inbettwen each number"""

    if ascending:
        for i in range(num):
            print(i + 1)
            if sleep:
                time.sleep(1)
    if not ascending:
        for i in range(num):
            print(num - i)
            if sleep:
                time.sleep(1)


if __name__ == '__main__':
    count(get_num_int('Enter number to count to: '), False, True)
