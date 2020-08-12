# 013
# Ask the user to enter a number that is under 20.
# If they enter a number that is 20 or more,
# display the message “Too high”, otherwise display “Thank you

while True:
    try:

        num = float(input('Please enter a number below 20: '))

        if num < 20:
            print('Thank you')
            break
        if num == 20:
            print('Less than 20, not equal to it. Try again.')
        else:
            print('Less than 20, try again.')

    except Exception as e:
        print(e)
        print('Please enter a number.')

