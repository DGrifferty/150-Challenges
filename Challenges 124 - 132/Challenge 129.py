# 129
# Create a window that will ask the user to enter a number in a text box
# When they click on a button it will use the code
# variable.isdigit() to check to see if it is a whole number. If it is
# a whole number, add it to a list box,
# otherwise clear the entry box. Add another button that will clear the
# list

# Similar to solution to challenge 129

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


window = tk.Tk()
window.title('Number List')
window.geometry('250x240')

num_textbox = tk.Entry(justify='center')
num_list = tk.Listbox()
add_num_to_lst_btn = tk.Button(text='Add to list',
                               command=_add_num_to_lst_cmd)
clear_num_list_btn = tk.Button(text='clear',
                               command=_clear_num_list_cmd)

num_textbox.place(x=40, y=20)
num_list.place(x=40, y=40)
add_num_to_lst_btn.place(x=169, y=18)
clear_num_list_btn.place(x=0, y=0)

window.mainloop()
