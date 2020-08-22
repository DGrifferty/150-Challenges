# 116
# Import the data from the Books.csv file into a list.
# Display the list to the user. Ask them to select which row
# from the list they want to delete and remove it from the
# list. Ask the user which data they want to change and allow
# them to change it. Write the data back to the original .csv file,
# overwriting the existing data with the amended data.

from typing import List


def print_csv_table(lst: List, print_row_num: bool = False,
                    prt: bool = True):
	"""prints a csv table in a cleaner way"""

	string = ''

	if print_row_num:
		for i in range(len(lst)):
			string += f'{i+1} {lst[i]}'
	else:
		for i in range(len(lst)):
			string += f'{lst[i]}'

	if prt:
		print(string)

	return string


if __name__ == '__main__':

	with open('Books.csv', 'r+') as f:
		table = f.readlines()
		print_csv_table(table, print_row_num=True)



