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


def button1_command(x, y):
    msg = tk.Label(window, text = 'Hello')
    msg.place(x=x, y=y + 30)
    button1['bg'] = _random_rgb()
    button1['fg'] = _random_rgb()


window.title('Title')
window.geometry('400x400')
button1x, button1y = 30, 20
button1 = tk.Button(text='Click here', command=partial(button1_command, button1x, button1y))
button1.place(x=button1x, y=button1y, width=120, height=25)

window.mainloop()
