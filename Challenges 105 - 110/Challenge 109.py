# 109
# Display the following menu to the user:
# 1) create a new file
# 2) Display the file
# 3) add a new item to the file
# Make a selection, 1 two or 3
# Ask the user to enter 1, 2 or 3. If they select anything
# other than 1, 2 or 3 it should display a suitable error message.
# If they select 1, ask the user to enter a school subject and
# save it to a new file called “Subject.txt”. It should overwrite
# any existing file with a new file. If they select 2, display the
# contents of the “Subject.txt” file. If they select 3, ask the user
# to enter a new subject and save it to the file and then display
# the entire contents of the file.
# Run the program several times to test the options.

from typing import List


def get_num_int(prompt: str) -> int:
	"""Function to check if users input is an integer"""

	while True:
		try:
			number = int(input(prompt))

			return number

		except Exception as e:
			print(e)


def remove_n(lst: List[str]) -> List[str]:
	"""removes \\n from end of a all elements in list and returns
	string"""

	for index, element in enumerate(lst):  # To remove /n
		if element[-1:-2:-1] == '\n':  # Test if last two characters are "\n"
			lst[index] = element[:-1]
	return lst


def print_list(lst: List):
	"""prints a list in a cleaner way"""

	string = ''

	for i in range(len(lst)):

		if i == len(lst) - 1:
			string += f'{lst[i]}.'
		else:
			string += f'{lst[i]}, '

		if i > 0 and i % 10 == 0:
			string += '\n'

	print(string)


if __name__ == '__main__':

	menu = '1) Create a new file ' \
	       '\n2) Display the file ' \
	       '\n3) Add a new item to the file\n' \
	       'Make a selection, 1 two or 3: '

	while True:

		user_option = get_num_int(menu)

		if 1 <= user_option <= 3:
			break
		else:
			print('Please enter 1, 2 or 3')

	if user_option == 1:

		with open('Subjects.txt', 'w') as f:
			f.write(input('Enter a subject: '))

	elif user_option == 2:

		with open('Subjects.txt', 'r') as f:
			subjects = f.readlines()
			subjects = remove_n(subjects)
			print_list(subjects)

	elif user_option == 3:

		with open('Subjects.txt', 'a') as f:
			f.write('\n')
			f.write(input('Enter a subject: '))
		with open('Subjects.txt', 'r') as f:
			subjects = f.readlines()
			subjects = remove_n(subjects)
			print_list(subjects)
