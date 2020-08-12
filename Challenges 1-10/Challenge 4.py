# 004
# Ask the user to enter two numbers.
# Add them together and display the answer as The total is [answer].


while True:
    try:
        numbers = input('Please enter the number you want to add: ')
        numbers = numbers.split(' ')
        for index, value in enumerate(numbers):
            numbers[index] = float(value)
        print(f'Sum of numbers: {sum(numbers)}')
        break
    except Exception as e:
        print(e)
        print('Please enter the numbers separated by spaces')