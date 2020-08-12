# 009
# Write a program that will ask for a number of days and then will
# show how many hours, minutes and seconds are in that number of days.


while True:
    try:
        days = input('Please enter the number of days: ')

        days = float(days)

        print(f'{days} days is equivalent to:')
        print(f'{days * 24} hours')
        print(f'{days * 24 *60} minutes')
        print(f'{days * 24 * 60 ** 2} seconds')

        break

    except Exception as e:
        print(e)
        print('Please enter one number.')