import tkinter

window = tkinter.Tk()
window.title('My first GUI Program')
window.minsize(height=300, width=500)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text='Yo!! How r u?', font=('Arial', 20))
# my_label.pack()   # my_label.pack(side='top') - default
# my_label.pack(side='left')
# my_label.pack(side='right')
# my_label.pack(side='bottom')
# my_label.pack(expand=True)
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady= 20)

# # changing the argument
# my_label['text'] = 'New Text'
# my_label.config(text='New Text')

# Button


def button_clicked():
    my_label['text'] = input_entry.get()   # can be above the input_entry definition


button = tkinter.Button(text='Yes?', command=button_clicked)
# button.pack(side='left')
# button.place(x=0, y=0)  # no negative coordinates
button.grid(row=1, column=1)

new_button = tkinter.Button(text='New one huh..?')
new_button.grid(row=0, column=2)

# Entry

input_entry = tkinter.Entry(width=10)
# input_entry.pack(side='left')
input_entry.grid(row=2, column=3)

window.mainloop()

# pack and place can be in the same program, grid and place also
# but grid and pack are incompatible
