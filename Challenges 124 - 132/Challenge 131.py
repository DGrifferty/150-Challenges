# 131
# Create a program that will allow the user to create a new .csv file.
# It should ask them to enter the name and age of
# a person and then allow them to add this to the end of the file
# they have just created.
import tkinter as tk
import datetime
import tkinter.messagebox

def _create_csv_cmd():
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y_%H:%M:%S")
    file_name = f'num_list_{dt}.csv'
    file_name_label = tk.Label(text=file_name)


def _clear_list_cmd():
    num_list.delete(0, 'end')


def _send_to_csv_cmd():
    if not file_name_label:
        _create_csv_cmd()
    file_name = file_name_label['text']
    with open(file_name, 'w') as f:
        





def _add_to_lst_cmd():
    pass


window = tk.Tk()
window.title('Create CSV')



window.mainloop()