# 010
# There are 2,204 pounds in a kilogram.
# Ask the user to enter a weight in kilograms and convert it to pounds.
import time

start_time = time.time()

print('This program converts between pounds and kilograms')
onekgtopound = 2.20462262
convert = {
    'k': 1 / onekgtopound,
    'p': onekgtopound
}
response = False

while True:
    try:
        if response == False:
            print(f'If you would like to convert to pounds enter p')
            response = input(
                'or if you would like to convert to kilograms'
                'please enter k\n: ')

            if response.lower() not in convert.keys():
                response = False
                continue

        numbers = input(
            'Please enter the weights you would like to convert'
            'or a list separated\nby spaces if you would like'
            'to convert more than one weight\n: ')

        numbers = numbers.split(' ')

        if response.lower() == 'k':
            for index, value in enumerate(numbers):
                numbers[index] = float(value)
                print(f'{numbers[index]} pounds = '
                      f'{numbers[index] * convert[response.lower()]:.3f}'
                      f' kg')
        elif response.lower() == 'p':
            for index, value in enumerate(numbers):
                numbers[index] = float(value)
                print(f'{numbers[index]} kg = '
                      f'{numbers[index] * convert[response.lower()]:.3f}'
                      f'pounds')
        break

    except Exception as e:
        print(e)
        print('Please enter the weights you would like to convert'
              'separated by spaces.')

print(f'Completed in {time.time() - start_time:.2f}s.')
