# 127
# Create a window that will ask the user to enter a
# name in a text box. When they click on a button it
# will add it to the end of the list that is displayed on
# the screen. Create another button which will clear
# the list.
import tkinter as tk


def _add_to_list_cmd():
    name = name_textbox.get()
    name_list.insert('end', name)
    name_textbox.delete(0, 'end')


def _reset_list_cmd():
    name_list.delete(0, 'end')


window = tk.Tk()
window.title('List of names')
window.geometry('500x500')

name_textbox = tk.Entry(text='', justify='center')
name_textbox.place(x=100, y=150)

name_list = tk.Listbox()
name_list.place(x=100, y=250)

add_to_list_btn = tk.Button(text='Add to list',
                            command=_add_to_list_cmd)
add_to_list_btn.place(x=100, y=100)

reset_list_btn = tk.Button(text='Reset List', command=_reset_list_cmd)
reset_list_btn.place(x=100, y=200)

window.mainloop()

print('window closed')
