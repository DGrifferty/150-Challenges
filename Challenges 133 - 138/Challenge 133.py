# 133
# Create your own icon that consists of several vertical multi-coloured
# lines. Create a logo which measures 200 x 150, using Paint or
# another graphics package. Create the following window using your own
# icon and logo.
# When the user enters their name and clicks on the Press Me button
# it should display “Hello” and their name in the second text
# box.
import tkinter as tk


def _say_hello_cmd():
    name = name_textbox.get()
    name_textbox.delete(0, 'end')
    hello_msg['text'] = f'hello {name}!'


window = tk.Tk()
window.title('Hello!')
window.geometry('300x300')
window.wm_iconbitmap("logo.ico")

logo = tk.PhotoImage(file='logo.gif')
logo_image_label = tk.Label(image=logo)
name_textbox = tk.Entry(justify='center')
say_hello_btn = tk.Button(text='Click here', command=_say_hello_cmd)
hello_msg = tk.Message(text='')

logo_image_label.place(x=0, y=0, width=200, height=150)
name_textbox.place(x=0, y=160)
say_hello_btn.place(x=130, y=155)
hello_msg.place(x=0, y=180, width = 200)

window.mainloop()
