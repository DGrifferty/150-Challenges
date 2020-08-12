# 017
# Ask the user’s age. If they are 18 or over, display the message
# “You can vote”, if they are aged 17, display the message
# “You can learn to drive”, if they are 16, display the message
# “You can buy a lottery ticket”, if they are under 16,
# display the message “You can go Trick-or-Treating”.

while True:
    try:

        age = float(input('Please enter your age: '))

        if age >= 18:
            print('You can vote.')
        elif age == 17:
            print('You can learn to drive')
        else:
            print('You can go Trick-or-Treating.')

        break

    except Exception as e:
        print(e)
        print('Please enter a number')
