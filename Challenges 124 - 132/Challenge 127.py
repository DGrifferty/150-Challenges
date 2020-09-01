# 127
# Create a window that will ask the user to enter a
# name in a text box. When they click on a button it
# will add it to the end of the list that is displayed on
# the screen. Create another button which will clear
# the list.
import tkinter as tk


def _add_to_list_button():
    pass


def _reset_button():
    answer_text['text'] = 0

window = tk.Tk()
window.geometry('400x400')
window.title('Add')

add_button = tk.Button(text='Add', command=_add_to_list_button)
add_button.place(x=100, y=20)

reset_button = tk.Button(text='Reset', command=_reset_button)
reset_button.place(x=100, y=50)

number_textbox = tk.Entry(text='')
number_textbox.place(x=45, y=20, width=50, height=25)
number_textbox['justify'] = 'center'
number_textbox.focus()

answer_text = tk.Message(text=0)
answer_text.place(x=40, y=55)

window.mainloop() 
