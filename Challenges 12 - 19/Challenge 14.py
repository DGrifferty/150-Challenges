# 014
# Ask the user to enter a number between 10 and 20 (inclusive).
# If they enter a number within this range,
# display the message “Thank you”, otherwise display the message
# “Incorrect answer”.


while True:
    try:

        num = float(input('Please enter a number below between 10 '
                          'and 20: '))

        if 10 <= num <= 20:
            print('Thank you')
            break
        else:
            print('Incorrect answer, try again.')

    except Exception as e:
        print(e)
