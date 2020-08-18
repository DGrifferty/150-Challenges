# 097
# Using the 2D list from program 096, ask the user to select
# a row and a column and display that value.

def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))
            return number

        except Exception as e:
            print(e)
            

if __name__ == '__main__':
    
    lst = [[2, 5, 8],
           [3, 7, 4],
           [1, 6, 9],
           [4, 2, 0]]

    rows = len(lst)

    while True:
        
        user_row = get_num_int('Enter row: ')

        if 0 <= user_row <= rows - 1:
            break
        else:
            print(f'Enter a number between 0 and {rows - 1}')

    columns = len(lst[user_row])

    while True:

        user_column = get_num_int('Enter column: ')

        if 0 <= user_column <= columns - 1:
            break
        else:
            print(f'Enter a number between 0 and {columns - 1}')

    print(lst[user_row][user_column])

    

    
    

