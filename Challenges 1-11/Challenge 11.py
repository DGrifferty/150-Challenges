# 011
# Task the user to enter a number over 100 and then
# enter a number under 10 and tell them how many times
# the smaller number goes into the larger number in a
# user-friendly format

print('This program will tell you how many times a number below 100'
      'goes into a number above 100')

skip = False

while True:
    try:
        if not skip:
            larger_num = float(
                input('Please enter the larger number: '))
            skip = True

        smaller_num = float(input('Please enter the smaller number: '))

        print(f'{smaller_num} goes into {larger_num} '
              f'{larger_num // smaller_num} times with a remainder of '
              f'{larger_num % smaller_num}')

        break

    except Exception as e:
        print(e)
