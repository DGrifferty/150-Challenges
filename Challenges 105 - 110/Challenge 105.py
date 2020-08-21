# 105
# Write a new file called “Numbers.txt”. Add five numbers to the
# document which are stored on the same line and only separated by
# a comma. Once you have run the program, look in the location where
# your program is stored and you should see that the file has been
# created. The easiest way to view the contents of the new text
# file on a Windows system is to read it using Notepad.

import random
from typing import List


def create_random_list(length: int = 50, lowest_num: int = 0,
                       highest_num: int = 100) -> List[int]:
    """Returns a random list at a user set len, and lower and upper
    bounds"""

    # used to test return_index function

    random_list = list()

    for i in range(length):
        random_list.append(random.randint(lowest_num, highest_num))

    return random_list


if __name__ == '__main__':

	lst = create_random_list(5)

	with open('Numbers.txt', 'w') as f:

		for index, value in enumerate(lst):

			if index < len(lst) - 1:
				parsed_num = str(value) + ', '
				f.write(parsed_num)
			else:
				f.write(str(value))




















