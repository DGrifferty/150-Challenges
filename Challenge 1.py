# 001
# Ask for the user’s first name and display the output
# message Hello [First Name].

while True:
    try:
        First_name = input('Please enter your name:')
        break
    except Exception as e:
        print(e)

print(f'Hello {First_name}')
