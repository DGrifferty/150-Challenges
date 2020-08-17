# 086
# Ask the user to enter a new password. Ask them to enter it again.
# If the two passwords match, display “Thank you”. If the letters
# are correct but in the wrong case, display the message “They must
# be in the same case”, otherwise display the message “Incorrect”.

from getpass import getpass

while True:
    pass1 = getpass('Enter password: ')
    pass2 = getpass('Confirm password: ')

    if not pass1 == pass2:

        if pass1.lower() == pass2.lower():
            print('Please check the cases')
            continue
        else:
            print('Try again')

    else:
        print('Thank you')
        break
