# 132
# Using the .csv file you created for the last challenge, create a
# program that will allow people to add names and ages to the list
# and create a button that will display the contents of the .csv
# file by importing it to a list box.

# Using code from challenge 131

import tkinter as tk
import datetime
from typing import List


def remove_n(lst: List[str]) -> List[str]:
    """removes \\n from end of a all elements in list and returns
	string"""

    for index, element in enumerate(lst):
        if element[
           -1:-2:-1] == '\n':  # Test if last two characters are "\n"
            lst[index] = element[:-1]
    return lst


def _select_csv_cmd():
    name = csv_textbox.get()
    csv_textbox.delete(0, 'end')
    if name == '':
        now = datetime.datetime.now()
        dt = now.strftime("%d-%m-%Y_%H-%M-%S")
        file_name = f'{dt}.csv'
        file_name_msg['text'] = file_name
    else:
        if name[-4:].lower() != '.csv':
            name += '.csv'
        file_name_msg['text'] = name


def _clear_list_cmd():
    tk_lst.delete(0, 'end')


def _send_to_csv_cmd():
    if not file_name_msg['text']:
        _select_csv_cmd()
    file_name = str(file_name_msg['text'])
    lst = tk_lst.get(0, 'end')
    with open(fr'{file_name}', 'w') as f:
        for value in lst:
            f.write(f'{value}\n')


def _add_to_lst_cmd():
    num = tk_textbox.get()
    tk_lst.insert('end', num)
    tk_textbox.delete(0, 'end')


def _append_to_csv_cmd():
    if not file_name_msg['text']:
        _select_csv_cmd()
    file_name = str(file_name_msg['text'])
    lst = tk_lst.get(0, 'end')
    with open(fr'{file_name}', 'a') as f:
        for value in lst:
            f.write(f'{value}\n')


def _load_from_csv_cmd():
    file_name = str(file_name_msg['text'])
    with open(fr'{file_name}', 'r') as f:
        lst = f.readlines()
        lst = remove_n(lst)
    for value in lst:
        tk_lst.insert('end', value)


window = tk.Tk()
window.title('Create CSV')
window.geometry('300x300')

file_name_msg = tk.Message(text='')
tk_lst = tk.Listbox()
tk_textbox = tk.Entry(justify='center')
csv_textbox = tk.Entry(justify='center')
clear_list_btn = tk.Button(text='Clear', command=_clear_list_cmd)
send_to_csv_btn = tk.Button(text='Print to csv',
                            command=_send_to_csv_cmd)
select_csv_btn = tk.Button(text='Select csv',
                           command=_select_csv_cmd)
add_to_lst_btn = tk.Button(text='Add', command=_add_to_lst_cmd)
load_from_csv_btn = tk.Button(text='Load from csv',
                              command=_load_from_csv_cmd)
append_to_csv_btn = tk.Button(text='Append to csv',
                              command=_append_to_csv_cmd)
msg1 = tk.Message(text='Enter csv name:')
msg2 = tk.Message(text='Current csv:')

clear_list_btn.place(x=0, y=0)

send_to_csv_btn.place(x=130, y=260)
add_to_lst_btn.place(x=130, y=38)
load_from_csv_btn.place(x=130, y=200)
append_to_csv_btn.place(x=130, y=230)
tk_textbox.place(x=0, y=40)
tk_lst.place(x=0, y=70)
msg1.place(x=125, y=80)
select_csv_btn.place(x=190, y=80)
csv_textbox.place(x=125, y=120)
msg2.place(x=125, y=140)
file_name_msg.place(x=180, y=140)

window.mainloop()
