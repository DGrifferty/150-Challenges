# 003
# Ask the user to enter three numbers.
# Add together the first two numbers and then multiply this
# total by the third. Display the answer as The answer is [answer].


while True:
    try:
        numbers = input('Please enter 3 numbers: ')
        numbers = numbers.split(' ')
        if len(numbers) != 3:
            continue
        for index, value in enumerate(numbers):
            numbers[index] = float(value)

        print(f'Result: {(sum(numbers[0:2]) * numbers[2])}')
        break
    except Exception as e:
        print(e)
        print('Please enter the numbers separated by spaces!')