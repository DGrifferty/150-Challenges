# 128
# 1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres. Using
# these figures, make a program that will allow the user to
# convert between miles and kilometres.
import tkinter as tk
import tkinter.messagebox


def _km_to_miles_cmd():
    try:
        kms = float(measurement_textbox.get())
        miles = kms * 0.6214
        result = f'{kms} km -> {miles} miles'
        results_list.insert('end', result)
        measurement_textbox.delete(0, 'end')

    except Exception:
        tk.messagebox.showinfo('Error', 'Please enter a number!')
        measurement_textbox.delete(0, 'end')


def _miles_to_km_cmd():
    try:
        miles = float(measurement_textbox.get())
        kms = miles * 1.6093
        results_list.insert('end', f'{miles} miles -> {kms} km')
        measurement_textbox.delete(0, 'end')

    except Exception:
        tk.messagebox.showinfo('Error', 'Please enter a number!')
        measurement_textbox.delete(0, 'end')


def _clear_results_cmd():
    results_list.delete(0, 'end')


window = tk.Tk()
window.title('Distance Converter')
window.geometry('300x250')

measurement_textbox = tk.Entry(text='', justify='center')
results_list = tk.Listbox()
km_to_miles_btn = tk.Button(text='kms to miles',
                            command=_km_to_miles_cmd)
miles_to_km_btn = tk.Button(text='miles to kms',
                            command=_miles_to_km_cmd)
clear_results_btn = tk.Button(text='reset', command=_clear_results_cmd)


measurement_textbox.place(x=90, y=20)

km_to_miles_btn.place(x=70, y=45)
miles_to_km_btn.place(x=160, y=45)
clear_results_btn.place(x=0, y=0)
results_list.place(x=50, y=75, width=200)

window.mainloop()

print('window closed')
