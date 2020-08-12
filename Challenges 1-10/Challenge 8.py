# 008
# Ask for the total price of the bill,
# then ask how many diners there are.
# Divide the total bill by the number of diners
# and show how much each person must pay.

print('Split the bill!')

while True:
    try:
        numbers = input('Please enter the cost of the bill, and how'
                        ' many people ate: ')
        numbers = numbers.split(' ')
        if len(numbers) != 2:
            continue
        for index, value in enumerate(numbers):
            numbers[index] = float(value)

        cost_per_person = (numbers[0]/numbers[1])
        left_over = numbers[0] - round(cost_per_person, 2) * numbers[1]

        print(f'Cost for each person £{cost_per_person:.2f}')
        print(f'With £{left_over:.2f} left over.')

        break

    except Exception as e:
        print(e)
        print('Please enter the numbers separated by spaces!')