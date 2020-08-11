# 007
# Ask the user for their name and their age. Add 1 to their age and
# display the output [Name] next birthday you will be [new age].


while True:
    try:
        age = input('Enter your age: ')
        age = float(age)
        print(f'Your age on your next birthday: {int(age + 1)}')

        break
    except Exception as e:
        print(e)
        print('Please enter a single number!')
