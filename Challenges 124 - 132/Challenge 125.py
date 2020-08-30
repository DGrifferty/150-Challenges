# 125
# Write a program that can be used instead of rolling a six-sided
# die in a board game. When the user clicks a button it should
# display a random whole number between 1 to 6 (inclusive).

import tkinter as tk
import random
from functools import partial
import random
import time

window = tk.Tk()
window.title('Dice roller')
window.geometry('400x400')


def _random_rgb():
    """Creates a random rgb colour then translates it into a form
     tkinter can interpret"""
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0, 255))
    rgb = tuple(rgb)

    return "#%02x%02x%02x" % rgb


def _rgb(rgb: tuple):
    return "#%02x%02x%02x" % rgb


def _button_dice_roll(x, y):
    dice_result = random.randint(1, 6)
    msg = tk.Label(window, text=f'Dice rolled: {dice_result}')
    msg.place(x=x, y=y)
    button1['bg'] = _random_rgb()
    button1['fg'] = _random_rgb()


button1x, button1y = 50, 50
button1 = tk.Button(text='Roll dice',
                    command=partial(_button_dice_roll, button1x,
                                    button1y+30))
button1.place(x=button1x, y=button1y, width=120, height=25)

window.mainloop()
