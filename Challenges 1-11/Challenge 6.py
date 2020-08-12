# 006
# Ask how many slices of pizza the user started with and ask how many
# slices they have eaten. Work out how many slices they have left and
# display the answer in a userfriendly format.


while True:
    try:
        numbers = input('Please enter how many slices of pizza you had'
                        ' and how many you have eaten:')
        numbers = numbers.split(' ')
        if len(numbers) != 2:
            continue
        for index, value in enumerate(numbers):
            numbers[index] = float(value)

        print(f'How many slices you have left: {numbers[1]-numbers[0]}')

        break
    except Exception as e:
        print(e)
        print('Please enter the numbers separated by spaces!')