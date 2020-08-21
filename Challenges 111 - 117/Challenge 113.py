# 113
# Using the Books.csv file, ask the user how many records they
# want to add to the list and then allow them to add that many.
# After all the data has been added, ask for an author and display
# all the books in the list by that author. If there are no
# books by that author in the list, display a suitable message.
from typing import List


def get_num_int(prompt: str) -> int:
	"""Function to check if users input is an integer"""

	while True:
		try:
			number = int(input(prompt))

			return number

		except Exception as e:
			print(e)


def print_csv_table(lst: List, prt: bool = True):
	"""prints a csv table in a cleaner way"""

	string = ''

	for i in range(len(lst)):
		string += f'{lst[i]}'

	if prt:
		print(string)

	return string


def remove_n(lst: List[str]) -> List[str]:
	"""removes \\n from end of a all elements in list and returns
	string"""

	for index, element in enumerate(lst):  # To remove /n
		if element[-1:-2:-1] == '\n':  # Test if last two characters are "\n"
			lst[index] = element[:-1]
	return lst


def scan_table(table: List[str], element: str, seperator: str = ', ', prt: bool = False):
	rows_in = list()
	for index, row in enumerate(table):
		split_row = remove_n(row.split(seperator))
		if element.title() in split_row:
			if prt:
				print(row)
			rows_in.append(split_row)

	return rows_in


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
	with open('Books.csv', 'r+') as f:
		table = f.readlines()
		print_csv_table(table)

		for i in range(get_num_int('How many records would you '
		                           'like to add: ')):
			new_row = input(f'Enter record number {i + 1}: ')
			f.write(new_row)
			print('Record added.')

	with open('Books.csv', 'r+') as f:

		while True:
			table = f.readlines()
			data = input(
				'Enter a date, author or book to look for -').title()

			rows = scan_table(table, data)
			if rows:
				print('Relavant data Found')
				for row in rows:
					print_list(row)
				break
			else:
				print('Nothing found, sorry.')
