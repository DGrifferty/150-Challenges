# 018
# Ask the user to enter a number. If it is under 10, display
# the message “Too low”, if their number is between 10 and 20,
# display “Correct”, otherwise display “Too high”.

while True:
    try:

        num = float(input('Please enter a number: '))

        if 10 > num:
            print('Too low')
        elif 20 < num:
            print('Too high.')
        else:
            print('Correct')
            break

    except Exception as e:
        print(e)
        print('Please enter a number')

