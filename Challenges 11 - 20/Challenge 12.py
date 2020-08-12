# 012
# Ask for two numbers. If the first one is larger than the second,
# display the second number first and then the first number,
# otherwise show the first number first and then the second.

import time
import numpy as np
start_time = time.time()

print('This program tells you useful information out of an '
      'inputted list of numbers, including the largest number.')

while True:
    try:

        numbers = input('Enter your numbers: ')

        numbers = numbers.split(' ')

        for index, value in enumerate(numbers):
            numbers[index] = float(value)

        print(f'Largest number - {max(numbers)} ')
        print(f'Smallest number - {min(numbers)}')
        print(f'Sum of numbers - {sum(numbers)}')
        num_array = np.array(numbers)
        print(f'Mean of numbers - {np.mean(num_array):.2f}')
        # Without numpy -
        # print(f'Mean of numbers - {sum(numbers)/len(numbers):.2f}')

        break

    except Exception as e:
        print(e)
        print('Please enter your numbers separated by spaces!')

print(f'Completed in {time.time() - start_time:.2f}s.')
