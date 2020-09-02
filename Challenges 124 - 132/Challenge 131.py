# 131
# Create a program that will allow the user to create a new .csv file.
# It should ask them to enter the name and age of
# a person and then allow them to add this to the end of the file
# they have just created.
import tkinter as tk
import datetime


def _create_csv_cmd():
    now = datetime.datetime.now()
    dt = now.strftime("%d-%m-%Y_%H-%M-%S")
    file_name = f'num_list_{dt}.csv'
    file_name_msg['text'] = file_name


def _clear_list_cmd():
    tk_lst.delete(0, 'end')


def _send_to_csv_cmd():
    if not file_name_msg['text']:
        _create_csv_cmd()
        print('Called')
    file_name = str(file_name_msg['text'])
    # print(f'msg - {file_name_msg["text"]}')
    # print(f'file_name = {file_name}')
    lst = tk_lst.get(0, 'end')
    with open(fr'{file_name}', 'w') as f:
        for value in lst:
            f.write(f'{value}\n')


def _add_to_lst_cmd():
    num = tk_textbox.get()
    tk_lst.insert('end', num)
    tk_textbox.delete(0, 'end')


window = tk.Tk()
window.title('Create CSV')
file_name_msg = tk.Message(text='')

tk_lst = tk.Listbox()
tk_textbox = tk.Entry(justify='center')
clear_list_btn = tk.Button(text='Clear', command=_clear_list_cmd)
send_to_csv_btn = tk.Button(text='Send to csv',
                            command=_send_to_csv_cmd)
create_csv_btn = tk.Button(text='New csv', command=_create_csv_cmd)
add_to_lst_btn = tk.Button(text='Add', command=_add_to_lst_cmd)

clear_list_btn.place(x=0, y=0)
create_csv_btn.place(x=40, y=0)
send_to_csv_btn.place(x=95, y=0)
add_to_lst_btn.place(x=130, y=38)
tk_textbox.place(x=0, y=40)
tk_lst.place(x=0, y=70)
file_name_msg.place(x=125, y=100)

window.mainloop()
