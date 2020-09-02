# 130
# Alter program 129 to add a third button that will save the list
# to a .csv file. The code tmp_list = nm_list.get(0,END)
# can be used to save the contents of a list box
# as a tuple called tmp_list.
import tkinter as tk
import tkinter.messagebox


def _add_num_to_lst_cmd():
    num = num_textbox.get()
    num_textbox.delete(0, 'end')

    if num.isdigit():
        num_list.insert('end', num)
    else:
        tkinter.messagebox.showinfo('Error', 'Please enter a number')


def _clear_num_list_cmd():
    num_list.delete(0, 'end')


def _num_list_to_csv_cmd():
    lst = num_list.get(0, 'end')
    with open('Num_List.csv', 'w') as f:
        for value in lst:
            f.write(f'{value}\n')


window = tk.Tk()
window.title('Number List')
window.geometry('250x240')

num_textbox = tk.Entry(justify='center')
num_list = tk.Listbox()
add_num_to_lst_btn = tk.Button(text='Add to list',
                               command=_add_num_to_lst_cmd)
clear_num_list_btn = tk.Button(text='clear',
                               command=_clear_num_list_cmd)
num_list_to_csv_btn = tk.Button(text='Send to csv',
                                command=_num_list_to_csv_cmd)

num_textbox.place(x=40, y=40)
num_list.place(x=40, y=60)
add_num_to_lst_btn.place(x=169, y=38)
clear_num_list_btn.place(x=0, y=0)
num_list_to_csv_btn.place(x=50, y=0)

window.mainloop()
