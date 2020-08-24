# 124
# Create a window that will ask the user to enter their name.
# When they click on a button it should display the message
# “Hello” and their name and change the background colour
# and font colour of the message box.

# (Using Tkinter)

import tkinter as tk
import random
from functools import partial
window = tk.Tk()


def _random_rgb():
    """Creates a random rgb colour then translates it into a form
     tkinter can interpret"""
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0, 255))
    rgb = tuple(rgb)

    return "#%02x%02x%02x" % rgb


def _button1_command(x, y):
    name = textbox1.get()
    msg = tk.Label(window, text=f'Hello {name}')
    msg.place(x=x, y=y + 40)
    button1['bg'] = _random_rgb()
    button1['fg'] = _random_rgb()


window.title('Print name')
window.geometry('400x400')

button1x, button1y = 240, 50
button1 = tk.Button(text='Click here',
                    command=partial(_button1_command, button1x-100,
                                    button1y))
button1.place(x=button1x, y=button1y, width=120, height=25)

textbox1 = tk.Entry(text='')
textbox1.place(x=button1x - 200, y=button1y, width=200, height=25)
textbox1['justify'] = 'center'
textbox1.focus()

window.mainloop()
