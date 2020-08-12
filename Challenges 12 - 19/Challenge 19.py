# 019
# Ask the user to enter 1, 2 or 3. If they enter a 1, display the
# message “Thank you”, if they enter a 2, display “Well done”,
# if they enter a 3, display “Correct”. If they enter anything
# else, display “Error message”.


accepted = {
    1: 'Thank you',
    2: 'Well done',
    3: 'Correct'
}

while True:
    try:

        num = float(input('Enter 1, 2, or 3:'))

        if num not in accepted.keys():
            raise Exception('')

        print(accepted[num])
        break

    except Exception as e:
        print(e, end=' ')