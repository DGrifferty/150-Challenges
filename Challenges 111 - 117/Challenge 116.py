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


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


if __name__ == '__main__':


	with open('Books.csv', 'r+') as f:
		table = f.readlines()

	print_csv_table(table, print_row_num=True)

	while True:  # Deleting row

		row_to_delete = get_num_int('Enter row to delete: ')
		if 1 <= row_to_delete <= len(table):
			del table[row_to_delete - 1]
			print_csv_table(table, print_row_num=True)
			break
		else:
			print(f'Please enter a number between 1 and {len(table)}')

	while True:  # Changing row

		row_to_change = get_num_int('Enter row to change: ')

		if 1 <= row_to_change <= len(table):
			table[row_to_change - 1] = input('Enter new record: ') + '\n'
			print_csv_table(table, print_row_num=True)
			break
		else:
			print(f'Please enter a number between 1 and {len(table)}')

	with open('Books.csv', 'w') as f:
		for element in table:
			f.write(element)
