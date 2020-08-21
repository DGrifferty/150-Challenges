# 114
# Using the Books.csv file, ask the user to enter a starting year
# and an end year. Display all books released between those two years.

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


def scan_table_between_years(table: List[str], start_year: int,
                             end_year: int,  year_column: int,
                             seperator: str = ', '):
	rows_in = list()
	for index, row in enumerate(table):
		split_row = remove_n(row.split(seperator))
		if start_year <= int(split_row[year_column]) <= end_year:
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
		while True:

			print('This program will search a list of books between'
			      'two years and present the findings to you.')

			start_date = get_num_int('Enter starting year: ')
			end_date= get_num_int('Enter final year: ')

			rows = scan_table_between_years(table, start_date, end_date,
			                                2)
			if rows:
				print('Relavant data found! -')
				for row in rows:
					print_list(row)
				break
			else:
				print('Nothing found, sorry.')