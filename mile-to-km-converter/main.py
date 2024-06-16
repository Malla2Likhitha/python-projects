from tkinter import *

FONT = ('Arial', 15)

window = Tk()
window.title('Mile to Km Converter')
window.minsize(height=150, width=300)
window.config(padx=50, pady=50)

miles_input = Entry(width=15)
miles_input.insert(END, '0')
miles_input.focus()
miles_input.grid(row=0, column=1)


def calculate():
    val_in_miles = miles_input.get()
    km_val.config(text=f'{float(val_in_miles) * 1.60934}')


calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(row=2, column=1)

miles = Label(text='Miles', font=FONT)
miles.grid(row=0, column=2)
km = Label(text='Km', font=FONT)
km.grid(row=1, column=2)
equal = Label(text='is equal to', font=FONT)
equal.grid(row=1, column=0)
km_val = Label(text='0', font=FONT)
km_val.grid(row=1, column=1)

window.mainloop()
