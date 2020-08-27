# 126
# Create a program that will ask the user to enter a number in a
# box. When they click on a button it will add that number
# to a total and display it in another box. This can be
# repeated as many times as they want and keep adding to
# the total. There should be another button that resets the
# total back to 0 and empties the original text box, ready for
# them to start again.

import tkinter as tk


def _add_button():
    total = float(number_textbox.get()) + float(answer_text['text'])
    answer_text['text'] = total


def _reset_button():
    answer_text['text'] = 0


window = tk.Tk()
window.geometry('400x400')
window.title('Add')

add_button = tk.Button(text='Add', command=_add_button)
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
