# 110
# Using the Names.txt file you created earlier, display the list
# of names in Python. Ask the user to type in one of the names
# and then save all the names except the one they entered into
# a new file called Names2.txt.

from typing import List


def remove_n(lst: List[str]) -> List[str]:
	"""removes \\n from end of a all elements in list and returns
	string"""

	for index, element in enumerate(lst):  # To removing /n
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

		if i > 0:
			if i % 10 == 0:
				string += '\n'

	print(string)


if __name__ == '__main__':

	with open('Names.txt', 'r') as f:
		names = f.readlines()
		names = remove_n(names)
		print_list(names)

	while True:

		user_name = input('Enter a name in the list to remove').title()

		if user_name in names:
			names.remove(user_name)
			print_list(names)
			break
		else:
			print('Please only enter a name from the list')
			print_list(names)

	with open('Names2.txt', 'w') as f:

		for name in names:
			parsed_name = name + '\n'
			f.write(parsed_name)

		print('Names printed to file Names2.txt')
