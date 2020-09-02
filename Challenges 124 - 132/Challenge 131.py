# 131
# Create a program that will allow the user to create a new .csv file.
# It should ask them to enter the name and age of
# a person and then allow them to add this to the end of the file
# they have just created.
import tkinter as tk
import datetime


def _create_csv_cmd():
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y_%H:%M:%S")
    file_name = f'num_list_{dt}.csv'
    file_name_label = tk.Label(text=file_name)


def _clear_list_cmd():
    tk_lst.delete(0, 'end')


def _send_to_csv_cmd():
    if not file_name_label:
        _create_csv_cmd()
    file_name = file_name_label['text']
    lst = tk_lst.get(0, 'end')
    with open(file_name, 'w') as f:
        for value in lst:
            f.write(f'{value}\n')


def _add_to_lst_cmd():
    num = tk_textbox.get()
    tk_textbox.delete(0, 'end')


window = tk.Tk()
window.title('Create CSV')

tk_lst = tk.Listbox()
tk_textbox = tk.Entry(justify='center')
clear_list_btn = tk.Button(text='Clear', command=_clear_list_cmd)
send_to_csv_btn = tk.Button(text='Send to csv',
                            command=_send_to_csv_cmd)
create_csv_btn = tk.Button(text='New csv', command=_create_csv_cmd)

clear_list_btn.place(x=0, y=0)
create_csv_btn.place(x=40, y=0)
send_to_csv_btn.place(x=100, y=0)
tk_textbox.place(x=0, y=30)
tk_lst.place(x=0, y = 50)

window.mainloop()